# Workshop paper ideation — AI safety (was: InfPriv @ NeurIPS 2026)

Working repo for a short workshop paper. **The brief changed twice.** It began as a 4-page InfPriv
(privacy) submission and pivoted in round 10 to **AI safety** — CoT monitoring, AI control,
post-training, mech interp. Round 12 added a second objective: the paper must be relevant to
*general* AI safety research, not only acceptable at a workshop.

**State as of 2026-09-02 (round 14).** **EvoRobust, Sep 12 AoE, is the target.** The repo had ruled
it out from its title; the fetched CFP names *"human oversight and controllability"* of tool-using
agents and *"continuously evolving safety benchmarks, automated test case generation, coverage
metrics"* in two of five topic areas ([`notes/13`](notes/13-venue-calendar.md)). Ten days, 4pp,
non-archival, dual submission allowed — so it does **not** consume the SaTML target.

The lead is **C9 — the situation-controlled pre-action benchmark**, whose design is corrected in
[`ideas/25`](ideas/25-round-14-c9-design-flaw.md): `ideas/24`'s version was *still* unfalsifiable,
because reading state at an offset *before* the divergence point is chance by the same determinism
argument used to kill the version before it. The read position moves strictly after first divergence
and becomes the swept independent variable. **Sep 3 is a fork** — the owed R8 sweep plus the first
data load in fourteen rounds decides between C9 and the C4 fallback
([`ideas/26`](ideas/26-evorobust-reranked-board.md)).

**AIWILD on Sep 5 passes deliberately.** The **InfPriv** paper (Sep 7, `notes/15`) is designed,
reviewed and ~$30 — but it is a privacy result, not a safety one, and the brief is safety. Shipping
it costs five days of focus against a live scoop clock. Recorded as a live option, not the plan.

## Start here

| If you want… | Read |
|---|---|
| **What to do this week** | [`ideas/26`](ideas/26-evorobust-reranked-board.md) — the board re-scored for EvoRobust, and the Sep 3 fork |
| The InfPriv option, if taken | [`notes/15`](notes/15-infpriv-ship-checklist.md) — ship checklist, Sep 7, ~$30 |
| The safety lead, current | [`ideas/25`](ideas/25-round-14-c9-design-flaw.md) — C9's design flaw, the fix, and the gates it still owes |
| The recommendation it amends | [`ideas/24`](ideas/24-round-13-final-recommendation.md) — lead, venue plan, what changed |
| Why the round-12 board collapsed | [`ideas/23`](ideas/23-round-13-adversarial-review.md) — candidate-by-candidate teardown with the evidence |
| The superseded board | [`ideas/22`](ideas/22-round-12-final-recommendation.md) — kept for the reasoning, **not** for its scores |
| The scoring rubric | [`notes/11`](notes/11-safety-venue-review-rubric.md) — acceptance `A/30` and safety-relevance `B/25`, scored **separately**, plus five hard gates |
| **How to not waste a round** | [`notes/12`](notes/12-research-method-rules.md) — twelve standing rules, each bought with a failure here |
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
(`notes/08`). Compute budget **$200–300** — which is not the binding constraint; novelty verification
is. The entire round-12 board costs under $250 combined, so surplus goes to seeds, placebo controls
and a second model family, never to breadth.
