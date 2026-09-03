# Round 16 — the audit of `notes/17`, run against the artifact instead of the papers

Written 2026-09-02, after `notes/17` fixed the plan on one track. Round 15 read the *papers* around C9
and killed two branches. **This round read the *artifact* C9 is built on** — `maxf-zn/misalignment_monitoring`,
the repo Gate B clones on Sep 3 — and its `README.md`, `data/README.md`, `configs/` and
`docs/PAPER_RESULTS.md`. Everything below was fetched today; nothing needs a GPU.

**Headline: the plan does not die, but four of its load-bearing numbers are already published, and
three of them go the wrong way.** Gate C's threshold is contradicted by the incumbent's own measurement,
the transfer arm's result is pre-published, and the reframe's delta is smaller than `notes/17` §1 states.
Against that, one genuine accelerant was found that the plan does not use.

---

## 1. Gate C's PASS threshold is already answered NO by published data

`notes/17` Gate C routes on a **median minority-action rate ≥ 10%**, measured on a pilot.

`docs/PAPER_RESULTS.md`, Probe 3, steering specificity — **Gemma-3-27B-IT, T=0.7, n=300**, on the
committed `summitbridge_blackmail` scenario, ✅ fetched:

| Condition (alpha) | Blackmail rate |
|---|---|
| **Baseline (0)** | **5.3%**, CI **[3.3, 8.5]** |
| Desperate (0.10) | 20.3% |
| Random (0.10) | 16.7% |

**The unsteered base rate on this exact scenario is 5.3%, and the whole 95% CI sits below Gate C's
PASS line — at n=300, ten times the pilot's N=30.** The plan's primary model is *Llama-3.1-8B*, smaller
than the 27B this was measured on.

Consequences:

1. **The Sep 7 pilot is largely pre-answered, and the answer is AMBER-to-FAIL.** `ideas/27` §4's own
   arithmetic then applies: the AMBER band needs **4,200–26,000 rollouts for a single domain**. At 5.3%
   and a 210-pair-per-class target, the minority class alone needs ~4,000 rollout-sets *per domain*.
   `notes/17` §8's planning estimate of **5,000–10,000 rollouts total across two domains** is low by
   roughly 2–5×.
2. **The 20.3% "Desperate" figure is not a rescue.** Raising the rate by activation steering destroys
   the construction — the divergence would no longer be caused only by the sampler.
3. **There is a legitimate lever, and it is cheap — see §4.**

## 2. The transfer arm's result is already published, on our own model

`notes/17` §6 makes "one held-out-scenario transfer number, **reported even if negative**" non-negotiable.

`PAPER_RESULTS.md`, Probe 2 — **behavioral prefill probe, Llama-3.1-8B-Instruct**, n=1950, ✅ fetched:

| Quantity | Value |
|---|---|
| Best single-layer behaviour AUC (attn-out L14) | **0.801 ± 0.040**, **+5.1 pp over majority** |
| Label-shuffle null | 0.526 (200 perms) |
| **Domain classification (3-way, L31)** | **AUC 0.999, acc 0.985** — "reads domain, not behavior" |
| MLP (512-unit) | 0.788; **LODO mean lift −4.2 pp, 5/6 non-positive** |

So on the plan's own primary model the incumbent has already reported: a probe that looks like it
predicts behaviour, is shown to be mostly reading the *situation* (domain AUC 0.999 against behaviour
+5.1 pp), and **does not transfer across domains (−4.2 pp)**. The mandated transfer number has a
published expected value, and it is negative.

## 3. The reframe's delta is thinner than `notes/17` §1 claims

`notes/17` §1: the sampling-divergence framing is *"the one formulation the three incumbents do not
contain."* That is true of the **construction**. It is not true of the **conclusion**. The artifact's
own claims table, ✅ fetched, states both ends of C9's intended curve:

> **C2.** Prefill probes predict prompt-domain content near-perfectly but **lift behaviour prediction by
> only ~+5 pp over majority and fail to transfer across domains**; a 512-unit MLP does not close the gap.

> **C3b.** A shared-prefix minimal pair has indistinguishable pre-divergence hidden states; **the
> behavioural split is reactive to the environment, not predictively encoded.**

C3b is C9's *j* ≤ 0 anchor — which `ideas/25` §1 already concedes is a tautology — and it is stated as a
*claim*, not as a floor. C2 is the post-divergence end. **"How much is the situation and how much is the
sample" has a published directional answer from this group: mostly the situation, and it does not
transfer.** C9's increment is a cleaner construction, a properly indexed x-axis between those two points,
and confidence intervals.

