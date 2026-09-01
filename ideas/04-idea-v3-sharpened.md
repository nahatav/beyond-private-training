# v3 — sharpened framing (this is the paper)

## What changed from v2

v2 was a benchmark with a theory hook. v3 leads with the thesis and demotes the benchmark to
evidence. The trigger was finding the reward-hacking / verifier-overfitting literature
(EvilGenie arXiv 2511.21654; *Rethinking Verification for LLM Code Generation* arXiv 2507.06920;
*Before the Model Learns the Bug: Fuzzing RLVR Verifiers* arXiv 2606.01066). "Repair loops overfit
their verifier" is already known for ordinary code. If that is all we show, we are a DP-flavoured
replication.

The differentiator is the *reason* the verifier is weak:

> In ordinary code generation, verifier weakness is an **engineering** problem — LiveCodeBench
> missed 20% of medium / 40% of hard errors because its test suite was thin. Add tests, the gap
> shrinks. In differential privacy, verifier weakness is a **theorem**. Deciding ε-DP is
> coNP^#P-complete even for loop-free programs (Gaboardi–Nissim–Purser), and under black-box
> access any efficiently verifiable guarantee is efficiently breakable (Gilbert–McMillan). You
> cannot add tests until it is fixed.

**Thesis:** *differential privacy is the first practically-deployed task domain where the
generate–verify–repair loop is provably unfixable by better verification.* The workshop is
actively promoting "AI for Privacy — LLMs as infrastructure to enforce, redact, and **verify
mathematical guarantees**." We show the verification half of that agenda sits on a complexity
barrier, and measure the cost.

## Title
**You Can't Test Your Way to ε: LLM-Generated Inference-Time Differential Privacy and the Limits
of Empirical Auditing**

---

## Claims (final)

- **C1 — Silent failure.** A substantial fraction of model-written inference-time DP mechanisms
  violate the claimed ε while passing utility tests *and* LLM code review. Broken DP output is
  distributionally indistinguishable from correct DP output; nothing in the normal QA pipeline
  fires.
- **C2 — Generator–verifier gap.** Models that judge canonical mechanisms accurately (DPrivBench
  Cat-1: GPT-5-High 0.995) fail to produce them, and fail to detect the violation in their own
  output. Judging ≠ implementing.
- **C3 — The failure modes are inference-time-specific.** Not generic coding bugs. Expected:
  per-query vs. total budget confusion; data-dependent thresholds; un-noised nearest-neighbour /
  top-k selection; releasing intermediate retrieval scores; selection and stopping steps omitted
  from accounting; record- vs. user-level adjacency confusion; insecure float noise sampling.
- **C4 — Auditor overfitting (load-bearing).** Falsifier-in-the-loop repair drives *measured*
  violations toward zero while held-out-auditor and expert-confirmed violations persist. Unlike
  the code-generation case, this gap **cannot** be closed by strengthening the auditor — that is
  what the complexity results say.
- **C5 — The constructive half.** Re-run generation where the model must *compose vetted
  primitives* from a typed DP library rather than write noise code itself. If the failure rate
  collapses, the recommendation is concrete and actionable: **inference-time DP needs its Opacus**,
  and AI-for-privacy should target composition over synthesis.

C5 matters. Without it this is a complaint; with it, it is a design argument.

---

## Related work: how we sit relative to each neighbour

