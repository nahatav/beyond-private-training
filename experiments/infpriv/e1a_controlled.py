"""E1a -- the d_u / (k*m_u) measurement on the controlled arm, plus the E1 curve.

Runs DPSDA's own NearestNeighbors.compute_histogram for the "client" (p=2) and
"sample" (record-level) endpoints, cross-checks it against a numpy
reimplementation of the same per-client l2 normalisation, then sweeps the
within-user coherence parameter c.

No real identities anywhere: every "user" is a random unit centroid.
"""

import json
import os
import time

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from pe.histogram.nearest_neighbors import NearestNeighbors
# faiss-cpu and torch ship conflicting libomp on macOS arm64 (OMP Error #15), and
# DPSDA's own "auto" backend falls back to sklearn in exactly this situation, so we
# pin the sklearn brute-force backend. It is exact, and the corpus is tiny.
from pe.histogram.nearest_neighbor_backend.sklearn import search as auto_search
from pe.constant.data import CLEAN_HISTOGRAM_COLUMN_NAME

from common import PrecomputedEmbedding, make_corpus, to_data, vote_matrix, user_stats

HERE = os.path.dirname(os.path.abspath(__file__))
U, M, VSIZE = 200, 10, 2000
CS = [0.0, 0.25, 0.5, 0.75, 0.9, 0.99]
KS = [1, 4, 8]
DIMS = [64, 384]
MODE = "cos_sim"


def dpsda_histogram(priv, client_ids, syn, k, level):
    """Run the shipped DPSDA histogram end to end. Returns the count vector."""
    hist = NearestNeighbors(
        embedding=PrecomputedEmbedding(),
        mode=MODE,
        lookahead_degree=0,
        num_nearest_neighbors=k,
        backend="sklearn",
        vote_normalization_level=level,
    )
    _, syn_out = hist.compute_histogram(
        priv_data=to_data(priv, client_ids), syn_data=to_data(syn)
    )
    return syn_out.data_frame[CLEAN_HISTOGRAM_COLUMN_NAME].to_numpy()


def main():
    t_all = time.time()
    results = []
    checks = []

    for d in DIMS:
        for c in CS:
            priv, client_ids, syn = make_corpus(U=U, m=M, d=d, c=c, V=VSIZE, seed=1234)
            for k in KS:
                t0 = time.time()
                _, ids = auto_search(
                    syn_embedding=syn, priv_embedding=priv,
                    num_nearest_neighbors=k, mode=MODE,
                )
                Vmat = vote_matrix(ids, client_ids, VSIZE)
                st = user_stats(Vmat, k, M)

                # --- cross-check against the shipped DPSDA code path ---
                h_client_np = (Vmat / st["l2"][:, None]).sum(axis=0)
                h_sample_np = Vmat.sum(axis=0) / np.sqrt(k)
                h_client = dpsda_histogram(priv, client_ids, syn, k, "client")
                h_sample = dpsda_histogram(priv, client_ids, syn, k, "sample")
                checks.append({
                    "d": d, "c": c, "k": k,
                    "client_max_abs_err": float(np.abs(h_client - h_client_np).max()),
                    "sample_max_abs_err": float(np.abs(h_sample - h_sample_np).max()),
                    "client_total_mass": float(h_client.sum()),
                    "sample_total_mass": float(h_sample.sum()),
                })

                results.append({
                    "d": d, "c": c, "k": k,
                    "median_ratio": float(np.median(st["ratio"])),
                    "p10_ratio": float(np.percentile(st["ratio"], 10)),
                    "p90_ratio": float(np.percentile(st["ratio"], 90)),
                    "median_d_u": float(np.median(st["d_u"])),
                    "ceiling_km": k * M,
                    "median_w_p2": float(np.median(st["w_p2"])),
                    "w_p2_spread_p90_over_p10": float(
                        np.percentile(st["w_p2"], 90) / np.percentile(st["w_p2"], 10)
                    ),
                    "secs": round(time.time() - t0, 2),
                })
                print(f"d={d} c={c} k={k} median d_u/(k*m)={results[-1]['median_ratio']:.4f} "
                      f"({results[-1]['secs']}s)")

    with open(os.path.join(HERE, "e1a_results.json"), "w") as f:
        json.dump({"results": results, "checks": checks}, f, indent=2)

    # ---------- table ----------
    lines = []
    for d in DIMS:
        lines.append(f"\n### d = {d}   (U={U}, m_u={M}, |V|={VSIZE}, mode={MODE})\n")
        lines.append("| c (within-user coherence) | " + " | ".join(f"k={k}" for k in KS) + " |")
        lines.append("|---|" + "---|" * len(KS))
        for c in CS:
            cells = []
            for k in KS:
                r = next(x for x in results if x["d"] == d and x["c"] == c and x["k"] == k)
                cells.append(f"{r['median_ratio']:.3f}")
            lines.append(f"| {c} | " + " | ".join(cells) + " |")
    table = "\n".join(lines)
    with open(os.path.join(HERE, "e1a_table.md"), "w") as f:
        f.write("Median `d_u / (k*m_u)` over 200 users. 1.0 = maximal diversity "
                "(every vote a distinct candidate); 1/m_u = 0.100 = floor "
                "(all of a user's samples vote identically).\n")
        f.write(table + "\n")
    print(table)

    # ---------- the E1 curve ----------
    make_plot()
    print(f"\nTOTAL E1a wall clock: {time.time() - t_all:.1f}s")