That is a legitimate methods contribution. It is **not** an open question, and the abstract must not
imply it is. Round 15 read the incumbent's *limitations section*; nobody read the artifact's *results
doc*, which is where the answers live (**R8**, one level deeper than round 15 went).

**Costs this imposes:** A3 (outcome robustness) falls — the expected result is now "small lift, no
transfer," pre-published in weaker form and anticipable by a reviewer. G4 ("the obvious competing axis")
is owed a sentence in the abstract saying why the curve is worth more than C2's single number.

## 4. The one accelerant the plan does not use — the second domain is a template swap

`ideas/27` §5 promotes the second scenario domain from surplus to **mandatory** for EvoRobust, and
`notes/17` §9 calls it "the largest single lever." Neither says where it comes from. The harness commits
**one** scenario (`configs/scenarios/summitbridge_blackmail.yaml`), and its own regeneration route is
Petri — a second framework, plus **auditor and judge model roles the reference config runs on paid
Bedrock Claude**, plus an H100-class target. That route is blocked by the standing no-paid-API
constraint and by `notes/17` §2's own decision to drop the 27B.

**But the scenario config is two YAML fields — `system:` and `user:` — of plain text.** And its own
provenance header names the source, ✅ fetched:

> `anthropic-experimental/agentic-misalignment` (Lynch et al. 2025, **MIT**, 652 stars)

That repo ships **three harmful-action domains — `blackmail`, `leaking`, `murder`** — each with 7 email
templates and 5 goal-conflict variable sets, in the same SummitBridge email/tool format the harness
already consumes, plus `scripts/generate_prompts.py` and `templates/template_parser.py` that emit exactly
the two strings the scenario YAML needs.

**So: domains 2 and 3 are a template render, not a build.** This is the largest single de-risking
available and it costs hours, not days.

**It also fixes §1.** The templates vary the pressure condition (`none` / `replacement` / `restriction`)
and the goal conflict, which is the *designed* lever on the action rate — as opposed to steering, which
contaminates the construction. Picking the condition that puts the base rate near 20–30% is legitimate,
must be **pre-registered** (it is a scenario-inclusion criterion, `notes/17` §5 item 6), and is the
honest answer to §1.

## 5. Two hour-one facts that belong tonight, not on Sep 3

**G3/R6 say hour one is the load. These are the loads, and both are free.**

1. **`meta-llama/Llama-3.1-8B-Instruct` is a gated model.** The artifact's README says so twice —
   *"Models are gated and GPU-bound. Gemma-3 and Llama require accepting their HuggingFace licenses"* —
   and `data/README.md` records a "Built with Llama" obligation. **Accept the licence on HuggingFace
   tonight.** Approval is not always instant, and a 401 at 09:00 on Sep 3 spends the 90-minute Gate B box
   on paperwork.
2. **The repo commits no rollouts.** `data/README.md`: *"This repository commits no model weights,
   **rollout collections**, raw activations, transcripts, or aggregate result artifacts."* The 596
   rollouts behind the bridge probe are **not** released. `notes/16`'s DATA-FOUND branch — "pairs get
   cheaper, you may get a second domain free" — **does not fire here.** Every rollout must be generated.

Two smaller wrinkles found in the same pass:

- **The judge has no local provider.** `src/misalignment_monitoring/evaluation/providers/` contains
  `bedrock.py` and `replay.py` only, and `PAPER_RESULTS.md` states all blackmail rates are
  `leverage_attempt >= 5` from a Claude-via-Bedrock judge with **n=30 spot-check agreement 0.80,
  Cohen's κ 0.59**. Labelling ~10k new rollouts this way costs real money and breaks the no-paid-API
  constraint. The alternative is a rule-based "action commits" detector on the emitted email — feasible,
  cheap, and already required to be pre-registered (`notes/17` §5), but **nobody has scoped it**, and κ
  0.59 is the label-noise ceiling C9 inherits either way.
- **Gate B cannot reproduce the published floor as written.** The identity-cosine study
  (`configs/studies/divergence_minimal_pair.yaml`, min cosine **0.99999893** over 12 layers × 274
  positions) is configured for **Gemma-3-27B-IT**, which `notes/17` §2 deliberately dropped. `llama31_8b`
  *is* in `configs/models.yaml` (default layer 14), so a Llama divergence run is configurable — but it is
  a *new* run, not a reproduction. Say so, and don't spend the 90-minute box discovering it.

