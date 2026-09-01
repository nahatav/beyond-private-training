# The lead, hardened by the adversarial review — actionable delta over `ideas/10`

The lead survived a direct kill attempt: R1 re-derived Propositions 1–3 from scratch (correct, with
no hidden assumption beyond `v_u ≥ 0`), re-verified every load-bearing citation against primary
sources, and re-ran the novelty search including an angle the repo had missed. **No fatal flaw.**
This file records only what *changes* in `ideas/10` before writing. The thesis and the propositions
are unchanged.

## 1. Retarget the primary exhibit onto shipped code — the highest-leverage fix ★

`ideas/10` treats the DP-fy guide's two sentences as the object of study, with `aug-pe`'s
`dp_counter.py:53` as evidence of the *record-level* baseline. There is a strictly stronger anchor,
verified this round by reading the `microsoft/DPSDA` repository directly (GitHub API + raw files):

- File `pe/histogram/nearest_neighbors.py`, class `NearestNeighbors`, constructor parameter
  `vote_normalization_level` with values `"sample"` (record-level) and `"client"` (user-level).
  Docstring for `"client"`: *"normalize the votes from all private samples of the same client to
  have l2 norm = 1."* Implementation normalises each client's sub-count (`sub_count /=
  np.linalg.norm(sub_count)`) before summing into the histogram.
- The DP noise is added afterward, at a fixed pre-calibrated scale, by `Gaussian.add_noise` in
  `pe/dp/gaussian.py`, which **never inspects `vote_normalization_level`.** The accounting layer
  takes "sensitivity is bounded" on faith from whichever histogram mode is plugged in.
- Introduced in commit **`25cdf854a22f...`** (2025-02-20), title *"add the support of client-level
  DP,"* authored by **Zinan Lin**. This predates the DP-fy guide (Dec 2025) by ten months and is by
  PE's own inventor / this workshop's invited speaker.

**Action.** Make the shipped `"client"` mode the paper's primary exhibit; keep the DP-fy guide as
corroborating documentation, not the sole object of study. The opening sentence becomes: *the
reference PE library has shipped a user-level (`"client"`) vote-normalisation mode for a year and a
half, its accounting layer is blind to which mode is active, and — Propositions 1–3 — that mode is
not estimand-neutral.* That is a more concrete "channel the accounting silently omits" than guide
prose.

**Verify at write-time** (repos move; the CFP desk-rejects on unsubstantiated claims): re-confirm
the file paths, the parameter/docstring wording, and the commit SHA/date/author against the live
`microsoft/DPSDA` `main` before they go in the paper. The evidence dumps used this round were scratch
and have been deleted; re-fetch fresh.

## 2. Handle the speaker-adjacency deliberately

Retargeting means the paper now directly examines code committed by Zinan Lin, whose territory
`notes/06` flags as "Private Evolution + all its extensions." Frame the `"client"` mode as a
**reasonable, principled engineering choice** — Prop. 3 proves `p=2` is the SNR-optimal member of the
admissible family — **with an under-examined consequence**, never as an error. This is both diplomatic
and the mathematically honest framing (there is no tension between the two here), and it is the same
posture the repo already used for MAPLE and for `ideas/09`'s abandoned mechanism.

## 3. Hedge the ε→∞ corollary to match what is proven

`ideas/10`'s "survives ε→∞" paragraph currently states as settled fact that *"under the guide's
user-level adjustment the object PE converges to is a different measure."* Propositions 1–3 are all
**single-round** estimand statements; they do not establish that PE-with-normalisation even has a
clean fixed point, which is exactly what Claim 3 / E2 tests. R1 confirmed *Private Evolution
Converges* (2506.08312) proves convergence of the **unnormalised** histogram to `µ_S` with ℓ₂
sensitivity 2/n and contains zero "user-level" mentions — so the theorem, as stated, simply does not
cover the normalised variant.

**Action.** Rephrase to stay inside the proof: *"if PE-with-normalisation converges to a fixed point
(an open question — see Claim 3 / §E2), that fixed point cannot be `µ_S`, since the per-round target
already differs at the algebraic level (Prop. 2); [PE Converges]'s guarantee, as stated, covers only
the unnormalised histogram."* Removes the one place the draft outruns its evidence.

## 4. State the multi-owner assignment rule for the arXiv anchor

User-level sensitivity (and Prop. 1) requires that removing one user changes *only* that user's vote
vector — i.e. a clean partition of records into users. arXiv abstracts routinely have ≥2 co-authors,
so "group by author" is not a partition until a rule is fixed. The DP-fy guide itself flags this
(§7.2, "capping user contributions can become tricky, especially for multi-owner documents").

**Action.** State the assignment rule up front (e.g. credit each abstract to its first author only,
one identity per record), and cite the guide's own §7.2 flag as the reason it needs stating. One
sentence; pre-empts the first question a DP-theorist referee will ask.

## 5. Make E2's go/no-go conditional on E1's branch, not just its framing

`ideas/11` treats E1's `d_u/(k·m_u)` outcome as choosing only the *headline framing* (diversity-tilt
vs exponent-½), with both branches publishable — true for Propositions 1–3. But Claim 3 / E2 (the
compounding-erasure story) needs **cross-user variation in `d_u`** to have any content. In the weak
branch (`d_u ≈ k·m_u`, diversity saturated near ceiling for nearly everyone), there is little
heterogeneity for a feedback loop to amplify, so E2 risks an *uninformative* null, not just a less
dramatic one.

**Action.** If E1 lands in the weak branch, reallocate E2's two days to a cleaner write-up of the
(fully valid) exponent-½ result plus a stronger **E4 controlled sweep** — the controlled arm can
manufacture the heterogeneity the real corpus lacks, so E4 (not E2) is where saved time should go.
Decide this at the end of Day 1, per `notes/09`'s cut logic.

## 6. Bibliography, resolved this round (desk-reject hygiene)

- **DP-fy guide** (2512.03238) is now a **published JAIR article**, Vol. 86, Article 17 (2026) —
  cite as peer-reviewed JAIR, not only an arXiv preprint. Stronger "named, citable adversary."
- **Brown et al. 2022** = arXiv **2202.05520**, order Brown, Lee, Mireshghallah, Shokri, Tramèr,
  **FAccT 2022** (author order confirmed against the arXiv page itself; a secondary summary had it
  wrong).
- **Bagdasaryan, Poursaeed, Shmatikov** = **NeurIPS 2019**, pp. 15453–15462.
- **Novelty-search note:** the deployed mechanism is called **"client-level,"** not "user-level," so
  the repo's `lit/03` grep for "user-level" would never have found it. R1 re-ran the search for
  "client-level" against Tab-PE (2606.08259), MAPLE (2603.19258), PE-means (2606.00342), PCEvolve
  (2506.05407), SecPE (2510.10990): **zero hits.** Novelty holds, but under a check the repo had not
  actually run. Add "client-level" to the terminology sweep before submission.
- Still to resolve before submission (unchanged from `lit/02`): exact arXiv id for Charles et al.
  2024; the Amin/Kulesza/Muñoz-Medina/Vassilvitskii and Ganesh/Cohen-Addad entries.

## 7. Feasibility is slightly better than assumed

The `microsoft/DPSDA` library already implements both `"sample"` and `"client"` histogram modes
natively (`NearestNeighbors.compute_histogram`), so E1's harness can reuse real PE library code for
the `p=1` and `p=2` endpoints rather than being built from scratch; only intermediate `p` (e.g. 1.5)
needs a small custom patch. Lower engineering risk than `notes/08` assumed.

## What did not change

Propositions 1–3, the normalisation family, the diversity-floored mechanism, Claim 3's structure,
the outcome-robustness argument, and the data plan (controlled arm carries the weight; arXiv CC0
anchor) all stand exactly as in `ideas/10`. None of the fixes above touch the unconditional floor —
they retarget the exhibit, tighten one corollary, close one referee gap, and clean the bibliography.
