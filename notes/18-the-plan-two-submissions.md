# The plan — two submissions: InfPriv Sep 7, the validity audit Sep 12

Written 2026-09-02 (round 16), after `ideas/28`. **Supersedes `notes/17`**, which routes the whole
window into one rushed C9 submission at EvoRobust. `notes/17` is kept for its two correct structural
calls (drop Stage B2; never let the GPU idle) and for the Gate B mechanics, which survive into the
November leg.

Same discipline as `notes/09` and `notes/17`: thresholds and stopping rules fixed **now**, before
evidence arrives, so an outcome selects a path instead of starting an argument.

---

## 0. What changed, in one paragraph

`notes/17` sends **C9** to EvoRobust on Sep 12. Round 16 read the *artifact* C9 is built on rather than
the papers around it, and found that Gate C's threshold is contradicted by the incumbent's own published
base rate, that the mandated transfer number is pre-published on our own model, and that the reframe's
delta is thinner than `notes/17` §1 states (`ideas/28` §1–§3). Separately, an asset-first sweep produced a
candidate whose **central measurement needed no GPU and is already done** (`ideas/28` §12). So the
EvoRobust slot changes hands, and C9 goes to the November window — which round 16 established is real and
dated, not a void (`ideas/28` §8).

**The headline change is not "two papers instead of one." It is which paper goes to EvoRobust.**

## 1. The three tracks

| Deadline | Paper | State today |
|---|---|---|
| **Sep 7 AoE** | **InfPriv** — the PE vote-normalisation estimand paper (`ideas/10`, `ideas/14`, `notes/15`) | Designed, twice adversarially reviewed, ~$30. Primary exhibit **re-verified today** on live `microsoft/DPSDA` `main` — see §6. No LaTeX yet. |
| **Sep 12 AoE** | **The validity audit** — partial-input and selection floors for AI-control backdoor benchmarks (`ideas/28` §12) | Central number **already measured** on the full 5,000-row split. No harness yet. **Gated by K1/K2 — §3.** |
| **Nov** | **C9** — sampling-divergence pre-action predictability, built to full scope | Unchanged in substance; released from deadline pressure. Target set in §7. |

## 2. Why two submissions are affordable now, and were not before

Neither September paper needs the thing that made `notes/17` hard. The 10–30k agentic rollouts, the gated
Llama licence, the Bedrock-only judge, the Petri second domain, the unmeasured generation throughput —
none of it is on the critical path any more. InfPriv is ~1–2 GPU-hours plus writing. The audit is batch
inference over a dataset that downloads in minutes.

**The honest cost, stated so it stays a decision.** `notes/17`'s "never let the GPU idle" had a dual —
never let the human idle while the GPU generates — and that dual bought the second paper for free *only
because C9 had four unattended generation days*. **The audit has no such phase.** Its GPU work is roughly
one day of monitor runs. So these two tracks are **serial, not parallel**: InfPriv Sep 3–7, audit Sep 8–12.
Five days against a seven-day plan, with D1 already collapsed because the floors are computed. **Tight, and
with no buffer.** That is the price of the second submission and it is paid knowingly.

## 3. Sep 3 AM — the two killing checks, before anything else

The audit is a **round-16 lead**, which is exactly what R11 warns about. It gets built anyway, on R12's
narrow ground — R12 exists because this repo never builds, and this one is already partly built — but only
after the two checks that would kill it. **They run first, before InfPriv work starts, because they gate
the entire Sep 12 leg.** Desk work, 2–3 hours, no GPU.

