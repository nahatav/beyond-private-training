# Idea H — the lead, repositioned: user-level PE changes what PE estimates

Supersedes the framing in `ideas/09`. The technical machinery survives intact; the *claim* moves,
because `lit/03` found that the DP-fy guide (arXiv 2512.03238) already states a user-level recipe
for PE. Attacking the gap is no longer available. Attacking the recipe is, and it is better.

## Title candidates
1. **Normalising Users Changes What Private Evolution Estimates**
2. One Person, One Vote — But Whose Vote Counts?
3. The Privacy Unit Is Not a Free Parameter

## Thesis, one sentence

> The only published way to run Private Evolution under user-level DP re-weights every user by the
> square root of their semantic diversity, so PE stops converging to the private distribution — and
> unlike noise, this distortion does not vanish as ε → ∞ or as n → ∞.

## Setup and notation

Private corpus partitioned by user `u`; user `u` holds `m_u` samples. At iteration `t` the candidate
pool is `V_t`. Confirmed from `dpsda/dp_counter.py:53`: each private sample votes for its `k`
nearest candidates and the noise is scaled by `√k`, so a sample's vote vector has ℓ₂ norm `√k`.

Let `v_u ∈ Z^{|V_t|}` be user `u`'s aggregate vote vector, `‖v_u‖₁ = k·m_u`.

**Effective diversity.** `d_u := (‖v_u‖₁ / ‖v_u‖₂)²`. This is the inverse participation ratio of the
user's vote distribution — the effective number of distinct candidates their samples reach.
`d_u = 1` when all of a user's votes land on one candidate; `d_u = s` when spread evenly over `s`.
It is the same quantity as `ideas/09`'s concentration ratio, re-parameterised so that it reads as
*diversity* rather than *concentration*, which is what makes the bias statement legible.

## The normalisation family

The guide's fix is one member of a one-parameter family. Replace `v_u` by `ṽ_u = v_u / ‖v_u‖_p`.

**Proposition 1 (sensitivity).** For every `p ∈ [1,2]`, the user-level ℓ₂ sensitivity satisfies
`Δ = max_u ‖v_u‖₂ / ‖v_u‖_p ≤ 1`, by monotonicity of ℓ_p norms in `p`. So *every* member of the
family is a valid user-level mechanism at the noise level PE already ships. One line of proof.

**Proposition 2 (the estimand).** User `u`'s total mass in the normalised histogram is
`w_u(p) = ‖v_u‖₁ / ‖v_u‖_p`. Hence

