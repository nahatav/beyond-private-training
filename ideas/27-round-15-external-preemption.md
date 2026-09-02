# Round 15 — C9's headline is occupied, Branch C fails G2, and Stage A cannot see either

Written 2026-09-02, after `notes/16` was made executable. This round did the one thing fourteen
rounds of ideation never did: **it looked outside the eight targets Stage A was going to grep.**
Every claim below was verified by fetching the source, with a positive control recorded next to it,
per R1/R3/R8.

**Result: the Sep 3 gate day, as designed, returns GREEN on an occupied claim.** Two of the three
branches are dead on evidence available today, without renting a GPU.

---

## 1. Three pre-emptions, and precisely what each leaves open

`ideas/25` restated C9's contribution as *"pre-action predictability as a function of tokens elapsed
since divergence, on an action-versus-situation construction, anchored at a proven floor."* Each of
the three clauses is separately published.

### 1a. The benchmark — **PreAct-Bench**, `2606.09890` (3 Jun 2026) ✅ fetched

*PreAct-Bench: Benchmarking Predictive Monitoring in LLMs* — Xu, da Silva, Ye, Wang, Liu, Yang,
Schwarz, Paoletti, He, Yan (KCL / Alan Turing). Positive control on the extracted text:
`PreAct` = 44, ` the ` = 471, so the zero-results below are real.

Verbatim from the paper:

> "we study a critical yet overlooked safety task, which we term **Predictive Monitoring**: given only
> a partial action trajectory, can a model infer whether it will culminate in an unethical action
> **before the overt action is executed**? To support this task, we present PreAct-Bench, a benchmark
> of **1,000 paired ethical and unethical action trajectories spanning five domains**."

> "we first construct a task from a situation and a hidden objective, then generate paired
> trajectories for the same task: ethical and unethical. **This paired design reduces confounds by
> holding the surface task fixed while varying the underlying intent.**"

That sentence is C9's construction rationale, in print, three months ago. It also ships the metric —
*"varying fractions of the action trajectory using our **Prefix Foresight F1** metric"* — and the
probe arm C9 was going to contribute: *"use the representation from the **residual stream of the 22nd
layer** of Llama3."*

**What it does not have, and this is the whole of what survives:**

| Grep | Count |
|---|---|
| `divergen*` | **0** |
| `shared prefix` / `same prefix` / `identical prefix` | **0** |
| `token offset` | **0** |

Its pairs are **separately generated** from a task and a hidden objective — not sampled from one
model until it diverges. So the pair members never share a byte-identical prefix, and there is no
divergence point to anchor an axis at. Its trajectories and its labels are both **GPT-5-mini**
output, validated against two human annotators by Krippendorff's α — a circularity the paper itself
surfaces.

> ⚠️ **Not verified, do not cite:** the human-baseline figure 0.907, the probe figure 0.774 and the
> guardrail collapse range were reported to us second-hand and did **not** reproduce on a direct grep.
> A claimed "25% edit-distance guard" on pair construction returned **zero** hits and is withdrawn.

### 1b. The curve — `2507.12428` ✅ fetched

*Can We Predict Alignment Before Models Finish Thinking?* Positive control ` the ` = 513.
It defines C9's x-axis explicitly:

> "the **foresight** is n−k, which indicates **how far 'into the future' the monitor needs to
> predict**."

and it sweeps it as a 2-D grid, not a single point:

> "When trained for each **observed–foresight combination** (Figure 3(a)), probes with higher observed
> values (30–40 sentences) sustain F1 scores of 50–60 even when predicting **50 steps ahead**."

It also already runs the arm `ideas/25` §3 makes mandatory:

> "a simple linear probe trained on CoT activations significantly outperforms **all text-based
> baselines**… an average absolute increase of 13 in F1 scores."

**What it leaves open:** it is a CoT/response-alignment setting, not agentic (`agent` = 2), and
`divergen*` = **0**. Its index is distance-to-response, not distance-from-divergence.

### 1c. The construction and the floor — `2606.30449` ✅ fetched (positive control `probe` = 99)

The repo already owns this citation but has consistently under-read how much of C9 it contains. Its
bridge probe **already ran on same-scenario, sampling-divergent rollouts at two read positions**:

> "On **596 valid rollouts at two prefill fractions** (n=1192 rows, blackmail rate 13.3%), the best
> single-layer probe reaches **AUC 0.632**."

Two prefill fractions is a 2-point *j*-sweep. `ideas/24` describes this as "a single weak test"; it is
better described as the first two points of C9's own curve.

**What it leaves open — and it says so itself, twice:**

> "This rules out a readout that would have predicted the later split from the shared prefix alone;
> **it does not test whether a post-cue pre-action state can predict the action.**"

> "This is a condition-controlled prediction check, **not an identical-prefix minimal-pair test**: the
> prefill states include rollout-specific truncated assistant prefixes, so the per-row hidden state is
> **not byte-identical across rollouts within a condition**."

### 1d. The floor is not an asset