> ### K1 — which artifact?
> `2608.16190` reproduces a **1,375-sample test split (172 attack / 1,203 honest)** from *"the public
> backdoored-APPS dataset released with Koran et al. (2026)"* — **not** `RoganInglis/apps-control-arena`.
> **Two distinct APPS-backdoor datasets exist.** Fetch Koran et al., locate the artifact, and compute the
> same metadata floor on it.
>
> **PASS** — the floor reproduces, or the second artifact shares the selection mechanism. The claim is
> about the benchmark family. **AMBER** — the floor is specific to `apps-control-arena`. The paper still
> stands but must be scoped to that artifact in the title and abstract, and the contribution shrinks.
> **FAIL** — the second artifact is cleanly constructed and the first is an outlier nobody uses. Go to §5.
>
> *This also retires `notes/14`'s correction about the 1,936/482/1,375 split: that split is real, in a
> different artifact. Fix the ledger row in the same commit.*

> ### K2 — is the floor genuinely unreported?
> The novelty rests on full-text greps of ~10 papers returning zero for partial-input /
> problem-statement-only / construct-validity. **That is an R8-class negative and is not citable until
> its positive controls are recorded in `lit/02`.** Re-run it, record which papers were opened, and put
> the positive-control counts beside every zero (R3).
>
> The nearest neighbour is **`2607.06596`, which `notes/14` understates** — its full text carries
> difficulty-matched and blatancy-matched controls, code-only vs full-transcript cuts, head swaps and
> hash-disjoint splits. Read it properly and write the one-sentence distinction, or concede the point.
>
> **PASS** — zeros hold with controls, and `2607.06596` is distinguishable in one sentence.
> **FAIL** — the floor, or something equivalent, is already reported. Go to §5.

**Also on Sep 3 AM, free and owed:** accept the `meta-llama/Llama-3.1-8B-Instruct` HuggingFace licence.
It is gated (`ideas/28` §5), it costs nothing, and it is on the November leg's critical path.

## 4. Schedule

| Day | Work | Gate |
|---|---|---|
| **Sep 2, tonight** | Start the InfPriv LaTeX skeleton in the NeurIPS template. Begin `notes/15`'s six pre-flight items — item #1 is **already discharged**, see §6. | — |
| **Sep 3 AM** | **K1 and K2.** Accept the Llama licence. | **K1 / K2** |
| **Sep 3 PM** | InfPriv **E0** code checks + **E1a**, the `d_u/(k·m_u)` ratio. **Headline decided by end of day** (`notes/15`). | **InfPriv branch** |
| **Sep 4** | InfPriv **E1 full** — re-weighting curves for `p ∈ {1, 1.5, 2}` plus record-level. **Central figure done.** | — |
| **Sep 5** | InfPriv **E2** if E1a landed strong, else **E4**. Per `notes/15`'s branch rule. | — |
| **Sep 6** | Write InfPriv. Four pages. | — |
| **Sep 7** | Review against the CFP's unsubstantiated-claims policy. **Submit InfPriv.** | — |
| **Sep 8** | Audit: recompute **every** floor on the full split (§6). Freeze splits by `problem_id` hash. **Push the pre-registration public.** Stand up the GEPA harness on local vLLM. | — |
| **Sep 9** | Reproduce a published-style pooled monitor AUROC. Then run the monitor under four protocols: pooled / matched-within-problem / comment-stripped / `backdoor_works`-filtered. | **GATE M** |
| **Sep 10** | Second monitor lineage — the floors must be monitor-invariant or the thesis is wrong. Honest-but-buggy negative arm. | — |
| **Sep 11** | Figures, intervals, write. | — |
| **Sep 12** | Buffer. **Submit the audit.** | — |

> ### GATE M — Sep 9, on the harness
> **PASS** — the GEPA harness completes end-to-end on local vLLM and reproduces a pooled monitor AUROC in
> the neighbourhood of the published **0.64**. Continue.
> **FAIL** — no completed monitor run by end of Sep 9. **Ship the floors alone**: the metadata result,
> the `backdoor_works` result and the matched-pair analysis are a complete 4-page paper with no monitor in
> it. Do not spend Sep 10–11 debugging a harness.

