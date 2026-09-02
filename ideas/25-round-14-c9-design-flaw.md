# Round 14 — the reframed C9 is still unfalsifiable, and the fix is a better paper

Written 2026-09-02, after `ideas/24`. This round attacks the **surviving lead** rather than the
board, per the new rule `notes/12` R11. It finds one load-bearing design flaw, two unrun gates, one
unrun rule, and one missing control. **C9 is not dead.** The version that survives is a different
paper from the one in `ideas/24`, and it is stronger.

---

## 1. The flaw — a negative read offset is chance by construction

`ideas/24` correctly kills the input-matched design: a byte-identical prefix gives a byte-identical
forward pass, so no probe can beat chance. It then writes pre-registration item #1 as:

> **The divergence point** — the token index at which the two rollouts first differ, and **the offset
> before it** at which states are read.

**Any strictly-negative offset is provably chance, by the same argument.** Let two rollouts share a
prompt and first differ at token index `t`.

1. For every position `< t` the token sequences are identical, so the residual streams are identical
   up to the nondeterminism floor already measured in `ideas/24` — **0.99999803** cosine for the same
   transcript run twice.
2. At position `t` both rollouts sample from the **same distribution**. Which branch occurs is
   determined by the RNG, not by any hidden state.
3. Therefore the eventual action is **not a function of any state at or before `t`**. The ceiling on
   pre-action AUC is exactly **0.5**, in expectation, for every pair, forever.

This is stronger than "empirically hard." It is an information-theoretic zero: at the read position
the outcome is not yet a function of the thing being read. The design `ideas/24` diagnosed one
paragraph earlier is reintroduced in the item that would be pre-registered with a commit hash.

`ideas/24` also contains the viable version — "the probe reads a token position **after** the cue has
been received and before the action commits" — so the document contradicts itself. The broken form is
the one written into the protocol.

### The tension underneath, which no document in this repo has stated

**"Situation held fixed" and "action predictable from the pre-action state" cannot both hold.**

- If the state is identical, the action is unpredictable **by construction**.
- If the action is predictable from the state, the state differs — and then something in the
  situation or the history differed, which is the confound C9 exists to remove.

A consequence for the headline: C9's claim that *"existing data cannot test pre-action monitoring at
all"* is, in the strong form, **trivially true because the strong form is impossible**. Nobody built
the dataset because the dataset cannot exist. A reviewer who follows the determinism argument reaches
that in one paragraph, and the paper's central claim evaporates into a tautology. Do not ship the
strong form.

---

## 2. The fix — make distance-from-divergence the independent variable

Read state **strictly after first divergence and strictly before the action commits**, and stop
treating the read position as a nuisance parameter to be fixed. Make it the x-axis.

**The construction.** Pairs share the scenario and the triggering cue. Divergence arises from the
model's own sampling. The rollouts diverge at `t`; the action commits at `t + L`. Probe the residual
stream at `t + j` for `j ∈ {0, 1, 2, 4, 8, …, L}` and plot AUC against `j`.

**What this buys, in order of value to a reviewer:**

1. **A benchmark with an analytically-known floor.** `j ≤ 0` is provably 0.5. The determinism result
   stops being a threat to the design and becomes a **calibration anchor at one end of your own
   curve** — a property no other agentic-monitoring benchmark has, and the single most defensible
   thing on the board. It also converts the "you built the confound you are measuring" objection into
   a figure: the confound is the leftmost point, labelled, at chance, as predicted.
2. **It instruments the exact regime `2606.30449` left open.** Their scoping, twice: the shared-prefix
   pair "rules out only pre-difference prediction rather than **post-cue pre-action prediction**,"
   which their bridge probe tests once, weakly (AUC ≤ 0.632, negative leave-one-condition-out lift,
   one within-condition AUC of 0.640 flagged near-threshold). A curve over `j` is the general form of
   their single point.
3. **It is a quantity, not a verdict.** "How many tokens before the action does intent become
   linearly readable" is a number a safety case can be written against. "Do probes work" is not.

**Restate the contribution accordingly.** Not *matched pairs* (canonical — contrast sets, `2004.02709`).
Not *"existing data cannot test this"* (tautological in the strong form). The contribution is:
**pre-action predictability as a function of tokens elapsed since divergence, on an
action-versus-situation construction, anchored at a proven floor.**

---

## 3. The missing control — a text-only baseline, and the repo already owns the citation

Once the read position is post-divergence, the two members of a pair differ in **visible tokens**. A
probe may be reading those tokens rather than any latent intention. That is exactly `2509.21344`
(*Linear probes rely on textual evidence*), which this repo has verified and cited only against C1
and C3. It is a **mandatory arm for C9** and is currently unbudgeted:

