# v4 — course correction toward niche, and a new lead

## Why v3 got demoted

The LLM-generated-DP-code audit is strategically well-placed but **saturation-risky**: DPrivBench's
future-work section announces it, which means every group reading that paper has the same idea.
Being scooped by the organizers' own follow-up is a live outcome. Dropping it to a backup.

The corrective: stop chasing hot surfaces (agents, guardrails, benchmarks) and go where the
population of researchers is small — **DP-theoretic details of inference-time mechanisms**. Most
LLM people won't touch the accounting; most DP theorists aren't reading PE implementations.

## Second casualty of this round

Individual/Rényi privacy filters for retrieval was my other candidate. **Dead** —
*Private-RAG: Answering Multiple Queries with LLMs while Keeping Your Data Private*
(arXiv 2511.07637) is by **Ruihan Wu, Erchi Wang, Zhiyuan Zhang, Yu-Xiang Wang** — four of this
workshop's organizers. Do not enter.

Also dead this round: per-record/outlier empirical privacy of DP synthetic data
(*Risk-Equalized DP Synthetic Data*, arXiv 2602.10232; *Phantoms and Disclosures*, arXiv 2606.16952).

---

# NEW LEAD — "One Person, One Vote: User-Level DP for Private Evolution"

## The gap, verified

Every Private Evolution paper uses **sample-level add/remove adjacency**. Verified directly:

- *Private Evolution Converges* (arXiv 2506.08312) — NN_histogram is Algorithm 4; the privacy proof
  invokes "an adaptive composition of T Gaussian mechanisms where each of them adds noise to a NN
  histogram with **ℓ₂ sensitivity 2/n**", citing Dong et al. 2022 Cor. 3.3. The paper
  **contains no discussion of user-level privacy or of individuals contributing multiple samples.**
- Same for PE-1 (2305.15560), Aug-PE (2403.01749), APIs-3 simulators (2502.05505), APIs-4 tabular
  (2606.08259), PE-means (2606.00342), MAPLE (2603.19258).

Meanwhile **the benchmark datasets PE is evaluated on are user-structured**:

| Dataset (Aug-PE) | Size | Natural user unit | Records per unit |
|---|---|---|---|
| Yelp | 1.9M reviews train | reviewer (`user_id` in Yelp Open Dataset) | heavy-tailed, often ≫1 |
| **OpenReview** | 8,396 ICLR-2023 reviews | **reviewer** | ~3–6 |
| PubMed | 75,316 abstracts | author | many |

So the field publishes ε=1 *per review* on a corpus where a person wrote six of them. The number
that appears in the abstract is not the number a data subject cares about.

User-level DP is thoroughly developed on the **training** side (Levy et al., *Learning with
User-Level Privacy*, NeurIPS 2021; Ghazi et al., *User-Level DP With Few Examples Per User*,
arXiv 2309.12500). It has **never been carried across to inference-time synthesis.**

## The technical core (this is what makes it more than an observation)

Let `c(S) ∈ Z^{|V|}` be the vote-count vector: each private sample votes for its nearest synthetic
candidate in the pool `V`. PE adds Gaussian noise calibrated to the ℓ₂ sensitivity of `c`.

- **Sample-level:** removing one sample changes one coordinate by one → `Δ_record = 1`. Constant,
  independent of everything.
- **User-level:** removing user `u` who contributed `k_u` samples changes `c` by `u`'s own vote
  vector `v_u`, where `Σ_j v_u[j] = k_u`. So

  `Δ_user = max_u ‖v_u‖₂`, and `√k_u ≤ ‖v_u‖₂ ≤ k_u`.

  The lower end is votes spread across `k_u` distinct candidates; the upper end is all `k_u` votes
  landing on one candidate. Gaussian noise scales linearly in Δ, so **the entire user-level cost of
  PE is one number: how concentrated a user's votes are.**

Define the **concentration ratio** `ρ_u = ‖v_u‖₂ / √k_u ∈ [1, √k_u]`.

### Two consequences, one negative and one positive

**Negative.** A user's samples are semantically similar — same reviewer's prose, same author's
abstracts, same person's photos — so they fall in the *same Voronoi cell* of the candidate pool.
Votes should **concentrate**, pushing ρ toward its maximum and the cost toward the full factor
`k`. This is the opposite of the DP-SGD case, where a user's per-example gradients partially
cancel. **Hypothesis: vote-based inference-time mechanisms are structurally worse under user-level
DP than gradient-based training-time ones, because correlated records concentrate rather than
cancel.**

**Positive.** The direct ℓ₂ analysis is *never worse* than invoking the group-privacy lemma
(which costs a factor `k` in ε plus a δ blow-up) and is better by exactly `1/ρ`. So the paper
delivers a strictly tighter user-level accountant for PE, not only a complaint.

