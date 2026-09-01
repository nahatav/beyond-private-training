# Spin-offs harvested from other people's future-work sections

Three items, ranked. The first is free and generalises the lead beyond PE; the second is a genuine
open problem someone should do but not in six days; the third is recorded to be left alone.

---

## J1 — the unifying theme: parameters that are privacy-neutral at record level ★ take this

This is the observation that turns `ideas/10` from a note about one algorithm into a claim about a
class of algorithms, and it costs one paragraph.

> Inference-time DP mechanisms are built out of aggregation steps whose *shape* parameters — how
> many candidates, how many shards — have **no effect on sensitivity under record-level adjacency**.
> Under user-level adjacency they all become privacy knobs, because they control how far one
> person's contribution can spread. No paper on these mechanisms has had a reason to notice,
> because they were all analysed at record level.

Two instances, both verified:

**PE — the candidate pool size `|V|`.** Sensitivity is `2/n` regardless of `|V|`, so it is a pure
utility parameter in every PE paper. At user level `|V|` controls `d_u` directly: a larger pool
spreads a user's votes, raising their effective diversity and therefore their weight under the DP-fy
guide's recipe. Corroborating: *Private Evolution Converges* (arXiv 2506.08312) App. C.3 notes that
in practice PE maintains a synthetic set of size `n_s ≠ n` and that **setting `n_s` correctly is
critical for convergence** — a parameter their own analysis cannot vary. So a parameter already
known to be utility-critical turns out to be privacy-relevant the moment the unit changes.

**DP-ICL — the number of exemplar subsets `S`.** DP-ICL (Wu et al., arXiv 2305.01639) partitions
exemplars into **disjoint** shards, each producing an answer, aggregated by report-noisy-max or a
noisy embedding mean. Its guarantee rests on each exemplar living in exactly one shard, so changing
one exemplar changes one answer: sensitivity 1, independent of `S`. Under user-level adjacency a
user with `m` exemplars lands in up to `m` shards and perturbs all of them — **sensitivity `m`, and
the disjointness argument degrades to record-level protection.**

The fix is obvious and free: **user-aware sharding** — assign all of a user's exemplars to one
shard, restoring sensitivity 1. What is *not* free, and what makes this more than a footnote, is
that it collides with DP-ICL's own stated open problem. Its Discussion leaves "the efficiency–utility
tradeoff for the choice of the number of subsets" to future work. Under user-aware sharding:

- `S` is **upper-bounded by the number of users**, not the number of exemplars.
- Shard sizes inherit the user-size distribution, so heavy users produce heavy shards and the
  ensemble's members are no longer exchangeable — which is the assumption the noisy-consensus
  aggregation leans on.

So `S`, a free utility dial at record level, becomes jointly a privacy and a
population-heterogeneity parameter at user level. **Same structural pattern as `|V|` in PE.** Two
instances is enough to state the theme without over-claiming a taxonomy.

**Cost: zero extra compute.** This is the closing section of `ideas/10`, replacing the weaker DP-ICL
paragraph in `ideas/09`. It answers "does this generalise past PE?" with a second mechanism, a
second citation, and a shared mechanism for why the gap exists.

---

## J2 — streaming Private Evolution under user-level DP: real, and too big for this deadline

The DP-fy guide §5.7 lists online/streaming DP synthetic data as an open problem and says that both
PE and DP inference are potentially suitable but, to the authors' knowledge, unexplored. That is a
genuine invitation from a credible source.

**Why it is attractive.** In streaming PE a user's data arrives across many rounds, so the same
person participates repeatedly. That is precisely the *multi-participation* problem that
federated learning solved with correlated-noise mechanisms — DP-FTRL and banded matrix
factorisation, with a min-separation constraint between a user's participations (the machinery in
the guide's own federated section). Importing it into PE would be a clean cross-pollination:
user-level streaming PE as a multi-participation continual-release problem.

**Why not now, stated honestly rather than as a hedge:**

1. **The adjacent area is crowded.** He, Vershynin & Zhu, *Online Differentially Private Synthetic
   Data Generation* (arXiv 2402.08012) already gives near-optimal 1-Wasserstein continual-release
   rates; there is also continual release from longitudinal collections (arXiv 2306.07884) and
   PrivStream. "Streaming DP synthetic data" is occupied even if "streaming PE" is not, and a
   workshop reviewer will ask for the delta on page one.
2. **The obvious import may not transfer.** Matrix-factorisation mechanisms win on the *prefix-sum*
   workload. PE releases `T` histograms over **different, algorithm-generated candidate pools**, so
   the queries are not a fixed linear workload and the standard MF gain does not follow. Claiming it
   without the derivation would be exactly the kind of thing this repo has been killing in others.
   Settling it is a research question, not a week's work.
3. It needs a temporal corpus and a genuinely different experimental harness.

**Verdict: park with the reasoning attached.** This is the natural next paper after the lead, and
the lead's user-level analysis is a prerequisite for it. Recording it so round 8 does not
re-discover it and mis-price it as cheap.

---

## J3 — recorded and deliberately not taken

- **Variation without prompt engineering** (guide §5.7, and Tab-PE App. E on distance functions).
  Real open problems, but they are utility engineering, not privacy. Wrong committee — see
  `notes/06`.
- **Long-form DP synthetic text; DP synthesis without pretrained LLMs** (guide §5.7). Both are
  large research programmes, neither is inference-time-privacy-theoretic.
- **Data-dependent packing breaking per-example clipping** (guide §7.3, on packing
  embedding-similar documents together). Genuinely a sensitivity bug class and genuinely
  interesting — but it is training-time, which is the paradigm this workshop exists to move past.
- **Stronger MIAs / auditing datasets for DP synthetic text** (arXiv 2508.20452 §5). Crowded, and
  `lit/01` already killed the neighbouring empirical-auditing ideas.
