# Round 12 final — ranked candidates and the recommendation

> **⚠️ SUPERSEDED by [`ideas/24`](24-round-13-final-recommendation.md) on 2026-09-02.** The round-13
> adversarial review ([`ideas/23`](23-round-13-adversarial-review.md)) **killed C6** — Granite Guardian
> `2412.07724` Table 11 already publishes partial AUC and TPR at fixed FPR 0.1/0.01/0.001 across nine
> open guards — and removed both the novelty and the executability from **C1**. The scores in the board
> below are stale. Kept for the reasoning and the method note, not for its conclusions.

Six sweeps returned (AI control, CoT monitoring, deception/sandbagging, monitor operating points,
white-box monitoring, venues). Scored against `notes/11`: acceptance `A/30` and general-safety
relevance `B/25`, **reported separately, never averaged**, per the two-objective brief.

## Methodology note, recorded because it nearly poisoned the round

Two sweeps independently hit the same transport bug: `http://export.arxiv.org` returns **301**, and a
client that does not follow it parses an empty body as `totalResults=0`. One sweep also
double-escaped quotes (`%22` → `%2522`), which arXiv silently ignores, returning a date-sorted dump
of unrelated recent papers that *looks* like a successful 40-hit query. **Fake zero-results and fake
positive-results, from the same tool, in the same round.**

Every negative this repo now relies on was **re-run locally over HTTPS with a positive control in the
same script**: the control (`abs:"audit budget" AND abs:"monitor"`) returned 6 hits / 12,424 bytes,
while the negatives returned well-formed empty feeds of ~750–800 bytes. They hold. Standing rule
added: **a zero-result is only citable when a positive control ran in the same batch.**

---

## The board

| # | Candidate | A/30 | B/25 | Cost | Gate G1 |
|---|---|---|---|---|---|
| **C6** | **Guard models cannot be operated at a low audit budget** | 25 | **23** | ~$35 | ✅ clean |
| **C8** | **The instillation-depth ladder** | 25 | **23** | ~$90 | ✅ clean |
| **C1** | Does the sandbagging probe just read eval-awareness? | **27** | 20 | ~$10 | ✅ clean |
| C7 | Monitorable latent slots inherit concept-bottleneck leakage | 24 | 21 | ~$100 | ✅ (collision *is* the contribution) |
| C9 | Situation-controlled pre-action benchmark | 23 | 20 | ~$120 | ⚠️ narrow |
| C2 | Context grafting vs RMU | 22 | 21 | ~$15 | ✅ but **scoop-resistance 1/5** |
| C4 | Ensembles vs adaptive prompt injection | 19 | 18 | ~$25 | ⚠️ weakened |
| C5 | Legibility comments as an injection channel | 21 | 19 | ~$20 | ⚠️ weakened |

Killed by the sweeps' own gate checks, recorded so they stay dead: **localised deception probes**
(scooped by `2604.14865` Segment-Level Coherence, and generic multiple-instance-learning localisation
outside safety); **adversarial probe-evasion training** (the adaptive-attack canon; `2505.14300`
already ran red-team evasion plus an ensemble defence); **label-free lineage calibration** (the
phenomenon is thoroughly published as cross-generator generalisation failure in machine-generated-text
detection).

---

## C6 — Guard models cannot be operated at a low audit budget ★ best on relevance

**Claim.** AI control and the guardrail literature use incompatible metric conventions, and the
guardrail side ships models that cannot be operated where control needs them. Every control paper
fixes an FPR (0.3%–10%); **no guardrail paper does, and none has ever published an ROC curve for a
guard model.** Combined with the score-granularity gap (`2606.22179`), the low-FPR region control
works in may be *unreachable* for the guards the field ships.

**Verified negatives (locally re-run over HTTPS, positive control in-batch):**
`"guard model"`+(ROC OR AUROC) → **0** · `"guardrail"`+`"audit budget"` → **0** ·
`"fixed false positive rate"`+`"large language model"` → **0** · `"guard"`+`"pAUC"` → **0** ·
`"partial AUC"`+(guardrail/safety monitor/moderation) → **1**, a *2013 pedestrian-detection* paper ·
`"audit budget"`+`"monitor"` → **6, all six AI-control papers.**

**G1.** Nearest outside neighbours: `2606.22179` (the score-granularity gap — established on
*general* black-box classification, 9 LLMs, never on guards, never against an audit budget) and
`2410.10414` (guard-model calibration — measures **ECE and confidence, never realized FPR at a target
operating point**). Both must lead related work; neither claims this.

