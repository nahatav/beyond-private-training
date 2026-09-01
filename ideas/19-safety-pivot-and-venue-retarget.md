# Round 10 — pivot to AI safety, and a venue retarget

The brief changed. The repo optimised for *acceptance probability at InfPriv*, and converged on a
DP-theory result (user-level PE, `ideas/10`/`14`). That is a good paper for that venue and a poor
fit for the author's actual interests: CoT monitoring, AI control, post-training, mech interp.

This round asks a different question: **what is the highest-probability safety paper reachable on a
short clock?** Five parallel agents swept venues, accepted-paper form factors, the CoT/control
literature, the interp/post-training literature, and the safety x privacy intersection. Every
load-bearing claim below was re-verified locally by fetching the source.

## 1. The venue finding — InfPriv is not the only door, but most doors already closed

NeurIPS 2026 accepted 102 workshops. Almost every safety/interp workshop deadline has passed:
"Who Verifies the Agents?" (agent oversight/control) closed Aug 29; FLMSec Aug 27; InterpScience
Sep 1; AAAI-27's alignment track Aug 21.

**Still open, verified by fetching each CFP directly:**

| Venue | Deadline (AoE) | Format | Fit |
|---|---|---|---|
| **AIWILD** — 3rd Workshop on Agents in the Wild: Safety, Security, and Beyond (NeurIPS 2026, Sydney) | **Sep 5, 2026** | 9pp regular / **4pp short**, non-archival, WIP welcome | **Direct hit** |
| ATTRIB (NeurIPS 2026) | Sep 5, 2026 | 3-6pp main / 2-4pp idea track, non-archival | Attribution only |
| InfPriv (the incumbent) | Sep 7, 2026 | 4pp, non-archival | Privacy only |
| IEEE SaTML 2027 | Sep 29, 2026 | Full archival conference paper | Security; much higher bar |

AIWILD's verbatim topic list includes "Agent safety, alignment, **control**, and oversight";
"**Privacy**, robustness, factuality, identity, and accountability for agents"; "**Post-training**
and adaptation"; "Agentic **interpretability** and fairness". That is the author's interest list.

Also verified from the live InfPriv page: its own framing calls the frontier "inference-time
safety... local privacy filters, agentic privacy guardrails", and it solicits work on
"inference-time AI privacy **and models utilized for safety**". So guardrail/monitor work is in
scope at *both* venues, two days apart.

**Caveat, recorded honestly:** no acceptance rate could be verified for any of these. AIWILD's two
prior editions drew 237 and 327 submissions. Treat "workshops accept 60-80%" as folklore.

## 2. What actually gets accepted at these venues (form factor)

From fetched accept-lists: CogInterp @ NeurIPS 2025 (89 papers), MechInterp @ NeurIPS 2025 (139
posters), Trustworthy AI @ ICLR 2026 (144), SafeAI @ UAI 2026 (35).

**~55-75% are small empirical measurements on one open model family, single GPU, days of compute.**
Then ~15% narrow benchmarks, ~15% negative-result/failure demos, ~10% methods. Essentially nothing
needs frontier APIs or multi-GPU training. A tight 4-page measurement is the modal accepted paper,
not a weak version of one.

(Sample is partial: OpenReview sits behind a CAPTCHA, which the agent correctly declined to bypass,
so lists came from workshop sites instead.)

## 3. THE LEAD — "The Compression Tax": what quantizing a trusted monitor costs

**Claim.** AI-control deployments run a *trusted monitor* on every action. Cost pressure pushes that
monitor to a quantized open-weight model. Nobody has measured what quantization does to the metric
that actually matters — **catch rate at a fixed low audit budget**.

**Why the gap is real (verified, not inherited):**

- `2506.05296` **Control Tax** — fetched. Defines the tax as "the operational and financial cost of
  integrating control measures into AI pipelines." Contains **no** privacy/precision/quantization
  analysis. Names "explore weaker models and optimized prompting strategies" as its own future work.
