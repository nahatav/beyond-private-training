# Shipping InfPriv — what is actually left

**Deadline: 2026-09-07 AoE, strict.** Today is 2026-09-02, so **5 working days**. This file exists
because `ideas/24`'s venue plan dropped the Sep 7 row without deciding against it (`notes/13`), and
because "the paper is nearly written" is a claim nobody had converted into a task list.

**What "ship" means here:** `ideas/10` + `ideas/14` are a complete paper *design* — thesis,
propositions, mechanism, experiment plan, referee rebuttals, and a paper skeleton in `notes/09`. What
does not exist is **a LaTeX file, a single line of code, or one number**. The remaining work is
execution and verification, not research. Nothing below reopens a research question.

## Why this is worth 5 days

- **The floor is unconditional.** Propositions 1–3 are elementary algebra. No experimental outcome
  can invalidate them, so a complete short paper exists even if every measurement is boring
  (`notes/09`).
- **Survived two adversarial rounds** (6 sonnet agents, then 3 opus) with no fatal flaw and a clean
  scoop patrol.
- **~$30, ~1 GPU-hour for the decisive figure**, which needs no generation at all.
- **It does not compete with C9 for a single hour that matters.** C9 cannot be submitted anywhere
  before Sep 19 at the earliest, and realistically 6–10 weeks out (`notes/13`).
- The counterfactual is **no submission until roughly November**.

---

## Pre-flight — no compute, do these first (~half a day, today)

These are the six things `ideas/14` and `ideas/18` left as explicit write-time obligations. Every one
is a desk-reject risk under the CFP's strict policy, which auto-rejects on fabricated citations **and
on significant unsubstantiated claims** (`notes/00`).

| # | Task | Source | Done |
|---|---|---|---|
| 1 | **Re-verify the DPSDA exhibit against live `main`** — `pe/histogram/nearest_neighbors.py`, the `vote_normalization_level="client"` parameter and its docstring, `pe/dp/gaussian.py` never inspecting the mode, and commit `25cdf854a22f…` (2025-02-20, Zinan Lin). The round-8 evidence dumps were scratch and **were deleted**; re-fetch fresh. This is the paper's primary exhibit. | `ideas/14` §1 | ☐ |
| 2 | **Hedge the ε→∞ corollary** to what is actually proven. Propositions 1–3 are single-round estimand statements and do not establish that PE-with-normalisation has a fixed point at all. Rephrase to *"if PE-with-normalisation converges, that fixed point cannot be µ_S, since the per-round target already differs at the algebraic level (Prop. 2); [PE Converges] covers only the unnormalised histogram."* | `ideas/14` §3 | ☐ |
| 3 | **State the multi-owner assignment rule** for the arXiv anchor — one identity per record (e.g. first author only), citing the DP-fy guide's own §7.2 flag about multi-owner documents. One sentence; it is the first question a DP-theorist referee asks. | `ideas/14` §4 | ☐ |
| 4 | **Run the "client-level" terminology sweep.** The deployed mechanism is called *client-level*, not *user-level*, so `lit/03`'s original grep could never have found it. R1 re-ran it against Tab-PE, MAPLE, PE-means, PCEvolve, SecPE → zero hits. Re-run before submission with R3's positive control in the same batch. | `ideas/14` §6 | ☐ |
| 5 | **Resolve the last ⚠️ bibliography rows**: the exact arXiv id for Charles et al. 2024; the Amin / Kulesza / Muñoz-Medina / Vassilvitskii entry; Ganesh / Cohen-Addad. ⚠️ means do-not-cite, so these either become ✅ or come out of the draft. | `ideas/14` §6, `lit/02` | ☐ |
| 6 | **Write Claim 3 as a small formal contraction result** — a toy 2-region / 2-user model where the homogeneous user's mass contracts toward 0 across rounds under `p=2` and is a fixed point under `p=1`. Zero compute, and `ideas/18` judged it the single highest-leverage strengthening available: it shores up the one fragile novelty distinction (the feedback loop) whether or not E2 ever runs. | `ideas/14` round-9 additions | ☐ |

Two related-work obligations for the draft, same source: add novelty distinction **(d)** — this is a
vote-vector ℓ_p normalisation that **drops no data**, unlike Amin/Liu's scalar clip-count — and
cite-and-distinguish **Amin et al. ICML 2019**, **Liu 2206.03008**, **FedNova (2007.07481)** and
**Ganev (2109.11429)**, whose rebuttals are already written in `ideas/18` §2.

