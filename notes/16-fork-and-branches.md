# The current plan — one gate day, then three branches

Written 2026-09-02, runbook added the same day. Supersedes the venue plan in `ideas/24` and the
two-track sketch in `ideas/26`.

This is an **execution** document. The gate thresholds and the branch conditions are fixed **now**,
before any evidence arrives, so that Sep 3's outcome *selects* a path rather than starting an
argument. That is `notes/09`'s discipline, and it is the only part of this repo's method that has
never failed.

> # ⛔ SUPERSEDED IN PART — round 15, 2026-09-02 (`ideas/27`)
>
> This runbook was written before the sweep it schedules was run. Round 15 ran the *out-of-field* half
> of that sweep from the desk, and it changes the routing before Sep 3 starts:
>
> | Branch | Status now | Why |
> |---|---|---|
> | **A — AIWILD determinism note** | **DEAD** | Its content is `2606.30449`'s own published floor plus a tautology, submitted to the venue where they published it. **Stage D already buys the priority claim** in 30 minutes, on every branch. Branch A paid two of ten days for it. |
> | **C — C4** | **DEAD** | `2510.09462` is *Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols*, and **Andriushchenko — an EvoRobust invited speaker — is a co-author.** The G2 check this document schedules for Sep 3 is already answerable, and it fails. The paper *is* C4's attack. |
> | **B** | **the only branch** | And it needs the reframe in `ideas/27` §8 before a line is written. |
>
> **Stage A's target list is wrong** (`ideas/27` §2, new rule **R14**). All eight targets are inside AI
> safety; C9's three real pre-emptions — `2606.09890` PreAct-Bench, `2507.12428`, and `2606.30449`'s
> own bridge probe — are not among them and would not be found by grepping them. **As written, Gate A
> returns CLEAR and routes to green on an occupied claim.**
>
> **Gate C cannot resolve its own bands.** At the PASS boundary, 3/30, the Wilson 95% CI is
> **[0.035, 0.256]** — spanning FAIL, AMBER and PASS. Its statistical guard is one-sided: it protects
> against a false FAIL and ignores a false PASS, which is the error that routes into the dead branch.
>
> **Read `ideas/27` before running any of what follows.** Stages 0, B and B2 stand unchanged — loading
> the harness and reproducing the floor is still the right first day's work, and is now the *only*
> unrun question on the board.

**Step 1 is the fork. Everything below it is conditional.**

---

# STEP 1 — Sep 3 runbook

## Why this day exists

Fourteen rounds have produced no code and no loaded dataset, while gate **G3** and rule **R6** have
said from the beginning that hour one is the load. Every lead so far was chosen or killed on a
literature inference. This is the first decision this project makes on something it ran.

## Two ordering rules, and the reasons

**1. The free check goes first.** Stage A needs no GPU and has the highest kill probability on the
board — it is the check that killed C6 and gutted C1 when it was finally run. If it comes back
OCCUPIED you have spent two hours and **zero dollars**, and you never rent a box.

**2. Downloads run underneath everything.** Weights are 16–54GB. Start them at T+0:00 and do Stage A
while they land. Never sit watching a progress bar.

## The whole day at a glance

| Stage | Clock | GPU | Purpose | Gate |
|---|---|---|---|---|
| **0** | T+0:00 → 0:15 | none | start clone, env, weight downloads | none |
| **A** | T+0:15 → 2:15 | **none** | R8 sweep — is the claim occupied? | **A** |
| **B** | T+2:15 → 3:45 | 8B (24GB ok) | harness loads, floor exists | **B** |
| **B2** | T+3:45 → 4:45 | 27B (H100) | reproduce *their* number | gates Branch A only |
| **C** | T+4:45 → 7:15 | 8B | pair yield | **C** |
| **D** | +0:30 | none | push pre-registration **public** | none |

---

## Stage 0 — start the long pole (15 min, no gate)

1. `git clone https://github.com/maxf-zn/misalignment_monitoring` — **record the HEAD SHA.**
2. Create the env, install dependencies.
3. Start weight downloads **in this order**: `Llama-3.1-8B-Instruct` (~16GB, needed by Stage B),
   then the minimal-pair model (~54GB, needed by Stage B2) in the background.
