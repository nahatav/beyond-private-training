# Standing method rules

Every rule below was bought with a failure in this repo. They are recorded here rather than left in
commit messages or session memory so they survive into rounds nobody remembers.

---

## R1 — Verify every citation by fetching the source

Never cite from a search snippet. `arxiv.org/abs/<id>` for title, full author list, date and
abstract; `arxiv.org/html/<id>` plus a tag-stripping script when a claim about a paper's *content* is
load-bearing. PDFs frequently fail to extract — use the HTML route.

**Why:** a search snippet once appeared to kill the lead idea and turned out to describe a different
paper. Separately, a round-10 sweep attributed a quantization finding to `2607.06596`; the full text
contains **zero** occurrences of quantiz*/8-bit/FP16/AWQ/GPTQ. The venue desk-rejects on fabricated
or misattributed references.

**Corollary:** nothing enters `lit/02` without a ✅ earned by an actually-read page. ⚠️ rows are
explicitly do-not-cite, not "probably fine."

---

## R2 — Name the two nearest neighbours *outside* AI safety before adopting any measurement idea

This is gate **G1** in `notes/11`, and it is the most expensive lesson in the repo.

**Why:** three consecutive leads died the same way — each verified as unclaimed *inside AI control*,
each already published in a neighbouring field under different vocabulary.

| Round | Idea | Verified empty in | Actually published in |
|---|---|---|---|
| 10 | Compression Tax headline | AI control | compression evaluation (`2607.24440`, `2602.01459`, `2606.01850`, `2602.09130`) |
| 11 | Compression Tax decomposition | AI control | LLM-as-judge / selective prediction (`2606.22179`, `2603.12520`, `2604.25235`) |
| 12 | (pre-empted by this rule) | — | CoT monitorability (`2607.09786`), self-explanation faithfulness (`2601.00282`) |

**The structural reason, worth memorising:** *a monitor is a classifier, a suspicion score is a
confidence score, and an audit budget is a selective-prediction operating point.* Anything claimed
about one is claimed about all three. AI control's vocabulary is young enough that its literature
reads as empty while the same result sits in ML evaluation under a different name.

**Healthy shape vs failing shape.** The failing shape is a novel-sounding *claim* with a published
equivalent. The healthy shape is a **standard, well-validated method applied to an unasked question** —
e.g. candidate C1 uses amnesic probing (`2006.00995`) and control tasks (`1909.03368`), both textbook,
against a question nobody has posed. Reviewers trust the method and the finding carries the novelty.

---

## R3 — A zero-result is citable only with a positive control in the same batch

**Why:** in round 12, two independent sweeps produced *fabricated evidence in both directions* from
the same tool.

1. **`http://export.arxiv.org` returns 301.** A client that does not follow the redirect receives an
   empty body that parses as `totalResults=0`. One sweep reported "the CoT-monitoring line has gone
   quiet, zero hits Jun–Sep 2026." The correct answer was **25 hits, 8 of them in that window.**
2. **Double-escaped quotes.** Pre-encoding `"` as `%22` and then URL-encoding again yields `%2522`.
   arXiv **silently ignores** the malformed tokens and returns a date-sorted dump of all recent
   submissions. A 40-result response looked like a successful query and was pure noise — the
   giveaway was neutrino detectors and halide perovskites in a deception-probe search.

**The rule.** Use `https://export.arxiv.org/api/query`. Read `opensearch:totalResults` directly
rather than counting `<entry>` elements. Run a query you *know* returns hits in the same script, and
report its count next to the negatives. A genuine empty feed is ~750–800 bytes and well-formed; a
redirect stub or an error is not.

**Worked example (round 12, the C6 negatives):**

```
POSITIVE CONTROL  abs:"audit budget" AND abs:"monitor"          -> 6   (12,424 bytes)
                  abs:"guard model" AND (abs:"ROC" OR "AUROC")  -> 0   (779 bytes)
                  all:"guardrail" AND all:"audit budget"        -> 0   (755 bytes)
```

Without the first line the next three are worthless.

---

## R4 — Attack the repo's own ideas as hard as the literature

Every round should kill or retract at least one item, recorded with the evidence so it stays dead.
Finding that a previously-proposed mechanism is dominated, or that a novelty claim is false, is a
**successful** round.

**Why:** the alternative is discovering it in review. Round 12's own sweeps killed three of their own
proposals on the G1 gate before presenting them — that is the behaviour to reward.

---

## R5 — Prefer outcome-robust ideas, and check that the robustness is still real

