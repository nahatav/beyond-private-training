# The plan — one track, EvoRobust Sep 12

Written 2026-09-02 (round 15), after `ideas/27`. **Supersedes `notes/16`**, which was written before
its own sweep was run and which routes to two branches that no longer exist. `notes/16` is kept for
Stages 0/B and for the pre-registration checklist; everything about branching in it is void.

This is an **execution** document, in `notes/09`'s discipline: thresholds and stopping rules fixed
**now**, before evidence arrives, so an outcome selects a path instead of starting an argument.

---

## The one track

**C9, reframed → EvoRobust, Sep 12 AoE.** Ten days. There is no second branch and no fallback paper
in flight. That is a deliberate consequence of round 15, not an oversight — see §7.

**The 3-day venues are not reachable.** AIWILD (Sep 5 AoE) and IAB (Sep 6 11:59 UTC) both close before
any result can exist, and there is zero experiment code. `notes/13`'s calendar correction matters for
the record and for the next cycle; it does not hand us a venue in this one. **Branch A died on
content** (`ideas/27` §6), not on timing — do not revive it if the schedule looks generous.

## 1. What the paper is, in one sentence

> **How much of pre-action predictability is the situation, and how much is the particular sampled
> continuation** — measured on pairs whose divergence is caused only by the sampler, with the cue held
> fixed, indexed by tokens since the divergence token.

**What it is not**, and both must stay out of the abstract:

- *A benchmark for pre-action monitoring.* `2606.09890` PreAct-Bench published that in June, over
  1,000 paired trajectories in five domains, with the metric and the residual-stream probe arm.
- *Probes fail at pre-action monitoring.* `2606.30449` published that, and the field has stopped
  finding it surprising.

The sampling-divergence anchor is the one formulation the three incumbents do not contain, and
`2606.30449` names it as its own gap in its own words: the prefill states *"include rollout-specific
truncated assistant prefixes, so the per-row hidden state is **not byte-identical across rollouts
within a condition**."*

**⚠️ Standing risk, stated once so it is not forgotten.** That novelty rests on a *negative* search
result. Two independent sweeps found nothing on point and the three incumbents were checked directly,
but "nobody has done this" is exactly the class of claim **R8** exists to distrust, and OpenReview is
behind a CAPTCHA so in-flight submissions are invisible. Treat the reframe as **probably** unoccupied,
not verified unoccupied. The out-of-field sweep in §3 is what closes it.

## 2. Two structural cuts that buy the speed

**Drop Stage B2 entirely.** Reproducing `2606.30449`'s 27B numbers gated Branch A only, and Branch A
is dead. This removes a **54GB download and an H100 hour** from the critical path. Download the 8B and
nothing else.

**Merge Gate C into the build.** `notes/16`'s N=30 pilot cannot distinguish 3.5% from 25%
(`ideas/27` §4), so it buys almost nothing — and the rollouts it burns are the rollouts the corpus
needs anyway. Start production generation immediately after Gate B and read yield off the first ~300
rollouts as a **checkpoint on a running job**, not a separate stage.

This is the largest schedule win available: generation is unattended and embarrassingly parallel, so
it must be running while analysis code is written. **Never let the GPU idle while a human types.**

## 3. Schedule

| Day | Work | Gate |
|---|---|---|
| **Sep 2, tonight** | Fetch the **IAB** CFP and close that owed item (`notes/13`). Settle on paper: the divergence-point rule, the cue-identity criterion, the *j* schedule, the "action commits" rule that defines `L`. | — |
| **Sep 3 AM** | Clone `maxf-zn/misalignment_monitoring` (record HEAD SHA), env, **`Llama-3.1-8B-Instruct` only**. Run their pipeline on one released transcript; run the same transcript twice; report min and mean identity cosine. | **GATE B** |
| **Sep 3 PM** | Push the pre-registration **public** (§5) — before any probe trains. Then start generation on **two** scenario domains, unattended, overnight. | — |
| **Sep 4–6** | Generation runs unattended. In parallel, against released transcripts so nothing waits: pair-extraction rule, probe sweep code, **text-only baseline**, random-direction control, bootstrap harness. | — |
| **Sep 7** | Yield checkpoint on ~300 rollouts/scenario. Fix N against the pair target. Decide whether the corpus needs more generation or a third domain. | **GATE C** |
| **Sep 8–9** | The AUC-versus-*j* sweep. All controls. Confidence intervals. | — |
| **Sep 10** | Held-out-scenario transfer number — **reported even if negative**. | — |
| **Sep 11** | Write. Submit if ready. | — |
| **Sep 12** | Buffer. Submit. | — |

**The out-of-field sweep (`ideas/27` §2, R14)** is not a day of its own. Fold it into Sep 4–6 dead
time: early classification of time series (the earliness/accuracy tradeoff), prediction-horizon and
lookahead work in transformers, and *monitoring* rather than *benchmark* papers inside safety. Record
verdicts in `lit/02` with positive controls. It cannot stop the build; it can change the related-work
framing, and it is what discharges §1's standing risk.

## 4. Gates

> ### GATE B — Sep 3 AM, 90-minute hard box
> **PASS** — their pipeline completes end-to-end on one released transcript **AND** min identity
> cosine **≥ 0.9999** (an order of magnitude looser than their 0.99999803).
> **FAIL** — 90 minutes of debugging without a completed run, **or** no stable floor across reruns.
>
> The box **is** the definition of "the harness fights back." A fail here means you are not shipping
> Sep 12; go to §7. Do not decide that while tired at 11pm — decide it at the 90-minute mark.