## 6. Throughput is the number that decides Sep 12, and no gate measures it

Nowhere in `notes/16`, `notes/17`, `ideas/25` or `ideas/27` is generation throughput estimated in
rollouts per hour. Gate B measures pipeline completion and identity cosine — neither of which tells you
whether the corpus exists by Sep 9.

The one published datum, from the artifact's README: steering studies *"serialise one vLLM server per
condition; expect several hours per study at n=300"* → order **50–100 rollouts/hour**, with per-condition
server restarts C9 need not pay. Against §1's revised requirement (order 10–30k rollouts) that is
**100–600 GPU-hours**. The plan allots roughly 90–140.

**Good news: the harness already uses vLLM** (`src/misalignment_monitoring/models/vllm_server.py`), so
generation is batched, and C9's pairs share a prefix *by construction* — prefix caching should apply.
The pessimistic branch is unlikely. But it is unmeasured.

**Two fixes, both cheap:**

1. **Add a throughput reading to Gate B.** Twenty minutes of generation, reported as rollouts/hour.
   Route on it. It is the number that decides whether Sep 12 exists.
2. **Convert budget into wall-clock.** `notes/17` §8 says *"budget is not the binding constraint — time
   is,"* and then never makes the trade. Generation is embarrassingly parallel across scenarios, seeds and
   conditions. Renting 6–8 pods for 24–36 h is on the order of **$50–170** against a $200–300 budget
   (⚠️ *estimate from typical 4090/A6000 hourly rates; not verified today*). That is the difference between
   the corpus existing on Sep 6 and on Sep 11.

## 7. The sequencing error: the sweep runs after the irreversible step

`notes/17` §1 records a **standing risk** — the reframe's novelty rests on a negative search result — and
§3 discharges it with an out-of-field sweep folded into **"Sep 4–6 dead time."**

But the **public pre-registration goes out Sep 3 PM**, and generation starts the same evening. If the
sweep returns OCCUPIED on Sep 5, the plan has published a timestamped pre-registration on an occupied
claim and burned two days of GPU.

The sweep costs hours and needs **no GPU**. **Run it Sep 2–3, before the pre-registration.** This is
R14's own lesson applied one step further: round 15 correctly re-aimed the sweep and then demoted it from
a gate to dead-time filler, behind the one irreversible action in the plan.

## 8. The calendar was wrong in the other direction too — there is a November window

A venue sweep run today, every date read off the venue's own page:

**Two previously-unrecorded NeurIPS-workshop slots after Sep 8:**

| Venue | Deadline | Format | Note |
|---|---|---|---|
| **NeuralArtifacts** | **Sep 9 AoE** ✅ | ext. abstract **4–6pp**, non-archival | `notes/13` says *"do not plan around this venue"* on a stale-page discrepancy. **Resolved: its own CFP now shows `~~September 1~~ → September 9, 2026 (AoE)`.** Scope names *"Interpretability through weights, activations, representations, gradients, and other traces"* and *"Model safety and reliability interventions"* — but the community is weight-space / model-zoo, so `notes/13`'s ⚠️ on *reviewer fit* stands. |
| **FLLMPT** — Foundations of LLM Post-Training in Changing Environments | **abstract Sep 5 23:00 GMT (mandatory)**, paper **Sep 12 23:00 GMT** ✅ | NeurIPS main-track format, non-archival, dual submission welcome | Was misfiled in the Sep 5 cohort; it is a **Sep 12** venue. CFP names *"ML theory, reinforcement learning, and **AI safety**"* and *"**safety-critical settings**, where unintended regressions or feedback loops may arise."* ⚠️ **GMT, not AoE — 13 h earlier than EvoRobust.** Fit is post-training, so weaker than EvoRobust for C9, but the abstract is free. |

**And the "gap until roughly November" is a real, dated window, not a void:**

| Venue | Deadline ✅ | Why it matters |
|---|---|---|
| **SaTML 2027** main | abstract Sep 22 / paper **Sep 29** | 12pp, **archival** (IEEE). Already the repo's full-version target. |
| **FAccT 2027** | abstract Oct 27 / paper **Nov 3**, 11:59 PM AoE | 14pp, and it offers an explicit **non-archival** option. Topics list *"AI red teaming and adversarial testing"* and *"Interpretability/explainability"* verbatim. |
| **AAAI-27 workshops** | **Nov 20**, AoE | Workshop CFPs due to AAAI **Oct 2**, so the list is enumerable in a month. Historically the densest concentration of safety/alignment workshops in the window. |
| **SaTML 2027 workshops** | CFPs ~Oct–Dec | Organizers notified **Sep 18**. First SaTML workshop edition. |