- `2607.06596` **Calibration-Family Overfit** — full HTML extracted (97k chars). **Zero** occurrences
  of quantiz*/8-bit/FP16/AWQ/GPTQ/precision. A search engine attributed a quantization finding to
  this paper; that attribution was false. (Same failure mode `lit/02` was created to prevent.)
- `2605.15377` **Ensemble Monitoring for AI Control** (Koran & Yun, SPAR, 18 May 2026) — extracted.
  Its "precision" hits are all the classification sense. Zero numerical precision content.
- `2602.10153` **Basic Legibility Protocols Improve Trusted Monitoring** — extracted. Zero hits;
  its Sec 3.3 varies the monitor *model*, not its precision.

**The one real prior data point, which must be cited:** `2605.27157` (Yu, Xing, Ye, Teng, Yang, Lin,
Han; 26 May 2026), *Detecting Is Not Resolving: The Monitoring-Control Gap in Retrieval-Augmented
LLMs* — a different sense of "monitoring/control" (RAG epistemic conflict, not Redwood-style
control). Its **Appendix A.15 Quantization Sensitivity Check**: Qwen2.5-7B FP16 vs 8-bit,
"negligible impact (T3 danger differs by 0.012)."

**That citation is a gift, not a threat.** It validated 8-bit on a 7B model, then used that check to
justify running its 32B at **4-bit AWQ**. The extrapolation from "8-bit fine at 7B" to "4-bit fine at
32B" is exactly the unvalidated inference every budget deployment makes, sitting in a published
appendix as a concrete instance. The paper's job is to test it.

**Motivation partner:** `2605.15377` Sec 5.6, "Diversity outperforms vertical scaling" — spending
more compute on one monitor is worse than ensembling several cheap ones. If the field's advice is
*use many cheap monitors*, then **how cheap can one get before it breaks** is the immediate next
question, and quantization is the cheapening axis nobody measured.

### Experiment (this is why it fits four days)

The labeled backdoor data already exists, so **no code generation, no untrusted model, no agentic
rollout, and no Docker sandbox are needed.** The ControlArena APPS dataset pairs APPS problems with
LLM-generated backdoored solutions, filtered to working-honest and working-backdoored only:
**1,936 train / 482 val / 1,375 test at 50% attack rate**. The monitor's whole job is to read
(problem, code) and emit a 1-100 suspicion score. That is pure batch inference.

- **Sweep:** {Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct, Llama-3.1-8B-Instruct}
  x {FP16, INT8, 4-bit AWQ, 3-bit} over the 1,375-sample test split.
- **Metrics:** AUROC, and — the control-native one — **catch rate at fixed audit budget** (1%, 2%,
  5% FPR). Plus a capability control (MMLU or HumanEval) on the same quantized checkpoints.
- **The actual thesis:** tail metrics degrade before mean metrics. A monitor can look intact on
  general benchmarks while its catch rate at 1% FPR has collapsed — because low-FPR catch rate
  depends on the top of the score distribution, which is exactly what quantization noise smears.
  *"Your monitor still passes MMLU and no longer catches backdoors"* is the headline.
- **Cost:** inference only. Verified rates from `ideas/18`: RunPod A6000/4090 at $0.33-0.34/hr.
  Well under $20 and a few GPU-hours.

### Outcome-robustness

Both directions are publishable, which is the property this repo prizes most under a clock:
- Catch rate falls faster than capability → a concrete, practitioner-relevant safety warning.
- Catch rate holds to 3-4 bits → "quantize your monitors freely," a useful green light that
  extends 2605.27157's 8-bit appendix check into the regime people actually deploy.

The measurement cannot come out empty; only its slope is unknown.

### Risks, stated plainly

1. **Four days is genuinely tight.** This is the binding constraint, not compute or novelty.
2. **The dataset path needs direct verification before committing.** The 1,936/482/1,375 composition
   comes from a search summary of the ControlArena docs, not a page fetched end-to-end. Confirm the
   exact HF/ControlArena artifact in hour one; if it does not resolve, the fallback is the public
   `cracklinoatbran/collusion-apps-backdoor-recognized` HF dataset (also unverified) or generating
   backdoors, which would blow the timeline and should trigger an immediate switch to the Sep 25/29
   fallback venues.
