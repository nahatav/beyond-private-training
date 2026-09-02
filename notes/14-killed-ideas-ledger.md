# Killed ideas — consolidated ledger

One place for everything this repo has killed, with the evidence that killed it. Consolidated from
`ideas/11`, `ideas/13`, `ideas/16`, `ideas/19`–`ideas/22`, `notes/10` and `lit/01`–`lit/03`.

**Read this before proposing anything.** Reviving a dead idea without new evidence is the single
cheapest mistake available.

---

## Tier 1 — killed by the literature (a published paper makes the claim)

| Idea | Killed by | Note |
|---|---|---|
| **Compression Tax — headline** ("quantizing a monitor degrades catch rate faster than capability") | `2607.24440` (VLM, 4-bit: accuracy −1.6pp, error-detection AUROC 0.95→0.80, framed as selective-prediction operating points); `2602.01459` (ViT OOD, 19.2% AUPR-out delta); `2606.01850` (compression decouples accuracy from uncertainty); `2602.09130` **EMNLP 2026 Main** (performance–reliability decoupling); `2607.09999` (silent failures at preserved accuracy) | Round 10 declared it scoop-clean after sweeping **AI control only**. The claim lived in compression evaluation. |
| **Compression Tax — fallback decomposition** (emission failure / score-resolution collapse / true discrimination loss, with "read the score from logits") | `2606.22179` **Score Granularity Gap** — asks verbatim "at what resolution can the score be thresholded?", 7 confidence constructions incl. verbalized vs token-probabilities, 25 model-dataset pairs; `2603.12520` (coarse scoring → ties in **67%** of pairwise comparisons); `2604.25235` ("ranking–scoring decoupling" via score-token log-probs); `2608.17270` (logit-based scoring beats prompted judging for ranking) | Every leg taken, including the proposed fix. |
| **Compression Tax — third and fourth independent claims** | `2607.09786` *Length Penalties Make CoT Less Monitorable* (monitor hint-detection 69%→49%, **already runs the length-matched control**, names it "a compression and monitorability frontier"); `2601.00282` (quantization vs self-explanation faithfulness, with user study) | Five independent claims across three literatures. The kill is overdetermined. |
| **Outcome-robustness of the Compression Tax** | `2509.21173` **ICML 2026**, >700k runs — quantization can *improve* accuracy, calibration, OOD detection and noise robustness | The "green light" direction was already published, so a null result stopped being a second paper. |
| **`ideas/16` decoding-truncation breaks the LLM exponential mechanism** | **InvisibleInk** `2507.02974` (NeurIPS 2025) states the ε=∞-under-truncation fact verbatim as its Top-k+ motivation | Falsified its own "nobody states this" claim. |
| **MIA on safety classifiers** | `2605.22373`, author list includes **Niloofar Mireshghallah — an InfPriv organizer** | Gate G2. Hard kill. |
| **Activation / embedding-inversion PII extraction** | `2507.16372` (USENIX Sec '25, 4,112-token medical prompt at 86.9 F1); `2604.23711` Spore | — |
| **Membership inference via reasoning traces** | `2601.13607`, ACM Web Conf 2026, two new datasets | With the PII-in-CoT kill, the CoT-privacy door is shut from both sides. |
| **Contextual integrity for agents** | 7+ benchmarks/surveys 2025–26; Mireshghallah's turf | Gate G2. |
| **Unlearning + DP auditing** | Oversaturated; organizer Eli Chien's line | Gate G2. |
| **Whole private-RAG line** | `2412.04697` + `2511.07637` — organizers Ruihan Wu + Kamalika Chaudhuri | Gate G2. |
| **Localised deception probes** | `2604.14865` (Segment-Level Coherence) already published the "require multiple evidence tokens, not isolated spikes" objective; generic multiple-instance-learning localisation outside safety | Killed by a round-12 sweep on its own proposal. |
| **Adversarial probe-evasion training** | The adaptive-attack canon (Carlini/Tramèr); `2505.14300` already ran red-team evasion plus an ensemble defence | Killed by a round-12 sweep on its own proposal. |
| **Label-free lineage calibration for monitors** | The phenomenon is thoroughly published as cross-generator generalisation failure in machine-generated-text detection; `2607.06596` already re-published it inside safety | Killed by a round-12 sweep on its own proposal. |
| **Standalone LLM-written-DP-code auditing** | Saturated | — |
| Unaccounted model selection in PE; agentic compositional leakage; serving-layer / KV-cache / speculative-decoding / batch-numerics side channels (`2604.26505` Quantamination); CoT privacy; GUI-agent privacy | see `ideas/11`, `notes/10`, `lit/01` | — |

## Tier 2 — weakened, not dead (do not lead with these)

| Idea | Why weakened |
|---|---|
| **Ensembles vs adaptive prompt injection on trusted monitors** | Two AI-control papers point at it (`2510.09462` proposes ensembling; `2605.15377` states "We did not red-team our ensembles against an adaptive adversary"). But `2504.18333` **already recommends "multi model committees"** and reports **50.5–62.6% transferability**; `2403.17710` (CCS 2024) shows judge defences insufficient; `2606.25487` flips judges 57–100%. Plus the adversarial-ML prior that ensembles fail against adaptive attacks. The answer is substantially predicted. |
| **Legibility-protocol comments as an injection channel** | `2606.19235` (CodeSentinel) already covers instructions hidden "in comments, strings, identifiers, or decoy code"; `2510.09462` already showed adaptive injection subverts control protocols. What survives is only that a published protocol *mandates* the channel. |
| **Context grafting vs RMU** | Not scooped (`"grafting"`+`"unlearning"` → 0) but **scoop-resistance 1/5**: `2608.29458`'s conclusion names it as their own open problem, and that three-author group shipped two papers on the same day. Run it immediately or not at all. |

## Tier 3 — alive, parked (survived review, not currently the lead)

From `ideas/13` and `notes/10`, retained for completeness: Tab-PE label-distribution leak
(`ideas/17`); referent-level exposure measured vs mention-frequency; constructive falsification
extending DPrivBench with a StatDP-graded witness. **The PE/InfPriv paper (`ideas/14`) is not dead** —
it is nearly written and ~$30 to run; it is an interest-fit problem, not a research one.

---

## Corrections to our own records

Recording these because acting on a mis-remembered number is as costly as a hallucinated citation.

- **`2509.21344`** is *Linear probes rely on textual evidence* (Boxo, Neelappa, Raval; v2 2026-03-09).
  The **0.94 → 0.57 AUROC collapse is the model-organism comparison**, not filtering. **Filtering
  alone gives only 10–30 points.** Earlier notes overstated the filtering result by roughly 2×. The
  dramatic number requires *retraining a model organism*.
- **`2608.29461`** is *A Causal Model for Locating and Unlocking Sandbagging in Model Organisms*. The
  **28/33** figure covers **only prompted, fine-tuned and RL-trained locks**. Against a
  **circuit-breaking** lock "the single-layer graft **fails at every layer**." They introduce
  **context grafting** instead. Companion `2608.29458` was missed entirely.
- **ControlArena APPS split.** Round 10's 1,936 train / 482 val / 1,375 test at 50% attack rate came
  from a search summary. The real `RoganInglis/apps-control-arena` card shows **one 5,000-row split**.
  Construct and report your own splits.
- **`lit/01`'s "CoT privacy dead" verdict** targeted *PII-in-CoT only*. It does **not** extend to CoT
  monitoring as a safety mechanism — a different object.
- **`2607.06596`** contains **zero** occurrences of quantiz*/8-bit/FP16/AWQ/GPTQ. A search engine
  attributed a quantization finding to it; that attribution was false.

---

## Retained assets from dead ideas

Dead ideas leave usable infrastructure. Reuse rather than rebuild:

| Asset | Status |
|---|---|
| `RoganInglis/apps-control-arena` (HF) | ✅ 5,000 rows, ungated, labelled honest + backdoored solutions |
| DSPy tutorial *GEPA for Code Backdoor Classification* | ✅ working end-to-end trusted-monitor harness |
| `cais/Zephyr_RMU` (HF) | ✅ loads, fits a 4090 in bf16; the WMDP RMU baseline |
| `clarifying-EM/model-organisms-for-EM` (GitHub) | ✅ maintained; **no HF org models** — weights live elsewhere |
| `arrrlex/models-under-pressure`, `MaheepChaudhary/eval-aware-evasion` | ✅ HTTP 200 |
| `ApolloResearch/deception-detection` (GitHub) | ⚠️ exists but last push 2025-02-11 (~19 months stale); expect `transformers` drift; no license file |