def make_plot(d=384, k=4):
    """w_u(p) vs d_u, pooling users across the whole coherence sweep."""
    du, wr, w1, w15, w2 = [], [], [], [], []
    for c in CS:
        priv, client_ids, syn = make_corpus(U=U, m=M, d=d, c=c, V=VSIZE, seed=1234)
        _, ids = auto_search(syn_embedding=syn, priv_embedding=priv,
                             num_nearest_neighbors=k, mode=MODE)
        st = user_stats(vote_matrix(ids, client_ids, VSIZE), k, M)
        du.append(st["d_u"]); wr.append(st["w_record"])
        w1.append(st["w_p1"]); w15.append(st["w_p1p5"]); w2.append(st["w_p2"])
    du = np.concatenate(du)
    series = [
        ("record-level  $w_u = k\\,m_u$", np.concatenate(wr), "#444444", "o"),
        ("$p=2$ (DPSDA \"client\")  $w_u=\\sqrt{d_u}$", np.concatenate(w2), "#c0392b", "s"),
        ("$p=1.5$", np.concatenate(w15), "#e67e22", "^"),
        ("$p=1$ (user-uniform)  $w_u=1$", np.concatenate(w1), "#2980b9", "d"),
    ]

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    for name, w, col, mk in series:
        axes[0].scatter(du, w, s=7, alpha=0.35, color=col, marker=mk, label=name, linewidths=0)
    axes[0].set_yscale("log")
    axes[0].set_xlabel("effective diversity  $d_u=(\\|v_u\\|_1/\\|v_u\\|_2)^2$")
    axes[0].set_ylabel("user mass  $w_u(p)$  (absolute)")
    axes[0].set_title(f"Absolute user mass  (d={d}, k={k}, $m_u$={M})")
    axes[0].legend(fontsize=7, loc="center right")
    axes[0].grid(alpha=0.25)

    for name, w, col, mk in series:
        rel = w / np.mean(w)
        axes[1].scatter(du, rel, s=7, alpha=0.35, color=col, marker=mk, label=name, linewidths=0)
    axes[1].axhline(1.0, color="k", lw=0.6, ls=":")
    axes[1].set_xlabel("effective diversity  $d_u$")
    axes[1].set_ylabel("relative user mass  $w_u / \\overline{w}$")
    axes[1].set_title("Share of the histogram each user gets")
    axes[1].legend(fontsize=7, loc="upper left")
    axes[1].grid(alpha=0.25)

    fig.suptitle("E1: the vote-normalisation family re-weights users by their semantic diversity",
                 fontsize=11)
    fig.tight_layout()
    out = os.path.join(HERE, "e1_reweighting_curve.png")
    fig.savefig(out, dpi=160)
    print("plot ->", out)


if __name__ == "__main__":
    main()
