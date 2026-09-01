# Literature sweep #1 — mapping what is already occupied

Goal: find territory that is *not* already crowded. The agentic-privacy space in particular is
absorbing several papers per month, so anything obvious there is gone.

## Dead ground (occupied, do not enter)

### Compositional / cross-session agent leakage
The intuition "individually-benign disclosures compose into a leak" is fully claimed.
- *The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations in Multi-Agent
  Collaboration* — arXiv 2509.14284. Names the phenomenon "compositional privacy leakage".
- *OCELOT: Inference-Leakage Budgets for Privacy-Preserving LLM Agents* — arXiv 2606.12341.
  Posterior-risk control, certified min-entropy cost per operator, sink-trust-weighted budget,
  Merkle-chained ledger. This is the "stateful guardrail with a budget" idea, done thoroughly.
- *DP-MemView: A Memory Interface for Attribute-Level Transcript Privacy in Long-Term LLM Agents*
  — arXiv 2608.03130. Ledger charges for long-horizon memory.
- *CAMP: Cumulative Agentic Masking and Pruning for Privacy Protection in Multi-Turn LLM
  Conversations* — arXiv 2604.16521.
- Survey: *Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents* — arXiv
  2606.26627. Flags cross-session + compositional leakage as least-protected, but the papers above
  have already moved in.

**Verdict: dead.** My initial "stateless guardrails don't compose" idea is ~4 papers late.

### Serving-layer side channels (KV cache, prefix cache, semantic cache)
- *I Know What You Asked: Prompt Leakage via KV-Cache Sharing in Multi-Tenant LLM Serving*
  (PROMPTPEEK) — NDSS 2025.
- *The Early Bird Catches the Leak: Timing Side Channels in LLM Serving Systems* — arXiv 2409.20002.
- *InputSnatch: Stealing Input in LLM Services via Timing Side-Channel Attacks* — arXiv 2411.18191.
- *From Similarity to Vulnerability: Key Collision Attack on LLM Semantic Caching* — arXiv 2601.23088.
- *Cache Me, Catch You: Cache Related Security Threats in LLM Serving Frameworks* — NDSS 2026.
- Even the practitioner side is claimed: vllm-project/semantic-router issue #2134 documents
  soft embedding-distance user scoping causing cross-tenant response leaks.

**Verdict: dead**, and it is a systems-security venue's territory anyway.

### Speculative decoding side channel
- *When Speculation Spills Secrets: Side Channels via Speculative Decoding in LLMs* — arXiv
  2411.01076. Fingerprints queries at >90% across REST/LADE/BiLD/EAGLE. **Dead.**

### Reasoning-trace / chain-of-thought privacy
- *Chain-of-Sanitized-Thoughts: Plugging PII Leakage in CoT of Large Reasoning Models* — arXiv 2601.05076.
- *SALT: Steering Activations towards Leakage-free Thinking in Chain of Thought* — arXiv 2511.07772.
- *Safer Reasoning Traces: Measuring and Mitigating CoT Leakage in LLMs* — PrivateNLP @ ACL 2026.
**Verdict: dead.** The "to decide what not to say, the model must first think it" angle is taken.

### GUI / computer-use agent screen privacy
- *CAPED: Context-Aware Privacy Exposure Defense for Mobile GUI Agents* — arXiv 2606.12666.
- *GUIGuard-Bench* — arXiv 2601.18842. *MaskClaw* — arXiv 2605.28646. *AgentDAM* (data minimization).
**Verdict: dead.**

## Live ground

### A. Executable auditing of LLM-*written* DP code
- *DPrivBench: Benchmarking LLMs' Reasoning for Differential Privacy* — arXiv 2604.15851, by
  workshop organizer Erchi Wang. Tests **judgment only**: given an algorithm + claimed guarantee,
  does it satisfy DP? Finding: frontier models handle textbook mechanisms, all models fail on
  advanced ones.
- DPrivBench itself states the open question: whether LLMs can *detect implementation-level
  privacy violations* and *generate correct and faithful implementations of DP algorithms*.
- *Privacy in Theory, Bugs in Practice: Grey-Box Auditing of Differential Privacy Libraries* —
  arXiv 2602.17454. Audits **human-written libraries**, not model-written code.
- *PrivCode* (NDSS, arXiv 2512.05459) / *PrivCode++* (2606.09145) are the reverse problem — DP
  *for* code generation (protecting training code), not correctness of generated DP code.
- Falsifier tooling exists and is mature: DP-Sniper (ETH SRI), StatDP, DPCheck, Eureka.
**Verdict: open, and the gap is stated by an organizer's own paper.**

