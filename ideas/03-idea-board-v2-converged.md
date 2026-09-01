# Idea board v2 — converged direction + experimental design

## Title candidates
1. **You Can't Test Your Way to ε: Auditing LLM-Written Implementations of Inference-Time DP**
2. ε on Paper, ∞ in Practice
3. No Opacus for Inference

Working name for the artifact: **SILENT-ε**.

---

## The one-paragraph pitch

Training-time DP consolidated onto a few heavily-audited libraries; inference-time DP has none.
Private Evolution, DP-ICL, private prediction and private RAG are each re-implemented per
deployment, increasingly with LLM assistance — and DP is the worst domain in which to do that,
because a broken DP implementation emits output that is statistically indistinguishable from a
correct one. No test fails. We build a suite of inference-time DP mechanism specifications, have
LLMs implement them, and audit the results with a grey-box record-replay falsifier and black-box
empirical-ε estimation. We measure how often model-written mechanisms are not DP at the claimed ε
while passing utility tests and the model's own code review; we quantify the gap between a model's
ability to *judge* a mechanism (DPrivBench) and to *produce* one; and we show that a repair loop
driven by an empirical auditor drives measured violations to zero without fixing the mechanism.

## Why this is the right paper for *this* venue

DPrivBench (arXiv 2604.15851) is by organizer **Erchi Wang**, and the CFP name-checks it under
"AI for Privacy". Its future-work section states, verbatim:

> "how effectively LLMs can detect such implementation-level privacy violations, as well as
> generate correct and faithful implementations"

and

> "implementation-level automation ... subtle coding errors ... can completely invalidate its
> privacy guarantees"

We are answering the open question an organizer wrote down. Using DPrivBench's own model roster
(GPT-5, Gemini-3-Pro, Claude-Opus-4.5/Sonnet-4.5, DeepSeek-R1/V3.1, Qwen3-30) makes the
generator–verifier comparison apples-to-apples against their published judgment accuracies
(Cat-1: GPT-5-High 0.995; Cat-2: F1 ≈ 0.74).

## The theoretical spine (this is what makes it not-a-benchmark)

Deciding DP is not merely hard, it is *provably* out of reach of the verifiers being proposed:

- **Gaboardi, Nissim & Purser** — deciding ε-DP for *loop-free* probabilistic programs is
  **coNP^#P-complete**. Even the easy fragment is beyond any practical checker.
- **Gilbert & McMillan (Allerton 2018)** — with black-box access, *any privacy guarantee that can
  be efficiently verified is also efficiently breakable*. Verification demands a compromise from
  either the verifier or the algorithm owner.

Hence DP code generation is the canonical task with a **sound-but-incomplete-free** verifier:
you can only falsify, never confirm. Standard LLM self-improvement (generate → test → repair)
therefore has no fixed point at "correct" — it has a fixed point at "not caught". That is a
falsifiable prediction, and claim **C4** tests it directly.

## Human baseline (the comparison, not the rebuttal)

Experts get this wrong too, and that strengthens rather than weakens the paper:
- **Lyu, Su & Li (PVLDB 2017)**: of six *published* Sparse Vector Technique variants, **only two**
  satisfy DP at the intended parameter.
- **Grey-box auditing (arXiv 2602.17454)**: 13 privacy violations across 12 maintained
  open-source DP libraries (SmartNoise, Synthcity, diffprivlib, Opacus, MOSTLY AI, Private-PGM…).
- **Mironov (CCS 2012)**: all four general-purpose DP systems of the day were breakable via
  floating-point artefacts of the Laplace sampler.

So the honest framing is: DP implementation is *already* an unreliable human process; the question
is what happens when it is delegated to a model and the reviewer is also a model.

---

## Claims

- **C1 — Silent failure.** A substantial fraction of model-written inference-time DP mechanisms
  violate the claimed ε while passing (i) utility tests and (ii) LLM code review.
- **C2 — Generator–verifier gap.** Models that judge canonical mechanisms accurately fail to
  produce them, and fail to detect the violation in their own output.
- **C3 — Inference-time-specific failure modes.** Failures are not generic coding bugs. Expected
  taxonomy: per-query vs. total budget confusion; data-dependent thresholds; un-noised
  nearest-neighbour/top-k selection; releasing intermediate retrieval scores; selection and
  stopping steps omitted from the accounting; record- vs. user-level adjacency confusion;
  insecure float noise sampling.
