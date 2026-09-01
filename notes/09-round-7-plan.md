# Round 7 decision and execution plan

**6 days to the regular deadline (2026-09-07 AoE).** Ideation stops here; this round converts the
portfolio into a schedule with explicit cut lines.

## The decision

**Write `ideas/10` — "Normalising Users Changes What Private Evolution Estimates".**

The reasoning, compressed:

- The lead survived a direct hit. `lit/03` found the DP-fy guide already states a user-level recipe
  for PE, which retracts the old novelty claim, and `ideas/11` found that the guide's recipe
  dominates the mechanism this repo had been developing. Two rounds of work were invalidated.
- What replaced them is stronger. The paper now has a **named, citable adversary** — fifteen Google
  authors, in a document this area will read — instead of an unremarked gap, and the result is
  "the recommended fix is not estimand-neutral", which is sharper than "there is no fix".
- The floor is high. Propositions 1–3 in `ideas/10` are elementary algebra that no experimental
  outcome can invalidate. The paper exists even if every measurement comes out boring.
- The house style fits. `notes/06` reads this committee as TPDP with an LLM skin, rewarding short
  exact notes of the form *here is a channel the accounting silently omits, here is where it bites,
  here is the fix*. This is exactly that shape.

Everything else in the portfolio is now either dead (C, D, E), folded in as an arm (B, G, the
DP-ICL corollary), or parked with reasons (J2 streaming, v3 code audit).

## The one measurement that picks the paper

From `ideas/11` §3. Before any figure is drawn, measure `d_u / (k·m_u)` — how far a user's effective
vote diversity sits below its ceiling.

| Outcome | Paper we write |
|---|---|
| `d_u ≪ k·m_u` (users cluster) | **Diversity tilt.** The guide's recipe weights users by the square root of their semantic diversity. Strong version. |
| `d_u ≈ k·m_u` | **Exponent ½.** The recipe is a covert contribution-scaling rule sitting between the two named privacy units, adopted without comment. Weaker headline, same equations, still a correction to the record. |

This costs roughly an hour and is the first thing to run. Both branches are writable, so the risk
here is to the headline, not to the submission.

## Schedule

| Day | Work | Compute | Droppable? |
|---|---|---|---|
| **1 (Sep 1)** | E0 code checks: confirm the vote construction against `dp_counter.py`; determine what the noisy-count threshold-and-subtract does once per-user normalisation makes counts non-integer. Then E1a — the `d_u/(k·m_u)` ratio on the controlled arm. **Framing decided by end of day.** | ~1 GPU-hr | no |
| **2** | E1 full: re-weighting curves `w_u(p)` vs `d_u` for `p ∈ {1, 1.5, 2}` plus record-level, swept over within-group coherence and over `\|V\|`. Real anchor: arXiv abstracts by author (CC0). **Central figure done.** | ~1–2 GPU-hr | no |
| **3–4** | E2 compounding: 4 arms {record-level, ℓ₂, ℓ₁, diversity-floored} × `T` iterations, local 8B generator under vLLM, tracking per-iteration user representation. Claim 3. | ~2–4 GPU-hr/arm | **yes, first cut** |
| **5** | E3 utility at matched user-level ε, including the ε=0 prior baseline (`ideas/11` §5) — lift over the prior as a function of the privacy unit. | ~1 GPU-day | **yes, second cut** |
| **6** | Write. Four pages. | — | no |

**Cut order if the clock slips: E3, then E2.** Propositions 1–3 plus E1 plus the DP-ICL corollary is
already a complete short paper — a sensitivity family, an estimand table, one measured curve, and a
two-line mechanism. E2 and E3 upgrade it; they are not load-bearing. Deciding this now, rather than
at 3am on the 6th, is the point of writing it down.

## Paper skeleton (4 pages)

1. **Intro (0.75p).** PE is the flagship inference-time DP method and is deployed on genuinely
   user-structured data. Its adjacency is per-sample. The only stated user-level recipe is two
   sentences in a practitioner guide. State immediately that the recipe is valid but not
   estimand-neutral, and that the distortion survives ε → ∞ — pre-empting both obvious referee
   attacks in the abstract.
2. **The normalisation family (0.75p).** Prop. 1 sensitivity for all `p ∈ [1,2]`; Prop. 2 the
   estimand table (sample-uniform / user-uniform / diversity-tilted); Prop. 3 the bias–variance
   reading that makes the guide's choice defensible rather than wrong. Interaction with
   *Private Evolution Converges*.
3. **Measurement (1p).** E1: `d_u/(k·m_u)`, then the re-weighting curves over coherence and `|V|`.
   E2's drift plot if it exists.
4. **Diversity-floored normalisation (0.5p).** The mechanism, its sensitivity proof, and an explicit
   pointer to Liu et al. 2206.03008 for choosing `d₀` privately rather than re-deriving it.
5. **Beyond PE (0.25p).** J1: parameters that are privacy-neutral at record level and privacy knobs
   at user level — `|V|` in PE, shard count `S` in DP-ICL, with user-aware sharding as the fix.
6. **Limitations (0.25p).** `d_u` is embedder- and pool-dependent; we measure where data sits, we do
   not prove where it must; the real-data anchor is one corpus.

## Standing constraints, unchanged

Public datasets only, one local GPU, no experiments involving real people, nothing person-specific
reported. The controlled arm needs no identities and carries the weight; arXiv (CC0) supplies one
anchor point. Yelp stays dropped, OpenReview cannot support a user-level arm. Full reasoning in
`notes/08`, which round 7 did not change.

The `num_packing` modulo-folding hypothesis in `notes/08` stays out of scope and stays unpublished;
if it is ever confirmed it goes to the authors privately, not into a paper.
