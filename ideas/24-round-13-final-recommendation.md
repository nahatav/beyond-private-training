# Round 13 final — the recommendation

Supersedes `ideas/22`. Written 2026-09-02 after the adversarial review in `ideas/23`, which killed
one candidate outright and removed the novelty and the executability from the other two the
two-track plan depended on.

## The one-line answer

**Do not submit to AIWILD on Sep 5. Lead with C9, reframed as an evaluation-methodology
contribution, and target the Sep 19 SaTML-workshops window.**

---

## Why Track 1 is cancelled

`ideas/22` recommended C1 to AIWILD's 4-page short track as "the only candidate genuinely buildable
in three days." Both halves of that sentence are false.

**Not novel.** Sahil Raut ran the ablation arm with **24 random-direction placebo controls** on
LessWrong on 2026-06-25 and reported the null (p = 0.20; per-item sandbagging prediction 0.542 AUROC
— chance). The matched-norm placebo `ideas/21` called C1's credibility differentiator is the
mechanism by which someone else already answered the question. `2603.19426` owns the format-confound
control, `2606.23583` owns representation-versus-behaviour decoupling with random controls across 37
models, and `2603.03824` — which we dismissed in one line — owns a causal mediation result pointing
the other way.

**Not buildable.** `2509.21344` releases **no code and no data**. The 0.94 needs their prompt sets;
the 0.57 needs their passphrase-dependent sandbagging model organism, which they trained. `ideas/22`
scored A5 = 5/5 on "no training, public artifacts confirmed live." `ideas/21`'s own correction note
had already established the opposite and the score was never reconciled with it.

**The cost of going anyway.** Missing one non-archival workshop costs nothing — AIWILD is the third
in a series and will run again. Submitting a scooped paper carrying a false novelty claim to the one
venue whose reviewers read AI-control metrics natively costs standing at the venue we most need. That
trade is not close.

---

## The board, after review

| # | Candidate | Round-12 | Round-13 | Why it moved |
|---|---|---|---|---|
| **C9** | Situation-controlled pre-action benchmark | A 23 / B 20 | **A 22 / B 21 — lead** | Premise and target artifact verified live. `G1` rewritten, not failed; the artifact is the contribution. |
| **C7** | Monitorable latent slots inherit CB leakage | A 24 / B 21 | **A 20 / B 20 — second** | Quote verified verbatim, but the authors flagged *both* halves as their own next step and CB-LLM already ships the hybrid architecture. |
| C8 | The instillation-depth ladder | A 25 / B 23 | **A 14 / B 15 — park** | Three of four rungs are already in `2607.01033`'s own table; its documented variance breaks a 4-point monotonicity test; its stated size limitation contradicts our B3 = 5. |
| C1 | Sandbagging probe vs eval-awareness | A 27 / B 20 | **A 13 / B 16 — park** | Pre-empted four ways; G3 fails on artifact availability. |
| C6 | Guard models at a low audit budget | A 25 / B 23 | **DEAD** | Granite Guardian `2412.07724` Table 11 is the proposed deliverable, published Dec 2024. |
| C2 | Context grafting vs RMU | A 22 / B 21 | **park** | The "run today or never" window closed. |
| C3 | Non-linear white-box monitors | A 24 / B 20 | **park** | Occupied by `2607.01033`; residual needs `2509.21344`'s unreleased artifacts. |

---

## The lead — C9, reframed

**Do not frame it as "rescue pre-action monitoring."** That framing makes the paper a bet on which
way the result goes, and it invites the "you built the confound you are measuring" objection as the
*first* question rather than the third.

**Frame it as the methodology claim:** existing data cannot test pre-action monitoring claims at all,
because no dataset varies the action with the situation held fixed. Here is the construction that
makes those claims falsifiable, the pre-registered criteria that make it honest, and what the
published probe families do on it.

Three reasons this is the right lead:

1. **It is the only candidate whose value survives being scooped.** A claim that gets published first
   by someone else is worth nothing. A benchmark that gets published second is still cited, still
   reused, and still constrains the field. `2606.30449`'s authors are the obvious competitor and they
   have the head start — under the artifact framing that is survivable, under the claim framing it is
   not.
