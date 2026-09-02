# Workshop paper ideation — AI safety (was: InfPriv @ NeurIPS 2026)

Working repo for a short workshop paper. **The brief changed twice.** It began as a 4-page InfPriv
(privacy) submission and pivoted in round 10 to **AI safety** — CoT monitoring, AI control,
post-training, mech interp. Round 12 added a second objective: the paper must be relevant to
*general* AI safety research, not only acceptable at a workshop.

**State as of 2026-09-02 (round 13).** The lead is **C9 — the situation-controlled pre-action
benchmark**, reframed as an evaluation-methodology contribution and targeted at the **Sep 19 SaTML
workshops** window. Round 13's adversarial review killed C6 outright and removed the novelty and the
executability from C1, so **AIWILD on Sep 5 passes deliberately, with no submission.**

## Start here

| If you want… | Read |
|---|---|
| The current recommendation | [`ideas/24`](ideas/24-round-13-final-recommendation.md) — lead, venue plan, what changed |
| Why the round-12 board collapsed | [`ideas/23`](ideas/23-round-13-adversarial-review.md) — candidate-by-candidate teardown with the evidence |
| The superseded board | [`ideas/22`](ideas/22-round-12-final-recommendation.md) — kept for the reasoning, **not** for its scores |
| The scoring rubric | [`notes/11`](notes/11-safety-venue-review-rubric.md) — acceptance `A/30` and safety-relevance `B/25`, scored **separately**, plus five hard gates |
| **How to not waste a round** | [`notes/12`](notes/12-research-method-rules.md) — ten standing rules, each bought with a failure here |
| Deadlines | [`notes/13`](notes/13-venue-calendar.md) — canonical, and the UTC/AoE correction that closes ~25 apparently-open venues |
| **What is already dead** | [`notes/14`](notes/14-killed-ideas-ledger.md) — read before proposing anything |
| Verified citations | [`lit/02`](lit/02-verified-bibliography.md) — ✅ means the page was actually read; ⚠️ means do not cite |

## The rules that matter most

**Name the two nearest neighbours *outside* AI safety before adopting any measurement idea**
(`notes/12` R2, gate G1). Three leads died the same way — verified unclaimed inside AI control,
already published next door under different vocabulary. *A monitor is a classifier, a suspicion score
is a confidence score, an audit budget is a selective-prediction operating point.*

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
