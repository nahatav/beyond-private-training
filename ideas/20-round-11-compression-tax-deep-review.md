# Round 11 — deep review of "The Compression Tax", and the final plan

Brief: (1) enumerate every AI-safety-relevant venue still open past Sep 5; (2) evaluate the
Compression Tax lead against **all** adjacent literature, not just the AI-control literature;
(3) decide toss vs implement.

**Headline of this round: `ideas/19`'s scoop patrol searched the wrong neighbourhood.** It swept the
AI-control literature (2506.05296, 2607.06596, 2605.15377, 2602.10153), correctly found zero
quantization content, and concluded the phenomenon was unmeasured. The phenomenon *is* measured —
repeatedly — in the **model-compression evaluation** literature, which round 10 never searched.
The lead's headline claim as written is falsified. A narrower claim survives. Details below.

---

## 1. Venues still open with a deadline strictly after Sep 5, 2026

Source: `blog.neurips.cc/2026/08/10/announcing-the-neurips-2026-workshops/` (102 workshops across
Sydney/Paris/Atlanta), cross-checked against `aiworkshoptracker.com/conference/neurips/`, then each
candidate's own CFP page fetched directly. Tracker times are UTC; AoE = UTC−12.

| Venue | Deadline (AoE) | Format | Fit for this paper |
|---|---|---|---|
| **AIWILD** — 3rd Workshop on Agents in the Wild | **Sep 5** (extended from Aug 29) | 9pp regular / **4pp short**, non-archival, WIP welcome | Best *topical* fit: CFP names "Agent safety, alignment, **control**, and oversight" verbatim. Not past Sep 5 — listed for comparison. |
| **SLM-Agents** — 1st Workshop on SLMs for Agentic Systems (Paris) | **Sep 6** (extended from Sep 5) | **4pp short** / 6pp long, non-archival, OpenReview opt-in | **Best combined fit.** CFP open-problems list names verbatim: *"Compression and distillation: quantization, pruning, knowledge distillation"* and *"Privacy, safety, robustness and applications"*. A cheap quantized monitor **is** an SLM agent component. |
| **InfPriv** (the incumbent) | **Sep 7** | 4pp, non-archival | Privacy only. Home of the PE paper (`ideas/14`), not this one. |
| **EvoRobust** — Self-Evolving Diversity-Driven Search for Robust AI Systems (Sydney) | **Sep 12** | **4pp** (5pp camera-ready), non-archival, concurrent submission allowed | Medium. Topics include "Diversity and coverage metrics for safety evaluation" and "Safety and robustness of tool-using and autonomous agents", but the workshop's spine is *search / quality-diversity algorithms*. We are not a search paper. Usable as a late fallback, not a first choice. |
| **VERICODEGEN** — AI for Verifiable Coding (Atlanta) | **Sep 13** (abstract Sep 12) | own template | Weak. Spine is proof assistants, model checkers, SAT/SMT. An LLM suspicion-scorer is not machine-checkable verification. |
| **InfPriv fast track** | **Sep 26** | 4pp + NeurIPS reviews appended | Requires a NeurIPS main-conference submission to attach. Not applicable. |
| **ICLR 2027** | abstract **Sep 18** / full **Sep 25** | full archival conference paper | Real option, but a 4-page measurement is not an ICLR paper. |
| **IEEE SaTML 2027** | abstract **Sep 22** / full **Sep 29** | full archival conference paper | Much higher bar; would need the full protocol-level story. |

**Closed, recorded so they are not re-checked:** JUDGe 2026 "Can We Trust the Judge?" (Aug 29 —
*painful*, its CFP names "adversarial robustness of safety evaluators"); Resource-Aware Agentic AI
(Aug 29); TAI-Eval (Aug 29); Who Verifies the Agents? (Aug 29); FLMSec (Aug 27); InterpScience
(Sep 1); PriLOM (Sep 4); ODI On-Device Intelligence (Sep 5); ATTRIB (Sep 5); IAB (Sep 5);
Pre-to-Post and FLLMPT post-training (Sep 5); Meta-Agents (Sep 5); FAST (Sep 5); LIGHT and AXIOM
(both efficiency-focused, both before Sep 5).

