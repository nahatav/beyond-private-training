# Second paper — default decoding silently breaks the LLM-as-exponential-mechanism guarantee

> ## ⚠️ ROUND-9 CORRECTION — DEMOTED TO "REFRAME-OR-DROP". DO NOT WRITE AS-IS.
>
> An opus precedent-check fetched **InvisibleInk (2507.02974)** in full and found it states this
> file's headline fact **verbatim**, as the motivation for its Top-k+ decoding:
> *"a token … can 'jump out' of the top-k set … its probability … goes from a non-zero value to a
> zero value, leading to a privacy loss of … = ∞."*
>
> So the central claim below — *"neither Amin et al. nor InvisibleInk nor the DP-fy guide states
> this"* — **is false.** Shipping it would be exactly the "significant unsubstantiated claim" the CFP
> auto-rejects on. The round-8 sonnet scout that produced this file mis-assessed InvisibleInk; the
> opus round caught it.
>
> The top-k-vs-top-p hair-split does **not** rescue the novelty: the ε=∞ argument is identical for a
> token leaving the nucleus, and every finite-ε fix is already occupied — **Top-k+** (2507.02974),
> **DPS-MOZO** (2501.19287, truncates to a *public* top-k set), the **subsampled exponential
> mechanism** (Lantz, Boyd, Page, AISec 2015; data-independent set), and Tobaben et al. (2411.04680,
> public label space). **There is no cheap novel positive theorem left** (the only open lemma — exact
> finite ε of renormalised top-p + uniform floor as a function of nucleus mass — is a minor smoothing
> re-derivation of known mixing bounds, too thin for this venue).
>
> **What survives:** a practitioner config-audit ("HF/vLLM ship `top_p=0.9`; a deployment following
> the guide's citation trail inherits an unaccounted violation") — useful, but a **corollary of
> InvisibleInk's stated result, not a contribution.** If pursued at all, it must **cite InvisibleInk
> as the known ε=∞ result** and claim only the audit + empirical leak-size — and even then it is the
> weakest item in the portfolio. Fast-track second paper is now **`ideas/17` (Tab-PE)**; see
> `ideas/18` for the reranking. The text below is preserved as the round-8 version for the record.

---

The strongest independent candidate the review produced. Same winning shape as the lead — *a named,
credible source states or nearly states the fix, but nobody checks whether it transfers to the
deployed mechanism* — but on a **different mechanism** (private prediction, not Private Evolution), so
it does not compete with the lead for reviewer attention or turf. Best used as a second submission
for the **09-25 fast-track** window if there is bandwidth after 09-07, not as a fallback for the
lead. All citations below were established by direct full-text fetches this round.

## Thesis (one sentence)

The "private prediction" line realises the exponential mechanism by sampling directly from an LLM's
temperature-scaled next-token softmax, which is provably correct **only under full support over the
vocabulary** — but every mainstream serving stack (HuggingFace `generate`, vLLM, OpenAI-compatible
APIs) ships **nonzero-truncation decoding by default** (top-p / top-k), and truncation makes the
*worst-case* privacy loss of the deployed mechanism **infinite**, not merely larger: any token a
neighbouring dataset would push outside the truncation set gets probability exactly zero, so the
max-divergence ratio `max_x P(x)/Q(x)` is unbounded.

## The gap, and why nobody has stated it

- **Foundational target (fetched):** Amin, Bie, Kong, Kurakin, Ponomareva, Syed, Terzis,
  Vassilvitskii, *Private prediction for large-scale synthetic text generation*, arXiv **2407.12108**
  (Jul 2024). Builds on "the equivalence between the softmax layer for sampling tokens and the
  exponential mechanism." Full-text grep: **zero** occurrences of "top-p", "nucleus", "top-k"
  (outside an unrelated citation), "full support" / "full vocabulary." The full-support requirement
  is implicit in the exponential-mechanism framing and never checked against how sampling is run.
- **SOTA successor (fetched):** Vinod, Pillutla, Thakurta, *InvisibleInk*, arXiv **2507.02974**,
  **NeurIPS 2025**. Aware that naive full-support sampling is costly — but addresses it **for
  utility**, via **Top-k+** decoding (a fixed-size, data-independent superset trick that samples
  "without additional privacy cost"). Crucially, Top-k+'s retained-set size is fixed a priori, which
  is exactly what makes its superset argument go through; **top-p's retained-set size varies
  continuously with the private-conditioned logit shape** (peaked → small nucleus, flat → large), so
  a naive substitution of default top-p for Top-k+ does **not** inherit their proof. "nucleus" — 0
  hits; "top-p" — 1 hit, a false-positive table label.
- **The one place it is discussed (fetched, and it points the wrong way):** the DP-fy guide
  (2512.03238) cites Kurakin et al. 2023 (arXiv **2306.01684**) as advocating "temperature sampling
  with T=1.0 and no top-k or top-p restrictions." Kurakin et al.'s mechanism is **DP-SGD fine-tuning
  of the weights**, after which *any* decoding is pure post-processing and cannot affect the formal
  guarantee — so their "no top-p" is a **statistical-fidelity** choice, not a privacy requirement,
  answering a question that does not arise in the inference-time exponential-mechanism setting. The
  guide juxtaposes the two lines without noticing they answer different questions, and **neither the
  guide nor either primary paper states the decisive fact**: for the inference-time-only (no
  fine-tuning) private-prediction line, deploying via default decoding is not a quality regression,
  it is an unbounded, unaccounted privacy violation.

The gap took three chained full-text fetches to surface — which is why a search-snippet pass would
conclude "top-p is a known issue" and drop it, and likely why it is still open.

## Why it fits InfPriv

Squarely "Inference-only Private Synthetic Data — **private prediction**," named explicitly in the
CFP topic list, and directly the "AI for Privacy: advance the theoretical foundations / verify
guarantees" angle: the deliverable is a formal statement of which decoding configurations preserve
the exponential mechanism's guarantee and which silently zero it out.

## Decisive experiment (no private data for the headline)

- **(a) Documentation audit, ~free.** Pull `generation_config.json` for the most-downloaded open
  instruct models. Confirmed this round: **Llama-3.1-8B-Instruct ships `temperature=0.6,
  top_p=0.9, do_sample=true` by default.** Show what fraction of "drop-in `.generate()`" deployments
  inherit nonzero truncation nobody chose for privacy reasons.
- **(b) Direct measurement, ~1–2 GPU-hours.** Implement the Amin-style exponential-mechanism sampling
  step locally (clip + noise a logit vector, sample) on an open model via vLLM/HF, run it (i) at full
  support and (ii) through a shipped default decoding config (top-p=0.9). Measure the empirical
  probability mass placed on tokens *excluded* by truncation but assigned nonzero mass under the
  calibrated exponential-mechanism target, as a function of how peaked the (controlled, synthetic)
  logit distribution is — demonstrating the `max_x P(x)/Q(x)=∞` failure is the generic behaviour
  whenever the private signal makes a token confidently likely, i.e. exactly the useful regime.

## Outcome-robustness

The core claim — `support(Q) ⊊ support(P)` under top-p/top-k ⇒ ε=∞, by definition of max-divergence
— is a one-line algebraic fact **no experiment can invalidate**. The measurement only decides *how
bad in practice*, i.e. whether the fix (`top_p=1.0, top_k=0` unless using a mechanism designed for
truncation such as Top-k+ or a subsampled exponential mechanism) is a large or small utility cost.
Same "propositions can't be experimentally falsified" floor the lead relies on, on a different
mechanism.

## Strongest referee attack + answer

**"InvisibleInk already solved decoding-time truncation with Top-k+ — this is solved."** →
Solved *for Top-k+ specifically*, which requires bespoke sampling code most deployments won't write.
We show (a) InvisibleInk's proof does **not** transfer to the option every standard library defaults
to (top-p, whose retained-set size is data-dependent; and even model-specific `top_k` values are not
the data-independent `k′` the theorem needs), and (b) neither Amin et al. nor InvisibleInk nor the
DP-fy guide states this — the guide's only "no top-p" line is imported from a paper solving a
different problem. We are not reproving InvisibleInk; we show where it silently fails to transfer,
and it is exactly the failure a practitioner following the guide's citation trail walks into.

## Scoop risk & ownership

Low. Mechanism is new (2024–2025), so the "someone already checked" prior is low. None of the four
fetched papers is organizer/speaker-owned (Kurakin, Ponomareva, Vassilvitskii co-author the DP-fy
guide but are not InfPriv organizers/speakers per `notes/00`).

## Verify before writing (desk-reject hygiene)

Re-confirm: 2407.12108 and 2507.02974 author lists / venues; the InvisibleInk Top-k+ mechanism
description; the DP-fy guide's Kurakin-citation wording; and the live Llama-3.1-8B-Instruct
`generation_config.json` values (model configs change). The ε=∞ claim itself is definitional and
needs no external source, but its framing as "the deployed mechanism" rests on the decoding-default
facts, which must be current.
