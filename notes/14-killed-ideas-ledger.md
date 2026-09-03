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
| **Guard models cannot be operated at a low audit budget** (C6) | `2412.07724` **Granite Guardian** — ROC curves (Fig. 8); partial AUC + TPR at **fixed FPR 0.1 / 0.01 / 0.001** across **nine open guards** (Table 11, incl. 4× Llama Guard and 3× ShieldGemma); §6 argues threshold-free metrics mislead because "real-time applications have a strong need for low FPr"; cites `2404.17399` (Aerni et al.) for the low-FPR discipline. Adjacent: `2605.10901`, `2604.16542`, `2504.00441` | Killed in round 13. The proposed deliverable was published **Dec 2024**. Our negatives were transport-clean and space-wrong: Granite Guardian's *abstract* contains none of ROC/AUROC/pAUC/audit budget. See **R8**. |
| **Standalone LLM-written-DP-code auditing** | Saturated | — |
| Unaccounted model selection in PE; agentic compositional leakage; serving-layer / KV-cache / speculative-decoding / batch-numerics side channels (`2604.26505` Quantamination); CoT privacy; GUI-agent privacy | see `ideas/11`, `notes/10`, `lit/01` | — |

## Tier 2 — weakened, not dead (do not lead with these)

| Idea | Why weakened |
|---|---|
| **Ensembles vs adaptive prompt injection on trusted monitors (C4)** — ⛔ **PROMOTED TO DEAD, round 15.** `2510.09462` is *Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols* (Terekhov, Panfilov, Dzenhaliou, Gulcehre, **Andriushchenko**, Prabhu, Geiping — ICLR 2026), **not** "proposes ensembling as the mitigation": it *is* the attack, already run, already citing Tramèr 2020, with ensembling only in a future-work clause. **Andriushchenko is an EvoRobust invited speaker ⇒ hard G2 fail** (R7). The misdescription is an R1 violation — the citation was never opened. See `ideas/27` §3. *Row below kept for the round-13 reasoning.* |
| **Ensembles vs adaptive prompt injection on trusted monitors** | Two AI-control papers point at it (`2510.09462` proposes ensembling; `2605.15377` states "We did not red-team our ensembles against an adaptive adversary"). But `2504.18333` **already recommends "multi model committees"** and reports **50.5–62.6% transferability**; `2403.17710` (CCS 2024) shows judge defences insufficient; `2606.25487` flips judges 57–100%. Plus the adversarial-ML prior that ensembles fail against adaptive attacks. The answer is substantially predicted. |
| **Legibility-protocol comments as an injection channel** | `2606.19235` (CodeSentinel) already covers instructions hidden "in comments, strings, identifiers, or decoy code"; `2510.09462` already showed adaptive injection subverts control protocols. What survives is only that a published protocol *mandates* the channel. |
| **Sandbagging probe vs eval-awareness** (C1) | Pre-empted four ways. **Raut, LessWrong 2026-06-25** ran the ablation arm with **24 random-direction placebo controls** and got the null (p = 0.20; per-item sandbagging AUROC 0.542) — the placebo was our claimed differentiator. `2603.19426` owns the format-confound control; `2606.23583` owns representation-vs-behaviour decoupling with random controls over 37 models; `2603.03824` reports **99.3% of sandbagging causally driven by verbalized eval-aware reasoning**. Separately **G3 fails**: `2509.21344` releases no code or data. What survives is a reframe (representation-level mediation vs behaviour-level null), which still needs a trained model organism. |
| **The instillation-depth ladder** (C8) | Three of its four rungs are already in `2607.01033`'s own table (54 MOs, OLMo2-1B **and** gemma-3-1b-it, seven techniques incl. post-hoc SFT, post-hoc DPO and integrated DPO; AO/steering/logit-lens/SAE; expression-strength controlled). Its documented "substantial variance… even after controlling for expression strength" breaks a 4-point monotonicity test with one quirk; "switching the base model sometimes changes rankings" breaks the gemma replication; its own "likely too small" limitation contradicts our B3 = 5. Untested rungs are pre-training/SFT/RLVR — pre-training is out of budget and is the same group's obvious next paper. |
| **Non-linear white-box monitors** (C3) | Occupied: `2607.01033` already benchmarked activation oracles, steering, logit lens and SAEs across its MO suite. The residual textual-evidence axis needs `2509.21344`'s unreleased artifacts. |
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
- **ControlArena APPS split — ⛔ THIS CORRECTION WAS ITSELF WRONG (round 16).** Round 10's
  1,936 / 482 / **1,375** was filed here as a search-summary artifact, corrected by
  `RoganInglis/apps-control-arena`'s single 5,000-row split. But `2608.16190` reproduces a
  **1,375-sample test split (172 attack / 1,203 honest)** from *"the public backdoored-APPS dataset
  released with Koran et al. (2026)"* — **a different artifact.** **Two distinct APPS-backdoor datasets
  exist, and any paper must say which it used.** `RoganInglis/apps-control-arena` does have one 5,000-row
  split; that part stands. Resolving which artifact is which is check **K1** in `notes/18` §3.
