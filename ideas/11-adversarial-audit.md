# Adversarial audit of this repo's own ideas

Attacking our own material rather than the literature. Four findings, one of which invalidates a
mechanism this repo proposed and is the rigorous justification for the pivot in `ideas/10`.

## 1. The mechanism in `ideas/09` is dominated by the recipe it was meant to beat

`ideas/09` proposes per-candidate vote capping, `v_u[j] ← min(v_u[j], 1)`, and claims it delivers
"a provable √ dependence instead of linear". The algebra is right: after capping,
`‖v_u‖₂ ≤ √(#distinct candidates u hits)`.

But that bound is **≥ 1 and grows with the user's spread**, so the mechanism still requires noise
scaled to `√(#distinct)`. The DP-fy guide's normalisation achieves `Δ = 1` flat, for every user, at
PE's shipped noise level.

**So the guide's two-sentence recipe strictly dominates the mechanism this repo spent two rounds
developing, on the axis the repo was optimising.** Capping controls the *growth rate* of the
sensitivity; normalising controls its *value*. Only the second is what the noise calibration needs.

This is not a small correction — it removes the "algorithmic (the fix)" leg of `ideas/09`'s
three-legged pitch. It is also exactly why `ideas/10` must compete on the **estimand** rather than
on sensitivity: sensitivity is a solved problem and we would lose that fight.

## 2. `ideas/05` and `ideas/09` disagree with each other on the sensitivity range

- `ideas/05`: `Δ_user = max_u ‖v_u‖₂`, with `√k_u ≤ ‖v_u‖₂ ≤ k_u`, where `k_u` is *samples per user*.
- `ideas/09`: `√(k·m_u) ≤ ‖v_u‖₂ ≤ k·m_u`, where `k` is the *number of nearest neighbours* and `m_u`
  is samples per user.

`ideas/09` is the correct one. `ideas/05` silently conflates the neighbour count `k` with the
per-user sample count and drops a factor of `k` from both ends of the interval. **Erratum recorded
here so the wrong interval does not reach the paper.** Canonical form, from
`dpsda/dp_counter.py:53` (each sample votes for `k` candidates, noise scaled by `√k`):

```
‖v_u‖₁ = k·m_u        √(k·m_u) ≤ ‖v_u‖₂ ≤ k·m_u        d_u := (‖v_u‖₁/‖v_u‖₂)² ∈ [1, k·m_u]
```

## 3. The threat `ideas/10` must check before anything else

`ideas/10`'s headline is that the guide's recipe weights users by `√d_u`, read as *semantic
diversity*. That reading only holds if `d_u` sits meaningfully **below** its ceiling `k·m_u`.

If the candidate pool is large relative to the corpus, nearly every sample reaches distinct
candidates, `d_u → k·m_u`, and the recipe degenerates to `w_u ∝ √(k·m_u)` — mass proportional to the
square root of a user's *sample count*. That is still an estimand shift, and still worth stating
(the guide's fix silently interpolates between user-uniform and sample-uniform at exponent ½), but
it is a much less striking claim than a diversity tilt.

**So E1's first output is not the re-weighting curve, it is the ratio `d_u / (k·m_u)`.** The paper
has two framings and the data picks one:

- `d_u ≪ k·m_u` (users cluster, as the repo's structural hypothesis predicts) → the diversity-tilt
  paper, which is the strong version.
- `d_u ≈ k·m_u` → the exponent-½ paper: the recipe is a covert contribution-scaling rule, neither
  privacy unit, chosen without comment.

Both are correct results about the same equations. This is outcome-robustness at the level of
*framing* rather than just of sign, which is the more valuable kind. It also means the very first
hour of compute settles which paper we are writing.

## 4. Idea E (referent-level privacy) is weaker than this repo has been assuming

`ideas/07` scores E as "no direct match found". That was a search artefact. The DP-fy guide §5.1 has
a **"Sub-unit level of privacy"** paragraph making E's core observation directly: it cites Brown et
al. (2022) for the argument that the right unit is a *secret* rather than a record, notes that in
free-form text secrets are represented across multiple users, and concludes that user-level
protection is **not qualitatively stronger than example-level** when secrets span users — the guide's
own example being many people pasting the same sensitive document into a chatbot.

That is E's thesis, stated by fifteen Google authors, resting on a 2022 position paper. E is a
**restatement**, not a discovery. It also now has an occupant on the mechanism side: SecPE
(Wang, Chen, Du, Xiao, Zhang, Yan — *Secret-Protected Evolution*, arXiv 2510.10990) builds
secret-aware protection into PE directly, which is the constructive half E would have needed.

**Downgrade E from "warm backup" to dead.** Recorded so it is not revived in round 8.

## 5. Idea B (the ε=0 baseline) — partly pre-empted, but there is a version that survives

The DP-fy guide's own comparison table rates PE's resilience to distribution gaps between the
private data and the LLM as **Low**, and states that PE requires high-quality public data similar to
the sensitive data plus substantial prompt engineering. That is most of B's critique — PE's utility
is substantially inherited from the public prior — asserted by Google in a document everyone in this
area will have read. B as a standalone critique paper is now weak.

**The version that survives, and it is free:** lift over the ε=0 prior is not a constant, it is a
function of the privacy unit. Moving from record-level to user-level shrinks the effective sample
count from samples to *users*, so the private signal shrinks while the prior does not.

> Prediction: measured as lift over a zero-private-data baseline, PE's advantage degrades
> substantially faster in the privacy unit than in ε.

That is one extra arm inside `ideas/10`'s E3 — the same runs, one more baseline — and it converts B
from a demoted standalone into the sharpest single number in the lead paper. It is also the
quantitative form of `ideas/10`'s closing observation that PE's recommended operating regime
(small data, stringent ε) is exactly where a user-level unit costs most.

## Unchanged from previous rounds

- **C, D** — dead, evidence in `ideas/09`, unaffected by anything found this round.
- **v3 (LLM-written DP code audit)** — still demoted for saturation risk; `notes/06`'s reading that
  this committee rewards short exact notes over benchmark-shaped papers argues against it
  independently of scoop risk.
- **`num_packing` modulo folding** (`notes/08`) — still an unverified hypothesis about a possible
  sensitivity under-estimate in released code. Still requires reading the packing path end to end,
  and if real still warrants private disclosure to the authors rather than a workshop paper. Not a
  claim, not in scope, not to be mentioned publicly.
- **Post-processing check now needed for `ideas/10`:** aug-pe clips the noisy count at a threshold
  and subtracts it. Under any per-user normalisation the counts stop being integers, so the
  threshold's semantics change. Footnote at minimum; one hour of code reading to be sure.
