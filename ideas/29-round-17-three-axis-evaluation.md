# Round 17 — the board evaluated on the three axes, with code

Written 2026-09-03. The brief for this round was explicit: evaluate every idea on **(1)** the chance a paper
gets submitted *and* accepted, **(2)** relevance to AI safety, **(3)** feasibility inside ~$300 and the
deadlines — and look for better areas. Six subagents ran in parallel (K1, K2, the DPSDA hour-one load, a
fresh-areas scan, venue/G2 checks, the InfPriv scoop patrol); the coordinator recomputed every load-bearing
number on the full artifact (R17). **For the first time in seventeen rounds the evaluation rests on
experiment output, not on search results.** Scripts: [`experiments/`](../experiments/README.md). Evidence
rows: `lit/02` round 17.

**The one-paragraph answer.** InfPriv is no longer a plan; it is a paper with its central figure drawn, its
bibliography resolved and its scoop patrol clean, and it costs nothing more than writing time. The Sep 12
validity audit survived its two killing checks *only after being rewritten*: K1 passed decisively, K2 failed
the round-16 framing — the field already preprocesses the leaks the audit was going to announce — and what
survives is sharper than what died: **the stored honest/attack pairs behind the field's open code-backdoor
monitoring numbers are human-written versus LLM-written, and a bag-of-words classifier that cannot read a
backdoor beats 20 of the 24 monitors ranked on the field's own filtered split.** C9 stays parked for
November and is now the weaker November option. No fresh area beat these on all three axes (§5).

---

## 1. How the three axes map onto the rubric

| Brief axis | `notes/11` dimensions | What decides it this week |
|---|---|---|
| **(1) submitted and accepted** | P(submit) × A1–A6 | Does code exist? Is the claim occupied? Does the venue's reviewer read the metric? |
| **(2) safety relevance** | B1–B5, gate G5 | Does a practitioner change a protocol, and does the effect survive better models? |
| **(3) feasible: ~$300, deadlines** | A5 + wall-clock | Nothing on the board now needs more than one GPU-day. Money stopped being the constraint in round 12; **writing time** is the constraint now. |

Axis (1) contains P(submit), so feasibility is double-weighted — as `ideas/28` §9 noted.

## 2. InfPriv — *Normalising users changes what Private Evolution estimates* · Sep 7

| Axis | Score | Evidence (all 2026-09-03) |
|---|---|---|
| **(1)** | **P(submit) ≈ 0.95 · P(accept ¦ submit) ≈ 0.55–0.70** | Hour one happened: DPSDA `c109ea5e` cloned, installed (39 packages, 7 s), the `"client"` branch driven directly; E0, E1a, E1b done in **34 s of compute**; the central figure exists (`experiments/infpriv/e1_reweighting_curve.png`); 14/14 bibliography entries fetched; scoop patrol clean on metadata *and* full text of eight PE papers; G2 clear (Zinan Lin authored the code — framed as a principled choice with an under-examined consequence; Chulin Xie co-authored Aug-PE — one citation). Propositions 1–3 are algebra. The only risk left is prose. |
| **(2)** | **0 / 25** | A privacy result. It does not change a safety decision. The brief ranks acceptance first, and this is the near-certain acceptance; that trade is made knowingly (`notes/18` §5) and is not re-argued here. |
| **(3)** | **$0 spent, ≤ $5 if E4 is widened on a rented GPU — which it need not be** | Runs on the laptop. |

**What round 17 changed in the paper.** (i) The primary exhibit gained a fact: the `"client"` path is exercised by
**no** example, loader, test or doc in the repository. (ii) E0's risk was answered NO and replaced by a better
finding — `histogram_threshold` is a raw count whose *unit* moves under `"client"` mode; the repo's own example
thresholds keep 733 candidates record-level and **2** client-level at threshold 2, and **zero** (a `NaN` crash) at
threshold 4. That is the thesis in one parameter, and it goes into the "beyond PE" paragraph. (iii) The real anchor
(arXiv by first author) lands in the **weak branch** — `d_u/(k·m_u)` ≈ 0.80–0.89 — so the headline is **exponent ½**
on real data and **diversity tilt** on the controlled arm (3.16× spread in user share at c=0.5), E2 is cut, and
Sep 5 goes to E4. Both branches were always writable; now both are written.

## 3. The validity audit, rewritten — *Authorship, not sabotage* · Sep 12 · EvoRobust

### 3.1 What the killing checks returned