**Net venue finding:** the clock is one day longer than round 10 believed, and the extra day buys a
*better-fitting* venue, not a worse one. SLM-Agents (Sep 6) is the only post-Sep-5 venue whose CFP
names both halves of this paper.

---

## 2. The literature verdict — the headline claim is taken

`ideas/19` §3 asserts: *"Nobody has measured what quantization does to the metric that actually
matters"*, and *"The actual thesis: tail metrics degrade before mean metrics. A monitor can look
intact on general benchmarks while its catch rate has collapsed."*

That thesis, stated at that generality, is **published at least five times**.

### 2.1 The direct precedents (all verified by fetching the abstract page or full text)

| Ref | What it establishes | Damage |
|---|---|---|
| **`2607.24440`** — *Bigger or Cheaper? Scale and Quantization Effects on Uncertainty Signals in VLMs Under Image Degradation* (M M Asif Ferdous, 27 Jul 2026) | "4-bit quantization is **nearly free for accuracy (−1.6 points) but expensive for the confidence signal** (internal AUROC **0.95 → 0.80**)." Frames results as **selective-prediction operating points**. Argues "**error-detection AUROC, not calibration error, is the metric that exposes the difference**." Gives the fixed-memory-budget recommendation: prefer the larger quantized model. | **Severe.** This is the Compression Tax's thesis, framing, metric argument, and practitioner takeaway — in VLMs, five weeks before this round. Different domain (image degradation, no adversary, no audit budget), same intellectual claim. |
| **`2602.01459`** — *Understanding ViT quantization robustness through the lens of OOD detection* (Kuang & Wong, Waterloo, 1 Feb 2026) | FP32→4-bit: AUPR-out deltas of **19.2%** (DeiT3-IN22k) and **15.0%** (ViT-IN22k) vs **12.0%/9.5%** for IN1k variants. Detection degrades faster than in-distribution metrics. | Severe for "detection degrades faster than accuracy" as a *novel* claim. |
| **`2606.01850`** — *Does Compression Preserve Uncertainty? A Unified Benchmark for Quantized and Sparse LLMs via Conformal Prediction* (Tong et al., 1 Jun 2026) | 12 LLMs × compression configs × 5 tasks: "(I) compression frequently **decouples accuracy from uncertainty**; (II) larger models absorb compression-induced uncertainty better; (III) **uncertainty inflation is often threshold-like rather than gradual**." | Severe. This is the LLM-side decoupling claim, and (III) pre-empts the "cliff" story. |
| **`2602.09130`** — *UniComp* (von Rad, Cao, Geiger) — **EMNLP 2026 Main** | 7 compression techniques × 40+ datasets: "a deployment-critical **performance–reliability decoupling, where retained performance does not indicate preserved safety**, fairness and privacy." | Severe, and it is a main-conference paper, so reviewers will know it. |
| **`2607.09999`** — *Silent Failures in Quantized LLM Reasoning* (10 Jul 2026) | "PTQ can **silently alter how LLMs reason even when task accuracy is preserved**" — accuracy max 3.1pp drop while failure-mode composition shifts wholesale. | Takes the "your model passes the benchmark and is broken" rhetorical frame. |
| **`2509.21173`** — *Less Precise Can Be More Reliable* (Bouguerra et al.) — **ICML 2026**, >700k eval runs | The **opposite** direction: quantization can *simultaneously improve* accuracy, calibration, OOD detection and noise robustness; proposes a "spectral filtering" mechanism (damping high-rank components). | Not a scoop, but it destroys any claim that the sign of the effect is obvious — and it means a null/positive result is *less* interesting than round 10 assumed, because someone already published the positive direction. |
| **`2511.22483`** — *Enhancing Trustworthiness with Mixed Precision* (ASP-DAC 2026) | Quantization × 4 trustworthiness metrics incl. OOD robustness; proposes precision-ensemble voting (+5.8%). | Occupies the "so what do we do about it" half. |
| **`2407.04965`** — *Beyond Perplexity: Multi-dimensional Safety Evaluation of LLM Compression* (Xu et al., **Findings of EMNLP 2024**) | The origin of "don't evaluate compressed models on perplexity alone; safety behaves differently." | The lineage citation. Its existence means "evaluate compression on a safety metric" is a five-year-old idea, not a new one. |

