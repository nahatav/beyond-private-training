# Sweep #3 — reading other people's future-work sections

Method this round: stop searching for "is my idea taken?" and instead harvest the *stated open
problems* of the strongest adjacent work. Everything below was fetched and read as text, not
summarised from a search snippet.

## The headline finding, and it lands on our own lead

**Ponomareva, Xu, McMahan, Kairouz, Rosenblatt, Cohen-Addad, Guzmán, McKenna, Andrew, Bie, Yu,
Kurakin, Zadimoghaddam, Vassilvitskii, Terzis — *How to DP-fy Your Data: A Practical Guide to
Generating Synthetic Data With Differential Privacy*, arXiv 2512.03238 (Dec 2025).** ✅ verified
(title, full author list, date).

This is a Google/DeepMind practical guide, and it is the single most dangerous document for
`ideas/09`. It contains, inside its Private Evolution section, a subsection titled
**"User-level privacy unit adjustments"**. Paraphrasing its two substantive sentences:

- In the original algorithm each private example casts one vote (possibly split across its `k`
  nearest synthetic candidates), so the ℓ₂ sensitivity is 1 and the Gaussian noise is calibrated
  to that.
- When user-level privacy is required and a user contributes several samples, **the vote counts
  from each user can be normalised to sum to one in ℓ₂ norm**, which bounds the per-user
  sensitivity by one.

So the claim in `ideas/05` and `ideas/09` that user-level DP "has never been carried across to
inference-time synthesis" is **false as written and must be retracted.** A reviewer holding this
guide would sink the paper in one sentence.

### But read the rest of the guide and the position reverses

Three further passages, all verified in the fetched text:

1. **§5.1 (privacy unit for text).** After noting that most DP-synthetic-text papers omit the
   privacy-unit discussion entirely, the guide says DP-SGD has a large body of work on
   multiple-examples-per-user accounting (citing Charles et al. 2024), *while private evolution and
   DP inference* — in its words — "might be harder to adjust".
2. **§7.2 (user contribution bounding).** After contribution bounding, any example-level algorithm
   "like DP-SGD, Private inference or Private Evolution" can be used, but modifications to the
   accounting are still required — and the guide then states that improvements over the
   group-privacy lemma exist **for DP-SGD**. It names no such improvement for PE. The whole of §7.2
   is DP-SGD machinery: DP-SGD-ELS and DP-SGD-ULS (Charles, Ganesh, McKenna, McMahan, Mitchell,
   Pillutla, Rush 2024, *Fine-tuning large language models with user-level differential privacy*),
   plus contribution-bounding selection algorithms (Ganesh et al. 2025; Cohen-Addad et al. 2025).
3. **§5.1 closing.** The guide asserts that all the algorithms it describes "support example level
   privacy and can be also adjusted to account for group or user level privacy." That is an
   unverified claim about PE, offered without analysis, and it is exactly the claim to test.

**Net effect: the novelty claim moves, and gets better.** The gap is no longer "nobody noticed the
privacy unit." It is:

> The only stated user-level recipe for Private Evolution is two sentences in a practitioner guide,
> proposed without analysis, without experiments, and — as `ideas/10` shows — it silently changes
> what PE estimates. Meanwhile the guide's own authors flag PE as harder to adjust than DP-SGD and
> supply the DP-SGD improvement while leaving the PE one open.

That is a *better* setup than an unremarked gap, because it gives the paper a named,
citable adversary written by people in the field's centre of mass, and because "the recommended
fix is biased" is a sharper result than "there is no fix".

## Confirmed absent: user-level anywhere in the PE family

Fetched full text and counted case-insensitive occurrences of "user-level":

| Paper | arXiv | "user-level" hits |
|---|---|---|
| Aug-PE (text) | 2403.01749 | **0** |
| Private Evolution Converges | 2506.08312 | **0** |
| Tab-PE / APIs-4 tabular | 2606.08259 | **0** |
| DP-ICL | 2305.01639 | **0** |
| Evaluating DP Generation of Domain-Specific Text | 2508.20452 | **0** |
| Controlled Generation for Private Synthetic Text | 2509.25729 | **0** |
| SecPE | 2510.10990 | 4 (related work only) |
| **DP-fy guide** | **2512.03238** | **54** |

