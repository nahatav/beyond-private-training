# Hardened idea set — after code checks

Two portfolio items died this round, both from checks that cost under an hour. Recording the
evidence so they stay dead.

## Killed: C — unaccounted model selection on private validation splits
Read `aug-pe/main.py` directly. The iteration loop runs a fixed
`args.num_samples_schedule`; the only early exit is a checkpoint-resume test, not a performance
metric. **No private validation data is used to select the iteration, checkpoint, or
hyperparameters in the released code.** The idea dies cleanly and correctly.

## Killed: D — class-conditional PE and the private label distribution
The code *does* route private label statistics into generation:
`private_classes = list(private_labels_counter.keys())` and
`api.text_random_sampling(..., prompt_counter=private_labels_counter)`.

But this is **a documented assumption, not a hidden bug**. Aug-PE states plainly:

> "Following Yue et al. (2023), we assume that class labels are non-private."

And more decisively — **the paper I was about to write already exists, by a workshop organizer.**
*MAPLE: Metadata Augmented Private Language Evolution* (Chien et al., arXiv 2603.19258, TPDP 2026)
observes that Aug-PE "treats class labels available in the OpenReview dataset as public and does
not ensure corresponding DP protection", and privatizes that metadata through AIM with explicit
zCDP composition (ρ_AIM = 0.1ρ, ρ_PE = 0.9ρ).

This is the second time the obvious-and-good idea turned out to belong to someone in the room.
It is also exactly why the checks come before the writing.

---

# The surviving lead, hardened

## Thesis, in one sentence

**Private Evolution's privacy unit is a sample, but private data arrives in person-sized bundles,
and for a vote-based mechanism those bundles are the most expensive possible correlation
structure.**

## Why the gap exists — and this framing is the honest one

An earlier draft of this pitch said "Aug-PE's reported ε on Yelp is not the ε that matters." That
is sloppy: Yelp reviews and PubMed abstracts are *already public*. They are proxies, not private
data. Attacking the benchmark numbers would be attacking a methodological stand-in.

The correct framing is stronger, because it explains *why* nobody has hit this yet:

> PE's benchmarks are public corpora used as proxies for private ones, so the privacy unit has
> never had to be confronted. But PE is now deployed on genuinely private, genuinely
> user-structured data — **Apple has adopted it** — where the natural unit is a person: chat
> transcripts, support tickets, clinical notes, a user's photo roll. The accounting PE ships with
> is per-sample, and there is nothing anywhere in the algorithm or the code that accounts for one
> person contributing many correlated samples.

The gap is a consequence of the benchmark suite being public. That is a clean thing to say and
nobody has said it.

## The technical content

Confirmed against `dpsda/dp_counter.py:53`: each private sample votes for its `k` nearest
candidates, contributing ℓ₂ norm √k, and the noise scales by √k to match. Sensitivity is a
per-sample quantity.

Under person-level adjacency, removing user `u` removes their whole vote vector `v_u`:

`Δ_user = max_u ‖v_u‖₂`, with `√(k·m_u) ≤ ‖v_u‖₂ ≤ k·m_u` for a user with `m_u` samples.

Lower end = votes spread over distinct candidates. Upper end = every vote lands on the same
candidate. Gaussian noise scales linearly in Δ, so **the entire user-level cost reduces to one
measurable quantity: vote concentration.** Define `ρ_u = ‖v_u‖₂ / √(k·m_u)`.

Three results follow, and they are of three different kinds — which is what makes it a paper rather
than an observation:

1. **Structural (the interesting claim).** A person's samples are semantically similar, so they
   land in the same Voronoi cell and their votes *concentrate*, driving ρ toward its maximum. This
   is the opposite of the DP-SGD case, where a user's per-example gradients partially cancel.
   **Vote-based inference-time mechanisms are structurally worse under user-level DP than
   gradient-based training-time ones, because correlation concentrates rather than cancels.**
2. **Positive (the accountant).** The direct ℓ₂ analysis is never worse than the group-privacy
   lemma and is better by exactly 1/ρ, with no δ blow-up. A strictly tighter user-level accountant
   for PE, for free.