> ### GATE C — Sep 7, on the running corpus
> Judge **yield against the pair target**, not yield alone.
>
> **Pair target: 210–520 pairs per class.** Hanley–McNeil, per class, Bonferroni over an 8-point
> sweep: AUC 0.60 → **210**; 0.65 → 90; 0.55 → ~520 single-test. `2606.30449`'s bridge probe reached
> **≤ 0.632**, so 0.55–0.65 is the honest planning range.
>
> **PASS** — projected pairs ≥ 210 across two domains by Sep 9 at the observed rate. Continue.
> **AMBER** — 210 reachable on one domain only. Continue on one domain, **keep every control**, and
> state the single-domain scope in the abstract rather than hiding it in limitations.
> **FAIL** — 210 unreachable on either domain by Sep 9. Go to §7.
>
> **Two-sided guard.** N=30 could distinguish nothing; even at the checkpoint, a median rate in
> **5–20%** is uninformative for PASS as well as for FAIL — at 3/30 the Wilson 95% CI is
> **[0.035, 0.256]**. Escalate the sample before routing on a rate in that band. `notes/16`'s guard
> protected only against a false FAIL, which is the cheap error.

## 5. Pre-registration — Sep 3 PM, public, before any probe trains

To `origin` with a commit hash. Six items, carried from `notes/16` Stage D with #1 corrected:

1. **The divergence-point rule** — how token index `t` is located, as a rule, not per-pair.
2. **The read-offset schedule** — the exact `j` values, all **strictly after** `t`. Any `j ≤ 0` is
   reported as the proven 0.5 anchor and gets **one line**, as a sanity check, not a headline.
3. **The cue-identity criterion** — what makes two rollouts count as having received the same
   situation. *The one criterion that cannot be fixed after seeing results, and where a hostile
   reviewer will push.*
4. **The identity-control protocol.**
5. **The text-only baseline protocol** (`2509.21344`).
6. **Scenario inclusion criteria, including the yield threshold.** Selecting scenarios by yield after
   seeing results is a forking-paths problem: yield tracks behavioural uncertainty, which plausibly
   tracks predictability.

Also pre-register **the "action commits" rule** that defines `L`. It sets the range of the x-axis, and
a rule chosen after seeing curves is a reviewer's easiest attack.

## 6. Content: non-negotiable, and the cut order

**Never cut:**

- `2606.09890`, `2606.30449` and `2507.12428` cited **in the first paragraph.** Not citing them is the
  likeliest cause of a desk-level reject.
- **Two scenario domains.** One model family is fine — `2606.30449` used one primary model per probe
  family. One *domain* is what an evolutionary-computation PC rejects on: it reads as **n=1 problem
  instances** (`ideas/27` §5).
- **Text-only baseline at every `j`.** Post-divergence pairs differ in visible tokens; this is the
  control whose absence was fatal to C1.
- **One random-direction control** and **one held-out-scenario transfer number**, reported even if
  negative. Without both, the paper reads as pre-dating the June 2026 literature.
- **Confidence intervals.** They are the curve. Without them there are eight noisy points.
- **The released pair generator.** The artifact is the contribution; B5 is bought by the artifact, not
  by the result.
- **The public pre-registration.**

**Cut order if the clock slips:** (1) the G4 arm — named as future work, never silently dropped,
(2) extra probe families beyond the four `2606.30449` name, (3) read offsets *within* the sweep.

**Scope sentence that belongs in the abstract, not the limitations:** the construction only yields
pairs where the model is behaviourally uncertain, so this measures pre-action predictability
*conditional on behavioural uncertainty*. A reviewer finds that otherwise.

## 7. Stopping rules, and what happens after a stop

**Stop conditions:** Gate B fails · Gate C returns FAIL on both domains · anything that makes Sep 11
writing impossible.

**On a stop, the honest options — decided now, so they are not invented under pressure:**

1. **C2** — context grafting vs RMU, ~$15, `cais/Zephyr_RMU` ✅ verified to load on a 4090. Needs a
   venue that fits it; EvoRobust fit is "Multi-Objective Trustworthy AI," which is a stretch.
2. **Submit nothing on Sep 12** and take the SaTML window with a properly built artifact. Re-check
   satml.org **Sep 19**, when CFPs become legible, and run **G2** that day.

**There is deliberately no manufactured third branch.** Round 15 killed Branch C because it was rescued
on a venue-fit argument without re-opening its evidence. Inventing a replacement fallback under
deadline pressure is exactly how this board acquired four consecutive leads that were promoted for
being least-attacked and then died (**R11**). A stop is the plan working.

## 8. Resources

**Primary model: `Llama-3.1-8B-Instruct`**, 24GB card. It generates several times faster than the 27B
and the identity floor is a property of a deterministic forward pass, not of scale. Larger models are
a transfer arm at most; `notes/11` says breadth is padding.

**Budget is not the binding constraint — time is.** ⚠️ *Planning estimate, not a measurement:* on the
order of 5,000–10,000 8B rollouts, comfortably inside the $120 allocated to C9 against the $200–300
budget. Surplus goes to a third domain, then more pairs, then a transfer model — never to breadth.

**Standing constraints:** public datasets only · no experiments involving real people · nothing
person-specific reported (`notes/08`).

## 9. Odds, recorded so they can be scored later

**~35%** at EvoRobust with two domains. The second domain is the largest single lever. These are
judgment, not measurement — treat them as ordering, not as numbers.

The uncomfortable part, recorded so it stays a decision: with zero lines of experiment code and ten
days, a corpus of 210+ pairs across two domains with a text-only baseline, controls and intervals is
not obviously reachable. What round 15 changed is that the contribution it buys is **smaller** than
`notes/16` assumed, so the same schedule now purchases less.