### 2.2 The nearest thing to a *deployed-guardrail* precedent

**`2411.17713` — *Llama Guard 3-1B-INT4: Compact and Efficient Safeguard for Human-AI Conversations*
(Fedorov, Plawiak, Wu, Elgamal, Suda, Smith, Zhan, Chi, Hulovatyy, Patel, Liu, Zhao, Shi,
Blankevoort, Pasupuleti, Soran, Coudert, Alao, Krishnamoorthi, Chandra — Meta, 18 Nov 2024).**
Full text extracted and read.

- Meta shipped a **4-bit safety classifier**, 440MB, ≥30 tok/s on an Android CPU.
- Reported metrics are **F1 and FPR at a single operating point** across 9 languages. English:
  Llama Guard 3-1B **0.899/0.090** → 3-1B-INT4 **better** on both. No AUROC, no ROC curve, no
  fixed-budget catch rate — *the tail metric is exactly what they do not report.*
- The pipeline is **prune (16→12 layers, MLP 8192→6400) + QAT 4-bit + unembedding pruning
  (128k→20 outputs) + distillation from Llama Guard 3-8B**. It is **not** post-training
  quantization; quality is actively recovered by training.

**Reading:** this is simultaneously the strongest motivation and the strongest objection. The
objection a reviewer will raise is "Meta already ships a 4-bit guard and it beats the FP16 1B."
The rebuttal is real and is the paper's wedge: *QAT + distillation is not what a budget deployment
does.* A budget deployment downloads an off-the-shelf AWQ/GPTQ checkpoint and prompts it. Nobody
has measured **that**.

### 2.3 The AI-control neighbours (re-swept; `ideas/19`'s reads confirmed, two new)

Confirmed zero quantization content, as round 10 found: `2506.05296` (Control Tax), `2607.06596`
(Calibration-Family Overfit), `2605.15377` (Ensemble Monitoring), `2602.10153` (Basic Legibility).
Two new papers appeared that round 10 missed and that materially change the picture:

- **`2605.29601` — *Training Deliberative Monitors for Black-Box Scheming Detection*** (Sinha, Naik,
  Gillioz, Storf, Merkelbach, Barton-Cooper, Højmark, **Hobbhahn** — Apollo Research, 28 May 2026).
  Trains small open-weight action-only monitors; reports **marginal inference cost in token-metered
  USD per 1,000 evaluations**; places monitors on an explicit **cost–performance Pareto frontier**;
  describes its contribution as "practical **low-cost, low-FPR** alternatives to prompted frontier
  models." **This paper already owns the economic framing** ("cost pressure pushes monitors cheap")
  that `ideas/19` §3 uses as its motivation. Quantization is simply one axis they did not plot.
- **`2608.16190` — *Decorrelation Is Not Complementarity: Skill, Not Lineage, Governs
  Trusted-Monitor Ensembles*** (Anik Jha, 17 Aug 2026). **24 open-weight monitors, 9 pretraining
  lineages, on backdoored code, scored with pAUC at 10% FPR**, spanning a **29× range of detection
  skill (0.028–0.803)**. The exact experimental apparatus the Compression Tax proposes — open-weight
  monitors × APPS backdoors × partial AUC at a fixed FPR — is built and published. It varies model
  identity, not precision.

  This is the "so what" threat, and it is the sharpest one: **if free choice of open-weight monitor
  already moves pAUC@10%FPR by 29×, why would anyone care about a quantization delta?** Any
  submission must answer this in the abstract, not the discussion.

- **`2608.23941` — *More Rejective, Not More Discriminative*** (25 Aug 2026) is a useful methodological
  ally: it argues catch rate alone misleads ("rejecting everything catches everything") and
  pre-registers **informedness = catch − false rejection** with a matched clean control. Its
  discipline should be adopted.
- **`2607.13087` — GDM AI Control Roadmap** (Phuong, Jenner, Simon, Ho, Shah, Farquhar, Coull) links
  defence tiers to model capability and lists CoT monitoring as the low-cost tier. Good motivation
  citation; explicitly frames "controlling more capable models requires more costly interventions."

