# Round 8 — synthesis of a six-agent adversarial review

Six independent reviewers were run in parallel against the whole idea board: two to attack the
existing material (the lead, and the backups/kills), four to scout for something better (venue
calibration + scoop patrol; adjacent CFP topics; the inference-time-DP frontier; a cold
fresh-idea generator). Each verified its load-bearing citations by fetching primary sources, not
search snippets, because the CFP desk-rejects on a single bad reference — and, newly confirmed this
round, on "significant unsubstantiated claims" too (see `notes/10`).

**The verdict is unanimous: keep the lead (`ideas/10`), do not pivot.** No reviewer found a fatal
flaw; the scoop patrol came back clean from seven angles; and nothing generated or revived beats the
lead on the three values that decide acceptance. What the review *did* produce is a stronger version
of the lead, a stronger closing section, two credible second-paper candidates, and a set of
corrections that de-risk the submission. Each is written up as its own file and committed
separately.

## The single most valuable finding

`ideas/10` frames the object of study as *two sentences in a practitioner guide* (the DP-fy guide,
arXiv 2512.03238). The lead-attacker (R1) found a strictly stronger anchor by reading the actual
`microsoft/DPSDA` GitHub history: the exact ℓ₂ per-user normalisation has been **shipped, named, and
parameterised** in the reference Private Evolution library since **2025-02-20** (commit
`25cdf854a22f...`, *"add the support of client-level DP"*, authored by **Zinan Lin** — PE's inventor
and this workshop's invited speaker), ten months before the guide. The mechanism is a documented
toggle (`vote_normalization_level="client"` vs `"sample"`), and the DP noise is added afterward at a
fixed pre-calibrated scale by code that **never inspects which normalisation mode is active**. That
is not a metaphor for "a channel the accounting silently omits" — it is the literal software
architecture. Retargeting the paper's primary exhibit onto that code is the highest-leverage change
available, and it is free. Full detail and all the fixes in `ideas/14`.

## The portfolio after review, scored on the three values

Values: **(1) novelty/contribution**, **(2) obvious InfPriv fit**, **(3) cheap & testable in ~5 days
on one GPU / outcome-robust**.

| Rank | Idea | File | (1) | (2) | (3) | Role |
|---|---|---|---|---|---|---|
| 1 | **PE user-level estimand shift (hardened)** | `ideas/14` | High — scoop-clean, now anchored on shipped code by the invited speaker | High — topic 2 + 4, exact house style | High — E1 ~1 GPU-hr floor; Props 1–3 unconditional | **The submission (09-07).** |
| 2 | **Beyond-PE: record-neutral parameters, +PATE** | `ideas/15` | Medium-High — 3 verified instances, one canonical | High — same venue | ~Zero — no new experiments | **Closing section of the lead.** Not standalone. |
| 3 | **Decoding truncation breaks the LLM exponential mechanism** | `ideas/16` | High — needed 3 chained full-text fetches to confirm nobody states it | High — "private prediction" named in CFP; AI-for-privacy | High — algebraically unfalsifiable core; no private data | **Best second submission** (fast-track 09-25 if bandwidth). |
| 4 | **Tab-PE inherits the unpatched label-distribution leak** | `ideas/17` | High — freshly found, not in repo before | High — topic 2, Honkela/Tobaben archetype | Highest — near-zero compute | **Cheapest alt / same-day Plan B.** Frame as measurement, not fix. |
| 5 | Constructive falsification (witness-checked DP judgments) | see `notes/10` §Plan-B | Medium-High | High — extends organizer's DPrivBench, topic 4 | High — CPU-only, ~1.5 days | **Zero-GPU pivot target** if the lead's Day-1 check is ambiguous. |
| 6 | Referent-level exposure vs mention-frequency (revived E) | see `notes/10` §Plan-B | Medium — thesis scooped, measurement open | Medium — topic 2/3 | ~1 GPU-day, needs crisp definitions | Backup. |
| 7 | Refusals are rejection sampling | see `notes/10` §Plan-B | Medium | High — topics 2/5 | High — few GPU-hrs, outcome-robust | Backup. |

**Dead / parked (do not revisit — evidence in `notes/10`):** B ε=0 baseline (arm-only; the zero-data
prior is already precedented for tabular by 2502.06555); F reconstruction bounds (needs a matching
attack that PE's self-modifying pool makes hard); G subsampled PE (a section, with one low-ε check to
run first); J2 streaming PE (park — but for the corrected reason); the batch-numerics cross-tenant
channel (killed by Quantamination 2604.26505 + it is systems-security turf).

## Why the lead wins the execution bet at T-6

Every scout that proposed an alternative reached the same conclusion against its own idea: the
alternatives are competitive on *territory* but lose on *execution*. The lead has an unconditional
mathematical floor (Propositions 1–3 hold regardless of any measurement), a decisive first
experiment that needs no generation, already-completed code checks, and a locked cut-order schedule.
Every alternative starts from zero engineering with only an empirical floor. With six days on the
clock, the de-risked plan wins — the alternatives are second papers and fallbacks, not replacements.

## What to do, in order

1. **Day-1, first hour:** apply the `ideas/14` retarget onto the DPSDA `vote_normalization_level`
   code and adopt the bibliography fixes. Free, highest leverage, and it strengthens the abstract's
   opening sentence.
2. Run E0/E1a as in `notes/09` — the `d_u/(k·m_u)` ratio decides diversity-tilt vs exponent-½, and
   (per R1) now also gates whether E2 is worth running at all.
3. Fold the PATE instance (`ideas/15`) into the closing section — three instances make it a class.
4. If, and only if, the lead's Day-1 check is genuinely ambiguous or E2 is cut and the paper feels
   thin: pivot to constructive falsification (zero-GPU, comparably strong floor) — the one true
   same-day fallback (`notes/10` §Plan-B).
5. After the 09-07 submission, if bandwidth allows, `ideas/16` (decoding truncation) is the
   strongest independent second paper for the 09-25 fast-track window.

Pointers: hardened lead → `ideas/14`; generalization → `ideas/15`; second papers → `ideas/16`,
`ideas/17`; corrections, ownership map, dead ground, and Plan-B triggers → `notes/10`.
