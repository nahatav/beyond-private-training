# Alternative / same-day Plan B — Tab-PE inherits Aug-PE's unpatched label-distribution leak

The cheapest paper in the whole portfolio: near-zero compute, direct topic-2 fit, and the exact
Tobaben–Honkela "the accounting silently omits a channel" archetype `notes/06` says this committee
rewards. Idea D was killed for Aug-PE/text (documented "labels non-private" assumption; MAPLE, an
organizer's paper, privatises that metadata). The review found the **same assumption unpatched in a
newer, live mechanism — Tab-PE — that MAPLE's fix does not reach.**

## The gap (verified by full-text fetch)

**Tab-PE** — *DP Synthetic Data via Foundation Model APIs 4: Tabular Data*, arXiv **2606.08259** —
makes the identical assumption Aug-PE made, unpatched:

> "We assume class distributions are known as in (Lin et al., 2024; Xie et al., 2024)."

Its Algorithm 2 computes per-class synthetic sample counts directly from private proportions:

```
N(c) ← N · |D_priv(c)| / |D_priv|
```

with **no DP noise on the class distribution itself** — DP is applied only to the NN-histogram
scoring step. Releasing exact `N(c)/N` ratios is an unaccounted release of the private class
histogram, precisely the Tobaben–Honkela output-label-space side-channel transplanted to
inference-time tabular synthesis.

**MAPLE does not close it.** MAPLE (arXiv **2603.19258**, Chien, Hu, McKenna, Wu, Xu, Kairouz)
privatises exactly this metadata channel — but is **text-only** (OpenReview, bioRxiv), and its own
future work names the gap: *"A natural extension is to adapt the MAPLE framework to other data
modalities, including images, tabular data, and multimedia."* Tab-PE (dated after MAPLE, and citing
Aug-PE's assumption directly) does not acknowledge that MAPLE already flagged and fixed it for text.

## Why this fits, and the scoop trap to avoid

Direct hit on topic 2 (inference-only private synthetic data) with a built-in sympathetic reader:
Chien, an organizer, already established with MAPLE that this channel is real and worth privatising.

**The trap:** MAPLE's stated future work names the tabular case — so *building the fix* is Chien's
announced plan and would repeat the v3-vs-DPrivBench scoop that the repo already learned to avoid.
**The escape is the same lesson `ideas/05`→`ideas/10` learned with the DP-fy guide: do not build the
fix, measure and state the leak precisely.** Cite MAPLE's own fix as proof the channel is real and
MAPLE's own future-work line as proof the authors know tabular is unaddressed. This is a
measurement/accounting paper, not an engineering one — the "near-zero compute, accounting argument
plus a small demonstration" profile idea D always had.

## Decisive experiment (no generation, mostly reading)

1. Confirm from Tab-PE's algorithm listing (and public code if released) that `N(c)` and any category
   vocabulary are computed directly from `D_priv` with no noise. *(A five-minute check of whether
   Tab-PE ships reference code should precede committing — access friction, not compute, is the risk
   here.)*
2. One-paragraph accounting argument: releasing exact `N(c)/N` for `|C|` classes leaks up to
   `log₂(multinomial coefficient)` bits beyond the declared budget; with small `|D_priv|` (Tab-PE's
   own target regime) this is not negligible relative to the per-cell counts.
3. Optional, cheap toy demo: given only the released `N(c)` and public total `N`, show how tightly
   the true class histogram is pinned down as a function of `|D_priv|`.

Under a day, most of it reading; no GPU for the core claim.

## Outcome-robustness & role

The accounting argument is the floor and needs no experiment; the demo only sizes the leak. Ranked as
the review's **#1 alternative** (highest novelty-per-hour, cheapest, cleanest fit) and the **same-day
Plan B** if the lead's Day-1 `d_u/(k·m_u)` check comes back genuinely ambiguous. Its one weakness
relative to the lead is scoop-adjacency to an organizer's stated plan, fully mitigated by the
measure-don't-build framing above.

## Verify before writing

Re-confirm Tab-PE's arXiv id / title / the exact "class distributions are known" quote and Algorithm
2's `N(c)` expression from the live paper; and MAPLE's exact future-work sentence. Check whether
Tab-PE has released code (affects whether step 1 is a code read or an algorithm-listing read). One
negative result worth recording from the review: **DP-ICL has no analogous unaddressed label-space
channel** (its histograms are noised before release; partitioning is not shown to be
distribution-aware pre-noise) — do not spend time there.
