# Verified bibliography

The CFP enforces a **strict reference-hallucination protocol**: fabricated or AI-generated
citations are auto-rejected without review. Every entry below was confirmed by fetching the
arXiv abstract page, the publisher page, or a search result carrying title + authors + venue.
Nothing goes in the paper unless it appears here first.

Legend: ✅ title/authors/venue confirmed · ⚠️ found but details still to confirm.

## Theoretical spine — verifying DP is intractable
| Ref | Detail | Status |
|---|---|---|
| Gaboardi, Nissim, Purser — *The Complexity of Verifying Loop-Free Programs as Differentially Private* | arXiv **1911.03272**. ε-DP verification is **coNP^#P-complete**; (ε,δ) is coNP^#P-hard, in coNP^#P for restricted output domains, coNP^#P^#P generally; approximating the privacy level is NP-hard and coNP-hard. | ✅ |
| Gilbert, McMillan — *Property Testing for Differential Privacy* | arXiv **1806.06427**, Allerton 2018. "Any privacy guarantee that can be efficiently verified is also efficiently breakable." Verification requires compromise from verifier or algorithm owner. | ✅ |

## Human baseline — experts get DP implementations wrong
| Ref | Detail | Status |
|---|---|---|
| Lyu, Su, Li — *Understanding the Sparse Vector Technique for Differential Privacy* | arXiv **1603.01699**; PVLDB **10(6):637–648, 2017**. Of six published SVT variants, **only two** satisfy DP at the intended parameter. | ✅ |
| Mironov — *On Significance of the Least Significant Bits for Differential Privacy* | **CCS 2012**, DOI 10.1145/2382196.2382264. Floating-point Laplace sampling is porous over doubles; all four general-purpose DP systems of the day were breakable. | ✅ |
| *Privacy in Theory, Bugs in Practice: Grey-Box Auditing of Differential Privacy Libraries* | arXiv **2602.17454**. "Re:cord-play" — instrumented runs on neighbouring datasets under identical randomness. **13 violations across 12 libraries** (SmartNoise SDK, Synthcity, diffprivlib, Opacus, MOSTLY AI, Private-PGM, dpmm). Bug taxonomy: data-dependent leakage into data-independent code; sensitivity miscalculation; noise miscalibration; flawed primitives. No LLM component. | ✅ |

## Falsification tooling
| Ref | Detail | Status |
|---|---|---|
| Bichsel et al. — *DP-Sniper: Black-Box Discovery of Differential Privacy Violations using Classifiers* | ETH SRI; IEEE S&P 2021. Code: `github.com/eth-sri/dp-sniper`. Also finds floating-point violations. | ✅ |
| Ding, Wang, Wang, Zhang, Kifer — *Detecting Violations of Differential Privacy* (StatDP) | arXiv **1805.10277**; CCS 2018, DOI 10.1145/3243734.3243818. Hypothesis testing + counterexample generation. | ✅ |
| *Auditing Differential Privacy in the Black-Box Setting* | arXiv **2503.12045**. | ⚠️ authors TBC |
| *Debugging Differential Privacy: A Case Study for Privacy Auditing* | arXiv **2202.12219**. | ⚠️ authors TBC |
| *Eureka: A General Framework for Black-box Differential Privacy Estimators* | ePrint 2022/1250. | ⚠️ |

## The direct antecedent
| Ref | Detail | Status |
|---|---|---|
| *DPrivBench: Benchmarking LLMs' Reasoning for Differential Privacy* | arXiv **2604.15851**. **720 instances** (588 Cat-1 foundational sensitivity mechanisms across 6 types; 132 Cat-2 advanced algorithms across 16 topics). 11 models: GPT-5 (High/Minimal), Gemini-3-Pro, Gemini-2.5-Flash, Claude-Sonnet-4.5, Claude-Opus-4.5, DeepSeek-R1, DeepSeek-V3.1-chat, Qwen3-30-Instruct, Qwen3-30-Think, Goedel-Prover-V2. Cat-1: GPT-5-High 0.995, best open-source DeepSeek-V3.1-chat 0.841. Cat-2: GPT-5-High F1 0.742, Gemini-3-Pro 0.748. **Judgment only — no code generation.** Future work explicitly asks for exactly our contribution. | ✅ |

## Inference-time mechanisms being implemented
| Ref | Detail | Status |
|---|---|---|
| Lin et al. — *DP Synthetic Data via Foundation Model APIs 1: Images* (Private Evolution) | arXiv **2305.15560**, ICLR 2024. Code: `github.com/microsoft/DPSDA`. | ✅ |
| Xie et al. — *DP Synthetic Data via Foundation Model APIs 2: Text* (Aug-PE) | arXiv **2403.01749**, ICML 2024. | ✅ |
| *DP Synthetic Data via APIs 3: Using Simulators Instead of Foundation Models* | Microsoft Research. | ⚠️ arXiv id TBC |
| Wu et al. — *Privacy-Preserving In-Context Learning for Large Language Models* (DP-ICL) | arXiv **2305.01639**. Disjoint exemplar shards + noisy consensus / report-noisy-max. | ✅ |
| *Privacy-Preserving In-Context Learning with Differentially Private Few-Shot Generation* | Microsoft Research (Tang et al.). | ⚠️ arXiv id TBC |
| *Differentially Private In-Context Learning with Nearest Neighbor Search* | arXiv **2511.04332**. | ⚠️ authors TBC |
| *Private Evolution Converges* | arXiv **2506.08312**. Names the theory–practice gaps: multiplicity parameters and post-threshold normalisation of the DP NN histogram fall outside the convergence analysis; synthetic-set size coupled to private-sample count; initialisation sensitivity. | ✅ |
| *DP-TabICL: In-Context Learning with Differentially Private Tabular Data* | arXiv **2403.05681**; IEEE. | ⚠️ authors TBC |

## Context / motivation
| Ref | Detail | Status |
|---|---|---|
| *Hyperparameter Tuning with Renyi Differential Privacy* | arXiv **2110.03620**. | ⚠️ authors TBC |
| *Revisiting Hyperparameter Tuning with Differential Privacy* | arXiv **2211.01852**. | ⚠️ authors TBC |
| *Programming Frameworks for Differential Privacy* | arXiv **2403.11088**. | ⚠️ authors TBC |

## Not our problem, but adjacent — cite to disambiguate
| Ref | Detail | Status |
|---|---|---|
| *PrivCode: When Code Generation Meets Differential Privacy* | arXiv **2512.05459**, NDSS. DP *for* code datasets — the reverse direction. Must be distinguished explicitly in related work. | ✅ |
| *PrivCode++: Latent-Conditioned DP Code Generation* | arXiv **2606.09145**. Same reverse direction. | ✅ |

## To do before writing
- [ ] Confirm authors for every ⚠️ row.
- [ ] Pull the DPSDA repo and read the actual NN-histogram implementation — it is the reference for mechanism #6.
- [ ] Check whether DP-Sniper runs out of the box on Python 3.12 or needs a reimplementation.

---

## Round 3 additions (verified)

