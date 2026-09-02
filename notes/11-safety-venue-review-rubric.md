# Scoring rubric for round-12 candidates — AI-safety workshops

Written 2026-09-02, before the round-12 sweep results landed, so the rubric cannot be reverse-fitted
to whichever idea we end up liking. The brief changed in two ways this round: the compute budget
went from ~$20 to **$200–300**, and the objective is now explicitly **two** things —
(1) probability of acceptance at an open workshop, (2) relevance to *general* AI safety research.
Those two pull in different directions and the rubric has to price the tension rather than hide it.

## The tension, stated plainly

A paper can be accepted for being tidy, cheap, and unobjectionable while contributing nothing anyone
outside the workshop will cite. The previous round's Compression Tax drifted toward exactly that:
after the novelty was cut down by the compression-evaluation literature (`ideas/20`), what remained
was defensible and small. **Acceptance and relevance are separate axes and both must clear a bar.**
An idea that scores 5/5 on acceptance and 2/5 on relevance is not the answer to this brief.

## Dimensions (each 1–5; the gates below matter more than the total)

**A. Acceptance probability**

| # | Dimension | 1 | 5 |
|---|---|---|---|
| A1 | **Novelty, verified** | headline claim already published; we'd be replicating | verified-empty searches on the exact claim, and the nearest neighbour is clearly distinguishable in one sentence |
| A2 | **Scoop resistance over the review window** | 3+ active groups obviously converging on it | few groups, awkward to reach without our specific setup |
| A3 | **Outcome robustness** | only one direction of the result is publishable | both directions are a paper, *and* the framing does not depend on which |
| A4 | **Venue fit** | we'd be arguing the topic is in scope | the CFP names our object verbatim, and the reviewers run the thing we measure |
| A5 | **Executability at ≤9 days / ≤$300** | needs data we have not loaded, or generation, or training runs | data verified ungated and loaded, public harness exists, pure inference or light probing |
| A6 | **Claim discipline** | headline requires a claim bigger than the evidence | every sentence in the abstract is backed by a number in a table |

**B. Relevance to general AI safety research**

| # | Dimension | 1 | 5 |
|---|---|---|---|
| B1 | **Does a real safety decision change?** | a practitioner reads it and does nothing differently | it changes a deployment default, a safety case, or an eval protocol |
| B2 | **Generality beyond the setting** | one dataset, one prompt, one model family, no reason to expect transfer | mechanism-level, with a stated reason it should hold elsewhere and at least one transfer check |
| B3 | **Does it survive capability scaling?** | it is an artifact of today's weak open models and evaporates at the frontier | the effect is structural and gets *worse* or stays as models improve |
| B4 | **Threat-model honesty** | assumes an adversary nobody believes in, or no adversary where one is required | the threat model is stated, standard, and the result is robust to it |
| B5 | **Citability by the safety community** | a footnote in someone's related work | becomes the reference for a specific effect, or supplies an artifact others reuse |

## Hard gates — an idea failing any of these is out regardless of total

1. **G1 — Verified novelty.** The headline claim must survive a search of the *adjacent* literature,
   not just the home literature. Round 10 failed exactly here: it swept AI control, found nothing,
   and missed that the claim lived in compression evaluation (`ideas/20` §2). Every candidate must
   name the two nearest neighbours *outside* its home subfield.
2. **G2 — Organizer/committee collision.** Do not propose an idea that is an organizer's or invited
   speaker's own current line. This killed the MIA-on-safety-classifiers idea (Mireshghallah is an
   InfPriv organizer) and the whole private-RAG line. Check the committee list for every venue.
3. **G3 — Data and harness resolve before commitment.** Dataset must be confirmed ungated and
   actually loaded, not inferred from a docs page. Round 10 carried an unverified split composition
   for two rounds. Hour one of any build is the load, not the model.
4. **G4 — The "so what against the obvious axis" test.** If a cheaper or more obvious intervention
   already moves the metric more than our variable does, the paper needs an answer in the abstract.
   Concretely: `2608.16190` shows free choice of open-weight monitor spans **29×** in pAUC@10%FPR.
   Any monitor-property paper must say why its axis matters against that.
5. **G5 — Relevance floor.** B1 + B3 must both be ≥3. A result that changes no decision, or that
   evaporates as models get better, is not an AI-safety contribution regardless of how clean it is.

## Weighting

Acceptance and relevance are scored separately and reported separately. **Do not average them into
one number** — the whole point is that the brief has two objectives, and a single score would let a
high-acceptance/low-relevance idea hide. Report as `A: x/30, B: y/25`, plus gate pass/fail, plus a
one-line statement of the sharpest reviewer objection and whether we have an answer.

## Budget-specific note

$200–300 changes which ideas are reachable, and the temptation is to spend it on breadth (more
models, more bit-widths, more seeds). **Breadth is usually padding.** The dimensions it should buy
are the ones that answer a reviewer objection: a second *task setting* (does the effect transfer),
an *adversarial arm* (does it survive an attacker who knows), and *confidence intervals* (is the
effect real). Prioritize in that order. More points on an existing curve buy nothing.

## Standing constraints, unchanged

Public datasets only · no experiments involving real people · nothing person-specific reported
(`notes/08`). Verify every citation by fetching the source; a fabricated reference is a desk-reject
(`lit/02` protocol).
