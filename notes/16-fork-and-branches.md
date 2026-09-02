# The current plan — one gate day, then three branches

Written 2026-09-02. This supersedes the venue plan in `ideas/24` and the two-track sketch in
`ideas/26`. It is an **execution** document: the branch conditions are fixed **now**, before any
evidence arrives, so that Sep 3's outcome selects a path rather than starting an argument. That is
`notes/09`'s discipline, and it is the only part of this repo's method that has never failed.

**Step 1 is the fork.** Everything below it is conditional.

---

## Why the fork comes first

Fourteen rounds have produced no code and no loaded dataset, while gate **G3** and rule **R6** have
both said from the beginning that hour one is the load. Every lead so far has been chosen or killed
on a literature inference. The four checks below are the first time this project's decisions turn on
something it ran.

They are also *shared*: every branch needs checks 0 and 1, and no branch is harmed by having run
them. Nothing on Sep 3 is wasted, whichever way it resolves.

---

## Step 1 — Sep 3, the gate day (~1 working day)

Run in order. Stop at the first hard fail and go to Branch C.

### Check 0 — does the harness load? (~30 min)

Clone `maxf-zn/misalignment_monitoring` (HTTP 200, last push 2026-07-02). Install, load a model, run
their existing probe pipeline end-to-end on a released transcript.

- **PASS** — their pipeline runs to completion on at least one released transcript.
- **HARD FAIL** — unresolvable dependency drift or gated weights ⇒ **Branch C**.

### Check 1 — does the identity floor reproduce? (~1 hr)

Run the same transcript twice; compute cosine across their 12 pre-specified layers and 274 sampled
positions. Their reported floor is **0.99999803**.

- **PASS** — floor reproduces to within an order of magnitude of theirs.
- **HARD FAIL** — no stable floor ⇒ the paper's calibration anchor does not exist and every
  downstream number is unanchored ⇒ **Branch C**.

This check is not bookkeeping. **The floor is the anchor the entire benchmark is calibrated against**
(`ideas/25` §2), and it is also the whole of the AIWILD note.

### Check 2 — the R8 sweep on C9's own claim (~2 hrs)

The eight targets in `lit/02`: `2506.02946` (highest risk), `2602.08995` MisActBench, Petri,
SHADE-Arena, ControlArena, AgentHarm, ToolEmu, τ-bench. Open each, grep the construction section and
datasheet for paired / matched / counterfactual / minimal-pair trajectory construction. **Record which
you opened** — that recording is what makes the negative citable under R8.

Three outcomes, and the distinction matters more than the pass/fail:

- **PASS** — nobody publishes a cue-matched, action-divergent construction with post-cue state reads.
- **HARD FAIL — the *claim* is occupied.** Someone already built and analysed this ⇒ **Branch C**.
- **ACCELERANT — the *data* exists but the analysis does not.** τ-bench's multiple rollouts per task
  instance and ControlArena's honest-vs-backdoored solutions to one problem are action-versus-situation
  constructions under other names. If usable rollouts already exist, **that is good news**: pair
  construction gets cheaper, Check 3 may be skippable, and the paper gains a second domain for free.
  Note it and continue on the current branch.

### Check 3 — pair yield (~2–3 hrs)

Not previously in the repo, and it is the quiet budget killer. Take one Petri scenario, sample `N`
rollouts at their temperature, count how many diverge in **eventual action** (one takes the
misaligned action, one does not).

- **PASS** — divergence rate **≥ 10%**. ~200 pairs ≈ ~2,000 rollouts. Tractable.
- **MARGINAL** — **2–10%** ⇒ **Branch B** (reduced scope: fewer pairs, one domain).
- **HARD FAIL** — **< 2%** ⇒ pairs cost an order of magnitude more than budgeted ⇒ **Branch C**.

**Record this as a scope statement, not just a cost.** The construction only yields pairs where the
model is behaviourally uncertain, so the benchmark measures pre-action predictability **conditional on
behavioural uncertainty**. That belongs in the paper as stated scope — a reviewer will find it
otherwise. It is arguably the interesting regime anyway: a model that always defects needs no
pre-action probe.

### End of Sep 3, regardless of branch

**Push the pre-registration public** — the divergence-point rule, the cue-identity criterion, and the
identity control (`ideas/25` §2–3) — to `origin`, with a commit hash, **before any probe is trained.**
The design is both the contribution and the attack surface, and a timestamp is the only defence
against the competitor who holds the harness.