| Ref | Detail | Status |
|---|---|---|
| Roy, Hsu, Albarghouthi — *Learning Differentially Private Mechanisms* | arXiv **2101.00961** (Jan 2021). Pre-LLM **synthesis** of DP programs: strategic input selection + continuous optimisation + symbolic mapping back to code. Recovers foundational DP algorithms. The classical antecedent to LLM-based DP code generation. | OK |
| Sun, Schlegel, Nandakumar, Zahid, Wu, Wu, Li, Zhang, Del-Pinto, Nenadic, Lam, Bharath — *SynBench: A Benchmark for DP Text Generation* | arXiv **2509.14594**. Nine datasets (health/finance/legal), three methods (AUG-PE, DP-Gen, DP-Diffusion), eps in {0.5,1,2,4}. Finds empirical privacy loss can exceed claimed (eps,delta) bounds — **cause is pretraining contamination, not implementation bugs**. Does not evaluate LLM-written code. Complementary failure channel to ours. | OK |
| *Evaluating LLM Simulators as Differentially Private Data Generators* | arXiv **2604.15461**. "Profile-then-Simulate". | authors TBC |
| EvilGenie — reward hacking benchmark | arXiv **2511.21654**. Agents hardcode test cases / edit test files. | authors TBC |
| *Rethinking Verification for LLM Code Generation: From Generation to Testing* | arXiv **2507.06920**. LiveCodeBench-passing solutions failed LeetCode's judge on 20% of medium / 40% of hard — verifier weakness is an **engineering** gap there, unlike DP. | authors TBC |
| *Before the Model Learns the Bug: Fuzzing RLVR Verifiers* | arXiv **2606.01066**. | authors TBC |
| *The Sparse Vector Technique, Revisited* | arXiv **2010.00917**. | authors TBC |
| Zhu, Wang — *Improving Sparse Vector Technique with Renyi Differential Privacy* | NeurIPS 2020. Yu-Xiang Wang is a workshop organizer — worth citing. | authors TBC |

---

## Round 7 additions — the user-level spine

Each row below was verified by fetching the arXiv abstract page and reading title, full author
list and date, or by reading the fetched full text directly. These are the load-bearing citations
for `ideas/10`, so the verification bar is the highest in this file.

| Ref | Detail | Status |
|---|---|---|
| Ponomareva, Xu, McMahan, Kairouz, Rosenblatt, Cohen-Addad, Guzmán, McKenna, Andrew, Bie, Yu, Kurakin, Zadimoghaddam, Vassilvitskii, Terzis — *How to DP-fy Your Data: A Practical Guide to Generating Synthetic Data With Differential Privacy* | arXiv **2512.03238**, 2 Dec 2025. **The object of study.** §5.3.2 "User-level privacy unit adjustments" recommends normalising each user's vote counts to unit ℓ₂ norm. §5.1 flags PE and DP inference as harder to adjust to user level than DP-SGD; §7.2 gives the beyond-group-privacy improvement for DP-SGD only; §5.1 asserts without analysis that all described algorithms can be adjusted to user or group level. §5.7 names streaming PE as unexplored. §5.1 "Sub-unit level of privacy" restates idea E via Brown et al. 2022. Table 10 rates PE's resilience to distribution gaps as Low and recommends it for <1K samples and ε<1. | ✅ full author list + date verified |
| González, Fanti, Ramdas — *Private Evolution Converges* | arXiv **2506.08312**, 10 Jun 2025, **NeurIPS 2025**. Convergence to the private empirical distribution; ℓ₂ sensitivity 2/n under add/remove-one-sample. App. C.3: in practice `n_s ≠ n` and setting `n_s` correctly is critical for convergence. "Limitations and future work": the analysed `Variation_API` is not the practical one; rate suffers curse of dimensionality. **Zero occurrences of "user-level".** | ✅ authors + venue verified |
| Liu, Suresh, Zhu, Kairouz, Gruteser — *Algorithms for bounding contribution for histogram estimation under user-level privacy* | arXiv **2206.03008**. User-level histogram estimation via per-user clipping: 2-approximation to the best contribution bound (bounded domain), log-approximation (unbounded), explicit bias–variance characterisation of the threshold, post-processing debiasing under mild distributional assumptions. **The strongest antecedent and the main novelty threat** — see `lit/03` for the three ways PE differs (generated domain, histogram-as-selection-signal, feedback loop). | ✅ authors verified |
| Charles, Ganesh, McKenna, McMahan, Mitchell, Pillutla, Rush — *Fine-tuning large language models with user-level differential privacy* | 2024. DP-SGD-ELS (example-level sampling + contribution bounding) and DP-SGD-ULS (user-level sampling + per-user clipping); Mixture-of-Gaussians accounting beats group privacy. **The training-side template our paper is the inference-side analogue of.** | ⚠️ arXiv id to confirm before submission |
| Wang, Chen, Du, Xiao, Zhang, Yan — *Secret-Protected Evolution for Differentially Private Synthetic Text Generation* (SecPE) | arXiv **2510.10990**, 13 Oct 2025. Secret-aware protection replacing uniform DP guarantees; clustering-based voting for large speedups. Mentions user-level DP only in related work. **Occupies the constructive half of idea E.** | ✅ authors + date verified |
| He, Vershynin, Zhu — *Online Differentially Private Synthetic Data Generation* | arXiv **2402.08012**, 12 Feb 2024. Continual-release synthetic data, near-optimal 1-Wasserstein rates. Cited to price J2 honestly. | ✅ authors + date verified |
| Bagdasaryan, Poursaeed, Shmatikov — *Differential Privacy Has Disparate Impact on Model Accuracy* | NeurIPS 2019. Cited by the DP-fy guide for DP-generated text running short. The lineage for `ideas/10` Claim 3. | ⚠️ confirm exact venue string |
| Brown, Lee, Mireshghallah, Shokri, Tramèr — *What Does it Mean for a Language Model to Preserve Privacy?* | 2022. The secret-as-privacy-unit argument the guide's sub-unit paragraph rests on. Mireshghallah is a workshop organizer. | ⚠️ confirm author list + venue |
| Amin, Kulesza, Muñoz Medina, Vassilvitskii — bounding user contributions | Cited by 2206.03008 as originating the bias–variance question for contribution bounds. | ⚠️ confirm id + venue |
| Ganesh et al. (2025); Cohen-Addad et al. (2025) | Contribution-bounding selection under multi-attribution: sequential greedy with an LP upper bound, and a scalable distributed hypergraph formulation. Relevant only if we discuss multi-owner records. | ⚠️ ids TBC |

### Verified negative results (worth as much as the positives)

Counted case-insensitive occurrences of "user-level" in fetched full text: **0** in Aug-PE
(2403.01749), Private Evolution Converges (2506.08312), Tab-PE (2606.08259), DP-ICL (2305.01639),
2508.20452, and 2509.25729. 4 in SecPE (related work only). 54 in the DP-fy guide. The asymmetry is
itself citable evidence for the paper's framing.

### Still to do before writing
- [ ] Resolve every ⚠️ above; the CFP desk-rejects on citation errors.
- [ ] Confirm the DP-fy guide's exact section numbers for the two passages we lean on, since we
      cite them by location.

---

## Round 8 additions and resolutions (six-agent review)

Full detail and framing in `notes/10`; folded here because `lit/02` is the canonical citation home.
All ✅ rows were verified this round by full-text or GitHub fetch; ⚠️ rows still need it.