**Report `pAUC@1%FPR` alongside AUROC everywhere.** Control evals are read at an audit budget; AUROC
alone is not comparable to how the field states its safety numbers, and G4 asks for exactly this.

## 5. Stopping rules, and what happens after a stop

**Fixed now, so they are not invented under pressure.**

- **K1 or K2 returns FAIL** → **InfPriv is the only September submission.** C9 keeps November.
  **Do not backfill EvoRobust with rushed C9** — that is the thing `ideas/28` §1–§3 argues against, and
  reaching for it under deadline pressure is the R11 failure this repo has committed four times.
- **The schedule slips after Sep 8** → InfPriv is already submitted; **the audit slides to November** and
  joins C9. Nothing is lost but the slot.
- **Gate M fails** → ship the floors alone, per Gate M.
- **InfPriv's E0 finds the non-integer-count interaction** → that is a real finding on day one with four
  days left, and `notes/15` has two writable branches plus an unconditional algebraic floor. It degrades;
  it does not fail.

**The InfPriv leg is the one to argue about, and the argument is recorded here.** It is the only paper on
the board scoring **zero on objective (2)**, safety relevance, and it consumes the five days that would
give the audit real slack. The defensible alternative is to drop it and put everything into the audit.
This plan keeps it because the brief ranks acceptance first and InfPriv buys roughly half an expected
acceptance against a cost of perhaps 0.1 on the audit's — but that is a judgment on the weights, not a
fact, and it is the owner's call, not the plan's.

## 6. What is already verified, and what must be recomputed

**Verified today, ✅ fetched, no GPU:**

- **InfPriv pre-flight item #1 is discharged.** On live `microsoft/DPSDA` `main` (pushed 2026-08-21):
  `pe/histogram/nearest_neighbors.py` still carries `vote_normalization_level`, default `"sample"`,
  documented verbatim as *"'client' (normalize the votes from all private samples of the same client to
  have l2 norm = 1)"*, with `split_by_client()` in the `"client"` branch. And `pe/dp/gaussian.py` contains
  **zero** occurrences of `normaliz*` or `client` — ε is computed from `noise_multiplier` and `num_steps`
  alone. **The accountant never inspects the mode.** That is the paper's primary exhibit, on current code.
- **The audit's floors, on all 5,000 rows** (`ideas/28` §12): metadata-only held-out **AUROC 0.8229**;
  difficulty-only 0.6823; `solution_passes_tests` 0.9774 vs 0.3969 (≈0.790 alone);
  `backdoor_works` 1,582 vs `has_backdoor` 2,473 — **36% of labelled backdoors do not work**.

**⚠️ Must be recomputed before anything is written.** The sweep that proposed the audit reported two
numbers that **did not replicate** — `P(has_backdoor | difficulty=competition)` as 0.000 when it is
**0.203**, and difficulty-only AUROC as 0.751 when it is **0.6823** — and claimed its sample's marginals
matched the full split exactly, which they do not. The finding survived and got stronger, but **carry no
sampled figure into the paper.** Full split or nothing.

## 7. The November leg

`ideas/28` §8 establishes the window with every date read off the venue's own page: **SaTML main Sep 29**;
**FAccT 2027 Nov 3**, which offers an explicit non-archival option and names *"AI red teaming and
adversarial testing"* and *"Interpretability/explainability"*; **AAAI-27 workshops Nov 20**, with the
workshop list enumerable from **Oct 2**; **SaTML workshops** Oct–Dec, organizers notified **Sep 18**.

**C9 goes here, built to the scope it was always scored on** — two scenario domains, 210+ pairs per class,
confidence intervals, the transfer arm, and the released pair generator. `ideas/28` §4 makes the second
and third domains a **template render** rather than a build: `anthropic-experimental/agentic-misalignment`
(MIT) ships `blackmail`, `leaking` and `murder` in the same SummitBridge format the harness consumes, and
its `replacement` / `restriction` conditions are the legitimate lever on the action rate that `ideas/28`
§1 shows is needed.