### The mechanism: one person, one vote

Cap each user to at most one vote per candidate, `v_u[j] ← min(v_u[j], 1)`. Then

`‖v_u‖₂ ≤ √(#distinct candidates u hits) ≤ √min(k_u, |V|)`

— a **provable √k dependence instead of k**, from a two-line change to the histogram. Compose with
a total-contribution cap `C` (subsample `C` of a user's samples) for `Δ ≤ √C`.

### The design insight that only exists at user level

At sample level, the candidate-pool size `|V|` has **no effect on sensitivity** — it is always
2/n. At user level, `|V|` directly controls how much a user's votes can concentrate: a larger pool
spreads them. **`|V|` becomes a privacy knob, and PE's design space changes qualitatively.** No
existing PE paper has any reason to have noticed this.

## Why this idea is the right shape

- **Niche.** Intersection of two small populations: people who read PE's accounting, and people
  who care about privacy units. Not a surface anyone is racing on.
- **Straightforward.** The central figure is cheap: embed a user-structured corpus, run PE's
  nearest-neighbour assignment against a candidate pool, histogram `‖v_u‖₂ / √k_u`. Hours, not days.
- **Clear.** One question: what does a user's contribution actually cost in PE?
- **Defendable.** The sensitivity analysis is elementary and uncontroversial. Nothing rests on a
  contested empirical claim.
- **Robust to its own outcome.** If ρ is near `√k` → "PE's user-level cost is near worst case,
  here is a mechanism that fixes it." If ρ is near 1 → "user-level PE is far cheaper than group
  privacy suggests, here is the tighter accountant." **Both are publishable**, which is the single
  best property an idea can have with 7 days on the clock.
- **On-theme.** Topic 02, inference-only private synthetic data, squarely. Zinan Lin (PE's author)
  is an invited speaker; Honkela / Yu-Xiang Wang / Kamalika will read the accounting closely.

## Paper plan (4 pages)

1. **Intro.** PE is the flagship inference-time DP method. Its adjacency is sample-level. Its
   benchmarks are user-structured. State the mismatch with the OpenReview-reviewer example.
2. **User-level sensitivity of the NN histogram.** `Δ_user = max_u ‖v_u‖₂ ∈ [√k, k]`; the
   concentration ratio; comparison to the group-privacy lemma; the `|V|` knob.
3. **Measurement.** Distribution of ρ_u on Yelp / OpenReview / PubMed as a function of `|V|`,
   embedder, and iteration `t`. Central figure.
4. **One person, one vote.** Per-candidate cap + contribution cap `C`; sensitivity proof;
   utility-vs-ε curves at matched *user-level* ε against (a) naive group privacy and (b)
   record-level PE's reported numbers.
5. **Corollary for DP-ICL** (one paragraph). DP-ICL's privacy rests on partitioning exemplars into
   **disjoint** shards. A user with several exemplars lands in several shards and therefore
   perturbs all of them, so the shard argument gives record-level not user-level protection. Fix:
   user-aware sharding — assign all of a user's exemplars to one shard. Free extension, shows the
   problem is not specific to PE.
6. **Limitations.** ρ is dataset- and embedder-dependent; we measure, not prove, where real data sits.

## Execution risks
| Risk | Mitigation |
|---|---|
| Yelp Open Dataset licence / `user_id` availability | OpenReview arm needs only reviewer identity, which is in Aug-PE's own crawl structure; PubMed authors are public metadata. Three datasets means one can be dropped. |
| Full PE runs are API-expensive | The core measurement needs only the *embedding + nearest-neighbour assignment*, not generation. Full utility curves can use the smallest dataset (OpenReview, 8.4k) with a local open-weight generator. |
| "Isn't this just the group privacy lemma?" | No — the direct ℓ₂ analysis is strictly tighter by 1/ρ, and the capping mechanism changes the exponent. Must be stated in the abstract to pre-empt. |

---

## Alternate, kept warm

**Referent-level privacy: DP protects the author, not the subject.** In conversation logs and
agent traces the contributing record belongs to the *user*, but the sensitive content is often
about *third parties* they mention, who are not the privacy unit and whose attributes recur across
many records — exactly the population-level signal DP is designed to preserve. Same
"privacy unit is misaligned with the threat" family as the lead, different axis. Searched and no
direct match found, but it is fuzzier to operationalise than the PE work, so it stays as backup.

## Demoted, still viable
The DP-code audit (v3). Keep the verified bibliography — the Gilbert–McMillan and
Gaboardi–Nissim–Purser anchors are reusable.
