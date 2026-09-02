# Round 13 — adversarial review of the round-12 board

Written 2026-09-02, three days before AIWILD. The round-12 board (`ideas/22`) was attacked candidate
by candidate, and every load-bearing citation was re-fetched. **One candidate is dead, two are
substantially pre-empted, and the two survivors both have wrong `G1` paragraphs.**

## What held

Citation integrity. Every load-bearing arXiv ID re-fetched over HTTPS resolves, with titles and dates
matching the repo's records: `2606.22179`, `2607.01033`, `2608.04928`, `2606.30449`, `2607.25907`,
`2608.29458`, `2608.29461`, `2608.16190`, `2509.21344`, `2509.21173`, `2607.24440`, `2603.03824`.
Both verbatim quotes the board leans on are real, checked against the papers' own HTML:

- `2607.01033` §6: "We expect that progressively earlier instillation would make quirks progressively
  harder to detect, as the training signal becomes even more diffuse and entangled with the broader
  learning process."
- `2608.04928` §7: "…by reserving a subset of latent slots to be directly supervised for
  monitorability."

Venue facts hold too. AIWILD's own page confirms **Sep 5 AoE (extended from Aug 29)**, 9pp regular /
4pp short, non-archival, "papers under review or recently accepted at other venues" allowed. SaTML
2027's first-ever workshop track confirms proposals closed Aug 28 with **organizer notification
Sep 18**. `notes/13` is accurate. One addition: AIWILD's CFP also **discourages** submissions from
the NeurIPS/ICLR/ICML main tracks.

R1 is working. The problem is elsewhere.

---

## The systemic flaw — the instrument, not the discipline

Every novelty verification in this repo is an **arXiv `abs:` field query**. R3 hardened the
*transport* (301 redirects, double-escaped quotes) but never the *search space*. Two structural blind
spots follow, and both fired this round:

1. **Abstracts do not contain results-table vocabulary.** A paper that publishes ROC curves in §5.1
   and a fixed-FPR leaderboard in Appendix D will not say "ROC" or "pAUC" in its abstract. This
   killed C6.
2. **AI safety publishes a large fraction of its empirical work on LessWrong / the Alignment Forum
   first.** arXiv cannot see it; reviewers at safety venues have read it. This gutted C1.

A third, smaller failure: **exact stem matching**. `abs:"evaluation awareness" AND abs:"probe" AND
abs:"ablat"` returns 0 while at least three papers do the thing, because they write "steering,"
"controlled rewrites," and "random controls" instead of "ablation."

Rules **R8–R10** in `notes/12` are the fix.

---

## C6 — *Guard models cannot be operated at a low audit budget* — **DEAD**

The headline claim — "no guardrail paper does [fix an FPR], and none has ever published an ROC curve
for a guard model" — is **false**. **Granite Guardian** (`2412.07724`, IBM, Dec 2024) does all of it.

From §5.1, quoted from the paper's HTML:

> Model performance is assessed using multiple metrics, specifically, the area under the
> precision-recall curve (AUPRC), the area under the ROC curve (AUC), F1 score, recall, and
> precision…
>
> To further analyze the model's utility, we also compute **recall and AUC at fixed false positive
> rates (FPr) of 0.1, 0.01, and 0.001**, which allows us to evaluate performance under low FPr
> constraints (**Aerni et al., 2024**). This approach helps us understand the model's effectiveness
> when strict false positive rate requirements are critical.

And from Appendix D, in the paper's own words, "**partial AUC** and TPr values across different FPr
thresholds." Figure 8 is a pair of **ROC curves**. §6 states: "Real-time applications have a strong
need for low FPr. Thus, threshold-based metrics (e.g., AUC and AUPRC) can mislead the quality
evaluation of the model."

**Table 11 is C6's proposed deliverable, published 21 months ago:**

| model | AUC | AUC@0.1 | AUC@0.01 | AUC@0.001 | TPr@0.001 |
|---|---|---|---|---|---|
| Llama-Guard-7B | 0.824 | 0.454 | 0.148 | 0.037 | 0.068 |
| Llama-Guard-2-8B | 0.841 | 0.506 | 0.137 | 0.014 | 0.032 |
| Llama-Guard-3-1B | 0.796 | 0.414 | 0.152 | 0.030 | 0.054 |
| Llama-Guard-3-8B | 0.826 | 0.521 | 0.174 | 0.016 | 0.033 |
| ShieldGemma-2B | 0.748 | 0.308 | 0.112 | 0.021 | 0.035 |
| ShieldGemma-9B | 0.753 | 0.307 | 0.129 | 0.020 | 0.052 |
| ShieldGemma-27B | 0.772 | 0.305 | 0.133 | 0.016 | 0.049 |
| Granite-Guardian-3.0-2B | 0.782 | 0.355 | 0.102 | 0.012 | 0.021 |
| Granite-Guardian-3.0-8B | 0.871 | 0.515 | 0.170 | 0.041 | 0.072 |