**Re-check dates:** **Sep 18** (SaTML workshop organizers notified — run **G2** that day), **Oct 2**
(AAAI-27 workshop CFPs), **Oct 27** (FAccT abstract).

## 8. Open items

- ⏳ **The out-of-field pre-emption sweep on C9's reframe is still running** — early classification of
  time series, prediction-horizon and lookahead work, branched-rollout RL, LessWrong/AF. It bears on the
  **November leg's framing**, not on either September submission. Record its verdict in `lit/02` with
  positive controls when it lands; if it returns OCCUPIED, C9's November framing changes before any
  pre-registration is written.
- **`notes/14` owes two corrections** — the 1,936/482/1,375 row (see K1) and the `2607.06596` row, which
  understates the paper (see K2).
- **`notes/13` owes two rows** — NeuralArtifacts is **live at Sep 9 AoE**, its own CFP now showing
  `~~September 1~~ → September 9`; and **FLLMPT is a Sep 12 venue**, not Sep 5, with a mandatory Sep 5
  abstract. Both were misfiled.
- **A free option, not a target:** FLLMPT's abstract registration is Sep 5 and costs a title and an
  abstract. It and EvoRobust are both non-archival with concurrent submission explicitly allowed, so it
  buys a second Sep 12 shot at near-zero marginal cost once the paper exists. Fit is post-training, so it
  is weaker; take it only if Sep 5 is otherwise quiet.

## 9. Odds, recorded so they can be scored later

| Path | P(submit) | P(accept ¦ submit) | Note |
|---|---|---|---|
| InfPriv → Sep 7 | ~0.85 | ~0.55–0.70 | Design complete and twice reviewed; risk is LaTeX and the pre-flight list, none of it compute |
| Audit → EvoRobust Sep 12 | ~0.6 serial with InfPriv | ~0.45–0.60 | Conditional on K1/K2. Central number exists; the risk is the harness and the five-day squeeze |
| C9 → November | — | — | Not scored until the §8 sweep lands |

Judgment, not measurement — treat as ordering, not as numbers. `notes/17`'s single-track figure was
**~0.15–0.22 end to end**; the reason to prefer this plan is that both September legs clear that on their
own, and neither depends on generating a corpus from zero in nine days.

## 10. Standing constraints, unchanged

Public datasets only · no experiments involving real people · nothing person-specific reported
(`notes/08`). Compute budget **$200–300**; both September papers together are well under **$70**.
Local open-weight models, **no paid API**. Verify every citation by fetching the source (**R1**); a
zero-result needs a positive control in the same batch (**R3**).

---

## Appendix A — the C9 sweep: what it is and what closes it

The sweep is the outstanding **out-of-field pre-emption check on C9's reframe**. `notes/17` §1 records the
standing risk plainly: the reframe's novelty rests on a **negative** search result, which is the class of
claim **R8** exists to distrust. `notes/17` §3 folded the check into "Sep 4–6 dead time" — *after* the Sep 3
public pre-registration. `ideas/28` §7 calls that out: the one irreversible action in the plan was
scheduled ahead of the check that could void it.

**Moving C9 to November fixes the sequencing for free.** The sweep is no longer a scrap of dead time
between generation jobs; it can be run properly, and it must close before any C9 pre-registration is
pushed.

### A.1 The claim under test

> Pairs of agent rollouts whose divergence is caused **only by the sampler** — same prompt, same cue,
> byte-identical prefix, different sampled token at divergence point `t` — with the read position indexed
> by **tokens since `t`**, probing residual-stream activations to predict whether the rollout culminates in
> a harmful action.

Three papers are known to partially occupy it and are **not** what the sweep is looking for: `2606.09890`
(PreAct-Bench), `2507.12428` (foresight horizon), `2606.30449` (bridge probe at two prefill fractions).
The surviving novelty is **only** the sampling-divergence construction and the distance-from-divergence
index.