2. **B5 (citability) is bought by the artifact, not by the result.** This is the dimension every
   previous lead scored badly on.
3. **G3 passes on the target's side.** `maxf-zn/misalignment_monitoring` is live, HTTP 200, last push
   2026-07-02.

**The `G1` paragraph must be rewritten before anything is run.** `ideas/22` names WILDS group-shift
and counterfactual data augmentation. The real nearest neighbours outside safety are **contrast sets**
(Gardner et al. 2020 — minimal-perturbation *evaluation* construction, the canonical form of our
method), **`2506.02946` Abstract Counterfactuals for Language Model Agents** (counterfactual
construction over agent actions above the token level, with latent-space interventions), and
**`2602.08995` MisActBench** (computer-use-agent trajectories with human-annotated action-level
alignment labels). Cite all three in the introduction. The contribution is not matched pairs, which
are canonical; it is **the agentic action-versus-situation construction** and the pre-registration
that makes it a test rather than a demonstration.

Note also that `2606.30449` already built "a shared-prefix minimal pair" for the Gemma blackmail
case. Say so. The construction is being *generalised and pre-registered*, not invented.

**Cost and shape.** ~$120, ~9 days. Pre-register the pair-construction criteria — in the repo, with a
commit hash — **before any probe is run.** The design is both the contribution and the attack
surface, and a timestamp is the only defence.

---

## Second — C7, and only under one condition

Run it **only if a latent-CoT model is training within two days**. Its premise is the cleanest on the
board and verified verbatim, and the three-way decomposition it proposes — probe accuracy versus
causal accuracy versus leakage into unsupervised slots — is genuinely unmeasured. But `2608.04928`'s
authors named both the supervised-slot idea and the RL-pressure follow-up in the same sentence, they
have the harness, and CB-LLM (`2412.07992`) already ships the hybrid supervised-plus-free
architecture for LLMs, which makes the leakage direction the expected answer rather than a surprise.

**Do not run it in parallel with C9.** It is the only candidate requiring a trained latent-CoT model,
Coconut-style training is unstable, and splitting attention across two builds is how a nine-day
window becomes a missed one.

---

## Venue plan

| Date | Action |
|---|---|
| **Sep 5** | AIWILD passes. No submission. Recorded deliberately, not missed. |
| **Sep 19** | **SaTML 2027 workshops** — organizers notified Sep 18, so CFPs appear here first. Primary target for C9. |
| **~Sep 25** | AAAI-27 workshop list (organizer notification Sep 25; workshops Feb 22–23, 2027). Backup. |
| Unscheduled | ICLR 2027 workshops. |
| 2027 | **JUDGe** and **AIMS** — the two best fits in the entire round-12 calendar, both closed before the sweep ran. Diary them now (`notes/13` lesson 1). |

`notes/13` remains canonical and was re-verified this round. One addition: AIWILD's CFP **discourages**
submissions from the NeurIPS/ICLR/ICML main tracks, which does not affect us but belongs in the row.

---

## The change that matters more than the candidate choice

Four consecutive rounds have been lost to the same instrument. Not to bad ideas, not to bad
discipline — R1 through R7 are being followed, and the citation integrity of this repo is genuinely
good. They were lost to **arXiv `abs:` queries being treated as evidence about what the literature
contains.**

`notes/12` gains **R8** (an `abs:` query cannot certify a claim about what papers *report* — open the
top ~10 and grep their results sections and appendices, and record which ones you opened), **R9**
(search LessWrong and the Alignment Forum before claiming novelty in AI safety), and **R10** (check
artifact availability with an HTTP 200 on a named repo before scoring A5).

If only one of the two lands — the candidate or the protocol — the protocol is worth more. C6 and C1
were both killed by information that a correctly-scoped search would have surfaced in under ten
minutes, and neither had anything to do with the transport bug R3 was written to catch.

---

## Budget

Unchanged and still not binding. C9 at ~$120 leaves ~$150 of the $200–300. Spend it, in this order,
on: a second probe family beyond the four `2606.30449` named; confidence intervals on the pair-level
results; and a second scenario domain. Not on more models (`notes/11`: breadth is padding).
