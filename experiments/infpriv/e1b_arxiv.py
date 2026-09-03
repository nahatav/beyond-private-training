"""E1b -- the real anchor: arXiv abstracts (CC0) grouped by FIRST AUTHOR.

Multi-owner assignment rule (notes/15 item 3, DP-fy guide sec 7.2): each abstract
is credited to its first author only, so the records form a clean partition and
removing one "user" changes only that user's vote vector.

Nothing person-specific is reported: author strings are grouping keys, and only
aggregate distributions over d_u leave this script.
"""

import json
import os
import time
from collections import defaultdict

import numpy as np

from pe.histogram.nearest_neighbor_backend.sklearn import search
from pe.histogram.nearest_neighbors import NearestNeighbors
from pe.constant.data import CLEAN_HISTOGRAM_COLUMN_NAME

from common import PrecomputedEmbedding, to_data, vote_matrix, user_stats, unit

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "arxiv_raw.jsonl")
N_PRIV, N_POOL = 2000, 2000
M_MINS = [3, 5]   # first-authorship is thin; report both cuts
KS = [1, 4, 8]
MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def load_groups(M_MIN):
    by_author = defaultdict(list)
    with open(RAW) as f:
        for line in f:
            r = json.loads(line)
            if r["abstract"]:
                by_author[r["first_author"]].append(r["abstract"])
    prolific = sorted((a for a, v in by_author.items() if len(v) >= M_MIN),
                      key=lambda a: -len(by_author[a]))
    priv_texts, client_ids, n = [], [], 0
    for i, a in enumerate(prolific):
        if n >= N_PRIV:
            break
        for t in by_author[a]:
            priv_texts.append(t)
            client_ids.append(i)
            n += 1
    used = set(prolific[:len(set(client_ids))])
    pool = [t for a, v in by_author.items() if a not in used for t in v][:N_POOL]
    return priv_texts, np.array(client_ids), pool, by_author


def run(M_MIN, model, dev):
    priv_texts, client_ids, pool_texts, by_author = load_groups(M_MIN)
    U = len(np.unique(client_ids))
    sizes = np.bincount(client_ids)
    print(f"{len(by_author)} distinct first authors in the raw pull; "
          f"{U} of them have >= {M_MIN} first-authored papers.")
    print(f"private set: {len(priv_texts)} abstracts / {U} users, "
          f"m_u min/median/max = {sizes.min()}/{int(np.median(sizes))}/{sizes.max()}")
    print(f"candidate pool: {len(pool_texts)} held-out abstracts from other authors")

    t_emb = time.time()
    priv = unit(model.encode(priv_texts, batch_size=128, show_progress_bar=False)).astype(np.float32)
    syn = unit(model.encode(pool_texts, batch_size=128, show_progress_bar=False)).astype(np.float32)
    print(f"embedded {len(priv_texts)+len(pool_texts)} abstracts on {dev} "
          f"in {time.time()-t_emb:.1f}s  (dim={priv.shape[1]})")

    out = []
    for k in KS:
        _, ids = search(syn_embedding=syn, priv_embedding=priv,
                        num_nearest_neighbors=k, mode="cos_sim")
        Vmat = vote_matrix(ids, client_ids, len(pool_texts))
        l1 = Vmat.sum(axis=1)
        l2 = np.linalg.norm(Vmat, axis=1)
        d_u = (l1 / l2) ** 2
        ratio = d_u / (k * sizes)          # per-user m_u, not a global constant

        # cross-check against the shipped DPSDA client-mode histogram
        hist = NearestNeighbors(embedding=PrecomputedEmbedding(), mode="cos_sim",
                                lookahead_degree=0, num_nearest_neighbors=k,
                                backend="sklearn", vote_normalization_level="client")
        _, syn_out = hist.compute_histogram(priv_data=to_data(priv, client_ids),
                                            syn_data=to_data(syn))
        h = syn_out.data_frame[CLEAN_HISTOGRAM_COLUMN_NAME].to_numpy()
        err = float(np.abs(h - (Vmat / l2[:, None]).sum(axis=0)).max())

        floor = 1.0 / sizes
        frac = (ratio - floor) / (1.0 - floor)   # 0 = all a user's samples vote alike, 1 = ceiling
        rec = {
            "M_MIN": M_MIN, "U": int(U), "n_priv": len(priv_texts),
            "m_u_median": int(np.median(sizes)),
            "k": k,
            "median_frac_floor_to_ceiling": float(np.median(frac)),
            "median_ratio": float(np.median(ratio)),
            "p10_ratio": float(np.percentile(ratio, 10)),
            "p90_ratio": float(np.percentile(ratio, 90)),
            "median_d_u": float(np.median(d_u)),
            "w_p2_p90_over_p10": float(np.percentile(np.sqrt(d_u), 90)
                                       / np.percentile(np.sqrt(d_u), 10)),
            "dpsda_vs_numpy_max_abs_err": err,
            "client_total_mass": float(h.sum()),
            "record_total_mass": float(l1.sum() / np.sqrt(k)),
        }
        out.append(rec)
        print(f"k={k}: median d_u/(k*m_u)={rec['median_ratio']:.3f} "
              f"[p10 {rec['p10_ratio']:.3f}, p90 {rec['p90_ratio']:.3f}]  "
              f"median d_u={rec['median_d_u']:.1f}  "
              f"floor->ceiling frac={rec['median_frac_floor_to_ceiling']:.3f}  "
              f"p=2 spread p90/p10={rec['w_p2_p90_over_p10']:.2f}  "
              f"(DPSDA-vs-numpy err {err:.2e})")

    return {"M_MIN": M_MIN, "U": int(U), "n_priv": len(priv_texts), "n_pool": len(pool_texts),
            "m_u_min": int(sizes.min()), "m_u_median": int(np.median(sizes)),
            "m_u_max": int(sizes.max()), "model": MODEL, "results": out}


def main():
    t0 = time.time()
    from sentence_transformers import SentenceTransformer
    import torch
    dev = "mps" if torch.backends.mps.is_available() else "cpu"
    model = SentenceTransformer(MODEL, device=dev)
    allout = [run(m, model, dev) for m in M_MINS]
    with open(os.path.join(HERE, "e1b_arxiv_results.json"), "w") as f:
        json.dump(allout, f, indent=2)
    print(f"E1b wall clock: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