### A.2 The neighbourhoods, and why these

**R14: a gate's target list must be drawn from the rule it discharges.** This one discharges **R2/G1** —
name the two nearest neighbours *outside* AI safety — so the list is deliberately out-of-field:

1. **Early classification of time series** (ECTS) — a ~25-year literature on the earliness/accuracy
   tradeoff. Does anyone already index predictability by distance from a branch point?
2. **Prediction horizon / lookahead in transformers** — future-token prediction, belief states,
   multi-token prediction, "does the model plan ahead", future lens.
3. **Branched-rollout RL** — ⚠️ **the most dangerous neighbourhood.** VinePPO-style advantage estimation,
   GRPO variants, tree search, process reward models, value functions over partial rollouts. *Branch from
   a shared prefix and measure what the branch determines* is that literature's core operation.
4. **Interpretability** — residual-stream probing on partial trajectories, outcome prediction as a
   function of position relative to an event.
5. **Aleatoric/epistemic decomposition in generation** — "how much of the outcome is the prompt."
6. **LessWrong and the Alignment Forum** (**R9**) — MATS/LASR outputs and negative results land there
   first and often only, and workshop reviewers have read them.

### A.3 What closes it

A verdict is not closed until all of these are true:

- **Positive controls beside every zero, in the same batch (R3).** Use `https://export.arxiv.org/api/query`
  — the `http://` form 301s and the empty body parses as zero. Read `opensearch:totalResults` directly.
  *(Noted from today's run: the API rate-limits under rapid fire and returns 14-byte bodies that also parse
  as zero. Sleep ≥8s between queries and treat any sub-1KB response as a transport failure, not a result.)*
- **Full texts opened, not abstracts (R8).** For the top ~10 threats, fetch `arxiv.org/html/<id>`, strip
  tags, and grep the body for `divergen`, `branch`, `shared prefix`, `identical prefix`, `token offset`,
  `resampl`, `fork`, `prefix`. Record **which** papers were opened.
- **Search the concept, not the morpheme.** Exact stems fail — people write "steering", "controlled
  rewrites", "random controls" where you searched "ablation".
- **The OCCUPIED condition stated in advance** (R14's companion — a gate that cannot fail is not a gate):
  a target returns **OCCUPIED** if it constructs pairs by *sampling* from a shared prefix **and** analyses
  a state read at a position indexed *relative to the divergence point*. Either alone is **NEIGHBOUR**,
  cite and continue.
- **Recorded in `lit/02`** with the date, the verdict and the verbatim sentence for any non-CLEAR row. An
  unrecorded sweep is not evidence.

### A.4 Routing

- **CLEAR** → C9's framing stands. Write the one-sentence distinction against the nearest neighbour in
  each of neighbourhoods 1–3, and put it in the related-work paragraph.
- **NEIGHBOUR** → cite and continue; related work gets harder, the project does not change.
- **OCCUPIED** → **the framing changes before any pre-registration is pushed**, not after. This is the
  whole reason the check moved ahead of the irreversible step.

### A.5 Also owed on C9, independent of the sweep

From `notes/11`'s round-14 amendment, still open and now re-pointed at the November venues:

| Gate | Status | What closes it |
|---|---|---|
| **G2** — organizer/speaker collision | **unrunnable** | Re-run against **FAccT 2027**, **AAAI-27 workshops** (list from Oct 2) and **SaTML workshops** (organizers notified Sep 18) once each committee exists. `2606.30449`'s group is the plausible occupant of any agent-monitoring venue. |
| **G4** — the obvious competing axis | **owed** | Run probe family and training scale as a **competing arm**, not folded into the experiment. `2606.30449` name four untested families. |
| **G3** — data and harness, our side | **unrun** | Hour one is the load. The Llama licence is accepted Sep 3 (§3); the clone and a first Gate B run still have to happen. |