- **`2607.06596` is understated in the Tier-1 table above (round 16).** It is filed there as
  "cross-generator generalisation republished inside safety." Its **full text** also carries
  difficulty-matched and blatancy-matched controls, code-only vs full-transcript cuts, MLP/SVM/RF/
  gradient-boosting head swaps, and hash-disjoint splits against same-task leakage. It is a much heavier
  paper than the row implies and is the **nearest neighbour** to the round-16 lead — see `lit/02` and
  check **K2**.
- **C9's G1 tick is void (round 16).** The out-of-field sweep returned **PARTIALLY OCCUPIED, severely**:
  four of five clauses published, and the construction is a **named method with its own lineage** —
  Forking Paths (`2412.07961` → `2510.27484` → `2608.19611`), plus `2511.04527`, `2601.21183` and
  `2511.14773`, which names our construction as future work in print. **The pair framing is dead.** C9 is
  not in this ledger — it is reframed and moved to November — but do not cite its old novelty tick.
- **`lit/01`'s "CoT privacy dead" verdict** targeted *PII-in-CoT only*. It does **not** extend to CoT
  monitoring as a safety mechanism — a different object.
- **`2603.03824` was mischaracterised.** `ideas/21` recorded it as "about *inducing* eval-awareness
  in-context, not probing it" and used it to support C1's empty-claim finding. Its abstract states that
  "CoT causal intervention confirms that **99.3% of sandbagging is causally driven by verbalized
  eval-aware reasoning**" — a mediation result on C1's **claim**, not merely its setup.
- **`2509.21173` has no confirmed venue.** This ledger attributed it to **ICML 2026**; the arXiv abstract
  page carries no venue field. ⚠️ on the venue until confirmed. Title and content are real (*Less Precise
  Can Be More Reliable*, >700k evaluation runs).
- **Both Compression-Tax outcome-robustness kills are VLM papers.** `2509.21173` is CLIP/VLM zero-shot
  classification; `2607.24440` is Qwen2-VL under image degradation. Using them against an *LLM-monitor*
  claim is a cross-modality inference. The Compression Tax stays dead — `2607.09786` kills it directly and
  in-modality — but these two are not equally strong and should not be listed as if they were.
- **`2509.21344` releases no code or data.** Its only GitHub links are LaTeXML and arXiv-feedback
  boilerplate. Recorded below as ❌, not as an available harness.
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
| `maxf-zn/misalignment_monitoring` (GitHub) | ✅ HTTP 200, last push 2026-07-02. `2606.30449`'s release — the C9 starting point. |
| `2509.21344` probe / model-organism code | ❌ **no release.** No code, no data, no artifact statement in the paper. Blocks C1 and C3. |
| `ApolloResearch/deception-detection` (GitHub) | ⚠️ exists but last push 2025-02-11 (~19 months stale); expect `transformers` drift; no license file |