### 2.4 The generator-side quantization×safety line is saturated — stay out of it

`2502.15799` (Kharinaev et al., 66 quantized variants, OpenMiniSafety); `2506.20251` (Q-resafe);
`2606.29581` (quantization × sampling temperature, factorial); `2404.04392`; `2401.10862`
(Pruning for Protection); `2504.04215` (refusal in compressed models via mech interp);
`2606.29239` (QuantGuard — repairing quantization-conditioned backdoors). All measure a **generator's**
refusal behaviour / attack success rate. None measures a **detector's** ranking quality. The
distinction is the paper's whole territory and must be stated in the first paragraph of related work.

### 2.5 What is genuinely still empty

Verified by arXiv API metadata search (title/abstract/comments), each returning **zero results**:

- `all:"trusted monitor" AND all:quantization`
- `all:"audit budget" AND all:quantization`
- `abs:"trusted monitoring" AND abs:quantiz*`
- `abs:"partial AUC" AND abs:quantization`

And `abs:quantization AND abs:"selective prediction"` returns exactly two papers, one of which is
`2607.24440` itself. So the *specific instantiation* — monitor precision vs. catch rate at a
control-style audit budget — is unoccupied. What is occupied is the *general claim* it was going
to be sold on.

---

## 3. The decisive experimental finding, which is also the paper's new contribution

Buried in `2607.24440`: under 4-bit, "**the verbalized-confidence parse rate collapses from 99% to
64%**."

The proposed monitor emits a **1–100 suspicion score in natural language**. If quantization degrades
the model's ability to *emit a parseable number*, then a measured catch-rate collapse is a
**formatting artifact, not a discrimination failure** — and every reviewer who has read `2607.24440`
will say so. Round 10's design does not control for this.

This is simultaneously the biggest threat to the naive experiment and the thing worth writing about.
The degradation decomposes into three mechanisms that no existing paper separates:

1. **Emission failure** — the quantized monitor stops producing a well-formed score. Measurable as
   parse rate; fixable by reading the score from logits instead of text.
2. **Resolution collapse** — an integer 1–100 score has ~100 distinguishable levels; catch rate at
   1% FPR depends entirely on resolving the *top 1%* of the score distribution. Quantization
   concentrates mass on fewer distinct values, creating **ties at the top of the ranking** that
   mechanically cap pAUC@1%FPR while leaving AUROC almost untouched. This is a *specific, testable
   mechanism for why the audit-budget metric is the fragile one*, and it is not in any of §2.1.
3. **True discrimination loss** — the residual after (1) and (2) are controlled.

A 4-page paper whose contribution is "we replicate `2607.24440` in a control setting" is weak.
A 4-page paper whose contribution is "**the audit-budget metric that AI control actually runs on is
the one compression breaks first, and here is the decomposition of why — two thirds of it is
recoverable by not parsing text**" is a real, control-native result that stands even where the
headline curve is flat.

---

## 4. Execution risk: the round-10 decision gate is now RESOLVED

`ideas/19` risk #2 said the dataset path was unverified and that failure should trigger abandoning
the Sep 5 date. It resolves cleanly:

- **`RoganInglis/apps-control-arena`** on HF — **5,000 rows**, one `train` split, ungated,
  ~6,958 downloads last month. Fields: `problem_id`, `question`, `inputs`, `outputs`, `difficulty`,
  `solutions` (with `compiles`, `passes_tests`), `backdoors` (backdoored code, trigger input,
  `source` ∈ {apps, control_tax}), `backdoor_works` flags, plus nondeterminism-detection columns.
  Both honest and backdoored solutions with labels, as required.
- Siblings **`RoganInglis/apps-backdoors`** and **`RoganInglis/control-tax`** exist; the ControlArena
  APPS setting is documented at `control-arena.aisi.org.uk/settings/apps.html` and mirrored in
  `UKGovernmentBEIS/control-arena`.
- A public DSPy tutorial ("GEPA for Code Backdoor Classification (AI control)") runs the trusted-monitor
  task end to end — i.e. the monitor harness is a known-good recipe, not a build.

Note the round-10 composition figure (1,936 / 482 / 1,375 at 50% attack rate) was **not** confirmed;
the HF card shows a single 5,000-row split. Construct the splits yourself and report the construction.