---

## Schedule — 5 days, with the cut lines fixed now

Adapted from `notes/09`, which was written for a 6-day run. The lost day comes out of E2, which was
already first on the cut list.

| Day | Work | Compute | Droppable |
|---|---|---|---|
| **Sep 2 (today)** | Pre-flight table above. Start the LaTeX skeleton in the NeurIPS template. | none | no |
| **Sep 3** | **E0** code checks: confirm the vote construction against `dp_counter.py`, and determine what the noisy-count threshold-and-subtract does once per-user normalisation makes counts non-integer. Then **E1a** — the `d_u/(k·m_u)` ratio on the controlled arm. **Headline decided by end of day.** | ~1 GPU-hr | no |
| **Sep 4** | **E1 full** — re-weighting curves `w_u(p)` vs `d_u` for `p ∈ {1, 1.5, 2}` plus record-level, swept over within-group coherence and over `\|V\|`. Real anchor: arXiv abstracts by author (CC0). **Central figure done.** | ~1–2 GPU-hr | no |
| **Sep 5** | **E2** compounding (4 arms × `T≈10`) **only if E1a lands in the strong branch** — otherwise **E4**, the controlled sweep. See the branch rule below. | ~2–4 GPU-hr/arm | yes |
| **Sep 6** | Write. Four pages, to `notes/09`'s skeleton. | none | no |
| **Sep 7** | Internal review pass against the CFP's unsubstantiated-claims policy, then submit to OpenReview (double-blind). | none | no |

**E3 (utility at matched user-level ε) is cut now.** It was already second on `notes/09`'s cut list
and there is no day for it.

### The one measurement that picks the paper — decide it Sep 3, not Sep 6

Measure `d_u / (k·m_u)`: how far a user's effective vote diversity sits below its ceiling.

| Outcome | Headline |
|---|---|
| `d_u ≪ k·m_u` (users cluster) | **Diversity tilt** — the recommended recipe weights users by the square root of their semantic diversity. The strong version. |
| `d_u ≈ k·m_u` | **Exponent ½** — the recipe is a covert contribution-scaling rule sitting between the two named privacy units, adopted without comment. Weaker headline, identical equations, still a correction to the record. |

Both branches are writable, so this risks the headline and never the submission.

**And the branch also decides Sep 5.** `ideas/14` §5: Claim 3 / E2 needs **cross-user variation in
`d_u`** to have any content. In the weak branch there is little heterogeneity for a feedback loop to
amplify, so E2 returns an *uninformative* null rather than a smaller effect. **If E1a lands weak,
E2 is dropped and Sep 5 goes to E4**, whose controlled arm can manufacture the heterogeneity the real
corpus lacks. Decide at the end of Sep 3, per `notes/09`'s cut logic.

---

## Standing constraints that bind this build

- **Compute guard-rails** (`ideas/18` §1): local open-weight generator, **no paid API**; RunPod
  A6000/4090; **`n_s ≤ 2k`, `T ≈ 10`** — never at Aug-PE's full Yelp scale. Full lead is **$12–30**.
- **Data** (`notes/08`): controlled arm needs no identities; real anchor is arXiv abstracts grouped by
  author (CC0). Yelp stays dropped; OpenReview cannot support a user-level arm (anonymous reviewers).
  Public datasets only, no experiments involving real people, nothing person-specific reported.
- **Feasibility is better than `notes/08` assumed** (`ideas/14` §7): `microsoft/DPSDA` implements both
  `"sample"` and `"client"` histogram modes natively, so E1's harness reuses real PE library code for
  the `p=1` and `p=2` endpoints. Only intermediate `p` (e.g. 1.5) needs a small patch.
- **Framing discipline** (`ideas/14` §2): the paper examines code committed by **Zinan Lin, an invited
  speaker at this workshop**. Frame `"client"` mode as a principled engineering choice — Prop. 3
  proves `p=2` is the SNR-optimal member of the admissible family — with an under-examined
  consequence. Never as an error. This is both the diplomatic and the mathematically honest reading.

## The single largest risk

Not compute, not novelty, not the clock. It is that **hour one has never happened** — no DPSDA clone,
no embedding run, no `d_u` ever computed (`notes/12` R12, gate G3). If E0 on Sep 3 finds that the
noisy-count threshold-and-subtract interacts badly with non-integer per-user counts, that is a real
finding and it surfaces on day one, with four days left and two writable branches. Discovering it on
Sep 6 is the failure mode this schedule exists to prevent.