**Consequence for `notes/17`.** §7's fallback — *"submit nothing on Sep 12 and take the SaTML window"* — is
much better than it reads. The cost of not making Sep 12 is **7–11 weeks of delay into a well-populated
window**, not silence until an unknown date. That changes what the Sep 12 deadline is worth paying for.

**Also closed:** IAB's Oct 1 route and InfPriv's Sep 25 fast track both **require an existing NeurIPS 2026
main-conference submission with reviews appended** ✅. Neither is reachable from here. Do not re-check them.

**And the misfiling was expensive.** The Sep 5 cohort contains several venues that fit C9 *better than
EvoRobust* — **Meta-Agents** (*"Misalignment and Safety for Meta-Agents"*, *"Governance and Human Oversight"*),
**FAST** (*"Evaluation, detection, and bounding of emergent capabilities or failure modes"*,
*"Observability and steerability of agent populations"*), **IAB**, **ATTRIB**, **TTCL**. All close Sep 5
and none is reachable with zero experiment code. This is a lesson for the next cycle, not a door.

## 9. The path comparison — and why the portfolio dominates

The brief is three axes in priority order: **(1)** chance of acceptance, **(2)** relevance to AI safety,
**(3)** actually getting submitted to a NeurIPS venue in time. Note that (1) already contains
*P(submitted)*, so feasibility is effectively double-weighted.

**What §8 establishes:** for a NeurIPS venue, the door set is essentially **NeuralArtifacts Sep 9**
(wrong community), **EvoRobust Sep 12** and **FLLMPT Sep 12** (weak fit), plus **InfPriv Sep 7**. So
`notes/17`'s *venue choice* is right. What changes is that **missing Sep 12 now costs 7–11 weeks into a
dated, well-populated window**, not silence.

| Path | Axis 1 (accept) | Axis 2 (safety) | Axis 3 (submitted) |
|---|---|---|---|
| **A — `notes/17` as written**: C9 → EvoRobust Sep 12, single track, no fallback | P(submit) ~0.40–0.55 after §1/§5; P(accept¦submit) ~0.30–0.45 at an EC pool on a thin delta (§3) → **~0.15–0.22** | Object is safety; **audience is not**. B5 weak for a 1-model, possibly 1-domain benchmark | **Poor** — the plan's own words: *"not obviously reachable"* |
| **B — portfolio**: InfPriv Sep 7 · C9 keeps Sep 3 Gate B and starts generation Sep 3 PM · EvoRobust Sep 12 as a *free* shot with whatever exists · **real C9 target = the November window** | InfPriv ~0.8 × ~0.55–0.70 → **~0.45–0.60**, plus the EvoRobust shot on top | C9 built to full scope (2 domains, 210+ pairs, CIs, transfer, released generator) at a **safety-native** venue — strictly better than A on B2/B5 | **Near-certain** — a written, twice-reviewed paper into a NeurIPS workshop on Sep 7 |
| **C — abandon C9 for a fresh cheap idea** | Restarts novelty verification with 10 days left | — | R12 forbids it; four consecutive leads died this way |
| **D — build C9 for November only, submit nothing in September** | Best on 1 and 2 | Best | **Fails axis 3 outright** — and is dominated by B, which gets November *and* September |

**B dominates A on all three axes**, because the two legs are not competing for the same resource:

- **C9's Sep 4–7 is unattended generation.** `notes/17` §2 says *"never let the GPU idle while a human
  types."* **The dual is also true: never let the human idle while the GPU generates.**
- **InfPriv's compute is ~1–2 GPU-hours and needs no generation at all.** A second pod for its decisive
  figure is a couple of dollars against a $200–300 budget.
- The only genuine collision is **Sep 3**, which carries two hour-one loads. Sequence it: Gate B in its
  90-minute morning box → InfPriv E0/E1a in the afternoon → C9 generation starts that evening.