### Resolved from earlier ⚠️
| Ref | Resolution | Status |
|---|---|---|
| DP-fy guide 2512.03238 | Now published: **JAIR Vol. 86, Art. 17 (2026)** — cite as JAIR, not only arXiv. | ✅ |
| Brown, Lee, Mireshghallah, Shokri, Tramèr | arXiv **2202.05520**, **FAccT 2022** (order confirmed against the arXiv page). | ✅ |
| Bagdasaryan, Poursaeed, Shmatikov | **NeurIPS 2019, pp. 15453–15462**. | ✅ |
| DP-ICL nearest-neighbour 2511.04332 | Authors = **Koskela, Kulkarni, Zumot** (Koskela is an organizer). | ✅ |

### New load-bearing refs (verified this round)
| Ref | Detail | Status |
|---|---|---|
| **`microsoft/DPSDA` — `vote_normalization_level="client"`** | Shipped ℓ₂ per-user vote normalisation in `pe/histogram/nearest_neighbors.py`; noise added at fixed scale in `pe/dp/gaussian.py`, blind to the mode. Commit `25cdf854a22f...`, 2025-02-20, *"add the support of client-level DP,"* by **Zinan Lin**. The lead's primary exhibit (`ideas/14`). Re-verify against live `main` before submission. | ✅ (GitHub fetch) |
| Papernot, Song, Mironov, Raghunathan, Talwar, Erlingsson — *Scalable Private Learning with PATE* | **ICLR 2018, arXiv 1802.08908**. Third record-neutral-parameter instance (teacher count K), `ideas/15`. | ✅ authors/venue |
| Tab-PE / APIs-4 tabular — 2606.08259 | "We assume class distributions are known"; Alg. 2 sets `N(c)=N·|D_priv(c)|/|D_priv|` with no DP noise. `ideas/17`. | ✅ full text |
| MAPLE 2603.19258 | Confirmed **text-only**; future work names images/tabular/multimedia as unaddressed. | ✅ full text |
| Amin, Bie, Kong, Kurakin, Ponomareva, Syed, Terzis, Vassilvitskii — *Private prediction for large-scale synthetic text generation* | arXiv **2407.12108** (Jul 2024). Exponential mechanism via softmax; no mention of top-p/top-k/full-support. `ideas/16`. | ✅ full-text grep |
| Vinod, Pillutla, Thakurta — *InvisibleInk* | arXiv **2507.02974**, **NeurIPS 2025**. Top-k+ decoding (data-independent size); does not cover default top-p. `ideas/16`. | ✅ full text |
| Kurakin et al. — *Harnessing LLMs to generate private synthetic text* | arXiv **2306.01684**. "No top-p" is a fidelity choice after DP-SGD fine-tuning (post-processing), not an inference-time privacy requirement. | ✅ |
| Awan, Rao — *Privacy-Aware Rejection Sampling* | arXiv **2108.00965**, **JMLR 24 (2023)**. Rejection-sampler runtime leaks unless acceptance prob is data-independent. Plan-B (refusals). | ✅ |
| George, Ramesh, Singh, Tyagi — *Continual Mean Estimation Under User-Level Privacy* | arXiv **2212.09980**, IEEE JSAIT (Feb 2024). Streaming + user-level (multi-participation) already exists → corrects J2's parking reason (`ideas/15`). | ✅ authors/venue |
| Hayes, Mahloujifar, Balle — *Bounding Training Data Reconstruction in DP-SGD* | arXiv **2302.07225**, **NeurIPS 2023**. F's antecedent (pairs bound + matching attack). | ✅ |
| Koga, Wu, Zhang, Chaudhuri — *Privacy-Preserving RAG with DP* | arXiv **2412.04697**. Organizer-owned (Wu + Chaudhuri) → whole private-RAG line off-limits. | ✅ authors |
| DPCheatSheet — 2509.12590 (Chu, Tian, Yu-Xiang Wang, Jin) | Organizer (Yu-Xiang Wang) co-author; "LLM helps humans do DP" corner. | ✅ |
| StatDP — 1805.10277 (already above) | Sound black-box DP tester; the grader for the constructive-falsification Plan-B (`notes/10`). | ✅ |
| ToxicChat 2310.17389 (Findings EMNLP 2023); RealToxicityPrompts 2009.11462 (Findings EMNLP 2020) | Public moderation benchmarks for the refusals Plan-B. | ✅ |
| Swanberg, McKenna, Roth, Cheu, Kairouz — 2502.06555 | Contains a genuine zero-private-data ("Gemini, no DP") tabular baseline → weakens standalone idea B. | ✅ full text |
| Quantamination — 2604.26505 | Batch dynamic-quantization cross-tenant leak; kills the batch-numerics idea. | ✅ |
| Dead-ground (topics 1/3): MAGPIE 2510.15186, AgentLeak 2602.11510, TAMAS 2511.05269, MuPPET 2606.23217, PiSAs 2607.05318; SnapAudit 2511.13502, ContextLeak 2512.16059 | Saturated surfaces; do not enter. | ✅ (search) |

### Still ⚠️ (fetch before citing)
- ~~Charles et al. 2024 exact arXiv id~~ → **resolved, 2407.07737** (round 9). ~~Amin/Kulesza/Muñoz-Medina/Vassilvitskii~~ → **resolved, ICML 2019 PMLR v97:263–271** (round 9). Ganesh/Cohen-Addad still open.
- arXiv **2601.22320** (MF for continual mean estimation) — title/premise from search only.
- arXiv **2202.10517** (Individualized PATE) — from search summaries only.
- SuperDP **2603.26215** PLDI-2026 acceptance — ACM DL record only, not on the arXiv page.
- The exact PATE "taints at most one teacher" sentence — re-confirm from the paper's own text before quoting.

---

## Round 9 additions (opus precedent review)

Detail in `ideas/18`. These are the estimand-shift lineage the lead must cite-and-distinguish, plus
corrections. ✅ = fetched to a primary source this round.

### Estimand-shift / normalisation lineage (cite-and-distinguish in the lead)
| Ref | Detail | Status |
|---|---|---|
| **Amin, Kulesza, Muñoz-Medina, Vassilvitskii — *Bounding User Contributions: A Bias-Variance Trade-off in DP*** | **ICML 2019, PMLR v97:263–271** (no arXiv id — cite PMLR). The **origin** of "a contribution bound changes the estimand (bias), not just the variance." Scalar cap, fixed domain, one-shot → lineage, not a scoop. | ✅ dblp |
| **Charles, Ganesh, McKenna, McMahan, Mitchell, Pillutla, Rush — *Fine-Tuning LLMs with User-Level DP*** | **arXiv 2407.07737** (Jul 2024). Resolves the long-standing ⚠️ id. Training-side template; complement, not scoop. | ✅ |
| **Wang, Liu, Liang, Joshi, Poor — *Tackling the Objective Inconsistency Problem* (FedNova)** | **arXiv 2007.07481, NeurIPS 2020.** General "normalised aggregation converges to a mismatched objective" — cite-and-distinguish (optimisation objective, not a DP measure; no diversity tilt). | ✅ |
| Google federated **location heatmaps** | **arXiv 2111.02356.** Normalises each user's contribution to bounded ℓ₁ = the lead's `p=1` (user-uniform) endpoint, as pure sensitivity control. **Supports** the lead; nobody there notices ℓ₂ tilts toward diversity. | ✅ |
| Chua et al. — *Mind the Privacy Unit!* (2406.14322, COLM 2024); Levy et al. (2102.11845, NeurIPS 2021); Ghazi et al. (2309.12500, NeurIPS 2023) | User-level DP-SGD; none frames contribution bounding as an estimand shift. Cite as complements. | ✅ |
| **2502.04749** — *Bounding User Contributions for User-Level DP Mean Estimation* (2025) | Same Amin/Liu lineage; surfaced but **not fetched** — flag, do not lean on. | ⚠️ |

