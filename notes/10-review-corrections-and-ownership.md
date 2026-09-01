# Round 8 corrections, ownership map, dead ground, and Plan-B triggers

Housekeeping outputs of the six-agent review that don't belong in an idea file but must not be lost.
Everything here was verified by fetching primary sources unless marked ⚠️.

## CFP corrections (verified against the live site 2026-09-01)

The live CFP (a JS SPA — a plain `curl`/WebFetch sees only the `<title>`; use a JS-capable fetch)
matches `notes/00-cfp.md` with **no substantive discrepancy**, plus two additive facts:

- **The LLM/citation policy is broader than the digest states.** Verbatim: *"Papers found to contain
  fabricated references, AI-generated citations, **or significant unsubstantiated claims** will be
  rejected automatically without review."* Not just references — unsubstantiated *claims* too.
  Tighten the internal review pass to catch overclaiming, not only citation hygiene. (This is why
  `ideas/14` §3 hedges the ε→∞ corollary and every file here flags "verify before writing.")
- **PC members review at most 3 submissions each** — a small PC; reviewer bandwidth/expertise-match
  is tight.
- Prior-work clause: NeurIPS 2026 **main-conference submissions** (not only accept/reject decisions)
  are eligible for the regular track, separately for fast-track.

"TPDP with an LLM skin" (`notes/06`) reconfirmed: MAPLE, DPrivBench, and *The Access–Similarity Lens*
are all on the live **TPDP 2026** program. The accepted form factor is one crisp claim + one
proof/measurement, no sprawl — and it spans pure-theory notes (two TPDP-2026 items: a user-level DP
**space lower bound** by Epasto–Lyu–Manurangsi; a **PE-as-learning-augmented-clustering** reframing
by McMillan–Talwar–Zhou, Apple) as well as empirical-with-a-hook. The lead's *shape*, not just its
content, matches.

## Scoop patrol — clean

No 2025–2026 paper treats user-level DP for PE, the estimand/bias of vote-normalisation, or the
PE/DP-ICL privacy-unit choice. Nearest neighbours, all verified and all distinct: PE-means
(2606.00342, Zinan Lin — no user-level content), PE-as-clustering (Apple, TPDP 2026), the user-level
space lower bound (2606-era, Google, not PE-specific), and Risk-Equalized DP Synthetic Data
(2602.10232 — record-level, DP-SGD generator, out of this workshop's inference-time scope; useful
only as a disparate-impact related-work cite). The lead's territory is open as of 2026-09-01.

## Ownership map — additions to `notes/06`'s table (avoid these)

| Territory | Owner (organizer/speaker) | Artifact (verified) |
|---|---|---|
| Private RAG / retrieval-top-k — **the whole line**, not one paper | Ruihan Wu + Kamalika Chaudhuri | *Privacy-Preserving RAG with DP*, arXiv **2412.04697** (in addition to 2511.07637) |
| DP-ICL with nearest-neighbour retrieval | Antti Koskela | arXiv **2511.04332** (Koskela, Kulkarni, Zumot) — resolves `lit/02`'s "authors TBC" |
| "LLM helps humans implement DP" (scaffolding) | Yu-Xiang Wang | **DPCheatSheet**, arXiv **2509.12590** (Chu, Tian, Wang, Jin) |

## Bibliography resolved this round

- DP-fy guide **2512.03238** → published **JAIR Vol. 86, Art. 17 (2026)**.
- Brown et al. → arXiv **2202.05520**, FAccT 2022, order Brown/Lee/Mireshghallah/Shokri/Tramèr.
- Bagdasaryan/Poursaeed/Shmatikov → **NeurIPS 2019, pp. 15453–15462**.
- F's antecedent (was never recorded with an id): Hayes, Mahloujifar, Balle, *Bounding Training Data
  Reconstruction in DP-SGD*, arXiv **2302.07225**, **NeurIPS 2023**.
- PATE → Papernot et al., **ICLR 2018, arXiv 1802.08908** (see `ideas/15`).
- Continual Mean Estimation Under User-Level Privacy → George/Ramesh/Singh/Tyagi, arXiv **2212.09980**,
  IEEE JSAIT Feb 2024 (see `ideas/15`).
- Terminology: the deployed PE mechanism is **"client-level,"** not "user-level" — add to every
  novelty grep (see `ideas/14` §6).
- Still ⚠️ before submission: Charles et al. 2024 arXiv id; Amin/Kulesza/Muñoz-Medina/Vassilvitskii
  and Ganesh/Cohen-Addad entries; arXiv **2601.22320** (MF continual mean estimation — search-only,
  fetch before citing); arXiv **2202.10517** (Individualized PATE — summaries only); SuperDP
  **2603.26215** PLDI-2026 acceptance (ACM DL record only, not on the arXiv page).

## Dead ground (record so round 9 doesn't rediscover)

- **Topic 1, agentic-privacy measurement — saturated** beyond `lit/01`: MAGPIE (2510.15186),
  AgentLeak (2602.11510), TAMAS (2511.05269), MuPPET (2606.23217), PiSAs (2607.05318),
  *Searching for Privacy Risks in LLM Agents via Simulation* (2508.10880). ≥6 in under a year.