4. Read `configs/`, specifically `divergence_minimal_pair.yaml`, and **record which model the released
   `seed-115` transcripts came from.** The repo's record says the shared-prefix pair is the Gemma
   blackmail case, so expect `Gemma-3-27B-IT` — confirm it rather than assuming.

**Recorded output:** repo SHA · minimal-pair model id · download start time.

---

## Stage A — the R8 sweep (2h hard box, no GPU) → **GATE A**

**Question:** has anyone already built *and analysed* a cue-matched, action-divergent construction
with post-cue state reads?

**Targets — RE-AIMED round 15 (`ideas/27` §2, R14).** The original eight (`2506.02946` · `2602.08995`
MisActBench · Petri · SHADE-Arena · ControlArena · AgentHarm · ToolEmu · τ-bench) are all *inside* AI
safety and all *benchmark* papers. They cannot discharge G1/R2, which asks for neighbours **outside**
the home subfield, and they missed all three real pre-emptions.

**Already found from the desk, no sweep needed — record these and do not re-derive them:**
`2606.09890` **PreAct-Bench** (the benchmark, the metric, the probe arm) · `2507.12428` (the x-axis,
swept, plus the text-only baseline) · `2606.30449` (bridge probe at two prefill fractions = the first
two points of the curve). See `lit/02` round-15 rows.

**What remains to sweep, and it is out-of-field:** early classification of time series (the
earliness/accuracy tradeoff, ~25 years old, the closest thing to a canonical prior); prediction-horizon
and lookahead/future-token work in transformers; and *monitoring* papers rather than *benchmark*
papers inside safety. Keep the original eight as a DATA-FOUND scan only — they may still make pairs
cheaper, which is an accelerant, not a gate.

**Method per target (~15 min each):** fetch `arxiv.org/html/<id>` or the repo/datasheet, strip tags,
and grep the construction and dataset sections for: *minimal pair · matched · counterfactual · paired ·
contrast · same scenario · multiple rollouts · resample · trials · divergent · same prefix.* Read the
hits, not the counts.

> ### ⚠️ Positive control, mandatory per target — this is R3 in a new costume
> **`arxiv.org/html/<id>` does not exist for every paper** (the HTML rollout began ~Dec 2023, and even
> after it some papers have none). A 404 or an error page yields an **empty body, and an empty body
> greps as zero for every term — which reads exactly like CLEAR.** That is the same failure that made
> `http://export.arxiv.org`'s 301 parse as `totalResults=0` in round 12.
>
> **Before grepping any target, grep it for a term you know is present** — a distinctive word from its
> own title, or "agent" — and record the hit count next to the negatives. **A zero-result on a target
> with no positive control is not evidence and does not tick its box.** Target 7 (ToolEmu, Sep 2023) is
> the one most likely to trip this.

**Classification rule — both conditions, not either:**

| What the target has | Verdict | Action |
|---|---|---|
| (i) construction holding scenario fixed while the action varies **AND** (ii) analysis reading internal state after the cue, before the action commits | **OCCUPIED** | → **Branch C**. Stop. Do not rent a GPU. |
| (i) only — action-divergent rollouts exist, nobody analysed pre-action state | **DATA-FOUND** | **Accelerant, not a kill.** Pairs get cheaper, Stage C may shrink, and you may get a second domain free. Note it and continue. |
| (ii) only, on a different construction | **NEIGHBOUR** | Cite in related work. Continue. |
| Still ambiguous after **10 minutes** on one target | **NEIGHBOUR** | Record the verbatim sentence and move on. Ambiguity makes related work harder; it does not make the project dead. |

τ-bench (multiple rollouts per task instance) and ControlArena (honest and backdoored solutions to the
*same* problem) are the two most likely DATA-FOUND hits. Finding them is **good news.**

**Recorded output:** tick each box in `lit/02`'s round-14 table with the date, the verdict, and the
verbatim sentence for any non-CLEAR verdict. That recording is what makes the negative citable under
R8 — an unrecorded sweep is not evidence.