### Disparate-impact lineage (for Claim 3)
| Ref | Detail | Status |
|---|---|---|
| **Ganev, Oprisanu, De Cristofaro — *Robin Hood and Matthew Effects*** | **arXiv 2109.11429.** DP distorts subgroup *sizes* in synthetic data — the most dangerous Claim-3 precedent. Rebuttal: DP-**noise** effect (vanishes ε→∞), one-shot, no functional form, no PE, no loop. **⚠️ venue (ICML 2022?) re-confirm before citing.** | ⚠️ venue |
| **Andrey, Perrot, Le Bars, Tommasi — *Disparate Impact in Synthetic Data Generation*** | **arXiv 2606.13105** (Jun 2026). Concurrent; PGM-based, no functional form, no PE. Cite as concurrent. | ✅ |

### Private-prediction / decoding line (context for the demoted `ideas/16`)
| Ref | Detail | Status |
|---|---|---|
| **InvisibleInk — 2507.02974** | **States the ε=∞-under-truncation fact verbatim** as the Top-k+ motivation. This **falsifies `ideas/16`'s** "nobody states this" claim — see the round-9 correction there. | ✅ full text |
| DPS-MOZO — Flemings, Gan, Li, Razaviyayn, Annavaram, **2501.19287** | DP-ICL by mixing few-shot+zero-shot; truncates to a **public** top-k set (a data-independent finite-ε fix). | ✅ |
| Subsampled Exponential Mechanism — Lantz, Boyd, Page | **AISec 2015.** EM over a data-independent sampled set — the classical truncation fix. | ✅ |
| SubMix (2201.00971); PMixED (2403.15638) | Mixture / Rényi private next-token prediction — private-prediction context. | ⚠️ search-level |

### Corrections & flags
- **`ideas/16` demoted** to reframe-or-drop — its headline is falsified by InvisibleInk (above).
- **StatDP** (`cmla-psu/statdp`) is **Python-3.8, ~4 commits, effectively unmaintained**; **DP-Sniper**
  (`eth-sri/dp-sniper`, S&P 2021) returns a witness+ε. Getting either onto current Python is the
  constructive-falsification Plan-B's real risk (engineering time, not compute) — resolve before use.
- **Tab-PE = 2606.08259** authors confirmed: Tran, Backurs, **Zinan Lin** (invited speaker), Reis,
  Xiong, Yekhanin. Footnote 11 + Alg. 2 verified; **App. D.11 / App. B.1 not yet fetched** — decisive
  for `ideas/17`, read before writing.
- Verified GPU rates (2026-09-01) for `notes/08`: RunPod A6000/4090 ≈ $0.33–0.34/hr; Modal A100-40
  $2.10/hr + $30/mo free. Aug-PE full Yelp run = 27–139 GPU-hr/config (the budget landmine).

---

## Round 11 additions — the compression × monitoring sweep (`ideas/20`)

Every ✅ row below was verified this round by fetching the arXiv abstract page via the API
(`export.arxiv.org/api/query`, which returns title + full author list + date + verbatim abstract)
or by extracting and reading the `arxiv.org/html/<id>` full text. ⚠️ = surfaced but not fetched;
do not lean on those.

### The precedents that falsify `ideas/19`'s novelty claim (cite-and-concede in related work)

| Ref | Detail | Status |
|---|---|---|
| **M M Asif Ferdous — *Bigger or Cheaper? Scale and Quantization Effects on Uncertainty Signals in Vision-Language Models Under Image Degradation*** | arXiv **2607.24440**, 27 Jul 2026, 12pp, code at `github.com/Asif-Ferdous/vlm-scale-quant`. Qwen2-VL 2B/7B, 5,700 predictions, six photographic degradations × three severities. **"4-bit quantization is nearly free for accuracy (−1.6 points) but expensive for the confidence signal (internal AUROC 0.95 to 0.80, and the verbalized-confidence parse rate collapses from 99% to 64%)."** Frames results as selective-prediction operating points; argues error-detection AUROC, not calibration error, is the exposing metric. **The single most damaging precedent — same thesis, VLM domain, no adversary, no audit budget.** The parse-rate number is also the decisive experimental-design warning (`ideas/20` §3). | ✅ abstract verbatim |
| **Kuang, Wong (Waterloo) — *Understanding vision transformer quantization robustness through the lens of out-of-distribution detection*** | arXiv **2602.01459**, 1 Feb 2026. ViT-S16 / DeiT-S16 / DeiT3-S16 (IN1k and IN22k) × {FP32, W8A8, W6A6, W4A8, W8A4, W4A4}; metrics top-1, NLL, AUPR-out. FP32→4-bit AUPR-out deltas **19.2%** (DeiT3-IN22k), **15.0%** (ViT-IN22k) vs **12.0%/9.5%** for IN1k. Establishes "detection degrades faster than accuracy" in vision. | ✅ full text |
| **Tong, Wang, Wan, Zhang, Dong, Yuan — *Does Compression Preserve Uncertainty? A Unified Benchmark for Quantized and Sparse LLMs via Conformal Prediction*** | arXiv **2606.01850**, 1 Jun 2026. 12 LLMs × compression configs × 5 NLP tasks. "(I) compression frequently **decouples accuracy from uncertainty**; (II) larger models absorb compression-induced uncertainty far more effectively than smaller ones; (III) **uncertainty inflation is often threshold-like rather than gradual**." The LLM-side decoupling result; (III) pre-empts any "cliff" narrative. | ✅ abstract |
| **von Rad, Cao, Geiger — *UniComp: A Unified Evaluation of LLM Compression via Pruning, Quantization, and Distillation*** | arXiv **2602.09130**, **EMNLP 2026 Main**. 7 techniques × 40+ datasets. "a deployment-critical **performance–reliability decoupling, where retained performance does not indicate preserved safety**, fairness and privacy"; consistent knowledge bias (factual recall preserved, reasoning/multilingual/instruction-following degrade). Main-conference status means reviewers will know it. | ✅ abstract + venue |
| **Oladri, Varadaraju Priya, Wu — *Silent Failures in Quantized LLM Reasoning: A Taxonomy-Based Analysis of Hollow Convergence and Failure Mode Shifts*** | arXiv **2607.09999**, 10 Jul 2026. 30,000 CoT outputs, 5 models (3B–14B) × {FP32, FP16, NF4} × 4 benchmarks; Cohen's κ = 0.906. "PTQ can **silently alter how LLMs reason even when task accuracy is preserved**" (max 3.1pp accuracy drop). Owns the "passes the benchmark, is broken" rhetorical frame. | ✅ abstract |
| **Bouguerra, Montoya, Gomez-Villa, Mraidha, Arnez — *Less Precise Can Be More Reliable: A Systematic Evaluation of Quantization's Impact on VLMs Beyond Accuracy*** | arXiv **2509.21173**, **ICML 2026**. >700k evaluation runs. **The opposite direction:** "quantization can simultaneously improve accuracy, calibration, OOD detection, and robustness to noise, though not to covariate shift or spurious correlations"; proposes a spectral-filtering mechanism (damping high-rank components → reliance on robust low-rank features); ~40% of W8A8 runs show *improved* ECE. **Destroys the round-10 outcome-robustness argument** — the green-light direction is already published. | ✅ abstract + venue |
| **Lu, Chen, Que, Luk, Fan — *Enhancing Trustworthiness with Mixed Precision: Benchmarks, Opportunities, and Challenges*** | arXiv **2511.22483**, **ASP-DAC 2026 Special Session**. Quantization × {adversarial robustness, fairness, machine ethics, OOD robustness}; instability across compression ratios; precision-ensemble voting improves trustworthiness metrics by up to **5.8%**. Occupies the "and here is the fix" half. | ✅ abstract + venue |
| **Xu, Gupta, Li, Bentham, Srikumar — *Beyond Perplexity: Multi-dimensional Safety Evaluation of LLM Compression*** | arXiv **2407.04965**, **Findings of EMNLP 2024**. Code: `github.com/zhichaoxu-shufe/Beyond-Perplexity-Compression-Safety-Eval`. Unstructured/semi-structured pruning + quantization across degeneration harm, representational harm, dialect bias, downstream performance. "quantization mostly preserves bias while pruning degrades quickly." The lineage citation for "don't evaluate compressed models on perplexity alone." | ✅ abstract + venue |