> For every read position `j`, report the AUC of a text-only classifier over the same visible tokens
> alongside the activation probe. Any claimed pre-action signal must exceed **both** the identity
> nondeterminism floor and the text-only baseline.

Structurally this is the same class of objection as the matched-norm random-direction placebo whose
absence was fatal to C1 — the control that decides whether the headline is a finding or an artifact.
`ideas/24` lists neither this arm nor its cost.

---

## 4. Gates and rules never run against C9

| Check | Status in `ideas/24` | Actual |
|---|---|---|
| **R8** (open the top ~10 papers, grep construction sections) | not run | **Owed.** C9's claim is a negative about construction practice — the class R8 governs — and dataset construction hides in appendices and datasheets, further from the abstract than the metric vocabulary that killed C6. |
| **G2** (organizer collision) | silent | **Unrunnable.** SaTML 2027 workshop organizers are notified Sep 18. Recorded as unrunnable, not as a pass (`notes/12` R11). `2606.30449`'s group is the plausible occupant of any agent-monitoring workshop. |
| **G4** (the obvious competing axis) | not run | **Owed.** The competing explanation is *probe family and training scale* — `2606.30449` name four untested families. If a sequence-level probe trained across more scenarios moves the metric more than the construction does, the framing is undercut. Run it as a competing arm, not as part of the experiment. |
| **A3 / R5** (re-check outcome robustness) | inherited from `ideas/22` | **Weaker than recorded.** Under the methodology reframe, "signal vanishes" is the *expected* outcome and "signal survives" contradicts the group that owns the venue. The artifact framing is itself the hedge — legitimate, but it puts all the weight on B5, and a one-domain one-model benchmark is a weak adoption bid. |

### The R8 sweep that is owed, concretely

Open and grep the construction sections and datasheets of: **MisActBench** (`2602.08995`),
**Abstract Counterfactuals** (`2506.02946` — already does counterfactual construction over agent
actions *with latent-space interventions*; "machinery not claim" is asserted, never verified against
their actual constructions), **Petri**, **SHADE-Arena**, **ControlArena**, **AgentHarm**,
**ToolEmu**, **τ-bench**. Record which were opened. Two hours, and it runs before anything is built.

---

## 5. Consequences for the plan

**The timeline is not what `ideas/24` assumes.** SaTML 2027 notifies workshop *organizers* on Sep 18;
paper CFPs follow, and for a conference running in early 2027 those deadlines are realistically
**6–10 weeks out**, not Sep 19. ⚠️ Inference from the conference timeline, not verified — confirm on
Sep 19. Sep 19 is the date the target becomes *legible*, not a deadline.

Three things follow:

1. **The "~9 days" figure binds nothing.** The only real pressure is scoop pressure, from a group
   with the harness, the head start, and a public statement that this is their open problem.
2. **Push the pre-registration public on day 0**, not merely "before any probe runs." `origin` is
   `nahatav/beyond-private-training`; a timestamped public design costs nothing and converts scoop
   risk into priority evidence. `ideas/24` says "in the repo, with a commit hash" and does not say
   *public* or *when*.
3. **Reorder the surplus budget.** `ideas/24` spends it on a second probe family, then CIs, then a
   second scenario domain. Under the artifact framing, adoption **is** the contribution, so:
   **second scenario domain → text-only baseline (§3) → confidence intervals.** Drop "a second probe
   family beyond the four" — that is breadth, which `notes/11` explicitly deprioritises.

**AIWILD Sep 5 still passes, and §1 settles it independently of C1.** The design is not ready, and
the reason `ideas/24` gives is an argument about C1's false novelty claim rather than about C9. The
real reason to stay quiet: describing to `2606.30449`'s authors, at their own venue, which of their
named open problems you are building, while holding no results, is the worst available move against
the one competitor who matters.

---

## 6. What changes in `ideas/24`

- Pre-registration item #1 is **rewritten**: read position strictly after first divergence and before
  action commit; `j` is swept, not fixed; `j ≤ 0` is reported as the proven 0.5 anchor.
- The headline drops *"existing data cannot test pre-action monitoring at all"* and becomes the
  distance-from-divergence curve.
- The text-only baseline (§3) joins the identity control as a **mandatory** arm.
- G2 is marked unrunnable; G4 and R8 are marked owed, with the sweep list in §4.
- Budget order becomes second domain → text-only baseline → CIs.

Everything else in `ideas/24` stands: the artifact framing, the related-work rewrite onto
`2004.02709` / `2506.02946` / `2602.08995`, the friendly posture toward `2606.30449`, and the
identity-cosine floor as a reported control.