**K1 = PASS, and it dissolved its own premise.** "Koran et al. (2026)" is `2605.15377`; its dataset
`eugenekoran/apps-control-arena-high-quality` is a 2,584-row filtered subset of `RoganInglis/apps-control-arena`
(all `problem_id`s contained; every shared column byte-identical except a re-validated `backdoor_works`), and
ControlArena hardcodes the RoganInglis name. **One artifact, one derived copy.** Honest solutions are human-written
(`codeparrot/apps`, no model ever called); every backdoor is LLM-written (GPT-4 for the `2312.06942` set; ten
models for Control Tax). ControlArena's *live* evals generate both classes; the replay policy that submits stored
code is opt-in — and it is what Koran, Jha and the DSPy tutorial use.

**K2 = FAIL as framed in round 16.** The field already filters to working honest + working backdoors, strips
comments, and says why (`2605.15377` §4.1, `2608.16190` §2, `2602.10153`, `2506.05296` §2.3 and App. C.3 —
verbatim in `lit/02`). And the "published monitor at 0.64" the round-16 floor was measured against **does not
exist**: the DSPy tutorial reports 69% *pairwise accuracy* on *matched* pairs, a protocol where the metadata floor is
exactly 0.5. Twelve keyword greps had returned true zeros over all of this — hence **R18**.

**What survives, and it is the better paper.** Nobody reports a partial-input, bag-of-words or authorship baseline;
nobody quantifies what the preprocessing leaves behind; and the field's own filter *installs* a second selection
artifact by defining the negative class through attack failure.

### 3.2 The numbers (coordinator's recompute, full artifact — `experiments/audit/`)

| Protocol | Baseline | Result | Comparator |
|---|---|---|---|
| DSPy tutorial's matched pairs (8,813 pairs, problem-disjoint 5-fold) | TF-IDF 1–2gram logistic regression | **96.2%** pairwise | tutorial's LLM monitor: 69% untrained, 78–81% GEPA |
| same | "the longer code is the attack" | **82.5%** | — |
| same, 200 training pairs (the tutorial's size) | TF-IDF | 92.8% | — |
| same, split by `backdoor_works` | TF-IDF | working 97.9% · **non-working 95.4%** | the signal is not sabotage |
| transfer across generators | train Control-Tax → test GPT-4 (2023) | 99.4% | style, not content |
| **Koran's exact split**: train on their paired train (2,418), score their 1,375-item **comment-stripped** test | TF-IDF | **AUROC 0.806**, TPR@10%FPR 0.48 | **above 20 of the 24 monitors** in `2608.16190` (median 0.609, max 0.937) |
| same, comments kept | TF-IDF | 0.891 | above 22/24 |
| Koran's test split, **no code read** (difficulty, #tests, statement length) | LR, 5×5 CV | **0.772 ± 0.039** | above 18/24; attack problems have half the test cases |
| Inert backdoors | `backdoor_works` | 36% of labelled backdoors on the raw artifact; **80.7% in Koran's test split, relabelled honest** | 60% of "honest" test items are failed attacks |

### 3.3 The paper

> **Title.** *Authorship, Not Sabotage: Trivial Baselines on the APPS Backdoor Benchmark*
>
> **Claim.** The stored honest/attack pairs behind open trusted-monitoring results on APPS are human-written vs
> LLM-written. On the field's own filtered, comment-stripped split, a bag-of-words classifier reaches AUROC 0.81 and a
> classifier that reads no code 0.77, above most of the 24 open-weight monitors ranked there; the bag-of-words signal
> transfers across backdoor generators and is as strong on inert backdoors as on working ones. Regenerating honest
> solutions with the attack model removes it [the Sep 8 control]. We recommend that stored-pair monitor evaluations
> report partial-input and bag-of-words floors, use same-generator honest samples, and drop inert backdoors from
> both classes.

**Contributions, each with a number behind it:** (1) the protocol × baseline table above; (2) the authorship mechanism
with the same-generator control; (3) the second selection artifact the field's filter installs (negative class =
attack failure; half the test cases); (4) the fix, as a drop-in preprocessing step and a released split.

