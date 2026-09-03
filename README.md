# Workshop paper ideation — AI safety (was: InfPriv @ NeurIPS 2026)

Working repo for a short workshop paper. **The brief changed twice.** It began as a 4-page InfPriv
(privacy) submission and pivoted in round 10 to **AI safety** — CoT monitoring, AI control,
post-training, mech interp. Round 12 added a second objective: the paper must be relevant to
*general* AI safety research, not only acceptable at a workshop.

**State as of 2026-09-03 (round 17). Read [`notes/19`](notes/19-the-plan-round-17.md) first.**

> ### ✅ Round 17 ran the killing checks, wrote the first code, and both September papers have numbers
> Six subagents in parallel plus the coordinator's own recompute of every load-bearing figure (R17). Everything is
> in [`experiments/`](experiments/README.md) — the first experiment code in seventeen rounds.
>
> - **InfPriv is a paper, not a plan.** DPSDA cloned and driven directly; E0, E1a, E1b done in **34 seconds of
>   compute** on the laptop; the central figure is drawn; 14/14 bibliography entries fetched; scoop patrol clean on
>   metadata and on the full text of eight PE papers; G2 clear. E0's real finding: the histogram threshold is a raw
>   count whose *unit* moves under `"client"` mode. The real anchor lands in the weak branch, so E2 is cut. **Sep 7.**
> - **K1 = PASS and dissolved its premise.** Koran et al. is `2605.15377`; its dataset is a 2,584-row subset of
>   `RoganInglis/apps-control-arena`, which ControlArena hardcodes. **One artifact, not two.** Honest solutions are
>   human-written; every backdoor is LLM-written.
> - **K2 = FAIL as framed in round 16, and the rewrite is the better paper.** The field already filters and strips
>   comments and says so (`2605.15377` §4.1, `2608.16190`, `2602.10153`, `2506.05296`); the "published monitor at
>   0.64" never existed. What survives: on the field's own filtered, comment-stripped split, a **bag-of-words
>   classifier scores AUROC 0.81 — above 20 of the 24 monitors ranked there** — and a classifier that **reads no
>   code scores 0.77, above 18**. Five same-generator agentic settings supply the negative control for free.
>   **→ *Authorship, Not Sabotage*, EvoRobust Sep 12.** Gate M is deleted: Jha's repo ships per-item scores.
> - **The fresh-areas scan found nothing that beats it** and one thing that broadens it (six corpora, two
>   mechanisms). Three fresh candidates are sections of the audit, not rivals. AgentHarm is excluded on G2.
> - **New rule R18:** twelve full-text keyword greps returned true zeros while four setup paragraphs held every
>   kill. Read the setup sections of the five nearest papers; a grep certifies vocabulary, not practice.
>
> **September total: ≤ $25 of the budget. Expected accepted papers ≈ 1.0, up from ≈ 0.75 under `notes/18`.**

## Start here