**`notes/15`'s justification has expired and was never re-decided.** It reads: *"It does not compete with
C9 for a single hour that matters. C9 cannot be submitted anywhere before Sep 19 at the earliest."*
`notes/17` moved C9 to **Sep 12**, which makes that sentence false — and `notes/17` §7's stopping options
list C2 and "submit nothing," but **not the one paper that is already written, twice-reviewed and ~$30.**
This is the same omission `notes/13` already caught once (*"dropped the Sep 7 row without deciding
anything"*), recurring one round later.

**And the R11 appeal is a misapplication.** R11 forbids promoting a *least-attacked* idea and inventing a
replacement branch under deadline pressure. InfPriv is neither: it is the oldest, most-reviewed asset in
the repo, with an unconditional algebraic floor. Declining to ship it is a decision that should be made
on its merits, not by citing a rule about something else.

**Verified tonight, in support of the InfPriv leg** — `notes/15` pre-flight item #1, ✅ fetched against
live `microsoft/DPSDA` `main` (pushed 2026-08-21):

- `pe/histogram/nearest_neighbors.py` still carries `vote_normalization_level`, defaulting to `"sample"`,
  documented verbatim as *"'client' (normalize the votes from all private samples of the same client to
  have l2 norm = 1)"*, with `split_by_client()` in the `"client"` branch.
- `pe/dp/gaussian.py` contains **zero** occurrences of `normaliz*` or `client` — ε is computed from
  `noise_multiplier` and `num_steps` alone. **The accountant never inspects the mode.** That is the
  paper's primary exhibit, standing on current code.

**Honest cost of B, stated so it is a decision.** Axis 2 gets nothing from the InfPriv leg — it is a
privacy paper and the brief is safety. What it buys is axis 3 outright, and what it costs C9 is not
safety content but *the rush*. And the risk is real: two hour-one loads on Sep 3, neither ever performed.
The mitigation is that both degrade gracefully — InfPriv falls back to its algebraic floor plus one
figure (Propositions 1–3 are elementary and no measurement can invalidate them), and C9 falls back to the
November target.

**One free option worth taking either way:** FLLMPT's abstract registration is **Sep 5, mandatory, and
costs a title and an abstract**. Both it and EvoRobust are non-archival with concurrent submission
explicitly allowed, so filing it buys a second Sep 12 shot at essentially zero marginal cost once the
paper exists. Its fit is weaker (post-training), so this is an option, not a target.

## 10. What this round does not change

- **The idea survives.** Nothing here occupies the sampling-divergence construction. §3 shrinks the
  delta; it does not take it.
- **`notes/17`'s structural calls stand.** Dropping Stage B2, merging Gate C into the build, and never
  letting the GPU idle are all correct and are the reason a Sep 12 submission is arguable at all.
- **No new candidate is proposed here.** R12 caps novelty verification; this round attacks the plan, not
  the board.

## 11. Amendments owed to `notes/17`

| § | Item | Change |
|---|---|---|
| §5 | Pre-registration | Add the scenario *condition* (none/replacement/restriction + goal conflict) as an inclusion criterion — §4 |
| §4 | Gate C threshold | Re-derive against a **published 5.3% baseline**, not an assumed 10% — §1 |
| §4 | Gate B | Add a **rollouts/hour** reading and route on it — §6 |
| §3 | Sep 2 tonight | Accept the Llama-3.1 HF licence; render `leaking` + `murder` scenario YAMLs; scope the rule-based action detector — §4, §5 |
| §3 | Out-of-field sweep | Move **before** the Sep 3 PM pre-registration — §7 |
| §6 | Transfer arm | Keep it, but state that the incumbent already published **−4.2 pp LODO** — §2 |
| §1 | Abstract | Do not imply the situation-vs-sample question is open; cite C2 and C3b and claim the *curve*, not the *answer* — §3 |
| §8 | Budget | Convert surplus into **parallel pods**, not breadth — §6 |

---

## 12. A third path, found in this round and verified on the full split

An asset-first sweep produced one candidate whose central measurement **needed no GPU and is already
done**. I reproduced it myself on all 5,000 rows of `RoganInglis/apps-control-arena` (parquet pulled from
the HF datasets-server; `pandas` + `sklearn`, held-out 30% split, stratified, `random_state=0`):

```
rows: 5000
has_backdoor:    2473 / 5000 = 0.4946
backdoor_works:  1582 / 5000 = 0.3164

P(has_backdoor | difficulty)      size   sum    mean
  competition                     1000   203   0.2030
  interview                       3000  1874   0.6247
  introductory                    1000   396   0.3960

solution_passes_tests by has_backdoor    size    mean
  False                                  2527  0.3969
  True                                   2473  0.9774

METADATA-ONLY held-out AUROC:   0.8229
DIFFICULTY-ONLY held-out AUROC: 0.6823
```