> ### GATE A
> **OCCUPIED → Branch C, immediately.** Anything else → Stage B.

---

## Stage B — harness and floor, on Llama-3.1-8B (90-min hard debug box) → **GATE B**

**Question:** does their pipeline run, and does a determinism floor exist at all?

1. Run their existing probe pipeline end-to-end on one released transcript.
2. Run the same transcript through the model **twice**. Capture residual streams at their 12
   pre-specified layers × 274 sampled positions. Compute per-position cosine; report **min and mean**.

**Why the 8B here:** the floor is a property of a deterministic forward pass, not of scale. It
reproduces on any model, and this stage is asking *does anything work*, not *does their number
replicate*. That question is Stage B2's.

**Recorded output:** pipeline completes y/n · min and mean identity cosine · model id · their repo SHA.

> ### GATE B
> **PASS** — pipeline completes **AND** min identity cosine **≥ 0.9999** (an order of magnitude looser
> than their 0.99999803).
> **FAIL → Branch C** — more than **90 minutes** of debugging without a completed run, **or** no stable
> floor (min cosine swinging across reruns).
>
> The 90-minute box **is** the definition of "the harness fights back." Past it you are in a rabbit
> hole, and the branch exists precisely so you do not have to decide that while tired.

---

## Stage B2 — reproduce *their* number (1h, conditional) → gates **Branch A only**

Run only if the minimal-pair model's weights have landed. On the released `seed-115` pair, reproduce:

| Quantity | Their value |
|---|---|
| Identity check — same transcript twice | **0.99999803** |
| Minimum cosine over the shared prefix | **0.99999893** |

**This stage is the entire content of the AIWILD determinism note**, which is why it gates Branch A
and not the day. **If the weights are not down, do not wait** — defer to Sep 4 AM and proceed to
Stage C. Branch A survives; it just gets tighter.

**Recorded output:** their two numbers next to yours, and the model + SHA that produced them.

---

## Stage C — pair yield, on Llama-3.1-8B (2.5h) → **GATE C**

**Question:** how many rollouts buy one usable pair?

**Design: 3 scenarios × 30 rollouts = 90 rollouts**, at their temperature. Three scenarios rather than
one, because yield is scenario-dependent and a single scenario can be degenerate — same cost, strictly
more information, and you learn the variance as well as the rate.

**Metric per scenario:** `minority-action rate = (rollouts taking the minority action) / 30`. Usable
pairs per scenario ≈ the minority count.

**Measure it on the 8B** because the 8B is the primary build model (see scoping below). Yield is
model-specific, so measuring it on the model you will actually use is the correct choice, not a
shortcut.

> ### GATE C — on the **median** rate across the three scenarios
> **PASS ≥ 10%** → Branch A (if B2 passed) or Branch B.
> **AMBER 2–10%** → **Branch B**, reduced scope.
> **FAIL < 2%** → **Branch C**.
>
> **Statistical guard — MADE TWO-SIDED, round 15.** N=30 cannot distinguish 2% from 0%, and it also
> cannot distinguish 10% from 3.5% or from 25%: at 3/30 the Wilson 95% CI is **[0.035, 0.256]**, which
> spans all three bands. So:
> - **≤ 1 minority rollout** → uninformative, **not** evidence of FAIL. Escalate to N=150 on the most
>   promising scenario. Never declare FAIL from a small-N zero.
> - **A median rate in 5–20%** → equally uninformative for **PASS**. Escalate to N=150 before routing.
>   A false PASS is the expensive error and the guard previously ignored it entirely.
>
> **State the pair target before measuring the rate** (`ideas/27` §4). Hanley–McNeil, per class, with
> Bonferroni over an 8-point sweep: AUC 0.60 → **210 pairs**; 0.65 → 90; 0.55 → ~520 single-test.
> `2606.30449`'s bridge probe reached **≤ 0.632**, so plan for **210–520 pairs** = 2,100–5,200 rollouts
> per scenario at a 10% rate. Yield is not the decision; **yield against the pair target** is.