An idea is outcome-robust when both directions of the headline measurement are publishable. Near a
deadline this dominates raw novelty.

**Caveat added in round 12:** outcome-robustness can be *destroyed by later literature* without the
idea itself changing. The Compression Tax's "green light" direction ("quantize monitors freely")
stopped being publishable the moment `2509.21173` (ICML 2026) published the
compression-improves-reliability result. **Re-check robustness at each round; it is not a permanent
property.**

---

## R6 — Resource honesty: dataset friction kills more ideas than GPU hours

Confirm datasets are ungated and actually load before committing to a plan. Round 10 carried an
unverified split composition (1,936/482/1,375) for two rounds; the real artifact is a single
5,000-row split.

**Round-12 finding:** at a $200–300 budget, money is not the binding constraint — novelty
verification is. The entire round-12 candidate board costs under $250 combined. Spend surplus on
seeds, placebo controls, and a second model family, never on breadth (`notes/11`).

---

## R7 — Check organizer and speaker lines before proposing

Gate **G2** in `notes/11`. An idea sitting on an organizer's own research line is dead regardless of
merit. This killed the MIA-on-safety-classifiers idea (Mireshghallah is an InfPriv organizer) and the
entire private-RAG line (Wu + Chaudhuri). Check the committee list for every venue under
consideration, not just the primary target.

---

## R8 — An `abs:` query cannot certify a claim about what papers *report*

**Why:** round 13 killed candidate C6, whose headline was "no guardrail paper has ever published an
ROC curve for a guard model." Granite Guardian (`2412.07724`, Dec 2024) publishes ROC curves in
Figure 8, reports partial AUC and TPR at **fixed FPR of 0.1 / 0.01 / 0.001** across nine open guards
in Table 11, and argues in §6 that threshold-free metrics mislead because "real-time applications
have a strong need for low FPr." Its **abstract** contains none of "ROC", "AUROC", "pAUC", "audit
budget" or "fixed false positive rate". The searches were transport-clean, positive-controlled, and
looking in the wrong place.

**The rule.** A negative about *reporting practice* — "nobody measures M", "no one plots C", "the
field never fixes parameter P" — is only citable after you have **opened the top ~10 papers in the
target subfield and searched their results sections and appendices**, and recorded which ones you
opened. Fetch `arxiv.org/html/<id>`, strip tags, grep. Metric vocabulary lives in §5 and Appendix D,
never in the abstract.

**The tell we ignored.** Gate G4 already cited `2608.16190` using **pAUC@10%FPR on monitors**. That
should have made `abs:"guard" AND abs:"pAUC" → 0` implausible on its face. When a zero-result
contradicts something the repo already knows, the query is wrong, not the literature.

**Corollary — exact stems fail too.** `abs:"evaluation awareness" AND abs:"probe" AND abs:"ablat"`
returned 0 while at least three papers do the thing, because they write "steering", "controlled
rewrites" and "random controls" instead of "ablation". Search the concept, not the morpheme.

---

## R9 — Search LessWrong and the Alignment Forum before claiming novelty in AI safety