- **C4 — Auditor overfitting.** Falsifier-in-the-loop repair drives *measured* violations toward
  zero while expert-confirmed and held-out-auditor violations persist.

C4 is the load-bearing result. It generalises past this paper: **you cannot bootstrap a privacy
guarantee out of empirical auditing**, which is a direct caution to the "AI for Privacy" agenda
this workshop is promoting.

---

## Mechanism suite (all inference-time, all from the workshop's own topic list)

**Tier 1 — primitives that inference-time pipelines are assembled from**
1. Laplace / Gaussian mechanism for a counting query
2. Report-Noisy-Max / exponential mechanism, top-1 selection
3. DP top-k selection (private RAG retrieval)
4. Sparse Vector Technique, above-threshold (the classic trap)
5. Stability-based / thresholded DP histogram release

**Tier 2 — the actual inference-time mechanisms**
6. Private Evolution's DP nearest-neighbour histogram (noisy voting over candidates)
7. PE's T-iteration loop with composition accounting
8. DP-ICL: disjoint exemplar shards → ensemble → report-noisy-max over answers
9. DP-ICL embedding-space aggregation (noisy mean of embeddings)
10. DP few-shot / private synthetic generation
11. Private RAG: DP retrieval + DP aggregation
12. Exponential-mechanism DP decoding over next-token logits
13. Private prediction with an explicit query budget + accountant
14. **User-level** adjacency variant of one of the above (tests unit-of-privacy comprehension)
15. Subsampling amplification + RDP/PLD composition accounting

Each spec ships: natural-language task, function signature, **explicit adjacency definition**,
target (ε, δ), and a reference implementation held out from the model.

## Audit harness

- **(a) Grey-box record-replay.** Instrument the generated program; run on neighbouring D, D′
  under an identical frozen RNG stream; assert that every pre-noise quantity meant to be
  data-independent is invariant, and that the claimed sensitivity holds over a search of
  neighbour pairs. Directly falsifies data-dependent control flow and sensitivity errors.
- **(b) Black-box empirical ε.** For scalar/low-dimensional outputs, DP-Sniper-style classifier
  over many samples on adversarially-searched neighbour pairs; report ε_emp with
  Clopper–Pearson intervals. Records ε_emp = ∞ separately (deterministic distinguishers).
- **(c) Expert labels.** Hand-label a stratified subsample. **Essential** — the auditors are
  unsound, so we must report auditor *recall*, not just violation counts. This is also what
  makes C4 measurable.
- **(d) Standard-QA arm.** Utility tests + LLM code review, to establish the silent-failure rate.

## Metrics
`SoundRate` · `SilentFailRate` · distribution of `ε_emp / ε_claimed` (with an ∞ bucket) ·
`GVGap` = judge-accuracy − generate-accuracy on matched mechanisms · `SelfAuditAcc` ·
`RepairCurve`: measured-violation vs. expert-confirmed-violation across feedback rounds.

## C4 protocol, concretely
Auditor **A** returns a counterexample (neighbour pair + distinguishing event). Model patches.
Re-audit with **A** → violation rate falls. Re-audit with held-out auditor **B** (different
neighbour search, different adjacency family, grey-box where A was black-box) and with expert
labels → violation persists. Predicted failure mechanism: the model special-cases the reported
pair, clamps the specific output, or adds noise only on the tested path. The A–B gap *is* the
result.

## Scope for 7 days
~10 mechanisms × ~6 models × ~10 samples ≈ 600 programs. Tier-1 mechanisms are scalar and
vectorise, so auditing is cheap and GPU-friendly. Open-weight generators (DeepSeek-V3.1,
Qwen3-30-Instruct/Think) run locally and are sufficient on their own; frontier API models are an
upgrade, not a dependency.

**Engineering caveat:** generated code is untrusted and must be executed in a sandbox
(subprocess + resource limits + no network). Non-negotiable.

## Open decisions for the user
1. **Frontier API access?** If available, the DPrivBench roster gives a direct comparison; if not,
   the open-weight arm still supports every claim.
2. **Do we also audit published research implementations** of inference-time DP (DPSDA, DP-ICL
   repos)? Highest-impact arm, but it means making public claims about named third-party code —
   it would need airtight findings and responsible disclosure first. Recommend: **not in v1.**
