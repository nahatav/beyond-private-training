# The board, re-scored for EvoRobust (Sep 12 AoE)

Written 2026-09-02 after the EvoRobust CFP was actually fetched (`notes/13`) and `notes/12` R13 was
written. **The answer to "is there nothing safety-shaped left to submit" is: there are three, and two
of them were marked down for reasons that partly dissolve at this venue.**

Every `A` score in `ideas/22` and `ideas/24` is really **`A @ AIWILD`** — A4 is venue fit, and the
board never said which venue it was scoring against. Re-scoring, not re-reading, per R13.

**The venue.** Sep 12 AoE · 4pp (5pp camera-ready) · non-archival · dual submission explicitly
allowed. Ten days. Two of five topic areas name our objects: *"Agentic Safety & Interactive
Robustness: safety of tool-using agents … human oversight and controllability"* and *"Benchmarks and
Governance: continuously evolving safety benchmarks, automated test case generation, coverage
metrics."* Non-archival plus dual-submission means **EvoRobust does not consume the SaTML target** —
the same work can go to both.

---

## C9 — situation-controlled pre-action benchmark · **A 25 @ EvoRobust** (was 22 @ AIWILD) / B 21

**Why A4 rises.** "Continuously evolving safety benchmarks, automated test case generation, coverage
metrics" is the deliverable, stated in the CFP. "Human oversight and controllability" of tool-using
agents is the object. And `ideas/25`'s reframe **moves toward this venue rather than away**: building
pairs by searching the rollout space for cue-matched, action-divergent trajectories *is*
diversity-driven search over failure scenarios, and the distance-from-divergence sweep is a coverage
metric. What reads as a stretch at a QD-search workshop is the spine of the paper here.

**Why it is still the risky one.** `ideas/24` scoped it at ~9 days against a 10-day window — no slack,
and **day 1 is the R8 sweep it owes on its own claim** (`lit/02`, eight targets). That sweep can kill
it. Under `notes/11`'s three-state rule this is `A5 = 3`, not 5: nothing has been cloned or loaded.

**Interest fit is the best on the board** — probes on residual streams, agentic monitoring, oversight.

**Submitting here is not the AIWILD tip-off problem.** At AIWILD on Sep 5 it would have been a
results-free announcement of a competitor's own open problem at their home venue. At EvoRobust on
Sep 12 it is a timestamped result at a venue they do not organize.

---

## C4 — ensembles vs adaptive prompt injection on trusted monitors · **A 24 @ EvoRobust** (was 19 @ AIWILD) / B 18

**The biggest re-rank on the board, and the reasoning is not a rescue.** `ideas/21` cut C4 to A19 on
one ground: *"the headline would be a result three literatures already expect"* — `2504.18333` already
recommends multi-model committees and reports 50.5–62.6% transferability, `2403.17710` (CCS 2024)
shows judge defences insufficient, `2606.25487` flips judges 57–100%.

**At a workshop whose stated topic is "novelty search … behavioral repertoires of failures *and
defenses*", low surprise is not the penalty it is elsewhere.** The deliverable is the repertoire and
the coverage, not the twist. This is the one venue where "we ran the search the two AI-control papers
declined to run, and here is the failure repertoire" is the native contribution rather than a
negative result about novelty.

**Motivation is already written and quotable:** `2510.09462` proposes ensembling as the mitigation;
`2605.15377` states *"We did not red-team our ensembles against an adaptive adversary with knowledge
of the monitoring system."* Two control papers point at each other and neither ran it.

**~$25, ~6–7 days** — the only candidate with real schedule slack inside Sep 12. Interest fit is
control/monitoring, which is on-brief.

**⚠️ G2 owed before committing.** Invited speaker **Maksym Andriushchenko** works directly on adaptive
attacks against safety-aligned LLMs. That is close enough to C4's line to need the R7/G2 check —
publication-list, not vibes. It may be an asset (a reviewer who grades the adaptive-attack
methodology correctly) or a collision. **Check first.**

---

## C2 — context grafting vs RMU · **A 22 @ EvoRobust** / B 21 · the cheap fallback

Fits "Multi-Objective Trustworthy AI" and the model-tampering literature; not as native as C4 or C9.
**~$15, `cais/Zephyr_RMU` verified to load on a 4090**, the fastest thing on the board. Its parking
reason was scoop-resistance 1/5, not a flaw — and **non-archival lowers the cost of being second**,
which is exactly the objection that parked it. Still a bet on a group that ships fast.

## Out, and why the venue does not change it

**C7** needs a trained latent-CoT model; Coconut-style training is unstable and will not start and
finish in ten days. **C8, C1, C3** are parked on published rungs and unreleased artifacts — facts
about the literature, not about reviewers. **C6** is dead. **C5** (~$20) is third-tier here: real but
a narrow instance of a known result even under this venue's framing.

---

## The plan — Sep 3 is a fork, and the day-1 work is owed either way

| | |
|---|---|
| **Sep 3 (both branches)** | The R8 sweep on C9's own claim — the eight targets in `lit/02`, ~2h — **and** clone `maxf-zn/misalignment_monitoring`, load it, reproduce their identity-cosine floor. This is owed under R12/G3 regardless of which paper gets written, and it has never been done. |
| **Sweep clean + repo loads** | **C9 → EvoRobust.** Nine days, no slack. Pre-registration pushed public that day. |
| **Sweep finds occupancy, or the harness fights back** | **C4 → EvoRobust**, after the G2 check on Andriushchenko. ~$25, 6–7 days, comfortable inside Sep 12. C2 if even that slips. |

The point of the fork is that **the expensive day is shared.** Nothing is wasted in either branch,
and for the first time in fourteen rounds the deciding evidence is a load and a grep rather than
another search.

**Do not run two of these.** `ideas/24` was right about that even though its venue premise was wrong.

**EvoRobust does not close the SaTML door.** Non-archival, dual submission allowed, 4pp here and the
full version there once the Sep 19 CFPs exist.
