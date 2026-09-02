# The current plan — one gate day, then three branches

Written 2026-09-02, runbook added the same day. Supersedes the venue plan in `ideas/24` and the
two-track sketch in `ideas/26`.

This is an **execution** document. The gate thresholds and the branch conditions are fixed **now**,
before any evidence arrives, so that Sep 3's outcome *selects* a path rather than starting an
argument. That is `notes/09`'s discipline, and it is the only part of this repo's method that has
never failed.

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

**Targets (8, do not expand):** `2506.02946` (highest risk) · `2602.08995` MisActBench · Petri ·
SHADE-Arena · ControlArena · AgentHarm · ToolEmu · τ-bench.

**Method per target (~15 min each):** fetch `arxiv.org/html/<id>` or the repo/datasheet, strip tags,
and grep the construction and dataset sections for: *minimal pair · matched · counterfactual · paired ·
contrast · same scenario · multiple rollouts · resample.* Read the hits, not the counts.

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
> **Statistical guard, pre-committed:** N=30 cannot distinguish 2% from 0%. If a scenario returns
> **≤ 1** minority rollout, that scenario is uninformative at this N — it is **not** evidence of FAIL.
> Escalate to **N=150** on the single most promising scenario before declaring FAIL. Never declare
> FAIL from a small-N zero.

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

| Branch | Trigger | Path |
|---|---|---|
| **A — green** | Gates A, B, B2, C all pass | AIWILD Sep 5 (determinism note) → EvoRobust Sep 12 (full benchmark) |
| **B — amber** | A and B pass; C amber, or B2 deferred | Skip AIWILD. EvoRobust Sep 12, reduced scope |
| **C — red** | Any hard fail | Abandon C9. C4 → EvoRobust Sep 12 |

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

**Cut order if the clock slips:** (1) second scenario domain, (2) the G4 arm — named as future work,
never silently dropped, (3) extra probe families beyond the four `2606.30449` name.

**Never cut:** the identity floor · the text-only baseline (`2509.21344` — post-divergence pairs differ
in visible tokens, and this is the same class of control whose absence was fatal to C1) · the public
pre-registration.

**Do not run two branches.** `ideas/24` was right about that even though its venue premise was wrong.
Branch A's two submissions are one project at two maturity levels, not two projects.

## Standing constraints

Budget **$200–300**; C9 ~$120 **with no slack at H100 rates** (`ideas/18` scope correction), C4 ~$25,
C2 ~$15. Public datasets only · no experiments involving real people · nothing person-specific
reported (`notes/08`). Both target venues are **non-archival with dual submission explicitly allowed**,
so nothing here consumes the SaTML 2027 workshop target — re-check **Sep 19**, and run **G2** that day,
when it stops being unrunnable.