- **Topic 3, auditing private ICL — closed in ~90 days:** SnapAudit (2511.13502, snapshot-based
  DP-ICL auditing) and ContextLeak (2512.16059, worst-case leakage in private ICL via canaries).
- **Batch-numerics cross-tenant channel — killed:** Quantamination (arXiv **2604.26505**) already
  shows the phenomenon as an attack, and `lit/01` already ruled the serving-layer side-channel
  cluster systems-security turf.
- **B (ε=0 baseline) — arm-only, weaker than assumed:** Swanberg et al. (arXiv **2502.06555**) *does*
  contain a genuine zero-private-data baseline ("Gemini data with no DP," prompted on schema only)
  for tabular — the technique is precedented, not just the qualitative point. B survives **only** as
  the lead's E3 (lift over the ε=0 prior degrading faster in the privacy *unit* than in ε, which
  neither 2502.06555 nor the guide's Table 10 makes). Not a standalone paper. Kairouz co-authors both
  2502.06555 and the guide.
- **F (reconstruction bounds) — dead for 6 days:** the antecedent (2302.07225) pairs its upper bound
  with a **matching attack**; PE's self-modifying candidate pool makes constructing a tight matching
  attack materially harder than the fixed-model DP-SGD case, and a bound without one reads as
  incomplete to Mahloujifar (invited speaker), the exact likely referee.
- **G (subsampled PE) — a section, with one check first:** subsampling amplification is strongest at
  small per-step ε, and the guide recommends PE for **ε<1** — so the regime where G is *not* null is
  PE's own recommended operating point. Run the low-ε `(q,T)` accounting check (≤1 hr, no generation)
  before writing the "likely null" sentence.
- **C — dead** (fixed `num_samples_schedule`, no private-data-dependent selection; `ideas/09`).
- **SecPE does NOT fully occupy idea E:** SecPE (2510.10990) protects **single-record** secrets
  (PII fields, rare words); its experiments **exclude** the multi-user-redundant-secret case, and its
  own limitations name the formal-definition gap as open. E's *thesis* is scooped (Brown 2022 /
  guide §5.1); E's *measurement* (referent protection vs mention-frequency) is not — see Plan-B.

## Plan-B triggers and roster

**Pivot only if** the lead's Day-1 `d_u/(k·m_u)` check (`notes/09`) is genuinely ambiguous, or E2 is
cut and the remaining paper feels thin. In that case, in order of preference:

1. **Constructive falsification** (zero-GPU, comparably strong floor, the true same-day fallback).
   Extend DPrivBench (organizer Erchi Wang, arXiv **2604.15851**, public dataset
   `github.com/erchiw/DPriv-Bench`): have LLMs emit a checkable `(D, D', event)` **witness** for each
   "violates DP" verdict, and grade the witness with an independent **sound** tester — **StatDP**
   (arXiv **1805.10277**, CCS 2018) / DP-Sniper (IEEE S&P 2021) — not another LLM, so the headline
   number can't be a hallucination. Central metric: judgment accuracy vs **witness-verified**
   accuracy per model. CPU-only, ~1–1.5 days. Distinct from the killed v3 (a witness is a few lines,
   not an implementation). Scoop risk: DPrivBench's future work gestures here (Erchi Wang in the
   room) — frame the smaller-than-implementation task + independent sound checker as the point.
   *(Resolve the repo's open TODO — does DP-Sniper/StatDP run on current Python? — before relying on
   it.)* A sibling (LLM-guided search seeding StatDP/DP-Sniper) shares the same suite and could ship
   as one note.
2. **Referent-level exposure measured vs mention-frequency** (revived E). Plant a synthetic
   third-party attribute in a controlled fraction of records by distinct synthetic users, run PE
   (or DP-ICL) across ε, measure recovery vs (ε, mention-frequency). ~1 GPU-day; permissibility
   already cleared in `notes/08`. Needs crisp operational definitions of "mention"/"recovery" up
   front to avoid reading as hand-wavy. Lead with: the paper closest to a mechanism (SecPE) declined
   to test this and calls the definition open.
3. **Refusals are rejection sampling** (S4 Idea A). The content-moderated LLM call inside PE's
   `Variation_API` / Aug-PE's paraphrase step is a rejection sampler; Awan & Rao (*Privacy-Aware
   Rejection Sampling*, arXiv **2108.00965**, JMLR 2023) proved rejection-sampler runtime leaks
   unless acceptance probability is data-independent — content moderation isn't. Measure refusal /
   retry-count stratified by content-sensitivity on a public moderation benchmark (ToxicChat
   **2310.17389**; RealToxicityPrompts **2009.11462**) via an open instruct model. A few GPU-hours;
   floor is the Awan–Rao reduction (needs no experiment). Scoop risk low-moderate (the concept is
   known to DP theorists but unconnected to the PE/Aug-PE/DP-ICL family).

For the **09-25 fast-track** as an independent *second* submission (not a fallback): `ideas/16`
(decoding truncation) is the strongest, then `ideas/17` (Tab-PE label leak).