### The deployed-guardrail precedent — motivation and objection at once

| Ref | Detail | Status |
|---|---|---|
| **Fedorov, Plawiak, Wu, Elgamal, Suda, Smith, Zhan, Chi, Hulovatyy, Patel, Liu, Zhao, Shi, Blankevoort, Pasupuleti, Soran, Coudert, Alao, Krishnamoorthi, Chandra (Meta) — *Llama Guard 3-1B-INT4: Compact and Efficient Safeguard for Human-AI Conversations*** | arXiv **2411.17713**, 18 Nov 2024. 440MB, ~7× smaller than Llama Guard 3-1B, ≥30 tok/s on an Android CPU via ExecuTorch/XNNPACK. Pipeline = **prune (16→12 decoder layers, MLP 8192→6400, 1,123M params) + QAT 4-bit (torchao, per-token dynamic activation quant, rest of net BF16) + embedding quant to 4-bit + unembedding pruning 128k→20 outputs + distillation from Llama Guard 3-8B** (distillation alone worth +1.3pp F1). Table 1 metrics are **F1/FPR at one operating point** across 9 languages; English: LG3-8B 0.939/0.040, **LG3-1B 0.899/0.090**, LG3-1B-INT4 better than the 1B on English and ≥ on 5/8 non-English. **No AUROC, no ROC, no fixed-budget catch rate — the tail metric is precisely what is not reported.** Not PTQ: quality is actively recovered by training. | ✅ full text (`arxiv.org/html/2411.17713v1`) |

### AI-control neighbours new since round 10

| Ref | Detail | Status |
|---|---|---|
| **Sinha, Naik, Gillioz, Storf, Merkelbach, Barton-Cooper, Højmark, Hobbhahn (Apollo Research) — *Training Deliberative Monitors for Black-Box Scheming Detection*** | arXiv **2605.29601**, 28 May 2026. Action-only open-weight monitors distilled from a frontier teacher (SFT + RL) over a scheming spec; 5 training sets, 6 OOD agentic-misalignment benchmarks. Qwen3.5-27B monitor beats all low-cost frontier prompted monitors *and* Gemini 2.5 Pro at lower **marginal inference cost (token-metered USD per 1,000 evaluations)**; stronger frontier monitors cost **16–34×** more. Explicit **cost–performance Pareto frontier**, self-described as "practical low-cost, **low-FPR** alternatives." **Already owns the economic framing round 10 used as motivation.** | ✅ abstract |
| **Anik Jha — *Decorrelation Is Not Complementarity: Skill, Not Lineage, Governs Trusted-Monitor Ensembles*** | arXiv **2608.16190**, 17 Aug 2026. **24 open-weight monitors, 9 pretraining lineages, backdoored code, scored by pAUC at 10% FPR, spanning 0.028–0.803 (29×).** Agreement splits into shared-detectability signal (Spearman −0.25 w/ ensemble gain) and idiosyncratic error (+0.26), summing to ≈0 (+0.05); skill predicts agreement with the pool (ρ 0.84, n=24, p<0.0001); cross-lineage panels do not beat matched-capability panels (p=0.13); no correlation-weighted selection beats picking the single best monitor OOS. **The proposed apparatus already exists at scale, varying model identity instead of precision — and the 29× skill span is the sharpest "so what" objection to a quantization delta.** | ✅ abstract |
| **Han, Yan, Zhang — *More Rejective, Not More Discriminative: The Unit of Verification in Pre-Execution LLM Oversight*** | arXiv **2608.23941**, 25 Aug 2026, 37pp. Twin-prefix framework: each gold plan yields an error-injected prefix and a **matched clean twin**, judged at five nested review lengths; pre-registered **informedness = catch − false rejection**. "Catch alone misleads: rejecting everything catches everything." Informedness peaks at 1–2 actions for all six judges. **Adopt its discipline: never report catch rate without the matched clean series.** | ✅ abstract |
| **Phuong, Jenner, Simon, Ho, Shah, Farquhar, Coull (GDM) — *GDM AI Control Roadmap*** | arXiv **2607.13087**, 13 Jul 2026. TRAIT&R threat taxonomy over MITRE ATT&CK; Detection tiers D1–D4, Prevention/Response R1–R3; 15 tiered mitigations. **"Because controlling more capable models requires more costly interventions, we link specific defensive measures to evolving model capabilities."** The institutional motivation citation for monitor cost. | ✅ abstract |

### Generator-side quantization × safety alignment — saturated dead ground

Listed so related work can disclaim the whole line in one sentence. **Our object is a *detector's*
ranking quality; every paper below measures a *generator's* refusal behaviour or attack success rate.**

| Ref | Detail | Status |
|---|---|---|
| Kharinaev, Moskvoretskii, Shvetsov, Studenikina, Mikhail, Burnaev — *Investigating the Impact of Quantization Methods on the Safety and Reliability of LLMs* | arXiv **2502.15799**, 18 Feb 2025 (rev. 29 Jun 2025). OpenMiniSafety (1,067 questions), **66 quantized variants**, 4 safety benchmarks, 4,268 annotated QA pairs. PTQ *and* QAT can degrade safety alignment; no method consistently best. No detector metrics, no AUROC/FPR. | ✅ abstract |
| Q-resafe — quantization-aware safety patching | arXiv **2506.20251**. Reported ASR increases of up to 16.6% (Llama) / 11.5% (Gemma) at INT4/INT8 vs pre-quantization. | ⚠️ search-level |
| *The Joint Effect of Quantization and Sampling Temperature on LLM Safety Alignment: A Factorial Analysis* | arXiv **2606.29581**. AWQ INT4 within ~1.6pp of FP16 ASR for 7/8 models; SmolLM3-3B the exception (34.5%→44.1%). | ⚠️ search-level |
| Wang, Li, Zhang, Zhang, Ma, Cheng, Pan — *Hidden Reliability Risks in LLMs: Systematic Identification of Precision-Induced Output Disagreements* (PrecisionDiff) | arXiv **2604.19790**, 2 Apr 2026. Differential testing across bf16/fp16/int16/int8; jailbreak divergence — inputs refused at one precision produce harmful output at another. Closest generator-side analogue to our framing; cite to disambiguate. | ✅ abstract |
| QuantGuard — *Learnable Rounding for Repairing Quantization-Conditioned Backdoors in LLMs* (2606.29239); *Pruning for Protection* (2401.10862); *Towards Understanding and Improving Refusal in Compressed Models via Mechanistic Interpretability* (2504.04215); *Fine-Tuning, Quantization, and LLMs: Navigating Unintended Outcomes* (2404.04392) | The rest of the saturated line. | ⚠️ search-level |

