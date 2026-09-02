# Round 9 — opus adversarial review under the ~$300 compute ceiling

> **⚠️ SCOPE CORRECTION, 2026-09-02.** §1's compute guard-rails are **specific to the PE/InfPriv
> paper**, whose E1–E3 are NumPy/FAISS plus a small local generator. **They do not transfer to the
> safety line, and applying them to C9 is a hardware error.** `2606.30449` uses
> **Qwen2.5-Coder-32B-Instruct** (~64GB bf16), **Gemma-3-27B-IT** (~54GB) and **Llama-3.1-8B-Instruct**
> (~16GB). A **4090 (24GB) and an A6000 (48GB) cannot hold the 32B or the 27B in bf16 at all**, so
> "A6000/4090, never H200" is exactly backwards for C9: an **H100 80GB is close to the minimum**, and
> it is KV-limited for batched generation at ~13k context (~3–4GB of KV per sequence on the 32B, so
> roughly four concurrent sequences in the ~16GB left after weights). An H200 or 2×H100 is materially
> faster for the rollout phase. **Consequence for C9's ~$120 estimate:** at $2–3/hr an H100 buys 40–60
> hours, which is plausible for ~2,000 long-context rollouts but has no slack — which is why
> `notes/16` scopes the build to the **8B as primary** with 27B/32B as a transfer arm, and why pair
> yield is a gate rather than an assumption.

Three opus reviewers, run in parallel with a harder brief than round 8: price every idea against a
**~$300 Modal/RunPod ceiling** (less if paid APIs are needed), and test each idea against **published
papers that did a similar kind of thing** — to decide which idea maximises acceptance-per-dollar.
Every load-bearing citation was fetched to a primary source.

**Headline verdict: keep the lead as the 09-07 primary — money is not the binding constraint, and
the deeper precedent check confirms the core claim is scoop-clean.** But the round produced three
consequential results: a **desk-reject risk removed** from a second-paper candidate, a **flipped
second-paper ranking**, and a **free, high-leverage strengthening of the lead**.

## 1. Compute: the ceiling is never in play (O1)

- **The hidden-API fear is refuted.** Aug-PE (arXiv 2403.01749) ships a local open-weight path
  (OPT-6.7B / Vicuna-7B / Falcon-7B / LLaMA-2-7B / Mixtral via HF `transformers`; `scripts/hf/.../generate.sh`);
  GPT-3.5 is one option, not a requirement. The lead's primary exhibit (DPSDA
  `vote_normalization_level`) is pure NumPy/FAISS. **E1/E2/E3 run on a rented GPU with zero paid-API
  spend.**
- **Verified rates (2026-09-01):** RunPod A6000 / 4090 **$0.33–0.34/hr**; Modal A100-40 $2.10/hr,
  plus **$30/month free Starter credit**. ($300 ≈ 900 A6000-hours. Modal's "$10k academic" program
  is currently **paused** — do not rely on it.)
- **Per-idea cost (cheap GPU):** lead **E1 ≈ $0.3–1** (arguably CPU-free), **E2 ≈ $3–8**, **E3 ≈
  $8–16** → full lead **$12–30**. Decoding-truncation **$0–3**. Tab-PE **~$0 (CPU-only, no GPU)**.
  Constructive falsification **~$0 compute**. **The full lead *and* a second paper together cost
  <$50.**
- **The one landmine:** running E2 at Aug-PE's *full* Yelp scale (n_s=100k, T=20 → 27–139 GPU-hr/config)
  × 4 arms × several ε = 500+ GPU-hr ≈ $500–1000. **Guard-rails: keep `n_s ≤ ~2k`, `T ≈ 10`, one
  small corpus, on A6000/4090 (never H200).** Gate E2/E3 on E1's branch and on *time*, never on budget.
  *(PE only — see the scope correction at the top of this file. C9 needs an H100 80GB minimum.)*
- **One engineering risk, not a $ risk:** StatDP (`cmla-psu/statdp`) is Python-3.8 and ~unmaintained
  (~4 commits) — the constructive-falsification Plan-B's real cost is getting it (and DP-Sniper, 2021)
  to run on current Python. De-risk before committing to that fallback.

## 2. The lead vs. its precedents: scoop-clean, with new cite-obligations (O2)

The core claim (an **ℓ_p normalisation family of per-user vote vectors**, the **√d_u** diversity
tilt named as an inverse-participation ratio, applied to **PE**) is **scoop-clean** — verified. But
the *general* framing "a contribution bound changes the estimand, not just the variance" is **not**
new, and the lead must now cite its lineage or read as reinvention:

- **Amin, Kulesza, Muñoz-Medina, Vassilvitskii — "Bounding User Contributions: A Bias-Variance
  Trade-off in DP", ICML 2019 (PMLR v97:263–271)** — the *origin* of the estimand/bias framing. Cite
  as lineage. (Scalar cap, fixed domain, one-shot — not a scoop.)
- **Liu et al. 2206.03008 (ICML 2023)** — the single most dangerous precedent; rebuttal below.
- **FedNova (Wang et al., NeurIPS 2020, arXiv 2007.07481)** — the general "normalisation changes the
  target you converge to" result. Cite-and-distinguish (optimisation objective, not a DP measure).