| `p` | user mass `w_u` | the histogram estimates |
|---|---|---|
| record-level (no normalisation) | `k·m_u` | **sample-uniform** mixture — PE's original estimand |
| `p = 1` | `1` for every user | **user-uniform** mixture — the natural user-level estimand |
| `p = 2` (**the guide's recipe**) | `√d_u` | a **diversity-tilted** mixture — neither |

That table is the paper. The guide's normalisation is not the user-level analogue of PE; it is a
third thing, and it corresponds to no population anyone would name.

**Corollary (why it is worse than noise).** DP noise is zero-mean and averages out: PE's guarantees
degrade gracefully as ε shrinks and improve as ε grows. The `√d_u` re-weighting is a deterministic
distortion of the target measure. It is present at ε = ∞. It does not shrink as `n → ∞`.
*Private Evolution Converges* (González, Fanti, Ramdas, arXiv 2506.08312, NeurIPS 2025) proves
convergence to the private empirical distribution; under the guide's user-level adjustment the
object PE converges to is a different measure, so that theorem's conclusion no longer describes the
deployed algorithm. This is the sentence that belongs in the abstract.

**Proposition 3 (why the guide's choice is not stupid).** At matched worst-case sensitivity the
noise σ is identical across the family, while total signal mass `Σ_u w_u(p)` is *maximised* at
`p = 2`. So `p = 2` is the SNR-optimal member. The family is a genuine bias–variance trade-off:
`p` trades estimand fidelity against signal. The guide picked the variance end without saying that
there was a bias end. Presenting it as a trade-off rather than an error is both honest and stronger.

## The mechanism we propose: diversity-floored user normalisation

Take ℓ₁ (correct estimand) and buy back SNR by rescaling, capped so sensitivity still holds:

```
ṽ_u  =  v_u · min( √d₀ / ‖v_u‖₁ ,  1 / ‖v_u‖₂ )
```

- Sensitivity ≤ 1 unconditionally (the second term binds exactly when the first would violate it).
- User mass `= min(√d₀, √d_u)`: **exactly equal for every user with `d_u ≥ d₀`**, and the only
  down-weighted users are the maximally homogeneous ones, whose votes genuinely carry less
  information about the pool.
- One hyperparameter `d₀`, a diversity floor. We do **not** re-derive how to choose it privately —
  that is precisely the contribution-bound selection problem solved by Liu, Suresh, Zhu, Kairouz &
  Gruteser (arXiv 2206.03008); we cite their machinery and fix `d₀` a priori in experiments.

Two lines of code, same noise, correct estimand for the bulk of the population.

## Claim 3 — the part no one-shot histogram paper can have

PE is a **loop**, and the histogram is a *selection signal*, not the output: the top-`N` candidates
survive and get varied into the next pool. So consider a homogeneous user under the guide's `p = 2`:

1. Low `d_u` ⇒ low mass `√d_u` ⇒ their candidates are less likely to make the top-`N`.
2. The next pool therefore contains fewer candidates near their region.
3. With fewer nearby candidates, their samples crowd onto still fewer cells ⇒ `d_u` falls further.
4. Go to 1.

**The bias is a positive feedback loop.** Prediction: under ℓ₂ normalisation, homogeneous users are
progressively erased from the synthetic population across iterations, at an accelerating rate; under
ℓ₁ or the diversity floor they are not. Under ℓ₁ a homogeneous user is in fact *protected* — their
unit of mass lands concentrated on one candidate, which is a stronger per-candidate signal than a
diverse user's `1/√s` spread.

This is a disparate-impact result with a mechanism, in the lineage of Bagdasaryan, Poursaeed &
Shmatikov (*Differential Privacy Has Disparate Impact on Model Accuracy*, NeurIPS 2019) — which the
DP-fy guide itself cites when noting DP-generated text runs short. The difference is that theirs is
an observed accuracy gap and ours is a derivable re-weighting with a named functional form, `√d_u`.

## Experiments — the decisive one needs no generation

**E1 — the re-weighting curve (central figure, ~1 GPU-hour, arguably CPU).** Embed a user-structured
corpus, build a candidate pool, compute `v_u` by PE's own nearest-neighbour assignment. Plot user
mass `w_u(p)` against `d_u` for `p ∈ {1, 1.5, 2}` and against record-level. No generation, no PE run.
This alone demonstrates the estimand shift and its magnitude.

**E2 — the compounding test (~2–4 GPU-hours per arm, 4 arms).** Run PE for `T` iterations under
{record-level, ℓ₂, ℓ₁, diversity-floored} and track, per iteration, the representation of each user
group in the surviving population. Plot drift vs. `t`. Tests Claim 3 directly.

**E3 — utility at matched user-level ε (optional, ~1 GPU-day).** Downstream accuracy for each arm
against the naive group-privacy baseline.

**E4 — controlled arm, no real identities (carries the scientific weight).** Construct groups with a
tunable within-group coherence parameter, sweeping `d_u` directly. Turns E1/E2 from an observation
about one corpus into a curve a reader can locate their own deployment on. This is `notes/08`'s
design and it is unchanged.

**Data.** Controlled arm needs no identities. Real anchor: arXiv abstracts grouped by author (CC0).
Yelp stays dropped; OpenReview cannot support a user-level arm (anonymous reviewers). Per `notes/08`.

## Outcome-robustness — still the reason to pick this

- Compounding observed → "the recommended user-level recipe for PE erases homogeneous users, and the
  erasure accelerates; here is the two-line fix."
- Compounding not observed → "the estimand shift is real and measurable at iteration 1 but does not
  compound; the recommended recipe is safe in practice, and here is the analysis of why."

Both correct the record and both are publishable. Propositions 1–3 hold regardless of any
measurement, so the paper has a floor that no experimental outcome can drop below — which is the
property that matters with the clock where it is.

## Referee attacks and answers

| Attack | Answer |
|---|---|
| "The DP-fy guide already gives the user-level fix." | Yes — and it is the object of study, cited in the abstract. The contribution is that the fix is not estimand-neutral. Pre-empt in sentence two. |
| "This is Liu et al. 2206.03008 (user-level histogram contribution bounding)." | Their domain is fixed and their histogram *is* the output, so their clipping bias is one-shot. PE generates its own domain every round and the histogram is a selection signal, so the bias compounds. Claim 3 is not expressible in their setting. We cite, not re-derive, their threshold selection. |
| "Isn't user-level DP just the group-privacy lemma?" | Factor `k` in ε plus a δ blow-up; the direct ℓ₂ analysis is tighter and the normalisation family avoids both. |
| "Does the estimand shift matter, given DP data is approximate anyway?" | It is systematic, not stochastic: present at ε = ∞, invariant in `n`. Noise averages out; this does not. |
| "Cherry-picked corpus." | E4 is a swept curve on constructed groups; the real corpus supplies one anchor point, not the claim. |
| "Does it generalise past PE?" | Closing paragraph on DP-ICL — see `ideas/12`. |

## The discussion line worth saving for last

The DP-fy guide recommends PE specifically for the small-data, stringent-ε regime — it calls PE the
only method that works below ~1K datapoints and the right choice for ε < 1. But user-level
accounting replaces the effective sample count `n` by the number of *users*. **PE's recommended
operating regime is exactly the regime where switching to a user-level privacy unit costs the most.**
