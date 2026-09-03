# experiments/ — the first code this repo has ever held (round 17, 2026-09-03)

Sixteen rounds produced zero lines of experiment code. Round 17 produced these. Every number quoted in
`ideas/29` and `notes/19` was computed by a script in this directory, on the full artifact, on 2026-09-03.

## `audit/` — the AI-control backdoor-benchmark validity audit
- `fetch.py` — pulls the three parquet shards of `RoganInglis/apps-control-arena` (5,000 rows) from the HF datasets-server.
- `floors.py` — problem-level and sample-level **metadata-only** floors under five eval protocols (P0–P4).
- `matched.py`, `exact.py` — the DSPy trusted-monitor tutorial's matched-pair protocol reproduced; TF-IDF / length / surface-feature baselines; 5-fold and 200-pair regimes.
- `transfer.py` — cross-generator transfer of the bag-of-words classifier and style markers (comments, `__main__`).
- `koran.py` — Koran et al.'s filter (passing honest + working backdoors, comments stripped) reproduced on the full artifact, pooled AUROC / pAUC@10% / TPR@10%FPR.
- `koran_split_eval.py` — **the apples-to-apples number**: train on Koran's paired train split, score their exact 1,375-item test split, compare against the 24 monitors in `2608.16190`'s `runs/x0/monitor-summary.json`.
- `data.py`, `auroc.py`, `bow.py`, `analyse.py`, `analyse2.py`, `fetch_cols.py`, `K1-report.md` — the K1 agent's artifact-lineage check (Jha's `src/data.py` port, the Koran split reconstruction that bit-reproduces three of Jha's harness numbers).
- `K2-grep-table-*.tsv` — the K2 full-text keyword counts over 17 papers (14 AI-control + 3 out-of-field positive controls).
- `RESULTS.md` — the coordinator's own recompute log (R17).

Run with `uv venv && uv pip install pandas pyarrow scikit-learn requests`, then `python fetch.py` first.
Nothing here needs a GPU; the whole directory runs in minutes on a laptop.

## `infpriv/` — the Private Evolution estimand paper
- `e0_threshold.py`, `e0_threshold_results.md` — E0: the histogram threshold is a raw count whose *unit* moves under `"client"` mode.
- `e1a_controlled.py`, `e1a_table.md` — E1a: `d_u/(k·m_u)` on the controlled arm, 36 configs, using DPSDA's own `NearestNeighbors` for the `"sample"`/`"client"` endpoints.
- `e1b_arxiv.py`, `fetch_arxiv.py` — E1b: the real anchor, arXiv abstracts by first author (CC0), `all-MiniLM-L6-v2`.
- `e1_reweighting_curve.png` — **the central figure**, `w_u(p)` vs `d_u` for `p ∈ {1, 1.5, 2}` and record-level.
- `common.py` — the `PrecomputedEmbedding` pass-through that drives DPSDA without a generator.
- `refs.bib`, `scoop_sweep.tsv` — the resolved bibliography (14 entries, every one fetched) and the scoop-patrol query log with positive controls.

Needs `git clone https://github.com/microsoft/DPSDA` beside the scripts and `uv pip install -e DPSDA/` (39 packages, ~7 s warm). Pin `backend="sklearn"`: faiss-cpu and torch cannot be co-imported on macOS.