### Verified negative results (worth as much as the positives)

arXiv API metadata search (title/abstract/comments), each returning **zero results** on 2026-09-01:

- `all:"trusted monitor" AND all:quantization`
- `all:"audit budget" AND all:quantization`
- `abs:"trusted monitoring" AND abs:quantiz*`
- `abs:"partial AUC" AND abs:quantization`

`abs:quantization AND abs:"selective prediction"` returns exactly two papers, one of which is
`2607.24440` itself. `"compression tax"` as a phrase returns one unrelated paper (2607.28263, a
context-memory paper). **The specific instantiation is unoccupied; the general claim is not.**

### Artifacts (verified available, `ideas/20` §4)

| Artifact | Detail | Status |
|---|---|---|
| `RoganInglis/apps-control-arena` (HF) | **5,000 rows, single `train` split, ungated**, ~6,958 downloads last month. Fields: `problem_id`, `question`, `inputs`, `outputs`, `difficulty`, `solutions` (with `compiles`/`passes_tests`), `backdoors` (code, trigger input, `source` ∈ {apps, control_tax}), `backdoor_works` flags, `is_nondeterministic`/`nondeterminism_score`/`nondeterminism_category`. Both honest and backdoored solutions, labelled. | ✅ dataset card |
| `RoganInglis/apps-backdoors`, `RoganInglis/control-tax` (HF) | Sibling datasets; `control-tax` is the Control-Tax paper's generated backdoors + exploits over APPS. | ✅ |
| `UKGovernmentBEIS/control-arena`, `control-arena.aisi.org.uk/settings/apps.html` | The APPS control setting: red team inserts backdoors, blue team's trusted monitor assigns suspiciousness. | ✅ |
| DSPy tutorial — *GEPA for Code Backdoor Classification (AI control)* (`dspy.ai/tutorials/gepa_trusted_monitor/`) | Public end-to-end trusted-monitor recipe on this data. The harness is a known-good recipe, not a build. | ✅ |

**Correction:** round 10's dataset composition (1,936 train / 482 val / 1,375 test at 50% attack
rate) came from a search summary and does **not** match the HF card (one 5,000-row split).
Construct and report your own splits; do not cite those numbers.

---

## Round 12 — the metric disjunction between AI control and the guardrail literature

> **⚠️ THE CENTRAL NEGATIVE IN THIS SECTION IS FALSE. See the round-13 section below.** The queries
> below are transport-clean and were genuinely run twice; they are also **abstract-scoped**, and the
> claim they were used to support is about what papers *report* in their results sections. Granite
> Guardian (`2412.07724`) publishes ROC curves and a nine-guard fixed-FPR leaderboard. The rows are
> kept because the *AI-control side* of the table is still accurate and still useful, and because
> `notes/12` R8 was bought with this mistake. **Do not cite the guardrail-side negatives.**

Surfaced by the round-12 sweep, then **independently re-verified locally** via the arXiv API on
2026-09-02. These negatives are load-bearing for candidate C6 in `ideas/21`, so they were run twice.

### Verified negative results (arXiv API, `opensearch:totalResults` read directly)

| Query | totalResults | Note |
|---|---|---|
| `abs:"fixed false positive rate" AND abs:"large language model"` | **0** | ❌ **False as stated.** `2412.07724` §5.1: "we also compute recall and AUC at fixed false positive rates (FPr) of 0.1, 0.01, and 0.001." |
| `abs:"guard model" AND (abs:"ROC" OR abs:"AUROC")` | **0** | ❌ **The inference drawn from this was false.** `2412.07724` publishes ROC curves (Fig. 8) and AUC/AUPRC tables; its *abstract* says none of these words. |
| `all:"guardrail" AND all:"audit budget"` | **0** | The control-native constraint never reaches the guardrail literature. |
| `abs:"guard" AND abs:"pAUC"` | **0** | ❌ **Same failure.** `2412.07724` App. D reports "partial AUC and TPr values across different FPr thresholds." |
| `all:"partial AUC" AND (all:"guardrail" OR all:"safety monitor" OR all:"moderation")` | **1** | And it is **1310.0900**, a *2013 pedestrian-detection* paper. |
| `abs:"audit budget" AND abs:"monitor"` | **6** | **All six are AI-control papers** — 2606.06529, 2602.04930, 2607.06596, 2607.14570, 2605.26047, 2506.05296. Not one guardrail paper. |

The last row is the cleanest statement of the finding: the phrase that defines the operating point in
AI control appears *only* inside AI control.

### What each side actually reports

**AI control — always a fixed FPR / audit budget:** 2605.26047 (0.3%), 2602.04930 (0.5%),
2606.06529 (1%), 2607.06596 (1%), 2605.29178 (≤2%), 2608.16190 (pAUC@10% FPR), 2506.05296 (explicit
auditing-budget constraints).

**Guardrails — never:**

| Guard | Ref | Metric reported |
|---|---|---|
| Llama Guard | **2312.06674** | AUPRC only; explicitly defers the threshold — AUPRC "is useful for **selecting the classification threshold** that balances precision and recall based on the specific requirements of use cases" |
| Llama Guard 3-1B-INT4 | **2411.17713** | F1 + FPR at one operating point |
| WildGuard | **2406.18495** | F1 at the model's own binary decode threshold |
| ShieldGemma | **2407.21772** | AU-PRC |
| Granite Guardian | **2412.07724** | ❗ **AUC *is* area under the ROC curve — this row falsified C6 and was recorded in the same round the claim was written.** Full detail in the round-13 section: ROC curves, AUPRC, and partial AUC + TPR at FPr 0.1/0.01/0.001 across nine guards. |
| GuardReasoner | **2501.18492** | F1 averaged over 13 benchmarks |
| Qwen3Guard | **2510.14276** | F1; its tri-class label yields exactly **two** operating points — strict mode "classifies controversial cases as unsafe", loose mode "treats them as safe" |
| Benchmarking Open-Source Guards | **2605.28830** | **Recall, and refuses FPR control on principle:** "recall is the critical metric for safety applications, as missing harmful content poses greater risk than false positives" |
| GuardEval | **2601.03273** | macro F1 |
| SoK: Jailbreak Guardrails | **2506.10597** | FPR reported as a free-floating scalar, never as a constraint; no ROC, no AUC, no threshold optimization |
| Constitutional Classifiers | **2501.18837** | Closest in the group: an FPR *delta* on real traffic — "absolute 0.38% increase in production-traffic refusals and a 23.7% inference overhead" |
| Prompt-injection defenses for tutors | **2605.06669** | The comparability failure in one line: "NeMo reaches 0 percent bypass at **16.22 percent FPR**… Prompt Guard yields 38.48 percent bypass with **3.60 percent FPR**" — two systems compared at unmatched operating points |

⚠️ Metric not confirmed from a fetched source, do not cite as fact: 2504.01081 (ShieldGemma 2),
2510.19169 (OpenGuardrails), 2503.06550 (BingoGuard), 2404.05993 (AEGIS).

### Supporting refs for the mechanism

