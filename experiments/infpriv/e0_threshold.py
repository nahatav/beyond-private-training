"""E0 -- what the noisy-histogram threshold-and-subtract does once per-client
normalisation makes the counts non-integer.

Uses the shipped DPSDA classes end to end:
    NearestNeighbors.compute_histogram  ->  Gaussian.add_noise
    ->  PEPopulation._post_process_histogram  ->  PEPopulation._select_data

The threshold values swept are exactly the ones the repo's own examples use
(0, 1, 2, 4, 10) plus None.
"""

import os
import time
import traceback

import numpy as np

from pe.histogram.nearest_neighbors import NearestNeighbors
from pe.dp.gaussian import Gaussian
from pe.population.pe_population import PEPopulation
from pe.constant.data import (
    CLEAN_HISTOGRAM_COLUMN_NAME,
    POST_PROCESSED_DP_HISTOGRAM_COLUMN_NAME,
)

from common import PrecomputedEmbedding, make_corpus, to_data

HERE = os.path.dirname(os.path.abspath(__file__))
U, M, VSIZE, DIM, C, K = 200, 10, 2000, 384, 0.5, 4
EPSILON, DELTA, ITERS = 1.0, 1e-5, 10
SHIPPED_THRESHOLDS = [None, 0, 1, 2, 4, 10]


def clean_histogram(priv, client_ids, syn, level):
    hist = NearestNeighbors(
        embedding=PrecomputedEmbedding(), mode="cos_sim", lookahead_degree=0,
        num_nearest_neighbors=K, backend="sklearn", vote_normalization_level=level,
    )
    _, syn_out = hist.compute_histogram(
        priv_data=to_data(priv, client_ids), syn_data=to_data(syn))
    return syn_out


def main():
    t0 = time.time()
    priv, client_ids, syn = make_corpus(U=U, m=M, d=DIM, c=C, V=VSIZE, seed=1234)

    dp = Gaussian()
    dp.set_epsilon_and_delta(num_iterations=ITERS, epsilon=EPSILON, delta=DELTA,
                             noise_multiplier=None)
    sigma = dp._noise_multiplier
    print(f"\nGaussian: eps={EPSILON}, delta={DELTA}, T={ITERS} -> noise_multiplier sigma={sigma:.4f}")
    print("NOTE: sigma is computed with no reference to vote_normalization_level.\n")

    # sigma=0 is the eps=inf arm: it isolates the DETERMINISTIC effect of the mode
    # change on the threshold semantics, with no noise to confound it.
    sigmas = [("eps=inf", 0.0), ("sigma=1", 1.0), (f"eps={EPSILON},T={ITERS}", sigma)]

    rows = []
    for level in ["sample", "client"]:
        base = clean_histogram(priv, client_ids, syn, level)
        clean = base.data_frame[CLEAN_HISTOGRAM_COLUMN_NAME].to_numpy()
        print(f"--- vote_normalization_level = {level!r} ---")
        print(f"    clean histogram: total mass {clean.sum():.1f}, "
              f"max bin {clean.max():.3f}, mean bin {clean.mean():.4f}, "
              f"integer-valued={bool(np.all(clean == np.round(clean)))}")

        for sname, s in sigmas:
            dp._noise_multiplier = s
            np.random.seed(7)
            noisy = dp.add_noise(base)
            for thr in SHIPPED_THRESHOLDS:
                pop = PEPopulation(api=None, histogram_threshold=thr, selection_mode="sample")
                pp = pop._post_process_histogram(noisy)
                cnt = pp.data_frame[POST_PROCESSED_DP_HISTOGRAM_COLUMN_NAME].to_numpy()
                surviving = int((cnt > 0).sum())
                status = "ok"
                try:
                    pop._select_data(pp, num_samples=VSIZE)
                except Exception as e:
                    status = f"{type(e).__name__}: {e}"
                rows.append((level, sname, thr, float(cnt.sum()), surviving, status))
                print(f"    [{sname:>12}] threshold={str(thr):>4}  "
                      f"surviving bins {surviving:>5}/{VSIZE}  "
                      f"mass {cnt.sum():>10.2f}  _select_data -> {status}")
            print()
        print()

    with open(os.path.join(HERE, "e0_threshold_results.md"), "w") as f:
        f.write("# E0: threshold-and-subtract under per-client normalisation\n\n")
        f.write(f"U={U}, m_u={M}, |V|={VSIZE}, d={DIM}, c={C}, k={K}; "
                f"eps={EPSILON}, delta={DELTA}, T={ITERS} gives sigma={sigma:.4f}\n\n")
        f.write("| mode | noise | histogram_threshold | mass after clip-and-subtract | surviving bins | `_select_data` |\n")
        f.write("|---|---|---|---|---|---|\n")
        for level, sname, thr, mass, surv, status in rows:
            f.write(f"| `{level}` | {sname} | {thr} | {mass:.2f} | {surv}/{VSIZE} | {status} |\n")
    print(f"E0 wall clock: {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