Nine open guards, partial AUC and TPR at **0.1 / 0.01 / 0.001** FPR — the last of which is *below*
the bottom of AI control's 0.3–10% range. Three further consequences:

- **The score-granularity sub-claim dies too.** They extracted probability scores from Llama Guard
  and ShieldGemma ("For metrics such as AUC, AUPRC, etc. that require probability score we suitably
  adapt each baseline") and reached FPr = 0.001. The low-FPR region is *reachable*, not unreachable.
- **The rank-instability result is already visible.** Llama-Guard-7B (AUC 0.824) beats
  Llama-Guard-3-8B (AUC 0.826) by more than 2× at TPr@0.001; ShieldGemma-27B beats ShieldGemma-2B on
  AUC but they invert at AUC@0.001.
- **The outside neighbour C6's G1 missed is the one Granite Guardian cites**: Aerni, Zhang & Tramèr,
  *Evaluations of Machine Learning Privacy Defenses are Misleading* (`2404.17399`) — the low-FPR
  evaluation discipline, imported from privacy auditing.

Adjacent occupancy, found in the same sweep: `2605.10901` (*Beyond Red-Teaming: Formal Guarantees of
LLM Guardrail Classifiers*, 42 mentions of "threshold", optimal vs pessimistic threshold selection,
"coverage collapse" at the optimal threshold); `2604.16542` (TWGuard, 20 FPR mentions, 11 AUPRC);
`2504.00441` (*No Free Lunch with Guardrails*, security/usability tradeoff over six industry
guardrails).

**Why the searches said zero.** Granite Guardian's abstract contains none of "ROC", "AUROC", "pAUC",
"audit budget", or "fixed false positive rate". The negatives were transport-clean and space-wrong.
The tell was in the repo already: gate **G4** cites `2608.16190` using **pAUC@10%FPR on monitors**,
which should have made `"guard" + "pAUC" → 0` implausible on its face.

**Residual, and it is not a paper.** An independent multi-dataset replication of Table 11 is
unclaimed — IBM ran one aggregated benchmark with their own model winning. But G4 bites hard
(`2608.16190` already shows monitor choice spans **29×** in pAUC@10%FPR), so "guards differ at low
FPR" is the expected answer. High A, low B — exactly the failure mode `notes/11` was written to
prevent.

---

## C1 — *Does the sandbagging probe just read eval-awareness?* — **pre-empted, and not buildable**

### Scooped on the differentiator

**Sahil Raut, *Eval-awareness steering detects the test, not the sabotage*, LessWrong, 2026-06-25.**
Llama-3.1-8B. Diff-in-means direction fit on a **format-controlled 2×2** eval/deploy dataset.
Steering with α ∈ [−2, +2] **plus an ablation arm projecting the direction out**. Noise injection as
an output-independent ground truth. **24 random-direction placebo controls.**

- Direction detects evaluation framing at ~0.81 AUROC under novel, format-matched framings
- Steering dose-response flat at layer 12: **−1.77pp** against a pre-registered 5pp threshold
- "does not beat the empirical null of 24 random directions (**p = 0.20**)"
- Per-item sandbagging prediction: **0.542 AUROC** — chance
- Conclusion: "the direction directs the situational framing, not the capability-withholding
  behaviour"

`ideas/21` calls the matched-norm random-direction placebo C1's "mandatory design constraint" and its
credibility differentiator. It was run in June, twenty-four times, and returned the null.

### Three more occupants the stem-match query could not see

| Paper | What it already establishes |
|---|---|
| `2603.19426` — *Is Evaluation Awareness Just Format Sensitivity?* | Runs the **controlled 2×2 + diagnostic rewrites**; probes "primarily track benchmark-canonical structure and fail to generalize to free-form prompts". The confound C1 wanted to isolate. |
| `2606.23583` — *Evaluation Awareness Is Not One Capability* | 37 open-weight models, 8 experiments. "probes retain AUROC 0.98 under rewrites that drive behavior below chance, and multi-layer steering causally moves three downstream tasks **while random controls do not**"; detectability / manifestation / controllability are **weakly coupled** (1/15 correlations significant). |
| `2603.03824` — *In-Context Environments Induce Evaluation-Awareness* | **Our dismissal of this was wrong.** `ideas/21` recorded it as "about *inducing* eval-awareness in-context, not probing it." Its abstract states: "CoT causal intervention confirms that **99.3% of sandbagging is causally driven by verbalized eval-aware reasoning**, ruling out shallow instruction-following." That is a mediation result on C1's question, pointing the opposite way from Raut. |

C1's headline now sits between three published results rather than in a gap. A: novelty 5 is not
defensible; realistically 2.

### And G3 fails — it cannot ship by Sep 5

Full text of `2509.21344` pulled and searched: the **only** GitHub links in the paper are
`brucemiller/LaTeXML` and `arXiv/html_feedback` boilerplate. There is **no code release, no data
release, and no artifact statement**. To reach the 0.94 you need their prompt sets; to reach the 0.57
you need their **passphrase-dependent sandbagging model organism**, which they trained (Appendix
C.5).

`ideas/22` scores C1 "~$10, ~30 GPU-hours, **no training**, public artifacts confirmed live", A5 =
5/5. That is false, and `ideas/21`'s own correction paragraph — "the dramatic number requires
*retraining a model organism*, not applying a filter" — already said so. The score was never
reconciled with the correction.

### What would survive

A reframe, not a rescue: *representation-level mediation versus behaviour-level null*. Raut shows the
direction does not drive sandbagging **behaviour**; `2606.23583` shows representations survive
behavioural collapse. Nobody has asked whether erasing eval-awareness degrades a **trained
sandbagging probe's AUROC**. That is a reconciliation of three conflicting published results — harder
to scoop than a gap claim — but it still needs the model organism, so it is not a three-day paper.

---

## C8 — *The instillation-depth ladder* — **three of four rungs already published**

By the paper it cites. `2607.01033` built **54 MOs on OLMo2-1B *and* gemma-3-1b-it**, trained with
**seven techniques including standard post-hoc SFT, post-hoc DPO, and integrated DPO into the OLMo
post-training phase**, benchmarked **activation oracles, activation steering, logit lens and sparse
autoencoders**, controlled for **quirk-expression strength**, and reported the direction: "our more
realistic *integrated training* often yields less interpretable MOs than standard post-hoc methods."

C8's ladder is post-hoc SFT → post-hoc DPO → integrated DPO → mid-SFT. **The first three are their
table.** C8's new information is one rung.

The source paper's own limitations then break the design that remains:

| `2607.01033` says | Consequence for C8 |
|---|---|
| "substantial variance remains even after controlling for differences in the strength of target behaviour expression" | A monotone trend over **n = 4 depths with one quirk** cannot clear the documented noise floor. |
| "Switching the base model sometimes changes training method interpretability rankings" (Fig. 8) | The gemma-3-1b replication proposed "to pre-empt *1B is too small*" is likelier to **disagree** than corroborate — producing a non-result, not a robustness check. |
| "our base models (`OLMo2-1B`, `gemma-3-1b-it`) are likely too small to support more sophisticated behaviours" | Directly contradicts `ideas/22`'s **B3 = strongest on the board** claim. |
| "One limitation of this experiment is its reliance on the CakeBake quirk… we did not have the resources to replicate it for all quirks" | C8 proposes one quirk and inherits the same trap. |

Their sentence names the untested rungs as "**pre-training, SFT, or RLVR**." The interesting one is
pre-training, which is out of budget. This is an active LASR/Cambridge line and the obvious next
paper for the same group; scoop-resistance is low, not 4.

**G1 is also understated.** `2410.13722` *Persistent Pre-Training Poisoning of LLMs* (ICLR 2025) and
`2506.14913` *Winter Soldier* both study **instillation stage**, not merely data fraction. The
detectability-by-third-party-probes axis does survive them — but "passes" overstates it.

---

## C7 — *Monitorable latent slots inherit concept-bottleneck leakage* — **alive, less surprising than claimed**

The quote is verified verbatim. Three corrections:

1. **The same future-work sentence names the adversarial arm too.** In full: "…by reserving a subset
   of latent slots to be directly supervised for monitorability; and (ii) whether latent reasoning
   states still expose hint-reliance **under optimization pressures such as RL, and which probes
   resist it**, since training against a monitor can…". The authors flagged **both halves** of C7.
   They are the competitor and they have the harness.
2. **The architecture partly exists already.** `2608.04928` itself trains **weakly- and
   strongly-supervised latent CoT**, and cites Wei et al. (2026), who "train an auxiliary decoder
   jointly with the model, supervising each latent state."
3. **G1 misses the closest neighbour.** **CB-LLM** (`2412.07992`, ICLR 2025) already builds a
   **hybrid concept-bottleneck layer plus an unsupervised layer** for LLMs. The free-slot escape
   hatch exists in that design *because* a pure bottleneck loses information. So "the model routes
   the safety-relevant information around the supervised slots" is a design assumption in the nearest
   LLM architecture, not a discovery — which makes the "no leakage" branch of the outcome-robustness
   argument close to a priori dead. Also relevant: `2410.06352` (*Tree-Based Leakage Inspection and
   Control in CBMs*) and `2507.04695` (*Interpretable Reward Modeling with Active Concept
   Bottlenecks* — CBMs already inside a safety-adjacent application).

The transfer contribution survives. The claimed *surprise* does not. Combined with it being the only
candidate needing a trained latent-CoT model (Coconut-style training is unstable), the
engineering-risk flag in `ideas/22` is if anything understated.

---

## C9 — *Situation-controlled pre-action benchmark* — **strongest survivor, wrong `G1`**

Premise verified. `2606.30449`'s code is live: `maxf-zn/misalignment_monitoring`, HTTP 200, last push
2026-07-02. G3 passes on the target's side.

**The `G1` paragraph is wrong.** `ideas/22` names WILDS/Waterbirds group-shift benchmarks and
counterfactual data augmentation, dismissing the latter as "a *training* remedy, not an evaluation
testbed." That skips the evaluation-side canon, which is the actual nearest neighbour:

- **Contrast sets** — Gardner et al. 2020, *Evaluating Models' Local Decision Boundaries via Contrast
  Sets*. Minimal-perturbation **evaluation** construction. This is C9's method, named and canonical.
- **`2506.02946`** *Abstract Counterfactuals for Language Model Agents* — counterfactual construction
  over **agent actions** above the token level, explicitly because "the actions of LM agents are
  often implicit in the strings they output"; includes latent-space interventions. This is C9's
  pair-construction machinery, already framed for exactly this object.
- **`2602.08995`** *When Actions Go Off-Task* — **MisActBench**, realistic computer-use-agent
  trajectories with human-annotated **action-level** alignment labels.

Also: `2606.30449` already built "a shared-prefix minimal pair" for the Gemma blackmail case, so the
construction is **started**, not absent.

None of this kills C9. It means the related-work paragraph is rewritten and the contribution is
restated precisely: not *matched pairs*, which are canonical, but **the agentic
action-versus-situation construction and the pre-registered criteria that make pre-action monitor
claims falsifiable.** Stated that way the outside collision is a strength, as it is for C7.

---

## C2, C3 — status

- **C2 (context grafting vs RMU).** Scoop-resistance was 1/5 with a "run it today or not at all"
  clause on 2026-09-02, against a group that shipped two papers in one day on 2026-08-29. That window
  is gone. Park it.
- **C3 (non-linear white-box monitors and textual evidence).** `ideas/21` held it "pending the
  white-box sweep, which may find this occupied." It is occupied: `2607.01033` already benchmarked
  activation oracles, steering, logit lens and SAEs across its MO suite. What remains is the
  textual-evidence axis specifically, on `2509.21344`'s setups — which needs the artifacts
  `2509.21344` did not release.

---

## Corrections to our own records

- **`2603.03824` was mischaracterised.** Recorded in `ideas/21` as "about *inducing* eval-awareness
  in-context, not probing it," and used to support C1's empty-claim finding. It contains a causal
  mediation result — 99.3% of sandbagging causally driven by verbalized eval-aware reasoning — which
  makes it a nearest neighbour on C1's **claim**, not merely its setup.
- **`2509.21173` has no confirmed venue.** `notes/14` attributes it to **ICML 2026**; the arXiv
  abstract page carries no venue field. Downgrade to ⚠️ on the venue until confirmed. The paper
  itself is real: *Less Precise Can Be More Reliable*, >700k evaluation runs, quantization can
  improve accuracy/calibration/OOD detection/noise robustness.
- **Both Compression-Tax outcome-robustness kills are VLM papers.** `2509.21173` is CLIP/VLM
  zero-shot classification; `2607.24440` is Qwen2-VL under image degradation. Using them to kill an
  *LLM-monitor* claim is a cross-modality inference. The Compression Tax stays dead — `2607.09786`
  kills it directly, in-modality — but the ledger should not present these two as equally strong.
- **`2509.21344` releases no code or data.** Add to the artifact table as ❌, not as an available
  harness.