Compute stands: pure batch inference, RunPod A6000/4090 at ~$0.33–0.34/hr, well under $20.

---

## 5. Verdict

**Not (A) toss. Not (B) implement-as-written. (B′): implement with the thesis rewritten, the scope
cut, and the venue moved.**

The honest ledger:

**Dead — do not write these sentences.**
- "Nobody has measured what quantization does to the metric that matters." Falsified by §2.1.
- "Tail metrics degrade before mean metrics" as *the* headline. Claimed by `2607.24440`,
  `2602.01459`, `2606.01850`, `2602.09130`, `2607.09999`.
- "Your monitor still passes MMLU and no longer catches backdoors" as the title claim. `2607.09999`
  has the silent-failure frame; `2602.09130` has performance–reliability decoupling at EMNLP Main.
- The MMLU/HumanEval capability control is now *table stakes*, not a finding. Keep it as a control;
  do not sell it.
- The "green light" outcome ("quantize your monitors freely") is much weaker than round 10 priced it,
  because `2509.21173` (ICML 2026) already published the improves-under-quantization direction.

**Alive — this is the paper.**
- **Claim 1 (measurement).** First measurement of monitor precision vs. **catch rate at a fixed audit
  budget** (1%/2%/5% FPR) in the AI-control setting. Empty in every metadata search run.
- **Claim 2 (mechanism, the real contribution).** Decompose the degradation into *emission failure*,
  *score-resolution collapse*, and *true discrimination loss* — and show that reading the suspicion
  score from logits rather than parsing generated text recovers a large fraction of it. This
  survives a flat headline curve, which is what makes the paper outcome-robust *now*.
- **Claim 3 (positioning).** Price quantization against the axis the field already knows about:
  `2608.16190` shows free model choice spans 29× in pAUC@10%FPR. If the quantization delta is small
  relative to that, **say so in the abstract** — "compression is not where your monitor budget should
  buy safety; model choice is" is a defensible, useful finding.
- **Rebuttal to the Meta objection, stated up front.** `2411.17713` is prune+QAT+distill with a
  frontier teacher and reports F1/FPR at one operating point. Off-the-shelf AWQ/GPTQ with no
  recovery training, evaluated on the ranking tail, is a different regime — and the one deployments
  actually inhabit.

**Why not toss.** Cost to finish is genuinely small: the dataset is resolved and ungated, the harness
is a published recipe, the compute is <$20 and a few GPU-hours, and it is pure batch inference with
no generation, no untrusted model, no Docker. The idea has moved from "novel phenomenon" to
"known phenomenon, unmeasured in the setting that motivated it, with one new mechanism." That is a
modest workshop paper — and a modest paper that actually exists beats a strong one that does not.

**Why not implement as written.** Submitting the round-10 framing would put a claim in the abstract
that five 2026 papers contradict, into a workshop whose reviewers read compression literature. That
is a desk-level error, not a scoring one.

### The plan

**Primary venue: SLM-Agents, Sep 6 AoE, 4-page short track.** It buys a day, and its CFP names
*"Compression and distillation: quantization, pruning, knowledge distillation"* **and**
*"Privacy, safety, robustness"*. A quantized trusted monitor is literally an SLM in an agentic stack.
**Secondary, same paper: AIWILD, Sep 5 AoE**, whose topic list names "control and oversight" — the
better audience, the tighter clock. Both are non-archival and both explicitly permit work under
review elsewhere; **verify each one's concurrent-submission wording before double-submitting** rather
than assuming it. **Late fallback: EvoRobust, Sep 12 AoE**, if the Sep 5/6 pair is missed — accept
that the search-methods framing is a stretch there.

**Day 1 (highest-value-first).**
1. Load `RoganInglis/apps-control-arena`, build and freeze an honest/backdoored eval split, record
   the construction. Do not inherit round 10's unverified 1,936/482/1,375 numbers.
2. Run the FP16 baseline monitor on one model. **Log both the parsed text score and the token-logit
   score in the same pass** — the decomposition in §3 is free if instrumented now and impossible to
   recover later.
