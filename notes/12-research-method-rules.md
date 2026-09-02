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