**Experiment.** 10–12 open guards (Llama Guard 3, WildGuard, ShieldGemma, Granite Guardian,
GuardReasoner, Qwen3Guard 0.6/4/8B, HaloGuard, BingoGuard). Extract the continuous score — logprob of
the `unsafe` token — on WildGuardTest + ToxicChat + OpenAI Moderation + a jailbreak set. Report full
ROC, pAUC@1%/10% FPR, and **the number of distinct achievable FPRs below 5%**. Then check whether the
published F1 ranking survives the move to a fixed budget.

**Both directions publish.** Coarse ⇒ the field's default metric is unreportable at deployment
thresholds, and guard leaderboards do not transfer to control. Fine ⇒ the first pAUC leaderboard for
guard models, plus a rank-stability result. Neither outcome is empty.

**Sharpest objection.** "The logprob is not the deployed decision rule — Qwen3Guard ships strict/loose
modes, not a score." Pre-empt by reporting both and showing strict/loose spans exactly **two** of the
needed operating points.

---

## C8 — The instillation-depth ladder ★ best on methodological consequence

**Claim.** Detectability of an instilled quirk decreases monotonically with how early in training it
is instilled. This is `2607.01033`'s (Model Organism Lottery, LASR/Cambridge) **own stated
expectation, never tested**: "We expect that progressively earlier instillation would make quirks
progressively harder to detect, as the training signal becomes even more diffuse."

**Experiment.** OLMo2-1B — the crux is that **only OLMo publishes checkpoints at every training
stage**. Instill one quirk at four depths (post-hoc SFT → post-hoc DPO → integrated DPO → mid-SFT),
holding quirk-expression rate constant. Run an activation oracle, a linear probe, and an SAE at each
depth. Partial gemma-3-1b replication to pre-empt "1B is too small."

**Both directions publish, and one of them is a big claim.** Monotone ⇒ **every probe result in the
white-box monitoring literature is an upper bound on real difficulty, because the field's model
organisms are systematically too easy.** Non-monotone ⇒ falsifies a LASR/Apollo prediction and
rehabilitates post-hoc model organisms. B3 (survives capability scaling) is the strongest of any
candidate: the effect is about *training-signal diffuseness*, which gets worse, not better.

**G1.** Outside neighbours: backdoor-poisoning literature (treats *data fraction*, not training-stage
depth, and does not hold behavioural strength constant) and curriculum/forgetting-order literature
(cares about capability retention, not third-party detectability). Passes.

---

## C1 — Does the sandbagging probe just read evaluation-awareness? ★ best on acceptance, and the only one buildable in 3 days

Detail in `ideas/21`. `abs:"evaluation awareness" AND abs:"probe" AND abs:"ablat"` → **0**
(re-verified over HTTPS). Method is standard and well-validated — amnesic probing (`2006.00995`),
control tasks (`1909.03368`), LEACE — applied to an unasked question, which is the inverse of the
shape that killed three ideas. **Mandatory:** random-direction placebo at matched norm, because
`2607.25907` found a placebo suppresses as hard as the real direction. ~$10, ~30 GPU-hours.

---

## C7 — Monitorable latent slots inherit concept-bottleneck leakage

**Claim.** `2608.04928` (Ferreira, Aziz, Titov) proposes, in its own future work, "reserving a subset
of latent slots to be **directly supervised for monitorability**." That is a **concept bottleneck**,
and it will fail the way concept bottlenecks are known to fail: the model routes the safety-relevant
information *around* the supervised slots, so probe accuracy on those slots stays high while **causal
control drops to zero**.

**Experiment.** Train small latent-CoT models (Qwen 0.5B/1.5B, Coconut-style) on the hint-reliance
setup with *k* supervised slots. Measure three quantities that the safety framing conflates:
(a) **probe accuracy** on the supervised slots; (b) **causal accuracy** — intervene on the slots and
check the answer actually follows; (c) **leakage** — probe accuracy recoverable from the
*unsupervised* slots. Then apply light adversarial pressure (RL against the slot probe) and re-measure.

**Both directions publish.** Leakage appears ⇒ you have pre-empted a fix a frontier-adjacent group has
publicly announced, with the mechanism named and a citable prior literature. No leakage ⇒
monitorability-supervised latent slots are a real architecture and you own the first result.

**G1 — passes, and unusually: the outside collision *is* the contribution.** Nearest neighbours are
**Concept Bottleneck Models** (Koh et al. 2020) with the leakage literature (Mahinpei et al. 2021;
Margeloiu et al. 2021), and **Self-Explaining Neural Networks** (Alvarez-Melis & Jaakkola 2018) /
ProtoPNet-style interpretability-by-architecture. The architecture is claimed outside; the
safety-relevant negative result is not. The point of the paper is that safety proposed a bottleneck
without inheriting the bottleneck literature's known failure mode.