- **Ganev, Oprisanu, De Cristofaro — "Robin Hood and Matthew Effects" (arXiv 2109.11429)** — most
  dangerous for Claim 3; rebuttal: it is a **DP-noise** effect (vanishes at ε→∞), one-shot, no
  functional form, no PE. (⚠️ re-confirm venue before citing.) Also **Andrey et al. 2606.13105**
  (Jun 2026) as concurrent.
- Complements, cite briefly: Charles et al. **2407.07737** (training-side template; resolves the
  `lit/02` ⚠️ id), Chua **2406.14322**, Levy **2102.11845**, Ghazi **2309.12500**; and the Google
  federated **location-heatmaps** (2111.02356), which normalises each user to bounded ℓ₁ = the lead's
  `p=1` endpoint and thereby *supports* the claim that ℓ₁ is the natural user-uniform choice.

**Add a fourth novelty distinction (d):** the operation is a **vote-vector ℓ_p normalisation (no data
dropped)**, not Amin/Liu's scalar clip-count — even on a fixed domain this is a different
sensitivity-control primitive with a previously unnamed bias signature. (a) generated domain and
(b) histogram-as-selection-signal remain the strongest separators; (c) the feedback loop is the
fragile one.

**Highest-leverage strengthening (free, theory, beats any extra experiment):** turn **Claim 3 into a
small formal contraction result** — a toy 2-region / 2-user model showing the homogeneous user's mass
under `p=2` is a contraction toward 0 across rounds, while under `p=1` it is a fixed point. This
converts the one fragile distinction (the compounding loop) from an empirical conjecture that
overlaps Ganev "in spirit" into the paper's genuinely new object.

**Form factor to imitate (Tobaben 2411.04680 archetype):** one identity (√d_u) + one measured curve
(E1) + a two-line fix (diversity floor). Under-claim the compounding unless it is made rigorous.

## 3. Alternatives reranked — decoding-truncation demoted (O3)

**New ranking: Lead > C (constructive falsification) > B (Tab-PE) > A (decoding-truncation).** This
flips round 8, which had A as the strongest second paper.

- **A — decoding-truncation (`ideas/16`): reframe-or-drop.** Its headline — "neither Amin et al. nor
  InvisibleInk nor the DP-fy guide states [the ε=∞ fact]" — is **false**: InvisibleInk (2507.02974)
  states it *verbatim* as the motivation for Top-k+ ("privacy loss … = ∞"). Shipping that claim is
  exactly the auto-reject-on-unsubstantiated-claims risk. The top-k-vs-top-p hair-split does not save
  it (DPS-MOZO 2501.19287 truncates to a *public* top-k; the subsampled exponential mechanism
  Lantz/Boyd/Page AISec 2015 samples a *data-independent* set; Tobaben uses a *public* label space —
  every finite-ε route is occupied, so **no cheap novel positive theorem remains**). Residual value:
  a practitioner config-audit, not a contribution. **`ideas/16` is corrected in place with this
  finding.**
- **B — Tab-PE label leak (`ideas/17`): cheapest fast-track second paper, with one must-verify.**
  Confirmed: Tab-PE = 2606.08259 (Tran, Backurs, **Zinan Lin — the invited speaker**, Reis, Xiong,
  Yekhanin); footnote 11 + Alg. 2 line 6 (`N(c)=N·|D_priv(c)|/|D_priv|`, no DP noise) verified;
  formal (ε,δ) covers only the noised NN-histogram. **New wrinkle:** footnote 11 + App. D.11 show the
  authors flagged it as an *assumption* and ran a robustness ablation — so B must claim **"unaccounted
  in the formal ε," not "unnoticed,"** and **must read App. D.11 / App. B.1 before writing** (single
  point of failure: if D.11 actually noises the class distribution and folds it into ε, B collapses).
  Same speaker-adjacency as the lead — measure-don't-build framing mandatory.
- **C — constructive falsification (`notes/10` Plan-B): the most primary-capable alternative / best
  zero-GPU pivot.** DP-Sniper already returns a `(D,D',event)`+ε witness; C's contribution is pairing
  LLM verdicts with an *independent sound checker* on an organizer's benchmark (DPrivBench) and
  reporting judgment-accuracy vs witness-verified-accuracy. The general LLM+sound-checker paradigm is
  precedented; the DP-specific witness-graded instantiation is not. Own the asymmetry (witnesses bite
  only on "violates"). CPU-only, outcome-robust — but starts from zero engineering and carries the
  StatDP Python-compat risk, so it does not beat the de-risked lead.

## 4. What to do (round-9 delta)

1. **Correct `ideas/16` now** — done in this round; it is no longer billed as the strongest second
   paper. Fast-track second paper is **B (Tab-PE)**, conditional on reading App. D.11/B.1.
2. **Spend the free win: formalise Claim 3** (toy contraction model) — this is the single most
   valuable addition and needs no compute.
3. **Add the cite-and-distinguish precedents** (Amin ICML 2019, Liu, FedNova, Ganev) and the fourth
   distinction (d) to the lead's related-work — pre-empts the "unacknowledged reinvention" and "you
   just redid Liu" attacks. Folded into `lit/02` (round-9 addendum) and flagged in `ideas/14`.
4. **Run on RunPod A6000/4090 community**, `n_s ≤ 2k`, `T ≈ 10`. Do the lead in full as *time*
   allows and build B for the 09-25 fast-track; the only scarce resource is human time, not GPU
   credits.
5. **Plan-B unchanged (C)** for the zero-GPU pivot, but resolve the StatDP/DP-Sniper Python-compat
   TODO first.
