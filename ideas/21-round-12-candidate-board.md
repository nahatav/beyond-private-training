# Round 12 — candidate board after the six-agent sweep

Scored against `notes/11`. Acceptance `A: x/30`, general-safety relevance `B: y/25`, reported
separately and never averaged. Gate **G1** (name the two nearest neighbours *outside* AI safety) is
applied to every candidate, because it has now killed three consecutive leads.

Status: four of six sweeps returned; CoT-monitoring and white-box-monitoring sweeps still out.
This board is provisional and will be revised when they land.

---

## Corrections to our own records — the sweep caught two

**`2509.21344` was mischaracterised in `ideas/19` and in memory.** Actual title: *Linear probes rely
on textual evidence: Results from leakage mitigation studies in language models* (Boxo, Neelappa,
Raval; v1 2025-09-16, **v2 2026-03-09**). The **0.94 → 0.57 AUROC collapse is the model-organism
comparison** — probes score 0.57 on trained organisms that emit no behavioural verbalization, versus
0.94 unfiltered. **Filtering alone gives only a 10–30 point reduction.** Our note said the collapse
happened "once textual evidence is filtered," which overstates the filtering result by roughly 2×.
Load-bearing: the dramatic number requires *retraining a model organism*, not applying a filter.

**`2608.29461` is narrower than recorded.** Actual title: *A Causal Model for Locating and Unlocking
Sandbagging in Model Organisms* (Tan, Le, Williams-King; 2026-08-29). The **28/33** figure covers
**only prompted, fine-tuned and RL-trained locks** (median held-out recovery 96%). Against a
**circuit-breaking** lock "the single-layer graft **fails at every layer**" — because circuit breaking
rewrites state through a *band* of layers. They introduce **context grafting** (replaying the
password's cached KV activations), which does recover, and is "surprisingly insensitive to the exact
password content." Companion paper we had missed: **`2608.29458`** *Reference-Grafting Matches
Fine-Tuning at Eliciting Sandbagged Capabilities* (Le, Tan, Williams-King, same day) — 11
password-locked models 1.5–32B, **+94 to +101%** of the honest–sandbagging gap recovered with **2–5
paired examples** and no weight updates.

---

## C1 — Does the sandbagging probe just read evaluation-awareness? **(current front-runner)**

**Claim.** The linear sandbagging probe's performance is (or is not) mediated by the
evaluation-awareness direction. Erase the eval-awareness subspace from activations before scoring the
sandbagging probe; measure how much of the 0.94 survives.

**G1 — nearest neighbours outside AI safety. PASSES.** This is the first candidate whose *method* is
standard and whose *claim* is unoccupied — the inverse of the shape that killed the last three ideas.
- **Elazar, Ravfogel, Jacovi, Goldberg — *Amnesic Probing: Behavioral Explanation with Amnesic
  Counterfactuals*** (arXiv **2006.00995**, 2020). The erase-a-property-then-measure-behaviour method.
- **Hewitt & Liang — *Designing and Interpreting Probes with Control Tasks*** (arXiv **1909.03368**,
  EMNLP 2019). The placebo/control methodology that makes the result credible.
- Modern erasure: **2506.11673** (*Improving Causal Interventions in Amnesic Probing with Mean
  Projection or LEACE*) — use **LEACE**, not naive projection. And **2606.13720** (*Refusal Beyond a
  Single Direction: Diff-in-Means vs INLP*, Jun 2026) is a same-year template for exactly this
  manoeuvre in the safety domain.
- **The claim itself is empty:** `abs:"evaluation awareness" AND abs:"probe" AND abs:"ablat"` →
  **zero results**; `abs:"evaluation awareness" AND abs:"sandbagging"` → **one** result
  (`2603.03824`, about *inducing* eval-awareness in-context, not probing it).

**Why both directions publish.** Mediation ⇒ white-box sandbagging monitors are eval-awareness
detectors in disguise, which reframes the threat model for every probe-based monitor. No mediation ⇒
the two most-cited latent directions in this literature are independent, a clean negative that
constrains everyone's design space.

**Mandatory design constraint.** `2607.25907` reports that a **placebo random direction suppresses as
hard and shifts behaviour as far** as a real eval-awareness direction. The random-direction control at
matched norm is not optional — without it a reviewer kills the paper, and rightly. Second constraint:
`2608.27340` finds eval-awareness splits into capabilities-flavoured and safety-flavoured variants
with a **+24 to +46 pp** compliance gap, so erase the two subspaces separately as well as jointly.

**Cost.** ~30 A6000-hours ≈ **$10**. Probe fitting is minutes. Far under budget — the surplus should
buy models and seeds, not scope.

**Scores.** A: novelty 5, scoop-resistance 4, outcome-robustness 5, venue fit 4, executability 5,
claim discipline 4 → **27/30**. B: decision-change 4, generality 4, capability-scaling 4,
threat-model honesty 4, citability 4 → **20/25**. Gates: G1 ✅ G2 ✅ G3 (artifacts confirmed) G4 n/a
G5 ✅.

---

## C2 — Context grafting versus RMU unlearning

**Claim.** Single-layer reference grafting fails against RMU (as `2608.29461`'s circuit-breaker row
predicts), but **context grafting recovers WMDP capability from `cais/Zephyr_RMU`** with no weight
updates.

**G1.** Nearest outside neighbours are the model-tampering and concept-erasure-robustness literatures
— `2502.05209` (model tampering attacks incl. latent-space attacks vs. unlearning) and `2605.24614`
(Unlearning Depth Score, 150 unlearned models, 8 methods). Adjacent and crowded, but
`abs:"grafting" AND abs:unlearning` → **zero results**. Passes, narrowly.

**The problem: scoop risk is severe.** `2608.29458`'s conclusion names this as *their* open problem
verbatim — "The open problems are an honest reference in the wild and a defence: defeating
circuit-breaking" — and that three-author group shipped **two papers on the same day** eight days ago.
Move first or not at all.

**Scores.** A: novelty 4, scoop-resistance **1**, outcome-robustness 4, venue fit 4, executability 5,
claim discipline 4 → **22/30**. B: **21/25**. Gates: all pass, but scoop-resistance is the binding
risk and it is not a gate — it is a bet.

---

## C3 — Do non-linear white-box monitors also depend on textual evidence?

Cashes `2509.21344`'s own future-work request verbatim: "evaluating other white-box architectures
(Activation Oracles, Attention Probes, Sparse Autoencoders) to determine whether reliance on textual
evidence is specific to linear probes." Generalises "linear probes are brittle" to "white-box monitors
are brittle" — a much stronger safety claim — or produces a positive result the monitoring agenda
needs. ~$30–50 including one LoRA model organism.

**A: 24/30, B: 20/25.** Held pending the white-box sweep, which may find this occupied.

---

## C4 — Ensembles versus adaptive prompt injection on trusted monitors

Two AI-control papers point at each other and neither ran it: `2510.09462` proposes ensembling as the
mitigation; `2605.15377` states "We did not red-team our ensembles against an adaptive adversary with
knowledge of the monitoring system."

**G1 — WEAKENED, do not lead with this.** Outside AI safety the answer is substantially predicted:
- **`2504.18333`** *Adversarial Attacks on LLM-as-a-Judge Systems* **already recommends "multi model
  committees"** as the mitigation and reports **50.5–62.6% attack transferability** — which is exactly
  what makes ensembles fail.
- **`2403.17710`** *Optimization-based Prompt Injection Attack to LLM-as-a-Judge* (**CCS 2024**,
  JudgeDeceiver) shows known-answer, perplexity and windowed-perplexity defences are all insufficient.
- **`2606.25487`** flips LLM-judges 57–100% with benign framing wrappers and 70% of a dedicated
  classifier's confident true positives via GCG.
- Plus the whole adversarial-ML prior that ensembles do not survive adaptive attacks.

**A: 19/30, B: 18/25.** Not dead — the control-protocol version with a safety–usefulness Pareto is
genuinely untested — but the headline would be a result three literatures already expect.

---

## C5 — Legibility-protocol comments as an injection channel into the trusted monitor

`2602.10153` shows commenting improves trusted monitoring, mandates that U write comments, and
declines to test the obvious attack twice ("We do not study how using comments may allow U to
jailbreak T").

**G1 — WEAKENED.** `2606.19235` (*CodeSentinel*, Jun 2026) already establishes attackers hiding
instructions "in comments, strings, identifiers, or decoy code" in code contexts, and ships a defence.
`2510.09462` already established adaptive injection subverts control protocols. What survives is the
narrower point that a *published safety improvement mandates the channel* — real, but a specific
instance of a known result.

**A: 21/30, B: 19/25.**

---

## Calibration finding worth keeping

The sweeps independently converged on the same read: the sharpest recent work in both territories is
**single-author or three-author, open-weight, ≤32B, with a placebo control** — `2607.06596`,
`2608.16190`, `2605.27958` (solo, Gemma-3 1B–27B), `2607.25907` (four authors, one model pair, and its
headline is a *negative* result about a placebo). Those are all affordable at this budget. What is out
of reach: Apollo's SFT+RL distillation, GDM's multi-service environments, UK AISI's 70B organisms,
frontier-scale monitor evaluation.

**The winning form is a sharp mechanism claim on 1–3 open-weight models with a proper control — not
breadth.** This is also why the $200–300 should not be spent on more models: `notes/11` already says
breadth is padding, and every exemplar above confirms it.

## Artifacts confirmed live (sweep-verified)

| Artifact | Status |
|---|---|
| `cais/Zephyr_RMU` (HF) | ✅ loads, 3 safetensors shards, fits a 4090 in bf16. The WMDP RMU baseline. |
| `clarifying-EM/model-organisms-for-EM` (GitHub) | ✅ actively maintained, last push 2025-09-22. **No HF org models** — weights live elsewhere. |
| `ApolloResearch/deception-detection` (GitHub) | ⚠️ exists but **last push 2025-02-11**, ~19 months stale; assume `transformers` API drift. No license file. |
| `RoganInglis/apps-control-arena` (HF) | ✅ 5,000 rows, ungated (retained from `ideas/20`). |
