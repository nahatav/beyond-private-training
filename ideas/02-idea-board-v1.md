# Idea board v1 — 10 candidates, scored

Scoring: **N**ovelty / **D**efendability (can a reviewer break it?) / **F**easibility in 7 days /
**V**enue fit. 1–5 each.

| # | Idea | N | D | F | V | Status |
|---|---|---|---|---|---|---|
| 1 | Stateless CI guardrails don't compose → stateful leakage budget | 1 | 4 | 3 | 5 | **dead** — OCELOT, DP-MemView, "Sum Leaks More Than Its Parts", CAMP |
| 2 | Semantic/KV cache cross-user leakage + DP cache defense | 1 | 4 | 3 | 3 | **dead** — NDSS'25/'26, Key Collision Attack |
| 3 | Speculative decoding side channel | 1 | 4 | 2 | 3 | **dead** — arXiv 2411.01076 |
| 4 | Reasoning traces as unguarded privacy channel | 1 | 4 | 4 | 5 | **dead** — CoST, SALT, PrivateNLP'26 |
| 5 | GUI-agent screenshot bystander privacy | 1 | 4 | 2 | 4 | **dead** — CAPED, GUIGuard, MaskClaw |
| 6 | DP synthetic *agent trajectories* via Private Evolution | 3 | 3 | 2 | 5 | parked — heavy build, low surprise |
| 7 | Deployment-scale query budgets for private prediction | 2 | 3 | 3 | 5 | parked — van der Maaten & Hannun (2020) made the core argument |
| 8 | Attacker-compute scaling curves for privacy evals; rank inversion | 4 | 3 | 3 | 4 | **alive, fallback** — obviousness risk |
| 9 | Private Evolution's unaccounted selection steps (iteration/threshold picked on private data) | 3 | 4 | 4 | 5 | **alive** — folds naturally into #10 |
| 10 | **Executable audit of LLM-written *inference-time* DP mechanisms** | 5 | 5 | 5 | 5 | **WINNER** |

---

## The winner, stated properly

### The argument the workshop is missing

The workshop's own framing is that DP is migrating from training to inference. Nobody has said the
uncomfortable corollary out loud:

> Training-time DP consolidated onto a handful of heavily-audited libraries — Opacus,
> TF-Privacy, JAX-Privacy. A practitioner running DP-SGD reuses an implementation that
> hundreds of experts have stared at. **Inference-time DP has no such library.** Private Evolution,
> DP-ICL, private prediction, private RAG retrieval — each deployment hand-rolls its own noisy
> histogram, its own report-noisy-max, its own budget split. And in 2026 that hand-rolling is
> increasingly done by an LLM.

So the migration to inference-time DP is *also* a migration from vetted shared code to bespoke
model-written code — and DP is the worst possible domain for that, because a broken DP
implementation produces output that is statistically indistinguishable from a correct one. There
is no test that fails. The pipeline runs, the numbers look plausible, ε is printed in the paper.

### Why DP is the canonical unsound-verifier task

Most code generation has cheap sound verification: run the tests. DP correctness is a
universally-quantified statement over all neighbouring dataset pairs and all measurable output
events. You cannot confirm it by sampling — you can only *falsify* it. Gilbert & McMillan (2018)
show auditing unconstrained algorithms is statistically intractable. So DP code generation is a
clean instance of the setting where LLM self-improvement loops are theoretically expected to
break: **the verifier is unsound, so the repair loop optimises against the falsifier rather than
against the property.**

That gives the paper a falsifiable prediction, not just a benchmark: a repair loop driven by an
empirical auditor should *appear* to converge while ground-truth violations persist.

### Planned claims
- **C1 (silent failure).** A large fraction of model-written inference-time DP mechanisms are not
  DP at the claimed ε, while passing utility tests and LLM code review.
- **C2 (generator–verifier gap).** The same model that correctly *judges* a canonical mechanism
  (DPrivBench-style) fails to *produce* one, and fails to detect the violation in its own output.
- **C3 (inference-time-specific failure modes).** The failures are not generic coding bugs. They
  are the ones the inference-time setting invites: per-query vs. total budget confusion,
  data-dependent thresholds, un-noised nearest-neighbour selection, releasing intermediate
  retrieval scores, selection steps left out of the accounting.
- **C4 (auditor overfitting).** Falsifier-in-the-loop repair drives measured ε below threshold
  without fixing the mechanism — verified on held-out adjacency families.

C4 is the result with teeth, and it is the one that generalises beyond this paper: **you cannot
bootstrap a privacy guarantee out of empirical auditing.**

### Fit to the CFP
Hits topic 04 (AI for Privacy — "verify mathematical guarantees") and topic 06 (Benchmarks and
Evaluation) head-on, and is *about* topics 02/03 (private synthetic data, private ICL) because
those supply the mechanism suite. Directly answers the open question stated in DPrivBench, which
the CFP name-checks and which an organizer wrote.

### Anticipated referee attacks and answers
1. *"This is software engineering, not ML privacy."* → The mechanisms audited are exactly the
   workshop's; the failure taxonomy is DP-specific; the theoretical frame (unsound verifier,
   Gilbert–McMillan intractability) is a privacy-theory result.
2. *"Better prompting fixes it."* → C2 and C4 say otherwise: it is a verification gap, not a
   capability gap. Report best-of-N and CoT/reasoning-budget ablations to close this off.
3. *"Next model version obsoletes it."* → Report a capability trend across model tiers; if the
   generator–verifier gap persists as capability rises, the point stands.
4. *"Human experts also get this wrong."* → Yes, and grey-box auditing found 13 violations across
   12 human libraries (arXiv 2602.17454). That is the **baseline**, not a rebuttal — the
   comparison is the contribution.