No paper presents *identical prefix ⇒ chance* as a contribution, because activations are a
deterministic function of the prefix and the field treats it as too obvious to state. `ideas/25` §1
reaches this conclusion correctly — *"trivially true because the strong form is impossible"* — and
then in §2 re-banks the same tautology as *"a benchmark with an analytically-known floor… the single
most defensible thing on the board."*

**An argument cannot both void the headline and be the headline.** Demote the floor to a sanity
check, where it belongs, and stop paying for it in the abstract.

### 1e. What actually survives

**Sampling-divergence as the anchor.** PreAct-Bench holds the task fixed and varies intent by
*generating* two trajectories; `2606.30449` has one input-driven divergence at n=2; `2507.12428`
indexes to the response. Nobody builds pairs whose divergence is caused **only by the sampler**, with
the cue held fixed, and indexes the read position at **tokens since the divergence token**.

That is one increment on a competitor's stated limitation. It is real, it is narrow, and it is worth
a short paper. It is **not** a benchmark with a novel curve, and it must not be sold as one.

---

## 2. Stage A is aimed at the wrong shelf

None of §1a–1c is among Stage A's eight targets, and none would be found by grepping them. All eight
targets — `2506.02946`, MisActBench, Petri, SHADE-Arena, ControlArena, AgentHarm, ToolEmu, τ-bench —
are **inside AI safety**, and are agentic-benchmark papers rather than monitoring papers.

**This violates the rule the sweep exists to discharge.** R2/G1 says *"name the two nearest neighbours
**outside** AI safety,"* and `notes/12` records three consecutive leads dying exactly that way. A
sweep drawn entirely from the home literature cannot discharge an out-of-field rule.

Consequence, stated plainly: **Gate A returns CLEAR, and the fork routes to green on an occupied
claim.** The most expensive day in the plan was pointed at the shelf least likely to hold the
pre-emption. See the new rule **R14** in `notes/12`.

The neighbourhoods Stage A should have covered: early classification of time series (the
earliness/accuracy tradeoff, ~25 years old); prediction-horizon and lookahead work in transformers;
and monitoring papers — as opposed to benchmark papers — inside safety.

---

## 3. Branch C fails G2 outright. It does not need Sep 3.

`ideas/26` and `notes/16` both motivate C4 with *"`2510.09462` proposes ensembling as the
mitigation."* ✅ Fetched — the paper is:

> **Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols** — Mikhail Terekhov, Alexander
> Panfilov, Daniil Dzenhaliou, Caglar Gulcehre, **Maksym Andriushchenko**, Ameya Prabhu, Jonas
> Geiping. ICLR 2026.

Three things follow, and each is independently disqualifying:

1. **Andriushchenko is an EvoRobust invited speaker and a co-author.** `notes/16` Branch C schedules a
   G2 check on him for Sep 3. The check is already answerable and it is a **fail** — C4 is a one-step
   execution of the future-work sentence in his own paper.
2. **The paper *is* C4's attack**, already run against single monitors, with C4's exact threat model:
   *"we assume the red team knows the monitoring model and the prompts, the protocol algorithm, and
   its thresholds. Many defenses fail once adversarial attacks do not rely on security through
   obscurity and are tailored to a particular defense (Tramer et al., 2020)."* Ensembling appears in a
   future-work clause. C4 therefore cannot claim to import adaptive-attack methodology into AI
   control; that import happened in this paper.
3. **The citation was never opened.** "Proposes ensembling as the mitigation" is only reachable from a
   search snippet. This is an **R1 violation on the single citation carrying all of Branch C** — the
   branch `notes/16` calls *"the highest-probability path on the board (~55–60%)."*

`notes/14` already had C4 in the *weakened* table ("the answer is substantially predicted"); `ideas/26`
rescued it on a venue-fit argument without re-opening the evidence. The rescue does not survive.

---

## 4. The gates cannot resolve their own bands

**Gate C.** The PASS threshold is a median minority-action rate ≥10%, measured at N=30 per scenario.
Wilson 95% intervals at that N:

| Observed | Rate | 95% CI |
|---|---|---|
| 2/30 | 0.067 | [0.018, 0.213] |
| **3/30** | **0.100** | **[0.035, 0.256]** |
| 4/30 | 0.133 | [0.053, 0.297] |

At the exact PASS boundary the interval spans **FAIL, AMBER and PASS**. The pre-committed statistical
guard is one-sided: it escalates to N=150 only on ≤1 minority rollout, protecting against a false
FAIL while ignoring a **false PASS** — which is the expensive error, because it routes into Branch A,
the path that budgets seven days for a nine-day build.

**No target pair count exists anywhere in `ideas/24`, `ideas/25`, `ideas/26` or `notes/16`.** The
entire paper is the shape of a curve, so this is the load-bearing number. Hanley–McNeil, N per class:

| True AUC | Pairs, single test | Pairs, Bonferroni over an 8-point *j*-sweep |
|---|---|---|
| 0.55 | 520 | — |
| 0.60 | 130 | **210** |
| 0.65 | 60 | 90 |
| 0.70 | 30 | 50 |

`2606.30449`'s bridge probe reached **AUC ≤ 0.632** with negative leave-one-condition-out lift, so
0.55–0.65 is the honest planning range → **210–520 pairs**. At Gate C's PASS rate that is
**2,100–5,200 rollouts per scenario**; in the AMBER band, 4,200–26,000.

