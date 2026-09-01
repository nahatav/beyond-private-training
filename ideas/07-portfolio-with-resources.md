# Idea portfolio with resource costs

Novelty status is **verified by search**, not assumed. Anything marked *needs code check* can be
confirmed or killed in under an hour and should be, before committing.

Shared baseline stack for everything PE-related:
`AI-secure/aug-pe` + `microsoft/DPSDA` · a sentence-embedding model (all-MiniLM / gte / stella,
<1 GB) · a local generator (Qwen3-8B or similar under vLLM) · BERT-base for downstream utility.
Nothing here needs more than one workstation GPU.

---

## A. User-level DP for Private Evolution — **"One Person, One Vote"** ★ recommended

**Gap (verified).** Every PE paper uses add/remove-one-*sample* adjacency; *Private Evolution
Converges* states ℓ₂ sensitivity 2/n and contains no mention of users contributing multiple
samples. PE's own benchmarks are user-structured. User-level DP is mature on the training side
(Levy et al. NeurIPS 2021; Ghazi et al. 2309.12500) and never crossed over.

**Core.** `Δ_user = max_u ‖v_u‖₂ ∈ [√k, k]` — the whole cost is vote concentration. Direct ℓ₂
analysis beats the group-privacy lemma by 1/ρ; per-candidate vote capping forces √k; the candidate
pool size `|V|` becomes a privacy knob that does not exist at record level.

**Resources**
- *Core measurement (the central figure):* embeddings + nearest-neighbour assignment only. **No
  generation.** ~1 GPU-hour, or CPU-feasible. This is the decisive experiment.
- *Utility curves:* real PE runs — T≈10–20 iterations × ~10–20k generations, local 8B under vLLM.
  ~2–4 GPU-hours per run; ~12–20 runs across (record-level / group-privacy / capped) × ε values →
  **1–2 GPU-days**.
- *Datasets:* **Yelp Open Dataset** (`user_id` present — but the Aug-PE *processed* Yelp from Yue
  et al. 2023 may have stripped it, so plan to re-derive from raw). **PubMed** (author identity via
  Entrez, public).
  ⚠️ **OpenReview will not work for this arm** — ICLR reviews are anonymous, so there is no
  reviewer identity to group by. Do not build the plan on it.
- *Wall-clock:* measurement day 1; utility curves days 2–4.

**Outcome-robust:** yes, both directions publishable. **Scoop risk:** low.

---

## B. The privacy-free baseline — how much of PE's utility is the public prior?

**Gap.** PE papers report *absolute* downstream accuracy at each ε. Nobody reports the **ε=0
baseline**: prompt the same foundation model to generate the same kind of data with **zero access
to the private corpus**. The correct quantity is *lift over that baseline*, and it is never shown.
This is the inference-time analogue of the public-pretraining critique in DP-SGD.

**Novelty status.** Open for **text**. Adjacent for tabular: *Is API Access to LLMs Useful for
Generating Private Synthetic Tabular Data?* (arXiv 2502.06555 — Swanberg, McKenna, Roth, Cheu,
Kairouz, Google) finds API access "does not always improve" over established baselines — but their
baselines are DP methods that still consume private data, not a zero-private-data prior. Must cite
prominently and state the delta in the abstract.

**Resources.** Generation-heavy but conceptually trivial: one extra arm per dataset. **~1 GPU-day**
total. Datasets: Aug-PE's own three, all public, no user IDs needed → **lowest access friction of
anything here.**

**Outcome-robust:** yes. Small lift → methodological correction. Large lift → a validation of PE
that the field currently cannot point to. **Scoop risk:** low–medium (the Google group is circling).

---

## C. Unaccounted model selection on private validation splits

**Gap.** Aug-PE's own data splits carve a **validation set out of the private corpus** (Yelp 5,000;
OpenReview 2,798; PubMed 14,423). If iteration count, thresholds, or hyperparameters are chosen by
looking at that validation set, the released synthetic data depends on private data beyond the
accounted budget. The generic hazard is known (Rényi-DP tuning 2110.03620; *Revisiting
Hyperparameter Tuning with DP* 2211.01852) but **has never been measured for PE**.

**Status.** *Needs code check* — read the aug-pe training loop and confirm how the best iteration
is selected. One hour. If selection is on a public/held-out split, this idea dies cleanly.

**Resources.** ~0.5 GPU-day if it survives the code check. Quantify utility inflation from
data-dependent iteration selection vs. a fixed-T protocol; propose DP selection as the fix.

**Outcome-robust:** no — it dies if the code selects honestly. **Do the check first.**

---

## D. Does class-conditional PE release the private label distribution?

**Gap.** Aug-PE does conditional generation on attributes drawn from the private corpora (Yelp:
rating + business category; OpenReview: recommendation + area). Two things must be checked: is the
**attribute vocabulary** derived from private data, and are the **per-class sample counts** taken
from the private class histogram without noise? Either would be an unaccounted release — precisely
the Tobaben–Honkela "output label space is a side channel" finding transplanted to inference-time
synthesis.