**Sharpest objection.** "Concept-bottleneck leakage is already known." Answer it in the introduction,
not the rebuttal: cite Mahinpei and Margeloiu explicitly and frame the contribution as the transfer.

**Cost.** Light fine-tuning of ≤1.5B models, ~250 A6000-hours ≈ **$85–100**. The highest engineering
risk on the board — it is the only candidate requiring a trained latent-CoT model.

---

## C9 — Situation-controlled pre-action benchmark

**Claim.** `2606.30449`'s finding that probes "read the situation, not the action" holds because **no
existing dataset varies the action with the situation held fixed**. Build matched pairs — identical
prefix and situation, divergent next action — and re-test the published probe families.

**Experiment.** Construct matched action-divergent pairs on agentic tool-use traces under
**pre-registered pair-construction criteria**, then evaluate the probe families `2606.30449` tested,
plus the four it named as untested: sparse-autoencoder features, sequence-level probes, larger
nonlinear classifiers, and probes trained across many tool-action scenarios.

**Both directions publish.** Signal survives ⇒ pre-action monitoring is rescued and you own the
benchmark. Signal vanishes ⇒ a single-source negative becomes a robust one, established on the
original authors' own named open items.

**G1 — passes narrowly.** Nearest neighbours: WILDS/Waterbirds-style **group-shift benchmarks** (same
logic, but no agentic action-vs-situation construction) and **counterfactual data augmentation** for
shortcut removal (a *training* remedy, not an evaluation testbed).

**Sharpest objection.** "You built the confound you are measuring." This is why the pair-construction
criteria must be pre-registered before any probe is run — the design is the contribution and it is
also the attack surface.

**Cost.** ~**$120**, ~9 days.

**⚠️ Competitor flag.** `2606.30449` was published **at AIWILD**, our primary venue. That makes this a
same-venue direct-successor paper — good for fit, but its authors are the obvious competitor for
exactly this follow-up, and they have the head start.

---

## The venue problem, stated plainly

**AIWILD (Sep 5 AoE) is the only venue whose reviewers read AI-control metrics natively.** It is
**3 days away.** Everything else carries a reviewer-background mismatch that damages objective (2):
SLM-Agents would grade a monitor result on efficiency merit; EvoRobust (Sep 12) is a
quality-diversity-search workshop; VERICODEGEN is formal methods; UniReps and NeuralArtifacts are
severe mismatches.

Two facts make AIWILD more viable than the calendar suggests: it takes a **4-page short track**,
explicitly welcomes **work in progress**, is non-archival, and permits concurrent submission. And
`2606.30449` — a probes-fail-on-pre-action-monitoring paper — **was published at AIWILD**, so the
venue demonstrably takes exactly this kind of white-box negative result.

---

## Recommendation

**Two-track, and the tracks do not compete for the same hours.**

**Track 1 — C1 to AIWILD, Sep 5, 4-page short track.** It is the only candidate genuinely buildable
in three days: ~$10, ~30 GPU-hours, no training, public artifacts confirmed live. It scores highest
on acceptance (27/30), passes G1 cleanly, is a white-box/interpretability result matching the stated
interests, and AIWILD has published its nearest neighbour. Non-archival and concurrent-friendly, so
it costs nothing later.

**Track 2 — C6 or C8 as the substantial paper, submitted after Sep 18.** Both score 23/25 on
relevance, above everything else on the board, and neither fits three days. C6 needs 10–12 model
downloads plus a score-extraction harness; C8 needs twelve LoRA runs. The venue sweep found the right
target: **SaTML 2027's first-ever workshop track — proposals close Aug 28, organizers are notified
Sep 18, so paper CFPs cannot exist before then.** Re-check on Sep 19. ICLR 2027 workshops and AAAI-27
workshops (list out ~Sep 25) are the other windows.

**Between C6 and C8:** C6 if the priority is a result the field must act on immediately — it indicts
a whole literature's reporting practice and hands over a reusable leaderboard. C8 if the priority is
depth — it tests a named, unfalsified prediction and, in one direction, reframes every existing probe
result as an upper bound. C6 is lower-risk to execute; C8 is the better paper if it works.

**Do not run C2** unless it starts today — `2608.29458` named it as their open problem eight days ago
and that group ships two papers a day.

**Budget note.** The whole board costs **under $250 combined**. Money was never the binding
constraint this round — novelty verification was, and it killed three consecutive leads. Spend the
surplus on seeds, placebo controls, and a second model family, exactly as `notes/11` says: not on
breadth.