The concentration of every single mention in one practitioner guide, and none in any PE research
paper, is itself the finding: the practitioners know the problem exists and the research literature
has not touched it.

## Stated open problems harvested (verbatim-adjacent, condensed)

| Source | Open problem stated | Usable? |
|---|---|---|
| DP-fy guide §5.7 | **Online/streaming DP synthetic data** — both PE and DP inference are "potentially suitable" but, to the authors' knowledge, unexplored in the literature | Yes but see `ideas/12` — the *general* area is crowded |
| DP-fy guide §5.7 | Long-form DP synthetic text; DP synthesis without pretrained LLMs; better variation without prompt engineering | Not privacy-theoretic enough for this committee |
| DP-fy guide §7.3 | Data-dependent **packing** (e.g. packing embedding-similar documents together) creates inter-example dependencies that break per-example clipping | Training-side; out of scope |
| PE Converges (González, Fanti, Ramdas) §"Limitations and future work" | The analysed `Variation_API` is not the practical one; the rate suffers the curse of dimensionality | Theory-heavy, 7-day risk |
| PE Converges App. C.3 | In practice PE keeps a synthetic set of size `n_s ≠ n`, and setting `n_s` correctly is **critical for convergence** — a parameter their analysis cannot vary | **Yes** — this is the `\|V\|` knob of `ideas/09`, now with a citation saying it matters |
| Tab-PE App. E | Distance function is raw scaled attributes, no embedding or attribute weighting | Modality-specific, low surprise |
| DP-ICL §6 | The **efficiency–utility tradeoff in the number of exemplar subsets** is left for future work | **Yes** — user-level sharding turns this into a real tradeoff; see `ideas/12` |
| SynBench-style benchmark 2508.20452 §5 | Stronger MIAs and diagnostic auditing datasets for DP synthetic text | Crowded |

## New antecedents that must be cited (and that constrain us)

| Ref | Detail | Status |
|---|---|---|
| Liu, Suresh, Zhu, Kairouz, Gruteser — *Algorithms for bounding contribution for histogram estimation under user-level privacy* | arXiv **2206.03008**. User-level histogram estimation with per-user **clipping**: near-optimal choice of the contribution bound (2-approx bounded domain, log-approx unbounded), explicit bias–variance characterisation of the clipping threshold, and a post-processing **debiasing** step under mild distributional assumptions. | ✅ |
| Charles, Ganesh, McKenna, McMahan, Mitchell, Pillutla, Rush — *Fine-tuning large language models with user-level differential privacy* | 2024. DP-SGD-ELS (example-level sampling + contribution bounding) and DP-SGD-ULS (user-level sampling + per-user clipping). The training-side template our paper is the inference-side analogue of. | ✅ (via guide bibliography) |
| Amin, Kulesza, Muñoz Medina, Vassilvitskii — bounding user contributions | Cited by 2206.03008 as originating the bias–variance question for contribution bounds. | ⚠️ confirm venue/id |
| He, Vershynin, Zhu — *Online Differentially Private Synthetic Data Generation* | arXiv **2402.08012**. Continual-release synthetic data, near-optimal 1-Wasserstein rates. | ✅ |

**2206.03008 is the real threat to a naive version of our lead**, and it is Google again. It already
owns: user-level histograms, contribution bounding, the bias–variance tradeoff of the clipping
threshold, and debiasing. Any pitch of the form "we do user-level contribution bounding for a
histogram" is a transplant of their paper and will read as such.

What it does **not** own, and what `ideas/10` is built on:
- Their histogram has a **fixed, given domain**. PE's domain is the candidate pool, which the
  algorithm *generates and re-generates every iteration*.
- Their histogram **is the output**. PE's histogram is a **selection signal** feeding a generative
  loop; the error metric that matters is which candidates survive, not ℓ₁ histogram error.
- Consequently their clipping bias is a **one-shot** distortion. In PE it is applied `T` times to a
  population that the previous round's bias already shaped. Nothing in the user-level histogram
  literature has a feedback loop.

Those three differences are the paper.