| Ref | Detail | Status |
|---|---|---|
| Sun, Sun, Geng — *The Score Granularity Gap in Black-Box LLM Classification* | **2606.22179**. The instrument: verbalized confidence "ranks cases surprisingly well, yet takes only a handful of distinct values… offers an operator only a few coarse thresholds." Established on **general** black-box classification (9 LLMs, 3 benchmarks) — **not** on safety guard models, and not against an audit budget. | ✅ |
| *On Calibration of LLM-based Guard Models* | **2410.10414**. Guard models "produce overconfident predictions" and "exhibit significant miscalibration when subjected to jailbreak attacks"; advocates "incorporating reliability evaluation of confidence calibration when releasing future LLM-based guard models." **Measures ECE/confidence, never realized FPR at a target operating point** — the axis that distinguishes C6. | ⚠️ authors TBC |
| Rule-blindness audit | **2608.16852**. "Deleting, permuting, or substituting the governing rule leaves detection accuracy unchanged for every guard and activation probe we test." | ⚠️ authors TBC |
| *Policy Invariance* | **2605.06161**. "existing safety scores conflate what the agent did with how the evaluator was prompted"; introduces the Policy Invariance Score and Judge Card, exposing "an order-of-magnitude spread in judge reliability that is invisible to accuracy-only leaderboards." | ⚠️ authors TBC |

### Organizer collision check (gate G2)

**JUDGe 2026** ("Can We Trust the Judge?", Atlanta, **closed Aug 29** — a collision check, not a
target). Organizers: **Shanu Sushmita** (Northeastern/UW), **Jayash Koshal** (Meta/Northeastern),
**Meghana Makhija** (Amazon), **Hui Wan** (Google DeepMind), **Amjad Abu-Jbara** (Amazon Ads).
Keynote **Eugene Yan** (Anthropic); panel **Jennifer Wortman Vaughan** (MSR NYC), **Wei Xu**
(Georgia Tech), **Vijai Mohan** (GDM). No published ownership of the threshold/operating-point line
found among them — **G2 appears clear**, but the community is active here, so re-check before
submission.

---

## Round 13 additions — the adversarial review (`ideas/23`, `ideas/24`)

Every row below was confirmed by fetching `arxiv.org/abs/<id>` for title, full author list and date;
rows marked ✅+HTML additionally had `arxiv.org/html/<id>` fetched, tag-stripped and searched, because
a claim about the paper's *contents* is load-bearing (R1). The round-12 board's own core citations
were never entered here — that gap is closed below.

### The C6 kill

| Ref | Detail | Status |
|---|---|---|
| Padhi, Nagireddy, Cornacchia, Chaudhury, Pedapati, Dognin, Murugesan, Miehling, Santillán Cooper, Fraser, Zizzo, Hameed, Purcell et al. — *Granite Guardian* | arXiv **2412.07724** (2024-12-10). **The paper that kills C6.** §5.1 names AUPRC, "the area under the ROC curve (AUC)", F1, recall and precision, then: "we also compute **recall and AUC at fixed false positive rates (FPr) of 0.1, 0.01, and 0.001**… to evaluate performance under low FPr constraints (Aerni et al., 2024)." Figure 8 plots **ROC curves**. §6: "Real-time applications have a strong need for low FPr. Thus, threshold-based metrics (e.g., AUC and AUPRC) can mislead the quality evaluation of the model." **Table 11** reports AUC, AUC@0.1/0.01/0.001 and TPr@0.1/0.01/0.001 for **nine open guards** — Llama-Guard-7B / 2-8B / 3-1B / 3-8B, ShieldGemma-2B / 9B / 27B, Granite-Guardian-2B / 8B — using probability scores "suitably adapt[ed]" from each baseline. App. D text uses the phrase **"partial AUC"**. | ✅ +HTML |
| Aerni, Zhang, Tramèr — *Evaluations of Machine Learning Privacy Defenses are Misleading* | arXiv **2404.17399** (2024-04-26). The low-FPR evaluation discipline Granite Guardian imports, from privacy auditing. **This is the outside neighbour C6's G1 should have named** — and it was sitting in the reference list of the paper that falsified C6. | ✅ |
| Kezins, Ekka, Berrang, Arnaboldi — *Beyond Red-Teaming: Formal Guarantees of LLM Guardrail Classifiers* | arXiv **2605.10901** (2026-05-11). Certifies guardrail classifiers in pre-activation space; 42 occurrences of "threshold"; reports "coverage collapse" to 55% "at the optimal threshold" for BERT, recovered only "by adopting an extremely conservative pessimistic threshold." Threshold/operating-point discipline for guardrails, from the verification side. | ✅ +HTML |
| Kumar, Birur, Baswa, Agarwal, Harshangi — *No Free Lunch with Guardrails* | arXiv **2504.00441** (2025-04-01). Security-vs-usability tradeoff across Azure Content Safety, Bedrock Guardrails, OpenAI Moderation, Guardrails AI, NeMo and Enkrypt. | ✅ |
| Chu, Wang, Huang — *TWGuard: LLM Safety Guardrails for Localized Linguistic Contexts* | arXiv **2604.16542** (2026-04-17). 20 occurrences of FPR, 11 of AUPRC in full text — further evidence the guardrail literature reports FPR routinely. | ✅ +HTML |

### The C1 pre-emption

| Ref | Detail | Status |
|---|---|---|
| **Sahil Raut — *Eval-awareness steering detects the test, not the sabotage*** | **LessWrong, 2026-06-25.** Not on arXiv — see R9. Llama-3.1-8B; diff-in-means direction on a **format-controlled 2×2** eval/deploy dataset; steering α ∈ [−2,+2]; **ablation arm projecting the direction out**; noise injection as output-independent ground truth; **24 random-direction placebo controls**. Detects eval framing at ~0.81 AUROC; steering swing **−1.77pp** vs a pre-registered 5pp threshold; "does not beat the empirical null of 24 random directions (**p = 0.20**)"; per-item sandbagging prediction **0.542 AUROC**. Conclusion: "the direction directs the situational framing, not the capability-withholding behaviour." | ✅ page read |
| Devbunova — *Is Evaluation Awareness Just Format Sensitivity?* | arXiv **2603.19426** (2026-03-19). Controlled 2×2 + diagnostic rewrites; probes "primarily track benchmark-canonical structure and fail to generalize to free-form prompts independent of linguistic style." | ✅ |
| Nayan, Kumar, Girmal, Anilkumar, Vaidyanathan, Nader Palacio, Ghosh, Srinivasan — *Evaluation Awareness Is Not One Capability* | arXiv **2606.23583** (2026-06-22). 37 open-weight models, 7 families, 8 experiments. "probes retain AUROC 0.98 under rewrites that drive behavior below chance, and multi-layer steering causally moves three downstream tasks **while random controls do not**"; the three axes are weakly coupled (1/15 correlations significant). The "benchmark illusion." | ✅ |
| **Chaudhary — *In-Context Environments Induce Evaluation-Awareness in Language Models*** | arXiv **2603.03824** (2026-03-04), single author. **`ideas/21` mischaracterised this** as "about *inducing* eval-awareness, not probing it." It reports "CoT causal intervention confirms that **99.3% of sandbagging is causally driven by verbalized eval-aware reasoning**, ruling out shallow instruction-following" — a mediation result on C1's **claim**. Note the artifact `MaheepChaudhary/eval-aware-evasion` already in the ledger is this author's line. | ✅ |
| Mody, Agarwal, Mittal, Mahato — *Minimizing Targeted Activations: Input-Only Suppression of Evaluation-Awareness Latents* | arXiv **2607.25907** (2026-07-28). Source of the "a placebo suppresses as hard as the real direction" constraint. | ✅ |
| Zhuang, Aranguri — *Not All Eval-Awareness Is Equal: Capabilities Framing Predicts Compliance* | arXiv **2608.27340** (2026-08-27). Qwen3-32B on FORTRESS; capabilities-framing predicts compliance with a **+24 to +46 pp** gap over safety-framing; 10 of 11 CoT prefills shift compliance as predicted. "aggregate suppression rates can move while the safety-relevant component does not." | ✅ |
| Boxo, Neelappa, Raval — *Linear probes rely on textual evidence* | arXiv **2509.21344** (v1 2025-09-16, v2 2026-03-09). Sandbagging / Sycophancy / Bias; filtering costs 10–30 AUROC points; model organisms give **0.57 vs 0.94** (Sandbagging) and **0.57 vs 0.74** (Bias). **❌ No code, no data, no artifact statement** — the only GitHub links in the full text are LaTeXML and arXiv-feedback boilerplate. Its §C.5 organism is *passphrase-dependent sandbagging*, trained by the authors. Blocks C1 and C3 (R10). Its §7.2 names AO / attention probes / SAEs as future work — that is C3. | ✅ +HTML |