**Status.** *Needs code check.* The Aug-PE README is silent on all of it. **Highest
information-per-hour item in this document** — one hour of reading either kills it or hands you a
concrete, Honkela-genre finding about a method Apple has deployed.

**Resources.** If real: near-zero compute. It is an accounting argument plus a small demonstration.
**Cheapest possible paper here.**

**Outcome-robust:** no — binary. But the check is an hour.

---

## E. Referent-level privacy — DP protects the author, not the subject

**Gap.** In conversation logs and agent traces the contributing record belongs to the *user*, but
the sensitive content is frequently about *third parties they mention*. Those people are not the
privacy unit, and their attributes recur across many records — exactly the population-level signal
DP is designed to preserve. So a correct, honest ε over conversational data provides essentially
no protection to the most exposed party.

**Novelty status.** No direct match found. Nearby but distinct: CIMemories and ConfAIde
(Mireshghallah/Chaudhuri) treat this normatively via contextual integrity, not as a privacy-unit
question.

**Resources.** Needs a conversational corpus with third-party mentions. Synthetic-canary construction
is the clean route: plant known third-party attributes at controlled frequency, run DP synthesis,
measure recovery vs. ε and vs. mention-frequency. **~1 GPU-day.** No restricted data.

**Outcome-robust:** yes, but fuzzier to state crisply than A. **Scoop risk:** low.

---

## F. Reconstruction bounds for inference-time DP

**Gap.** Mahloujifar's *Bounding Training Data Reconstruction in DP-SGD* has no inference-time
analogue. PE runs at ε≈10–20 in practice, where DP says little, but *reconstruction* is a much
weaker adversarial goal and PE has extra structure: output samples come from a public generator, so
reconstructing a private sample requires that generator to emit it.

**Resources.** Mostly derivation; a small empirical check. Speaks directly to an invited speaker.
**Risk: theory papers do not compress well into 7 days.** Park unless the maths falls out fast.

---

## G. Subsampled Private Evolution — likely a null result

PE uses the **full** private set every iteration; no amplification-by-subsampling is applied
(σ = 4√(T log(1.25/δ))/(nε), advanced composition, no amplification term). Tempting free lunch —
but to first order the gain cancels: subsampling at rate q shrinks the vote signal by q while
amplification buys back roughly the same factor, leaving SNR ∝ nε/√T, independent of q. The real
question is whether the freed budget buys enough extra **iterations** T to matter, given that PE
Converges shows utility is strongly T-dependent.

**Verdict:** a good *section* of paper A, a weak standalone paper. **~0.5 GPU-day** to settle.

---

## Killed this round (recorded so they are not revisited)

- **Refusal/abstention channel in privacy guardrails** — *Privacy Side Channels in ML Systems*
  (Debenedetti et al., arXiv 2309.05610, USENIX Sec 2024) already shows memorization filters create
  a side channel enabling near-perfect membership inference. A transplant to CI guardrails reads
  as derivative.
- **GPU / low-precision DP noise sampling** — the floating-point line is thoroughly worked:
  Mironov CCS 2012; *Are We There Yet? Timing and Floating-Point Attacks on DP Systems*
  (2112.05307); *Precision-based attacks and interval refining* (2207.13793); NumPy/PyTorch/Go all
  documented as susceptible; OpenDP/MPFR and Google discrete-sampling mitigations shipped.
- Everything in sweeps #1 and #2.

---

## Resource summary

| Idea | Compute | Datasets | Access friction | Days | Robust to outcome |
|---|---|---|---|---|---|
| **A. User-level PE** | ~1 GPU-hr core; 1–2 GPU-days full | Yelp (raw, for `user_id`), PubMed+Entrez | low–med (⚠ not OpenReview) | 4 | **yes** |
| **B. ε=0 baseline** | ~1 GPU-day | Aug-PE's three, as-is | **lowest** | 2–3 | **yes** |
| C. Selection leakage | ~0.5 GPU-day | Aug-PE's three | low | 2 | no (code check first) |
| D. Label-space release | ~0 | none | **none** | 1 | no (code check first) |
| E. Referent-level | ~1 GPU-day | canary construction | low | 3–4 | yes |
| F. Reconstruction bounds | minimal | — | none | ? | derivation risk |
| G. Subsampled PE | ~0.5 GPU-day | Aug-PE's three | low | 1 | folds into A |

**Nothing here needs more than one workstation GPU.** The binding constraint is dataset access
friction and the 7-day clock, not FLOPs. Explicitly avoided: anything requiring MIMIC/PhysioNet
credentialed access (CITI training alone exceeds the timeline).

## Recommendation

Spend the **first hour** on the D and C code checks — they are nearly free and one of them may
hand over a cheaper paper than the lead. Regardless of outcome, build **A**, with **G** as a
section and **B** as the natural second arm if time allows. A and B are the only two that are
robust to their own results, which is what matters most with seven days left.