**Recorded output:** per-scenario minority rate · N · model · temperature · the exact rule used to
decide "the action diverged."

**Record it as scope, not only cost.** The construction only yields pairs where the model is
behaviourally uncertain, so the benchmark measures pre-action predictability **conditional on
behavioural uncertainty**. That belongs in the paper as stated scope — a reviewer finds it otherwise.
It is arguably the interesting regime anyway: a model that always defects needs no pre-action probe.

---

## Stage D — push the pre-registration, public (30 min, every branch)

To `origin`, with a commit hash, **before any probe is trained.** Six items:

1. **The divergence-point rule** — how token index `t` is located, as a rule, not per-pair.
2. **The read-offset schedule** — the exact `j` values in the AUC-versus-`j` sweep.
3. **The cue-identity criterion** — what makes two rollouts count as having received the same
   situation. *This is the one criterion that cannot be fixed after seeing results, and it is where a
   hostile reviewer will push.*
4. **The identity-control protocol.**
5. **The text-only baseline protocol** (`2509.21344`).
6. **Scenario inclusion criteria, including the yield threshold.** Selecting scenarios by yield *after*
   seeing results is a forking-paths problem: yield tracks behavioural uncertainty, which plausibly
   tracks predictability. Fixing the rule in advance is what makes the benchmark a test rather than a
   demonstration.

---

## Scope traps — explicitly not on Sep 3

- **No probe training of any kind** until Stage D is pushed.
- **No improving their code** beyond what is needed to make it run.
- **No expanding the sweep** past the eight targets.
- **No writing.**
- **No 27B/32B generation** — 8B only, Stage B2 excepted.

## If you are behind

| Situation | Do this |
|---|---|
| Stage A overruns | Let it run. It is the gate that saves the most money; push the rest of the day back. |
| Stage B overruns its 90-min box | That **is** the fail condition. Go to Branch C. |
| B2 blocked on downloads | Defer to Sep 4 AM. Branch A survives. |
| Stage C unfinished at end of day | Finish Sep 4 AM. **Branch A is dead** (its bail-out stands) — go Branch B. |

---

# STEP 2 — the branches

| Branch | Trigger | Path | Round-15 status |
|---|---|---|---|
| **A — green** | Gates A, B, B2, C all pass | AIWILD Sep 5 (determinism note) → EvoRobust Sep 12 | ⛔ **DEAD** — `ideas/27` §6 |
| **B — amber** | A and B pass; C amber, or B2 deferred | Skip AIWILD. EvoRobust Sep 12, reduced scope | ✅ **The only branch.** Reframe per `ideas/27` §8 first |
| **C — red** | Any hard fail | Abandon C9. C4 → EvoRobust Sep 12 | ⛔ **DEAD** — G2 fail, `ideas/27` §3 |

> **There is no longer a red branch, and that is the uncomfortable part.** The fork's whole value was
> that a hard fail had somewhere to go. If Gate B or Gate C fails now, the honest options are: fall to
> **C2** (~$15, `cais/Zephyr_RMU` verified to load) at a venue that fits it, or **submit nothing on
> Sep 12** and take the SaTML window with a properly built artifact. Round 15 did not manufacture a
> replacement fallback, because inventing one under deadline pressure is how this board acquired four
> consecutive leads that died (R11). **Consider IAB (Sep 6, `notes/13`) — wrongly filed as closed —
> before assuming EvoRobust is the only door.**

## Model scoping, all C9 branches

**Llama-3.1-8B-Instruct is the primary build model.** Qwen2.5-Coder-32B and Gemma-3-27B are a
**transfer arm**, not the main run. The 8B fits a 24GB card, generates several times faster, and
`notes/11` asks for *at least one* transfer check while stating explicitly that breadth is padding.
The larger models are reserved for Stage B2 and the transfer arm, which is where they are actually
load-bearing. See the scope correction at the top of `ideas/18`: an **H100 80GB is the minimum** for
the 27B/32B, and batched generation there is KV-limited at ~13k context.

## Branch A — green