**Why:** round 13 gutted candidate C1. `ideas/21` called a matched-norm random-direction placebo
C1's mandatory design constraint and credibility differentiator. Sahil Raut had run exactly that —
diff-in-means eval-awareness direction, format-controlled 2×2 dataset, **ablation arm plus 24 random
direction placebo controls** — and published the null on **LessWrong, 2026-06-25** ("does not beat
the empirical null of 24 random directions, p = 0.20"; per-item sandbagging AUROC 0.542). arXiv
cannot see it. Reviewers at safety venues have read it.

**The rule.** A large fraction of empirical AI-safety work — MATS outputs, LASR streams, independent
replications, negative results — lands on LessWrong or the Alignment Forum first and often only.
Before any novelty claim in this domain, search both, plus the relevant lab blogs. A workshop
reviewer treating a well-read LessWrong post as prior art is behaving correctly.

---

## R10 — Score A5 on an HTTP 200, not on the absence of a stated gate

**Why:** `ideas/22` scored C1 "~$10, ~30 GPU-hours, **no training**, public artifacts confirmed live",
A5 = 5/5. The full text of `2509.21344` contains **no code release, no data release and no artifact
statement** — its only GitHub links are LaTeXML and arXiv-feedback boilerplate. Reproducing its 0.94
needs its prompt sets; reproducing its 0.57 needs its passphrase-dependent sandbagging model organism,
which the authors trained. `ideas/21` had already recorded that ("the dramatic number requires
*retraining a model organism*") and the score was never reconciled with the correction.

**The rule.** "Artifacts confirmed live" means a named repo or dataset returning HTTP 200, with a
`pushed_at` date, recorded in the candidate's own row. Extend R6 to code: **dataset friction and
missing harnesses kill more ideas than GPU hours.** And when a correction elsewhere in the repo
contradicts a score, the score is stale — reconcile it in the same commit that records the
correction.

---

## R11 — Turn every new rule on the *surviving* lead, not only on the candidates it killed

**Why:** round 13 wrote R8 (an `abs:` query cannot certify a claim about what papers *report*) and
used it to kill C6. It never applied R8 to C9 — whose headline is *"no existing dataset varies the
action with the situation held fixed,"* a negative about construction practice, and therefore
**exactly the class of claim R8 governs**. Dataset construction lives in appendices and datasheets,
even further from the abstract than metric vocabulary does. C9 inherited the lead by surviving a
review whose sharpest instrument was never pointed at it.

**The structural failure, worth naming:** an adversarial round exhausts itself on the candidates it
kills. Whatever survives is not the strongest idea — it is the least-attacked one. Four rounds in a
row have promoted a candidate on that basis and then killed it in the next round.

**The rule.** When a round produces a new method rule, re-run it against the surviving lead **in the
same round**, and record the result in the lead's own row. A gate is not passed until it has been
run; "not yet failed" is not a pass. Where a gate cannot be run — G2 against a venue whose organizers
have not been announced — write **unrunnable** in the board, never a tick.

---

## R12 — Novelty verification is capped; a lead that survives two rounds gets built

**Why:** thirteen rounds have produced **zero lines of experiment code and no dataset ever loaded**,
while R6 and gate G3 both say hour one of any build is the load. Each round satisfies R4 by killing
the previous lead and proposing a fresh one, which is a well-functioning kill-machine with no commit
step. Rounds 10–13 killed four consecutive leads; on that trend line round 14 kills C9 and there is
still no paper.

**The rule.** A candidate that survives two consecutive adversarial rounds moves to **build**, not to
a third review. The build's first day is the R8/R9 sweep on its own central claim plus loading the
data and reproducing one published number — which is cheaper than a review round and kills bad ideas
harder, because a harness that will not load is a fact and a novelty search is an inference.

**Corollary — R4 has a termination condition.** "Every round kills something" is a rule about
*rigour*, not a rule about *pace*. Once the marginal ideation hour is worth less than the marginal
build hour, killing one more idea is not progress. State that comparison explicitly at the end of
every round.

---

## R13 — Fetch a venue's topic list before grading fit, and remember that A4 is not a property of an idea

**Why:** `notes/13` graded EvoRobust "⚠️ Moderate — the spine is quality-diversity *search*; likely no
AI-control background," and `ideas/22` used that to conclude that **AIWILD was the only venue whose
reviewers could read our work.** The CFP says otherwise. Two of its five topic areas are
*"Agentic Safety & Interactive Robustness: safety of tool-using agents, long-horizon failures,
multi-agent risks, **human oversight and controllability**"* and *"Benchmarks and Governance:
continuously evolving safety benchmarks, **automated test case generation**, coverage metrics."*
Invited speakers include **Maksym Andriushchenko** and **David Wagner**. The judgment was read off
the workshop's *title*, which advertises its methods community, not its topic scope.

This is R8's failure in the venue domain: **a title is an abstract.** The scope lives in the topic
list, the speaker roster and the organizer affiliations, exactly as metric vocabulary lives in §5 and
Appendix D.

**The rule.** No venue gets a fit grade — least of all a *negative* one — until its CFP topic list,
speakers and organizers have been fetched from the workshop's own page. Ruling a venue out is a
stronger claim than ruling it in, and it needs more evidence, not less. Grading a venue out on its
name is how a board ends up with one viable target three days before its deadline.

**The corollary, which is the expensive half.** `notes/11` **A4 is venue fit** — so **an `A` score is
never a property of the idea alone.** Every A/30 on the round-12 board is really *"A at AIWILD,"* and
nothing in `ideas/21`, `ideas/22` or `ideas/24` says so. When the venue set changes, the board must be
**re-scored, not re-read**: a candidate downgraded for "the answer is already expected" can rank
*higher* at a venue whose topic is systematically searching for expected failures, and a candidate
carried on venue-native metrics can rank lower where nobody runs them. Record A as `A: x/30 @ <venue>`
from now on.
