# The "Beyond PE" closing section, strengthened — a third, canonical instance

`ideas/12`'s J1 theme — *shape parameters that are sensitivity-neutral under record-level adjacency
become privacy knobs under user-level adjacency* — was verified against primary sources and upgraded
from two instances to three, with the new one being the most canonical of the set. This is a
near-zero-cost strengthening of the lead's closing paragraph. J2 (streaming PE) stays parked, but the
stated reason was wrong and is corrected here so it does not reach a paper draft.

## J1 — verified, and now three instances sharing one proof template

The pattern in each case: a disjoint assignment of records makes the mechanism's sensitivity
independent of the shape parameter at record level; under user-level adjacency a single user's
records can span many partitions, so worst-case sensitivity scales with how many, and a user-aware
assignment restores the record-level bound at the cost of forcing the parameter ≤ #users and making
partition sizes inherit the (heavy-tailed) per-user distribution — which breaks the exchangeability
the aggregation implicitly assumes.

| Mechanism | Shape parameter | Record-level sensitivity | User-level worst case | Source (verified) |
|---|---|---|---|---|
| **Private Evolution** | candidate-pool size `\|V\|` / `n_s` | independent of `\|V\|` (2/n) | `\|V\|` controls how far a user's votes spread → sets `d_u` | PE Converges 2506.08312, App. C.3 (`n_s` critical for convergence) |
| **DP-ICL** | # exemplar subsets `S` | Δ=√2, independent of `S` | user with `m` exemplars spans `min(m,S)` shards → Δ scales with `min(m,S)` | Wu et al. 2305.01639, **Theorem 3** (verbatim: "the sensitivity Δ is √2"); §6 future work names the `S` tradeoff, verbatim |
| **PATE** ★ new | # teachers `K` | 1, independent of `K` | user's records span `min(m,K)` teachers → Δ scales with `min(m,K)` | Papernot, Song, Mironov, Raghunathan, Talwar, Erlingsson, *Scalable Private Learning with PATE*, **ICLR 2018, arXiv 1802.08908** |

### Why PATE is the instance worth adding

- **Canonical.** PATE is the founding paper of the private-teacher-ensemble paradigm (PATE-GAN,
  G-PATE, and DP-ICL itself all descend from it) — far more cited than DP-ICL, and a mechanism a DP
  theorist on the committee already trusts. Citing it, rather than only DP-ICL, makes "this is a
  class" land.
- **Same argument, one paper earlier.** PATE's privacy analysis rests on the load-bearing claim that
  *a private sample taints at most one teacher due to disjointness of the teachers' training sets* —
  DP-ICL's Theorem 3 argument, verbatim, in the more famous predecessor. The record→user split
  follows immediately: `K` is a pure efficiency/utility knob at record level, a
  privacy-and-heterogeneity knob the instant a user's records span teacher partitions.
- **Not organizer turf.** None of PATE's authors (nor Boenisch, for the adjacent *Individualized
  PATE*) appear on the InfPriv organizer/speaker list.

**Verify at write-time:** author list and venue for 1802.08908 are confirmed via the arXiv abstract
page. The exact "taints at most one teacher" wording was confirmed via the PATE literature as
consistent across the 2017 original and the 2018 scale-up; re-confirm the exact sentence from the
paper's own text before quoting it. *Individualized PATE* (Boenisch et al., PoPETs 2023, arXiv
**2202.10517**) does the opposite move — it deliberately breaks disjointness via upsampling for
**per-record** budgets, not user-level aggregation — so it does not close this gap; but that
characterisation rests on search summaries, not a full-text fetch. Flag as ⚠️ until fetched.

### Verdict: fold in, do not spin off

Three verified instances is enough to state the class without over-claiming a taxonomy — add PATE to
the lead's closing section now. It is **not** a standalone paper as scoped: the content in all three
is the *same* one-paragraph pattern-matching corollary, with no analogue of the lead's Propositions
1–3 or Claim 3. A standalone note would need a genuinely new technical result on top — e.g. proving
the bound `Δ_user = min(m_u, S or K)` is **tight**, and quantifying the utility cost of the
user-aware fix against DP-ICL's or PATE's own published ablations (near-zero compute, an accounting
exercise). That is a legitimate, cheap *second* short note if bandwidth exists for the fast-track,
but it cannibalises reviewer attention if pitched as competing with the lead. Keep it as the close.

## J2 — still park, but for the corrected reason

`ideas/12` parks streaming PE citing He–Vershynin–Zhu (*Online DP Synthetic Data Generation*, arXiv
2402.08012) as evidence the adjacent area is crowded. Full-text fetch shows that reasoning is wrong:

- He–Vershynin–Zhu is **classical / fixed-domain** (dyadic hypercube partition + noisy counting, a
  Binary-Mechanism descendant), and — more decisively — it **does not model multi-participation at
  all**: its neighbouring relation swaps exactly one arriving point for the whole infinite horizon,
  i.e. one contribution per identity, ever. It is not addressing user-level streaming's problem shape.
- User-level continual release is, separately, **not a green field**: George, Ramesh, Singh, Tyagi,
  *Continual Mean Estimation Under User-Level Privacy* (arXiv **2212.09980**, IEEE JSAIT, Feb 2024)
  is exactly streaming + user-level (multi-participation), with an error bound already featuring the
  per-user participation-count `M_t` — just for mean estimation, not synthetic data. A 2026
  matrix-factorisation follow-up appears to exist (arXiv **2601.22320**) but was **not fetched** —
  ⚠️ verify before any citation.

**Corrected reason to park:** importing correlated-noise / MF machinery into a streaming user-level
setting is *not itself* novel (the George/Ramesh/Tyagi line already does it); the only possibly-novel
piece is the PE-specific claim that the transfer is non-trivial because PE's workload is its own
algorithm-generated, round-varying candidate pool rather than a fixed linear (prefix-sum) workload.
Settling that requires first formalising what "streaming PE" even means (per-round fresh corpus?
sliding window? cumulative corpus with round-varying pool?) — unscoped modelling with no citable
precedent, not a measurement. Correct reason to park with 6 days on the clock; update `ideas/12`'s
J2 premise before it reaches a draft, since a referee who knows the George/Ramesh/Tyagi line would
read "the area is unexplored" as false.

## Frontier note: private RAG is fully off-limits

Beyond the one paper `notes/06` already flags (2511.07637), the *whole* private-RAG / retrieval-top-k
angle is organizer-adjacent: Koga, Wu, Zhang, Chaudhuri, *Privacy-Preserving RAG with DP*, arXiv
**2412.04697** (Dec 2024) — **Ruihan Wu and Kamalika Chaudhuri are both organizers**. Treat any
top-k-as-record-neutral-sensitivity-parameter angle there as off-limits regardless of what the
full text says. (Also: DP-ICL-NN arXiv 2511.04332 = Koskela, Kulkarni, Zumot — Koskela is an
organizer; resolves `lit/02`'s "authors TBC" and flags caution.)