3. **3-bit checkpoints may need making.** 4-bit AWQ/GPTQ are widely published; 3-bit often is not.
   Degrade gracefully to {FP16, INT8, 4-bit} if so — the curve still has three points.
4. **Scope honesty.** One task family (APPS backdoors), one monitor prompt. Say so; do not
   generalize to "monitors" in general.

## 4. Backup ideas that survived review

- **Privacy tax of control protocols.** Count how many times raw user data is read/copied across
  models under trusted monitoring vs. untrusted monitoring vs. resampling(k) vs. defer-to-trusted,
  as a data-exposure dual to the compute Control Tax. **Uniquely fits both AIWILD and InfPriv**, so
  it is the pick if the InfPriv Sep 7 date is preferred. Verified unclaimed.
- **Eval-awareness confound audit of sandbagging probes.** `2509.21344` found sandbagging-probe AUROC
  collapses 0.94 -> 0.57 once textual evidence is filtered. `2608.21766` (22 Aug 2026) names the
  representation/verbalization/steering disjunction as unresolved. Test whether ablating an
  eval-awareness direction explains the collapse. Public artifacts: ApolloResearch/deception-detection,
  clarifying-EM/model-organisms-for-EM. ~8-12 GPU-hr.
- **Sandbagging-lock grafting vs. RMU unlearning.** `2608.29461` (3 days before this round) restores
  capability in 28/33 sandbagging locks via single-layer activation grafting. Untested against
  representation-engineering unlearning (`cais/Zephyr_RMU`). Genuinely fresh.

## 5. Killed this round, with evidence

- **MIA on safety classifiers — HARD KILL.** `2605.22373` *Boundary-targeted Membership Inference
  Attacks on Safety Classifiers* (Hughes, Goldberg, Jha, Perer, Aletras, **Mireshghallah**; 21 May
  2026). Verified: Mireshghallah is the sixth author and an **InfPriv organizer**. Do not go near it.
- **Activation/embedding-inversion PII extraction — dead.** `2507.16372` (USENIX Sec '25) reconstructs
  a 4,112-token medical prompt at 86.9 F1; `2604.23711` Spore extracts agent-memory PII in one query.
- **Membership inference via reasoning traces — dead.** `2601.13607`, ACM Web Conf 2026, with two new
  datasets. Combined with the already-recorded PII-in-CoT kill (`lit/01`), the CoT-privacy door is
  shut from both sides.
- **Contextual integrity for agents — dead.** Seven+ 2025-26 benchmarks/surveys; Mireshghallah's turf.
- **Unlearning + DP auditing — dead.** Oversaturated and directly on organizer Eli Chien's line.
- **Correction to `lit/01`'s CoT kill:** that kill was aimed at *PII-leakage-in-CoT*. It does not
  extend to CoT *monitoring* as a safety mechanism, which is a different object. Recorded so the
  distinction is not lost — though note Sec 3 chose a control-monitor angle over a CoT one anyway,
  because CoT faithfulness is now extremely crowded (8+ independent groups).

## 6. Recommendation

**Primary: the Compression Tax paper, AIWILD 4-page short track, Sep 5.** It is a safety paper on the
author's own topics, it is verified unclaimed, it is pure inference under $20, its form factor is the
modal accepted paper at these venues, and it is outcome-robust in both directions.

**The PE/InfPriv paper is not wasted.** It is nearly written and costs ~$30 to run. Whether to also
land it on Sep 7 is a time question, not a research question, and it is the author's call. The two
deadlines are two days apart and the honest read is that doing both well in six days is unlikely.

**Decision gate, hour one:** resolve the APPS-backdoor dataset artifact. If it loads, the timeline
holds. If it does not, abandon Sep 5 and retarget SaTML (Sep 29) or InfPriv fast-track (Sep 25)
rather than generating backdoors under a four-day clock.
