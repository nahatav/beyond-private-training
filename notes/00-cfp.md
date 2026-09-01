# InfPriv @ NeurIPS 2026 — CFP digest

**Workshop:** *Beyond Private Training: The New Landscape of AI Privacy (InfPriv)*
**Venue:** NeurIPS 2026, Sydney, Australia — Dec 11 or 12, 2026
**Site:** https://beyond-private-training.ai.studio/#cfp

## Deadlines (all 23:59 AoE, strict)
| Milestone | Date |
|---|---|
| Regular submission (≤4 pages) | **2026-09-07** |
| NeurIPS fast-track (rejected/accepted NeurIPS papers + reviews appended) | 2026-09-25 |
| Author notification | 2026-09-29 |
| Camera-ready | 2026-11-30 |

*Today is 2026-08-31 → **7 days** to the regular deadline.*

## Format
- NeurIPS LaTeX template, **≤4 pages** excluding references/appendix. No checklist needed.
- Double-blind on OpenReview. ≥3 reviews guaranteed.
- Prior work accepted at conferences after Dec 2025 allowed, but **deprioritized for orals** — novel/ongoing work preferred.
- **Strict LLM policy:** hallucinated/fabricated references → desk reject. Every citation must be verified.

## Thesis of the workshop
Training-time DP (DP-SGD) is computationally prohibitive for foundation models. The field has
moved to non-finetuning paradigms: agents, ICL, inference-only synthetic data. The workshop
wants privacy work relocated to **inference time**, plus **AI for Privacy** — "leveraging LLMs as
active infrastructure to enforce, redact, and **verify mathematical guarantees**."

## Topics
1. **Privacy for Agentic Systems** — single/multi-agent risks, measurement, protective architectures.
2. **Inference-only Private Synthetic Data** — private evolution, private prediction, no training.
3. **Privacy in In-Context Learning** — prompt leakage, PII extraction from context, private ICL.
4. **AI for Privacy** — LLMs to automate sanitization, build privacy filters, *optimize the design of
   private algorithms*, and *advance the theoretical foundations of DP*.
5. **Other emerging inference-time privacy problems.**
6. **Benchmarks and Evaluation** — new benchmarks, auditing frameworks, metrics.

## Who is in the room (calibrates what will land)
**Speakers:** Zinan Lin (MSR — Private Evolution), Chulin Xie (GDM — LLM-PBE, PriGuardAgent,
GuardAgent), Mihaela van der Schaar (Cambridge — SynthCity), Dinh Thai Hoang (UTS — FHE/DRL),
Saeed Mahloujifar (FAIR — DP reconstruction bounds).

**Organizers:** Eli Chien (NTU — unlearning), Ruihan Wu (OpenAI), Kamalika Chaudhuri (GDM/UCSD),
Yu-Xiang Wang (UCSD — practical DP, watermarking), Niloofar Mireshghallah (humans&/CMU — LLM
privacy, contextual integrity), Erchi Wang (UCSD — **DPrivBench**, private RAG, inference-time
privacy), Jiachen "Tianhao" Wang (Princeton — data-centric TML), Antti Honkela (Helsinki — DP).

### Reading of the committee
Roughly half are **DP theorists** and half are **LLM-privacy empiricists**. A paper that is *only*
an LLM benchmark competes with a crowded field; a paper that is *only* theory misses the
workshop's applied pitch. The sweet spot is an **empirical result with a DP-theoretic hook** —
something where DP theory makes a falsifiable prediction that we then measure.

The CFP name-drops **DPrivBench** (organizer Erchi Wang's own work) under "AI for Privacy". Work
that extends or stress-tests it has a built-in sympathetic reviewer.