**Sep 4** — write the determinism note (4pp); start pair construction in parallel. Content is already
settled: the reproduced floor, the analytic argument that pre-divergence states are identical and that
both rollouts sample from the *same distribution* at the divergence token (so the pre-cue ceiling is
**0.5 by construction, not by difficulty**), the generalisation that any "situation fixed, action
varies" benchmark is analytically vacuous pre-divergence, and the post-cue construction as the
constructive half.

**Sep 5** — submit to AIWILD, 4pp short track, non-archival, WIP welcome.
**Sep 6–10** — the build: pair construction at scale, the AUC-versus-`j` sweep, text-only baseline,
identity control, G4 arm.
**Sep 11** — second scenario domain and/or confidence intervals, budget permitting.
**Sep 12** — write and submit to EvoRobust.

**The honest cost, stated so it stays a decision and not a drift:** Branch A spends **two days** of a
ten-day window on the note, leaving seven for a build estimated at nine. It buys a public priority
claim on the key insight, at the one venue whose audience would actually adopt the artifact, for
~35–40% unconditional odds on a second acceptance.

**Bail-out, fixed now:** if the note is not essentially finished by **end of Sep 4**, drop it and fall
to Branch B. Do not carry a half-written paper into Sep 5.

**Why this reopens a decision `ideas/24` closed.** That document's case against AIWILD was about *C1*'s
false novelty claim, and separately about tipping off `2606.30449`'s authors with a results-free design
at their own venue. The determinism note **inverts the second argument**: publishing the insight
establishes priority, whereas silence while the competitor holds the harness does not. And it is now
conditional on four gates rather than a bet.

## Branch B — amber

**Sep 4–10** build, reduced: one scenario domain, fewer pairs, **all controls intact**.
**Sep 11** write. **Sep 12** submit to EvoRobust. One day of slack, deliberately.

No AIWILD submission — same reasoning as `ideas/24`: a thin paper at the venue whose standing we most
need is worse than none.

## Branch C — red

**Sep 3, same day** — run the **G2 check on Maksym Andriushchenko** before committing. He is an
EvoRobust invited speaker and works directly on adaptive attacks against safety-aligned LLMs, close
enough to C4's line to need R7/G2. Publication list, not vibes. Collision ⇒ fall to **C2** (~$15,
`cais/Zephyr_RMU` verified to load).

**Sep 4–9** — build C4: ensembles versus an adaptive prompt-injection adversary on trusted monitors.
Motivation already quotable — `2510.09462` proposes ensembling as the mitigation; `2605.15377` states
*"We did not red-team our ensembles against an adaptive adversary with knowledge of the monitoring
system."* ~$25.
**Sep 10–11** write. **Sep 12** submit to EvoRobust.

**This is the highest-probability path on the board** (~55–60% unconditional) because it is the one
that reliably finishes. **Reaching Branch C is the fork doing its job, not failing.**

---

# Fixed in advance

**Cut order if the clock slips — REVISED round 15:** (1) the G4 arm — named as future work, never
silently dropped, (2) extra probe families beyond the four `2606.30449` name, (3) additional read
offsets *within* the sweep.

**Never cut:** the identity floor (now **one line, a sanity check** — not a headline, `ideas/27` §1d) ·
the text-only baseline (`2509.21344`) · the public pre-registration · **the second scenario domain** ·
**confidence intervals on the curve**.

The last two were promoted out of the surplus list. The second domain is what an evolutionary-
computation PC rejects on — one model × one domain reads to that pool as **n=1 problem instances**
(`ideas/27` §5). The intervals are the curve; without them there are only eight noisy points.

**Do not run two branches.** `ideas/24` was right about that even though its venue premise was wrong.
Branch A's two submissions are one project at two maturity levels, not two projects.

## Standing constraints

Budget **$200–300**; C9 ~$120 **with no slack at H100 rates** (`ideas/18` scope correction), C4 ~$25,
C2 ~$15. Public datasets only · no experiments involving real people · nothing person-specific
reported (`notes/08`). Both target venues are **non-archival with dual submission explicitly allowed**,
so nothing here consumes the SaTML 2027 workshop target — re-check **Sep 19**, and run **G2** that day,
when it stops being unrunnable.