| If you want… | Read |
|---|---|
| **What to do this week** | [`notes/19`](notes/19-the-plan-round-17.md) — **the plan**: InfPriv Sep 7 (writing only), *Authorship, not sabotage* Sep 12 (Gate S, routes fixed), budget, stopping rules |
| **The board on the three axes, with code** | [`ideas/29`](ideas/29-round-17-three-axis-evaluation.md) — every idea scored on acceptance / safety / feasibility; the rewritten audit; the fresh-areas scan |
| **The code and the numbers** | [`experiments/`](experiments/README.md) — every script behind the round-17 figures, run on the full artifacts |
| The plan it replaced | [`notes/18`](notes/18-the-plan-two-submissions.md) — **superseded**; kept for its stopping-rule discipline and the November window |
| What round 16 found | [`ideas/28`](ideas/28-round-16-plan-audit.md) — the artifact audit and the November window; ⚠️ its §12 headline comparison is retracted in `notes/14` |
| The one-track plan it replaced | [`notes/17`](notes/17-the-plan-sep12.md) — **superseded**; kept for the Stage B2 cut and the Gate B mechanics |
| Why two branches died in round 15 | [`ideas/27`](ideas/27-round-15-external-preemption.md) — the three pre-emptions, the G2 fail, the gate arithmetic, the reframe |
| The runbook it replaced | [`notes/16`](notes/16-fork-and-branches.md) — **superseded**; kept for Stage 0/B mechanics and the pre-registration checklist |
| Why these candidates | [`ideas/26`](ideas/26-evorobust-reranked-board.md) — the board re-scored for EvoRobust |
| **The InfPriv ship checklist** | [`notes/15`](notes/15-infpriv-ship-checklist.md) — ★ **ACTIVE**: E0/E1 done, items 1/3/4/5 discharged, revised writing schedule |
| The safety lead, current | [`ideas/25`](ideas/25-round-14-c9-design-flaw.md) — C9's design flaw, the fix, and the gates it still owes |
| The recommendation it amends | [`ideas/24`](ideas/24-round-13-final-recommendation.md) — lead, venue plan, what changed |
| Why the round-12 board collapsed | [`ideas/23`](ideas/23-round-13-adversarial-review.md) — candidate-by-candidate teardown with the evidence |
| The superseded board | [`ideas/22`](ideas/22-round-12-final-recommendation.md) — kept for the reasoning, **not** for its scores |
| The scoring rubric | [`notes/11`](notes/11-safety-venue-review-rubric.md) — acceptance `A/30` and safety-relevance `B/25`, scored **separately**, plus five hard gates |
| **How to not waste a round** | [`notes/12`](notes/12-research-method-rules.md) — **eighteen** standing rules, each bought with a failure here. R18 is round 17's: read the setup sections, a grep certifies vocabulary not practice; compare on the same protocol or not at all |
| Deadlines | [`notes/13`](notes/13-venue-calendar.md) — canonical, and the UTC/AoE correction that closes ~25 apparently-open venues |
| **What is already dead** | [`notes/14`](notes/14-killed-ideas-ledger.md) — read before proposing anything |
| Verified citations | [`lit/02`](lit/02-verified-bibliography.md) — ✅ means the page was actually read; ⚠️ means do not cite |

## The rules that matter most

**Name the two nearest neighbours *outside* AI safety before adopting any measurement idea**
(`notes/12` R2, gate G1). Three leads died the same way — verified unclaimed inside AI control,
already published next door under different vocabulary. *A monitor is a classifier, a suspicion score
is a confidence score, an audit budget is a selective-prediction operating point.*

**Turn every new rule on the surviving lead, not only on what it killed** (`notes/12` R11). An
adversarial round exhausts itself on the candidates it kills, so the survivor is promoted for being
*least attacked*, not for being strongest — four consecutive leads were promoted that way and then
killed. Its companion **R12**: a lead surviving two rounds gets **built**, not re-searched. Thirteen
rounds have produced zero lines of experiment code while G3 says hour one is the load.

**An `arXiv abs:` query cannot certify a claim about what papers *report*** (`notes/12` R8). Round 13
killed C6 on this: Granite Guardian publishes ROC curves and a nine-guard fixed-FPR leaderboard, and
says none of those words in its abstract. Open the top ~10 papers and grep their results sections.
Two companions: **a zero-result needs a positive control in the same batch** (R3 — `http://export.arxiv.org`
returns a 301 that parses as zero hits), and **search LessWrong and the Alignment Forum** (R9 — the
control that was C1's differentiator was published there in June).

## Layout

- `notes/` — CFP digests, venue calendar, method rules, killed-ideas ledger, scoring rubric
- `lit/` — literature sweeps and the verified bibliography
- `ideas/` — the idea board, round by round; highest number is most recent

## Standing constraints

Public datasets only · no experiments involving real people · nothing person-specific reported
(`notes/08`). Compute budget **$200–300** — of which September needs **≤ $25** (`notes/19` §6). The binding
constraint is now writing time. Surplus goes to a second task setting, an adversarial arm and
confidence intervals, never to breadth (`notes/11`).