---

## The branches

| Branch | Trigger | Path |
|---|---|---|
| **A — green** | Checks 0–3 all PASS | AIWILD Sep 5 (determinism note) → EvoRobust Sep 12 (full benchmark) |
| **B — amber** | 0 and 1 PASS; Check 3 MARGINAL | Skip AIWILD. EvoRobust Sep 12, reduced scope |
| **C — red** | Any HARD FAIL | Abandon C9. C4 → EvoRobust Sep 12 |

---

## Branch A — green

**Sep 4** — write the determinism note (4pp). Its content is already established: the reproduced
floor, the analytic argument that pre-divergence states are identical and that both rollouts sample
from the *same distribution* at the divergence token (so the pre-cue ceiling is **0.5 by
construction, not by difficulty**), the generalisation that any "situation fixed, action varies"
benchmark is analytically vacuous pre-divergence, and the post-cue construction as the constructive
half. Start pair construction in parallel.

**Sep 5** — submit to AIWILD, 4pp short track, non-archival, WIP welcome.

**Sep 6–10** — the build: pair construction at scale, the AUC-versus-`j` sweep, the text-only
baseline, the identity control, the G4 arm.

**Sep 11** — second scenario domain and/or confidence intervals, budget permitting.

**Sep 12** — write and submit to EvoRobust.

**The honest cost, stated so it is a decision and not a drift:** Branch A spends **two days** of a
ten-day window on the AIWILD note, leaving seven days for a build estimated at nine. It buys a
public priority claim on the key insight, at the one venue whose audience would actually adopt the
artifact, for ~35–40% unconditional odds on a second acceptance.

**Bail-out, fixed now:** if the note is not essentially finished by **end of Sep 4**, drop it and fall
to Branch B. Do not carry a half-written paper into Sep 5.

**Why this reopens a decision `ideas/24` closed.** That document's case against AIWILD was about
*C1*'s false novelty claim, and separately about tipping off `2606.30449`'s authors with a
results-free design at their own venue. The determinism note **inverts the second argument**:
publishing the insight establishes priority, whereas staying silent while the competitor holds the
harness does not. And it is now conditional on four checks rather than a bet.

## Branch B — amber

**Sep 4–10** — the build, reduced: one scenario domain, fewer pairs, all controls intact.
**Sep 11** — write. **Sep 12** — submit to EvoRobust. One day of slack, deliberately.

No AIWILD submission. Same reasoning as `ideas/24`: a thin paper at the venue whose standing we most
need is worse than none.

## Branch C — red

**Sep 3 (same day)** — run the **G2 check on Maksym Andriushchenko** before committing. He is an
EvoRobust invited speaker and works directly on adaptive attacks against safety-aligned LLMs, which
is close to C4's line. Publication list, not vibes. Collision ⇒ fall to **C2** (~$15,
`cais/Zephyr_RMU` verified to load).

**Sep 4–9** — build C4: ensembles versus an adaptive prompt-injection adversary on trusted monitors.
The motivation is already quotable — `2510.09462` proposes ensembling as the mitigation; `2605.15377`
states *"We did not red-team our ensembles against an adaptive adversary with knowledge of the
monitoring system."* ~$25.

**Sep 10–11** — write. **Sep 12** — submit to EvoRobust.

**This is the highest-probability path on the board** (~55–60% unconditional), because it is the one
that reliably finishes. Reaching Branch C is not a failure; it is the fork doing its job.

---

## Cut lines, fixed in advance

**Cut order if the clock slips:** (1) second scenario domain, (2) the G4 arm — named as future work,
not silently dropped, (3) extra probe families beyond the four `2606.30449` name.

**Never cut:** the identity floor, the text-only baseline (`2509.21344` — post-divergence pairs differ
in visible tokens, and this is the same class of control whose absence was fatal to C1), and the
public pre-registration.

**Do not run two branches.** `ideas/24` was right about that even though its venue premise was wrong.
Branch A's two submissions are one project at two maturity levels, not two projects.

## Standing constraints

Budget **$200–300**, not binding; C9 ~$120, C4 ~$25, C2 ~$15. Public datasets only · no experiments
involving real people · nothing person-specific reported (`notes/08`). Both target venues are
**non-archival with dual submission explicitly allowed**, so nothing here consumes the SaTML 2027
workshop target — re-check Sep 19, and run **G2** that day, when it stops being unrunnable.