| Work | What it does | Why we are different |
|---|---|---|
| DPrivBench (2604.15851) | LLMs **judge** whether an algorithm is DP. 720 instances, 11 models. | We test **generation** and **self-detection** — the exact open question in their future-work section. Same model roster → the gap is directly measurable. |
| Grey-box auditing of DP libraries (2602.17454) | Audits **human-written** libraries; 13 violations / 12 libraries. | We audit **model-written** code, and we borrow their record-replay method as one of two auditors. Their result is our human baseline. |
| Lyu–Su–Li (PVLDB 2017) | 4 of 6 **published** SVT variants are not DP. | Historical baseline: expert error rate on the single hardest primitive. |
| Roy, Hsu, Albarghouthi (2101.00961) | Pre-LLM **synthesis** of DP mechanisms via optimisation + symbolic mapping. | The classical antecedent. We ask whether LLMs displace it and whether an unsound falsifier can substitute for their principled search. |
| SynBench (2509.14594) | Empirical privacy loss exceeds claimed (ε,δ) for DP text generation — cause is **pretraining contamination**. | Complementary failure channel. They break the guarantee through the *data*; we break it through the *implementation*. Cite together: two independent routes by which a printed ε is not the real ε. |
| PrivCode / PrivCode++ (2512.05459 / 2606.09145) | DP *for* code datasets. | Opposite direction entirely. Must disambiguate in the first paragraph of related work — the titles collide. |
| EvilGenie (2511.21654), RLVR verifier fuzzing (2606.01066) | Reward hacking / verifier overfitting in general code gen. | Their verifier weakness is fixable by better tests. Ours is a complexity barrier. This contrast **is** the paper. |

---

## 4-page skeleton

1. **Intro (0.75p).** DP is migrating from training to inference. Training-time DP consolidated
   onto Opacus / TF-Privacy / JAX-Privacy; inference-time DP has no such library, so every PE /
   DP-ICL / private-RAG deployment hand-rolls its mechanism, increasingly with a model. DP is the
   worst domain for that because failures are silent. Contributions list.
2. **Why DP resists verification (0.5p).** coNP^#P-completeness; efficiently-verifiable ⟹
   efficiently-breakable; therefore falsify-only. Prediction: repair loops fixpoint at "not
   caught". Human error-rate baselines (SVT 4/6, 13 bugs / 12 libraries, Mironov).
3. **SILENT-ε: suite + audit harness (0.75p).** 15 inference-time mechanism specs with explicit
   adjacency and target (ε,δ). Two auditors: grey-box record-replay, black-box empirical ε with
   Clopper–Pearson intervals. Expert-labelled stratified subsample to measure auditor *recall*.
   Sandboxed execution.
4. **Results (1.25p).** C1 silent-failure rate · C2 GVGap and SelfAuditAcc vs. DPrivBench's
   published judgment accuracies · C3 failure taxonomy with counts · C4 repair curve, measured vs.
   held-out vs. expert.
5. **C5 + Discussion (0.5p).** Composition-over-synthesis result; the case for a standard
   inference-time DP library; what "AI for Privacy" can and cannot be asked to verify.
6. **Limitations (0.25p).** Auditors are incomplete, so every number is a **lower bound** on the
   violation rate — stated up front, since it is the honest and the stronger direction.

---

## Risk register

| Risk | Severity | Mitigation |
|---|---|---|
| DPrivBench authors publish this follow-up first | med | Concurrent work is acceptable at a workshop. Our differentiators (C4, inference-time suite, complexity framing) are not in their stated plan, which is generation+detection only. |
| C4 does not reproduce — repair genuinely fixes the mechanism | med | Then we report it, and it becomes a **positive** result for AI-for-Privacy, which is also publishable here. The paper survives either outcome — this is the main reason to pick it. |
| Violation rates come out low on frontier models | low | Tier-2 mechanisms (PE NN-histogram, SVT, user-level adjacency) are hard; DPrivBench Cat-2 F1 is already only ~0.74 on judgment alone. Generation should be worse. |
| Auditors miss violations, understating C1 | low | By design. Report as a lower bound; expert labels quantify auditor recall. |
| Reviewer says "software engineering, not ML privacy" | med | Mechanism suite is entirely from the CFP's topic list; failure taxonomy is DP-specific; framing is a privacy-theory result. |
| Executing untrusted generated code | **high (safety)** | Sandbox: subprocess, no network, resource + wall-clock limits, ephemeral FS. Non-negotiable before any run. |
| Public repo + double-blind | med | Flagged to user; user chose public. Keep the submission PDF and any author-identifying text out of this repo. |

## Deliberately out of scope for v1
Auditing published third-party research implementations (DPSDA, DP-ICL repos). Highest-impact
arm available, but it means publishing violation claims about named people's code and would
require airtight findings plus responsible disclosure first. Revisit after the workshop.