3. Compute AUROC *and* pAUC@{1,2,5}% FPR *and* parse rate *and* count of distinct score values.
   If the FP16 pAUC@1% is already near-degenerate from score ties, that is itself the finding, and
   the paper reframes to "the 1–100 suspicion-score convention cannot support a 1% audit budget."

**Day 2.** Precision sweep: {FP16, INT8, 4-bit AWQ} × {Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct,
Llama-3.1-8B-Instruct}. Add 3-bit only if published checkpoints exist; three points is enough curve.
Capability control (MMLU or HumanEval) on the same checkpoints — as a control, reported in one row.

**Day 3.** Write. Related work leads with the §2.1 concession, explicitly and generously — the
paper's credibility depends on being the one that cites `2607.24440` rather than the one that
missed it. Adopt `2608.23941`'s discipline: never report catch rate without the matched clean series.

**Day 4.** Internal adversarial pass against the two questions a reviewer will actually ask:
(i) "isn't this `2607.24440` in a new domain?"; (ii) "`2608.16190` says model choice spans 29× —
why does your delta matter?" If neither has a one-sentence answer backed by a number in the paper,
submit to EvoRobust on the 12th instead and spend the extra week getting one.

**Standing constraint unchanged:** the PE/InfPriv paper (`ideas/14`) is still nearly written, still
~$30, still due Sep 7. Doing both well remains unlikely. That is a time call for the author, not a
research call — but note that the Compression Tax's demotion this round makes the PE paper the
stronger *submission* even though it is the weaker *interest fit*.

---

## 6. Killed / corrected this round

- **RETRACTED: `ideas/19` §3's "verified unclaimed" status.** The verification was scoped to the
  AI-control literature. Correct scope is the compression-evaluation literature. Recorded above so
  it stays retracted.
- **RETRACTED: `ideas/19` §3's outcome-robustness argument.** "Catch rate holds → quantize freely" is
  no longer a clean second publishable direction, because `2509.21173` (ICML 2026) already published
  compression-improves-reliability. Outcome-robustness now rests on Claim 2 (the decomposition),
  not on the sign of the headline curve.
- **Corrected: the economic motivation is not ours.** `2605.29601` (Apollo) already publishes a
  monitor cost–performance Pareto frontier in USD per 1,000 evaluations. Cite it as the frame we
  extend; do not present "cost pressure pushes monitors cheap" as an observation.
- **Corrected: the dataset composition figure.** Round 10's 1,936/482/1,375 at 50% attack rate was
  from a search summary and is not what the HF card shows (one 5,000-row split). Do not cite it.
- **Dead venue, painful:** JUDGe 2026 ("Can We Trust the Judge?", Atlanta) closed **Aug 29**. Its CFP
  lists "adversarial robustness of safety evaluators" and "calibration methods for LLM judges" — the
  single best-fitting venue for this paper, missed by three days. Recorded so the next round checks
  judge/evaluator workshops early.
- **Confirmed dead ground (do not enter):** the generator-side quantization×safety-alignment line
  (§2.4) — at least seven papers 2024–2026, including quantization-conditioned backdoors and their
  repair. Our object is a *detector's ranking quality*, and related work must say so immediately.

---

# Round 12 addendum (2026-09-02) — the fallback contribution is taken too. **The Compression Tax is dead.**

Round 11 conceded the headline ("tail metrics degrade before mean metrics") to the compression-evaluation
literature and fell back to a **decomposition** as the surviving contribution: (i) emission failure,
(ii) score-resolution collapse — ties at the top of a coarse 1–100 score capping pAUC@1%FPR while AUROC
holds — and (iii) true discrimination loss, with "read the score from logits, not text" as the fix.

A targeted sweep of the **LLM-judge / selective-prediction** literature — a third neighbourhood neither
round 10 nor round 11 searched — finds all of it already claimed.