`ideas/24` ranks confidence intervals **third on the surplus list**. They are not surplus. Without
them there is no curve, only eight noisy points.

---

## 5. Venue fit is inverted

**EvoRobust** ✅ CFP fetched (positive control: `workshop` = 16). From its own page source:

> "Based on **60–80 expected submissions**, we will expand the PC beyond the preliminary members
> listed below to ensure **three reviews per submission and at most three papers per reviewer**."

Reviews are due **Sep 16** — four days after the deadline. The PC skews evolutionary computation
(Leiden, NTU, A*STAR) and CV robustness (Monash, Apple).

Two consequences `ideas/26` did not price:

1. **One model family × one scenario domain reads to that pool as n=1 problem instances** — the most
   reliable reject reason in evolutionary-computation benchmarking review. An AI-safety native accepts
   honestly-scoped single-domain work; this pool does not. **The second scenario domain moves from
   surplus to mandatory.**
2. **C9 has no search algorithm in it.** `ideas/26` lifts A4 by mapping "search the rollout space for
   divergent pairs" onto diversity-driven search and the *j*-sweep onto a coverage metric. Rejection-
   sampling 30 rollouts at temperature has no archive, no behavioural descriptor and no evolutionary
   operator. A static benchmark also cuts against a workshop whose thesis is *self-evolving*
   evaluation. This is a rhetorical mapping, and an EC reviewer will see through it in one pass.

**AIWILD** is the better fit for what C9 has actually become. Its short track explicitly invites
*"implementations of unpublished ideas, modest theoretical results, follow-up experiments, or fresh
perspectives on existing work"* — which is precisely the surviving contribution. `2606.30449` was
published at the ICML edition, so those reviewers arrive with the context already loaded.

> ⚠️ **Unverified:** an acceptance rate of ~64% for the ICLR edition was reported to us from a
> hand-count of the virtual site against an organizer's submission figure. Treat as an order of
> magnitude, not a number, and do not cite.

---

## 6. The AIWILD determinism note is dead

`notes/16` Branch A spends **two of ten days** writing a 4-page note whose content is (i) reproducing
`2606.30449`'s identity-cosine floor and (ii) the analytic argument of §1d. That is *their* published
number plus a tautology, submitted to the venue where they published it.

The priority-claim rationale does not hold either: **Stage D already buys the priority claim** with a
public timestamped pre-registration, in 30 minutes, on every branch. Branch A pays two days for
something the plan already gets for free.

---

## 7. What this round changes

| Item | Was | Now |
|---|---|---|
| **Branch A (AIWILD note)** | green path | **dead** — §6 |
| **Branch C (C4)** | "highest-probability path, ~55–60%" | **dead** — §3, G2 fail |
| **Branch B (C9 → EvoRobust)** | amber fallback | **the only branch**, and it needs the §8 reframe |
| **Stage A target list** | 8 in-safety benchmarks | re-aimed out-of-field — §2, R14 |
| **Gate C** | ≥10% at N=30 | needs a two-sided guard and a stated pair target — §4 |
| **Second scenario domain** | surplus, first to cut | **mandatory** — §5 |
| **Confidence intervals** | surplus, third | **mandatory** — §4 |
| **The proven floor** | "most defensible thing on the board" | a sanity check, one line — §1d |

## 8. The reframe, in one sentence

Not *a benchmark for pre-action monitoring* (PreAct-Bench dominates it on every axis a reviewer
checks). Not *probes fail at pre-action monitoring* (`2606.30449` published it, and the field has
stopped finding it surprising). But:

> **How much of pre-action predictability is the situation, and how much is the particular sampled
> continuation** — measured on pairs whose divergence is caused only by the sampler, indexed by tokens
> since the divergence token, with the transfer and specificity controls `2606.30449` requires.

That resolves a limitation `2606.30449` names in its own words, and it is the one formulation of C9
that three fetched papers do not already contain.

**Mandatory content, non-negotiable:** cite `2606.09890`, `2606.30449` and `2507.12428` in the first
paragraph — not citing them is the likeliest cause of a desk-level reject; at least one
random-direction control; at least one held-out-domain or held-out-scenario transfer number **even if
negative**; a released pair generator; and a stated pair count with intervals.

## 9. Honest odds

| Path | Odds | Binding reason |
|---|---|---|
| C9 as written → EvoRobust | ~20% | Occupied headline; n=1 instances to an EC pool; no search algorithm; zero slack |
| C4 → EvoRobust | ~15% | G2 fail; result predicted in advance by three published lines |
| AIWILD determinism note | ~0% | Their number, their venue, plus a tautology |
| **C9 reframed (§8) → EvoRobust + 2nd domain** | **~35%** | The realistic target |

**The uncomfortable part, recorded so it stays a decision.** With zero lines of code written and nine
days left, a benchmark carrying 210+ pairs, two domains, a text-only baseline and confidence
intervals is not obviously reachable. That was true before this round. What changed is that the
contribution it buys is **smaller** than `notes/16` assumes, so the same schedule now purchases less.
