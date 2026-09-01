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