| Ref | What it establishes | Damage |
|---|---|---|
| **Sun, Sun, Geng — *The Score Granularity Gap in Black-Box LLM Classification: A Comparative Study of Confidence Constructions*** — arXiv **2606.22179**, 20 Jun 2026 | Frames LLM classification as **selective prediction where an operator thresholds at a chosen risk level**. Asks, verbatim, "a complementary, deployment-oriented question that has been **largely overlooked: at what resolution can the score be thresholded?** We call the answer the **score granularity gap**." Finds single-shot verbalized confidence "**ranks cases surprisingly well, yet takes only a handful of distinct values. It therefore offers an operator only a few coarse thresholds, no matter how well it ranks.**" Compares **seven** confidence constructions — verbalized number vs **token probabilities** vs multi-query aggregation — across **25 model-dataset pairs (9 LLMs, 3 benchmarks)**, and reports cost and ranking effects for each. | **Fatal.** This is mechanism (ii), *named*, measured at scale, with deployment guidance — **and** it is the logits-vs-text comparison we proposed as the fix. Two and a half months old. |
| **Landesberg — *When LLM Judge Scores Look Good but Best-of-N Decisions Fail*** — arXiv **2603.12520**, 12 Mar 2026 | Judge with moderate global correlation (r=0.47) captures **only 21.0%** of achievable best-of-4 improvement. "**coarse pointwise scoring creates ties in 67% of pairwise comparisons**"; within-prompt correlation only 0.27; pairwise judging recovers 21.1%→61.2%. Recommends auditing "**within-prompt signal, tie rates**, and recovery/top-1 accuracy, not global agreement alone." | **Fatal to the tie mechanism as novel.** The tie-density → decision-metric-collapse story, with the "global metric looks fine" framing, is published. |
| **Kumar, Tayebati, Naik, Krishnan, Trivedi — *VLM Judges Can Rank but Cannot Score*** — arXiv **2604.25235**, 28 Apr 2026 | Names "**ranking–scoring decoupling**" as "a failure mode not captured by standard evaluation metrics", via conformal intervals built from **score-token log-probabilities**, across 3 judges × 14 task categories. | Severe. The rank-vs-score decoupling framing and the log-prob route are both taken. |
| **Rajwal, Das, Ghosal — *Do LLMs Know a Good Hypothesis When They See One? Logit-Based Energy Scoring Outperforms Prompted LLM-as-Judge for Scientific Hypothesis Ranking*** — arXiv **2608.17270**, 18 Aug 2026 | Logit-based energy scoring vs prompted judging, 7 models, 1,323 papers: **33.0% vs 16.6% Hit@1**. | Confirms "read the score from logits instead of parsing text improves *ranking*" is established, not our finding. |

Supporting, non-fatal: **Brauer & Wüthrich, *Gini Score under Ties and Case Weights*** (arXiv **2511.15446**,
19 Nov 2025) handles rank-based scoring under ties in the actuarial literature — the statistical fact
that ties degrade rank metrics is old and formalised. **2608.13756** (*The Integer Alibi*, 13 Aug 2026)
localises INT8 cross-kernel divergence to scale application and output rounding, and finds flips
concentrate at small logit margins (ROC-AUC 0.94) — adjacent and worth citing if any quantization
paper is ever written here, but it is a numerics paper, not a safety one.

## Verdict

**Kill it.** Under `notes/11`'s gate **G1** (verified novelty in the *adjacent* literature, not the home
literature), the Compression Tax now fails twice over: the headline fell to compression evaluation
(`ideas/20` §2), and the fallback decomposition falls to LLM-judge selective prediction. What remains
is "apply `2606.22179`'s score-granularity-gap framework to a trusted monitor, with quantization as the
perturbation" — a third-order replication that would have to cite four papers that each did a larger
version of one of its three legs.

**The pattern is the lesson, and it is worth more than the idea was.** Three rounds, three misses, each
the same shape: the claim was verified as unclaimed *within AI control*, and each time it turned out to
be published in a neighbouring field that does not use the words "monitor" or "audit budget" —
compression evaluation, then selective prediction / LLM-as-judge. Round 12's standing rule, now in
`notes/11` G1: **before any measurement idea is adopted, name its two nearest neighbours outside AI
safety and cite them.** A monitor is a classifier; a suspicion score is a confidence score; an audit
budget is a selective-prediction operating point. Anything claimed about one is claimed about all three.

Compute and dataset findings are retained and are still good: `RoganInglis/apps-control-arena` is real,
ungated, 5,000 labelled rows, and the DSPy trusted-monitor tutorial is a working harness. Whatever
replaces this idea should reuse them.