3. **Algorithmic (the fix).** Cap each user to one vote per candidate: `v_u[j] ← min(v_u[j], 1)`.
   Then `‖v_u‖₂ ≤ √(#distinct candidates hit)` — a **provable √ dependence instead of linear**,
   from a two-line change. Compose with a total-contribution cap `C` for `Δ ≤ √C`.

Plus a design consequence that only exists at user level: **the candidate-pool size `|V|` becomes a
privacy knob.** At sample level `|V|` has no effect on sensitivity whatsoever, so no PE paper has
had any reason to notice. A larger pool spreads a user's votes and lowers Δ.

## Experimental design — controlled first, real data second

**Arm 1 (carries the weight, no real identities).** Construct groups with a controlled
within-group similarity parameter and sweep it. Output: Δ_user / ρ as a function of intra-user
coherence. This turns a single-corpus observation into a curve a reader can place their own
deployment on.

**Arm 2 (one anchor point).** arXiv abstracts grouped by author — CC0, public scholarly record,
professional capacity, no sensitive attributes. Answers only: where does naturally-occurring
authorship sit on the curve?

**Arm 3 (if time).** Utility curves for user-level PE at matched user-level ε: naive group privacy
vs. the direct accountant vs. one-person-one-vote.

Costs: Arm 1 ≈ 1 GPU-hour, Arm 2 ≈ 1 GPU-hour, Arm 3 ≈ 1–2 GPU-days. Details in `notes/08`.

## Outcome-robustness

- ρ near maximum → "user-level PE is near worst case; here is the mechanism that fixes it."
- ρ near 1 → "user-level PE is far cheaper than group privacy implies; here is the tighter
  accountant."

**Both are publishable.** With seven days left this is the property that matters most, and it is
the reason to pick this over anything else in the portfolio.

## Referee attacks and answers

| Attack | Answer |
|---|---|
| "User-level DP is just the group-privacy lemma." | The direct ℓ₂ analysis is tighter by 1/ρ and avoids the δ blow-up; the capping mechanism changes the exponent from linear to √. Say this in the abstract. |
| "Your benchmarks are public data anyway." | Conceded and made into the argument: the unit was never confronted *because* the benchmarks are public proxies. The deployments are not. |
| "Isn't this MAPLE?" | No. MAPLE privatizes the *metadata channel*. This is the *privacy unit*. Orthogonal axes on the same algorithm; cite prominently. |
| "Does it generalise past PE?" | One paragraph on DP-ICL: its guarantee rests on partitioning exemplars into **disjoint** shards, but a user with several exemplars lands in several shards and perturbs all of them, so the argument degrades to record-level. Fix: user-aware sharding. |

## Scope decision
Keep the paper on PE, with DP-ICL as a closing paragraph. Four pages, and the venue rewards short
exact notes over broad ones (see `notes/06`).

---

# Second-strongest survivor

**B — the privacy-free baseline.** PE papers report *absolute* downstream accuracy per ε; nobody
reports the ε=0 arm, i.e. the same foundation model prompted to generate the same kind of data with
**zero access to the private corpus**. The meaningful quantity is lift over that baseline.

Honest assessment: this is a critique paper, and *Is API Access to LLMs Useful for Generating
Private Synthetic Tabular Data?* (Swanberg, McKenna, Roth, Cheu, Kairouz — arXiv 2502.06555) is
adjacent for tabular, though its baselines still consume private data rather than none. Solid, not
a knockout. **Best used as a second arm of the lead paper rather than standalone** — it is exactly
the right control to report alongside user-level utility curves.

Lowest data friction of anything in the portfolio: uses Aug-PE's corpora as-is, no identities.

# Everything else
- **E referent-level** — real but fuzzy; hard to make crisp in four pages. Backup.
- **F reconstruction bounds** — derivation risk; does not compress into seven days.
- **G subsampled PE** — likely null to first order; a section of the lead, not a paper.
- **C, D** — dead, evidence above.