### The C8 constraint

| Ref | Detail | Status |
|---|---|---|
| Szablewski, Konar-Steenberg, Fornasiere, Menon, Heimersheim — *The Model Organism Lottery* | arXiv **2607.01033** (2026-07-01). **54 MOs** on `OLMo2-1B` **and** `gemma-3-1b-it`, **seven techniques** incl. post-hoc SFT, post-hoc DPO and integrated DPO into the OLMo post-training phase; benchmarks activation oracles, activation steering, logit lens and SAEs; controls for quirk-expression strength. Findings: interpretability depends on objective/behaviour/architecture/data pipeline; "substantial variance remains even after controlling for differences in the strength of target behaviour expression"; "integrated training often yields **less** interpretable MOs." §6 verbatim, and the sentence C8 is built on: "quirks instilled during **pre-training, SFT, or RLVR** may produce qualitatively different signatures. We expect that progressively earlier instillation would make quirks progressively harder to detect, as the training signal becomes even more diffuse and entangled with the broader learning process." §6 also states the models are "**likely too small** to support more sophisticated behaviours" and that reliance on the single CakeBake quirk is a limitation. | ✅ +HTML |
| Zhang, Rando, Evtimov, Chi, Smith, Carlini, Tramèr, Ippolito — *Persistent Pre-Training Poisoning of LLMs* | arXiv **2410.13722** (2024-10-17), ICLR 2025. Studies **instillation stage** and survival through post-training — a nearer outside neighbour to C8 than the "data fraction" framing `ideas/22` gave the poisoning literature. | ✅ (venue from proceedings listing) |
| Bouaziz, Videau, Usunier, El-Mhamdi — *Winter Soldier: Backdooring Language Models at Pre-Training with Indirect Data Poisoning* | arXiv **2506.14913** (2025-06-17). Pre-training-stage instillation, <0.005% poisoned tokens. | ✅ |

### The C7 neighbours

| Ref | Detail | Status |
|---|---|---|
| Ferreira, Aziz, Titov — *Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability?* | arXiv **2608.04928** (2026-08-05). Hint-reliance monitorability across explicit → weakly- → **strongly-supervised latent CoT**. Monitorability depends more on task properties and access level than on reasoning mode. §7 future work, verbatim and complete: "…via explicit-latent reasoning hybrids…, or, given that hint-reliance signal is retained in activations, **by reserving a subset of latent slots to be directly supervised for monitorability**; and (ii) whether latent reasoning states still expose hint-reliance **under optimization pressures such as RL, and which probes resist it**." **Both halves of C7 are the authors' own stated next step.** Also cites Wei et al. (2026), who "train an auxiliary decoder jointly with the model, supervising each latent state." | ✅ +HTML |
| Sun, Oikarinen, Ustun, Weng — *Concept Bottleneck Large Language Models* (CB-LLM) | arXiv **2412.07992** (2024-12-11), ICLR 2025. **The neighbour C7's G1 missed.** Builds a **hybrid concept-bottleneck layer plus an unsupervised layer** for LLMs — the free-slot escape hatch already exists in the nearest LLM architecture, precisely because a pure bottleneck loses information. Makes C7's leakage direction the expected answer rather than a discovery. | ✅ |

### The C9 neighbours

| Ref | Detail | Status |
|---|---|---|
| Fomin, David, LeVi — *Internal-State Probes Read the Situation, Not the Action* | arXiv **2606.30449** (2026-06-29). C9's premise. Three methods, three model families; Qwen direction separates fine-tune from base at AUC 1.000 yet crosses threshold on **0/143** audited pre-assistant contexts; best future-behaviour probe 0.801 AUC and **+5.1pp** over majority; cross-domain transfer non-positive on 5/6 ordered pairs. Already builds "a shared-prefix minimal pair" for the Gemma case. **Published at AIWILD — same-venue competitor.** Code `maxf-zn/misalignment_monitoring` ✅ HTTP 200, pushed 2026-07-02. | ✅ |
| Gardner, Artzi, Basmova, Berant, Bogin, Chen, Dasigi, Dua, Elazar, Gottumukkala, Gupta, Hajishirzi, Ilharco, Khashabi, Lin, Liu, Liu, Mulcaire, Ning, Singh, Smith, Subramanian, Tsarfaty, Wallace, Zhang, Zhou — *Evaluating Models' Local Decision Boundaries via Contrast Sets* | arXiv **2004.02709** (2020-04-06). **Contrast sets** — the canonical minimal-perturbation *evaluation* construction. This is C9's method under its established name, and `ideas/22` named neither it nor its literature. Must lead C9's related work. | ✅ |
| Pona, Kazemi, Du, Watson, Paoletti — *Abstract Counterfactuals for Language Model Agents* | arXiv **2506.02946** (2025-06-03). Counterfactual construction over **agent actions** above the token level, explicitly because LM-agent action spaces are "implicit in the strings they output"; token-level **and latent-space** interventions. C9's pair-construction machinery, already framed for this object. | ✅ |
| Ning, Jones, Zhang, Ye, Ruan, Li, Gupta, Sun — *When Actions Go Off-Task* (MisActBench) | arXiv **2602.08995** (2026-02-09). Realistic computer-use-agent trajectories with **human-annotated action-level alignment labels**; ships DeAction, a pre-execution guardrail. The nearest existing action-level labelled resource. | ✅ |

### Standing obligations from this round

- [ ] C9's related work must open with `2004.02709`, `2506.02946` and `2602.08995`, and must state that
      `2606.30449` already built a shared-prefix minimal pair. The contribution is the **agentic
      action-versus-situation construction under pre-registered criteria**, not matched pairs.
- [ ] `2410.10414` (guard-model calibration) is still ⚠️ authors TBC in the round-12 section and is no
      longer load-bearing now that C6 is dead — resolve or drop it.
- [ ] `2509.21173`'s **ICML 2026** attribution is unconfirmed (`notes/14`); the arXiv abstract page
      carries no venue field. Resolve or downgrade before any citation.