### B. Attacker-compute scaling of empirical privacy evaluations
No prior work found on "leakage as a function of adversary inference compute". Adjacent:
- *Exploring the limits of strong membership inference attacks on LLMs* — arXiv 2505.18773
  (scales shadow models, not inference/reasoning compute).
- *Better Membership Inference Privacy Measurement through Discrepancy* — arXiv 2405.15140.
**Verdict: open but has an obviousness risk** — "DP bounds worst-case adversaries, heuristics
don't" is expected. Needs a surprising empirical hook (see idea board).

### C. Private Evolution's theory–practice gap
- *Private Evolution Converges* — arXiv 2506.08312. Names concrete gaps: multiplicity parameters
  and post-threshold normalisation of the DP nearest-neighbour histogram are not covered by the
  convergence analysis; synthetic-set size cannot be decoupled from private-sample count;
  initialisation far from the private distribution wrecks the privacy–utility trade-off.
- *MAPLE: Metadata Augmented Private Language Evolution* — arXiv 2603.19258.
- Unaccounted data-dependent iteration/hyperparameter selection is a known generic hazard
  (Renyi-DP tuning, arXiv 2110.03620; *Revisiting Hyperparameter Tuning with DP*, arXiv 2211.01852)
  but has not been measured for PE specifically.
**Verdict: half-open, somewhat incremental.**

### D. Inference-only DP synthetic data for *agentic* modalities
- *PrivORL: DP Synthetic Dataset for Offline RL* — arXiv 2512.07342 (diffusion, requires training).
- PE has images, text, tabular, simulators (DPSDA "APIs 3"). Tool-use traces are unclaimed.
**Verdict: open, but a "new modality for PE" paper is heavy to build and low-surprise.**

---

# Sweep #2 — hunting specifically for niche, non-mainstream ground

Trigger: the v3 direction (LLM-generated DP code) is announced as future work in DPrivBench, so
other groups plausibly have it in flight. Re-searched for thin corners rather than hot surfaces.

## Newly dead
- **Individual / Renyi privacy filters for retrieval-based inference.** *Private-RAG: Answering
  Multiple Queries with LLMs while Keeping Your Data Private*, arXiv **2511.07637**, by
  **Ruihan Wu, Erchi Wang, Zhiyuan Zhang, Yu-Xiang Wang** — four workshop organizers. Also
  *Beyond Per-Question Privacy: Multi-Query DP for RAG Systems* (OpenReview),
  *DP Datastore Generation for Retrieval-Augmented Inference* (arXiv 2606.01413).
- **Per-record / outlier empirical privacy of DP synthetic data.** *Risk-Equalized DP Synthetic
  Data: Protecting Outliers by Controlling Record-Level Influence* (arXiv 2602.10232);
  *Phantoms and Disclosures* (arXiv 2606.16952); *Advancing the SOTA in Empirical Privacy
  Auditing* (arXiv 2606.10481).
- **Deletion propagation / right-to-be-forgotten in inference pipelines.** *Agentic Unlearning*
  (arXiv 2602.17692); *Always-On Agents* survey (arXiv 2606.30306) already does dependency-aware
  deletion of derived artifacts.

## Confirmed open — the user-level privacy unit in inference-time DP
Checked every PE-family paper for any mention of users contributing multiple samples. None has one.
- PE-1 images 2305.15560 - Aug-PE text 2403.01749 - APIs-3 simulators 2502.05505 -
  APIs-4 tabular 2606.08259 - PE-means 2606.00342 - MAPLE 2603.19258 - PE Converges 2506.08312.
- *Private Evolution Converges* states the accounting explicitly: NN histogram with **l2
  sensitivity 2/n** under add/remove-one-sample adjacency, composed over T Gaussian mechanisms
  (citing Dong et al. 2022 Cor. 3.3). Confirmed: **no user-level discussion anywhere.**
- User-level DP is mature on the training side and simply never crossed over:
  Levy et al., *Learning with User-Level Privacy*, NeurIPS 2021 (arXiv 2102.11845);
  Ghazi et al., *User-Level DP With Few Examples Per User*, arXiv 2309.12500;
  *Mind the Privacy Unit! User-Level DP for LM Fine-Tuning*, arXiv 2406.14322 (fine-tuning only).
- Aug-PE's own benchmarks are user-structured: Yelp 1.9M reviews (reviewer ids), **OpenReview
  8,396 ICLR-2023 reviews (~3-6 per reviewer)**, PubMed 75,316 abstracts (per author).

**Verdict: open, small-population, and the motivating example uses the PE authors' own benchmarks.**