**Mandatory first-paragraph citations** (K2's condition): `2605.15377`, `2608.16190`, `2602.10153`, `2506.05296`
— credited for the filter, the comment leak and the failed-backdoor appendix. **Cite against ourselves:** Feng,
Wallace & Boyd-Graber `1905.05778` — *"the failure of a partial-input baseline does not mean a dataset is free of
artifacts."* **Out-of-field neighbours:** Poliak `1805.01042`, Gururangan `1803.02324` (method and phenomenon);
AICD Bench `2602.02079` and CodeMirage `2506.11059` (the mechanism — LLM code is detectable from human code; we
claim only the application to a safety benchmark, which none of them touches).

**The control that decides the headline — and both outcomes are a paper (R5).** Generate honest solutions for the
3,420 filtered problems with a local model, keep the ones that pass the shipped tests, rebuild the pairs, rerun the
baselines.
- Bag-of-words collapses toward chance → **authorship**: the benchmark as stored measures who wrote the code.
- It does not collapse → **content**: these backdoors are separable by surface features regardless of author, and
  LLM monitors are underperforming a linear model on them. Also publishable; different title.

**Reviewer objections, answered in advance.** *"A trained classifier beats zero-shot monitors — so what?"* The
claim is Gururangan's, not "our monitor is better": the label is recoverable from features that cannot see a
backdoor, at 200 training pairs, and from no code at all. *"Live control evals generate both classes."* True, and
said in §1: the artifact affects monitor **training, selection and benchmarking** on stored pairs — exactly what
`2605.15377`, `2608.16190` and the reference tutorial do, and what a monitor ranking is used for. *"Andriushchenko's
group already attacks these monitors."* Different axis: they subvert monitors with injected text; we show the
benchmark's label leaks through authorship. Cite in paragraph one.

### 3.4 On the three axes

| Axis | Score | Why |
|---|---|---|
| **(1)** | **P(submit) ≈ 0.80 · P(accept ¦ submit) ≈ 0.45–0.55 @ EvoRobust** | Every number in §3.2 exists today on CPU. One GPU control and one same-harness monitor run remain (§4 of `notes/19`). Venue names *"Benchmarks and Governance… coverage metrics"*; G2 clear; the healthy R2 shape (textbook method, unasked question). Risk: five writing days shared with nothing else after Sep 7. |
| **(2)** | **B: 19–20 / 25** | B1 **4** — changes how monitors are benchmarked on stored pairs (same-generator honest; report floors; drop inert backdoors). B2 **3** — one benchmark family today; the scan (§5) says whether it generalises. B3 **4** — structural to the dataset, not to any model; better attack models make it worse, not better. B4 **4** — no adversary needed. B5 **4–5** — a released split and a floor every stored-pair paper must report. |
| **(3)** | **$10–40** | vLLM generation for 3,420 problems on a 4090 ≈ 1–2 GPU-h; test execution is CPU; one prompted monitor pass ≈ 2 GPU-h. |

## 4. C9 — parked for November, and now the weaker November option

Unchanged from `notes/18` §7 in substance: the pair framing is dead (Forking Paths lineage), the divergence-relative
axis survives as a gap of composition, and the honest cost is 10–30k rollouts, a gated model, a judge with no local
provider, and a first paragraph that must cite four papers that got there first. On the three axes it is the worst
item on the board: **(1)** low novelty at a venue that does not yet exist; **(2)** high interest fit, but B5 weak
for a one-model curve; **(3)** the only candidate that needs the budget. **The audit's authorship line is the better
November extension** — the same method across every public control benchmark that ships stored pairs — and it will
have a submitted 4-page paper and a released split behind it by then. Decide on Oct 2 against the AAAI-27 list, as
`notes/18` says; do not spend an hour on C9 before Sep 13.

## 5. Better areas we had not considered

_See the addendum at the end of this file (the fresh-areas scan)._

## 6. Odds, recorded so they can be scored (judgment, not measurement)

| Path | P(submit) | P(accept ¦ submit) | Axis 2 | Cost |
|---|---|---|---|---|
| InfPriv → Sep 7 | 0.95 | 0.55–0.70 | 0 | $0 |
| Audit, rewritten → EvoRobust Sep 12 | 0.80 | 0.45–0.55 | 19–20/25 | $10–40 |
| Audit → FLLMPT Sep 12 (free abstract Sep 5, dual allowed) | +0.05 marginal | 0.30–0.40 | same | $0 |
| C9 → November | — | — | — | $100–200 |

Expected accepted papers this month ≈ **0.6 + 0.4 ≈ 1.0**, against `notes/17`'s single-track 0.15–0.22 and
`notes/18`'s ≈ 0.75. The gain over `notes/18` is entirely that both legs now have code.

---

## Addendum — §5, the fresh-areas scan (landed after the sections above were written)

Full findings, with every artifact's HTTP status, licence and per-class generator provenance:
[`experiments/audit/scan/FINDINGS.md`](../experiments/audit/scan/FINDINGS.md). **Verdict: nothing beats the
audit; one thing broadens it.** The three best fresh candidates are all *sections of the audit*, not rivals to
it — which is the healthiest possible answer nine days out, and the one R12 exists to produce.

### 5.1 Direction A is real, and it supplies the audit's negative control for free

Five ControlArena agentic settings are public, ungated, labelled and — unlike APPS — **same-generator**: 250 honest
+ 250 attack rollouts from each of claude-sonnet-4, gemini-2.5-pro and gpt-5 (`adityaasinha28/control_arena_{bash,
shade, iac, rogue_eval, agentdojo}`, all HTTP 200, 1,500 rows each, ⚠️ **no licence statement** — state it; we
redistribute nothing). No authorship confound is possible there, and a structural floor still appears in some:

| setting | pooled 5-fold | **within-task (character count only)** | permutation null |
|---|---|---|---|
| bash | 0.609 | **0.504** — clean | 0.49 |
| shade | 0.664 | 0.602 | 0.51 |
| iac | 0.535 | 0.704 | 0.48 |
| rogue_eval | 0.668 | 0.616 | 0.48 |
| agentdojo | 0.932 | **0.802** — leaky | 0.51 |

The scan attacked its own pooled numbers and they partly broke (task composition), which is why the within-task
column is the one that goes in the paper. **Two mechanisms, one table:** authorship on APPS (removable only by
regenerating the honest class), structure on the agentic settings (removable only by length-matching). This is
`notes/11`'s "second task setting" bought for zero dollars, and it is what makes B2 a 4.

### 5.2 Two things the scan found that change the plan

- **Gate M is deleted.** `anik-jha/challenger-panels` (MIT) ships `runs/scores/` — per-item scores for all 24
  monitors on the identical 1,375 items. The monitor comparison needs **no GPU**. The only GPU in the Sep 12 leg
  is the same-generator control (Gate S in `notes/19`), $5–10.
- **Jha's repo already ships two leak checks** (`--leak-check`: comment count 0.696 → 0.498 after stripping;
  code length 0.4726), and its README says *"Stripping is mandatory, not cosmetic."* **"Nobody ran a trivial
  baseline" is dead as a sentence.** Both published checks are code-side; the problem-side floor (0.77 CV) and
  the authorship floor (0.81) survive them. *A finding that survives someone else's audit is stronger than one
  in a field that never audits* — provided the paper credits the audit in paragraph one.