**The contribution.** A classifier that never reads one character of code scores **AUROC 0.823** on the
field's main open backdoor-monitoring benchmark, because the positive class is a *selected* subset of
problems. For reference, the DSPy/GEPA writeup reports a gpt-4o-mini monitor at **AUC 0.64** on this task
— *the metadata floor is above the published monitor.*

**The mechanism is one column.** `solution_passes_tests` is 0.9774 on backdoored problems and 0.3969 on
the rest; as a single binary predictor that alone is AUROC ≈ **0.790** of the 0.823. Backdoors were only
authored where the honest solution worked. That is a protocol artifact, and **no choice of monitor can
remove it** — which is also the answer to G4, since the 29× monitor-choice span (`2608.16190`) is a
property of monitors and this is a property of the evaluation.

**A second, independent validity problem, from a column the dataset already ships:**
`backdoor_works` = 1,582 against `has_backdoor` = 2,473 — **36% of labelled backdoors do not work.**

### ⚠️ Two of the sweep's numbers did not replicate — corrected here

| Claim as reported | Full-split truth |
|---|---|
| `P(has_backdoor \| difficulty=competition)` = **0/200 = 0.000** | **203/1000 = 0.203** — the claim is wrong |
| Difficulty-only AUROC **0.751** | **0.6823** |
| "the n=1,000 sample's marginals match the full split exactly" | **They do not** — the two rows above are the counterexample |
| Metadata-only AUROC 0.801 | **0.8229** — replicates, and stronger |
| `backdoor_works` 1,582/5,000 = 31.6% | **✅ exact** |
| `solution_passes_tests` 0.977 vs 0.503 | 0.9774 vs **0.3969** |

**The finding survives the corrections and gets stronger. Recompute every number on the full split
before anything is written; do not carry the sampled figures.**

### Where it sits on the three axes

- **Axis 3 (feasibility): decisively better than C9.** For the first time in sixteen rounds, hour one has
  happened. No generation, no gated model, no judge, no Petri, no H100. Batch inference only, ~15
  GPU-hours, **$25–40**. It can be written with slack before Sep 12 instead of on the buffer day.
- **Axis 1:** the healthy shape `notes/12` R2 names — a textbook method (partial-input / hypothesis-only
  baselines, Poliak et al. \*SEM 2018) on an unasked question. Every number is a *floor*, so nothing
  depends on beating a baseline. Venue fit at EvoRobust is *"Benchmarks and Governance: continuously
  evolving safety benchmarks… coverage metrics"* — and unlike C9 it has no n=1-problem-instances
  exposure, since it spans 5,000 problems.
- **Axis 2:** control evals feed safety cases through "safety at 1% audit budget." If the negative class
  is selected and a third of the positives are inert, published control numbers are inflated. That
  changes an eval protocol (B1), and it does not evaporate with scale (B3) — better models give better
  monitors, not a cleaner negative class.

### The two checks that would kill it, neither yet run

1. **Which artifact?** `2608.16190` reproduces a **1,375-sample test split (172 attack / 1,203 honest)**
   from *"the public backdoored-APPS dataset released with Koran et al. (2026)"* — **not** this one. **Two
   distinct APPS-backdoor datasets exist.** If the leak is a property of `RoganInglis/apps-control-arena`
   alone rather than of the benchmark family, the claim narrows sharply. *This also retires
   `notes/14`'s correction about the 1,936/482/1,375 split: that split is real, in a different artifact.*
2. **Is the floor genuinely unreported?** The claim rests on full-text greps of ~10 papers returning zero
   for partial-input / problem-statement-only / construct-validity. That is an **R8-class negative** and
   needs its positive controls recorded in `lit/02` before it is citable. The nearest neighbour is
   `2607.06596`, which `notes/14` **understates** — its full text carries difficulty-matched and
   blatancy-matched controls, code-only vs full-transcript cuts, head swaps and hash-disjoint splits.

**And the standing objection: this is a new lead in round 16.** R11's warning applies. The
counter-argument is narrow but real — **R12's rule exists because the repo never builds, and this one is
already partly built.** Both killing checks are hours of desk work, not a GPU day. Run them before
committing, not after.