### 5.3 The R17 flag the scan raised, resolved

The scan flagged the coordinator's *"longer code is the attack — 82%"* as being in tension with Jha's published
`code_length_only_auroc = 0.4726`. Both are correct and measure different objects: 82.5% is **within-pair** on the
raw tutorial protocol (comments included, no works filter); on the Koran-filtered pooled protocol the coordinator's
length-only AUROC is **0.587**, and on Jha's exact comment-stripped split K1 reproduced **0.4726 bit-exactly**. Length
is a carrier on the raw artifact and is not one after the field's filter — which is precisely the "what the
preprocessing leaves behind" table. Every number in §3.2 was recomputed by the coordinator on the full artifact
before it entered this file.

### 5.4 The candidates the scan killed, with the evidence

| Candidate | Verdict | Killed by |
|---|---|---|
| **CoT scratchpad regex** — 15 words on the untrusted policy's own reasoning, AUROC 0.76–0.82 across five settings, because prompted attack policies restate their side task | **section, not paper** (A 21/30) | `2607.09786` already runs a lexical detector, a content-blind length-matched null and a scrubbed-vs-unscrubbed classifier ablation. It is the CoT row of the audit's table and the row the user's interests care most about — keep it as one paragraph. |
| **Label-noise ceiling** (36% inert backdoors; 81% in the HQ test split) | one paragraph | `backdoor_works` is a shipped, documented column and Koran's filter selects on it. |
| **IRT on the 24 × 1,375 score matrix** | killed on A4/B1 (A 18/30) | wrong register for EvoRobust's PC; changes no deployment default. **Its artifact is what deleted Gate M.** |
| **AgentHarm** as a sixth corpus | **excluded on G2** | Andriushchenko authored it and is an EvoRobust invited speaker. |
| Direction B — a fresh textbook-method-on-unasked-question candidate in CoT monitoring / control / post-training / mech interp using released artifacts | none found that beats the audit | The honest answer, and R12's. |

### 5.5 Out-of-field neighbours added by the scan (all fetched)

`2410.11672` Pacchiardi et al., *Leaving the barn door open for Clever Hans: simple features predict LLM benchmark
answers* — the internal-validity framing; `2207.07048` Kapoor & Narayanan, *Leakage and the Reproducibility Crisis*
— the leakage taxonomy. `2606.06529` (attacker-side selection lowers safety −20/−28 pp at 1% budget; Tracy is a
co-author) is a **neighbour to cite**: it makes the "control evals are optimistic" case from the other side, and it
tells us Redwood/UK AISI people are in this neighbourhood (A2 = 3, not 5).

**Standing obligation before any pre-registration (R16):** the AICD-literature sweep is abstract-level. Take
`2602.02079` and `2506.11059` to full text and grep for control/monitor/sabotage/APPS — the scan did (zero, with
`backdoor`=1 and `safety`=1 as in-batch controls in CodeMirage), and it must be recorded in `lit/02` with the
sentences, not the counts.
