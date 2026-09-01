# What InfPriv will actually accept — calibrated from the committee's own output

## The venue this really is

Several organizers publish their short work at **TPDP** (Theory and Practice of Differential
Privacy). Confirmed TPDP 2026 papers from this committee: **MAPLE** (Eli Chien et al.),
**DPrivBench** (Erchi Wang, Pengrun Huang, Om Thakkar, Kamalika Chaudhuri, Yu-Xiang Wang,
Ruihan Wu), *The Access–Similarity Lens* (Chien et al.), *Do LLMs Really Forget?* (Wei, Niu, Hsu,
Ruihan Wu, …, Chaudhuri, Milenkovic, Pan Li).

So InfPriv is best modelled as **TPDP with an LLM-deployment skin**. That tells us the accepted
form factor: a *short, self-contained, technically exact note*. Not a system, not a survey, not a
sprawling benchmark.

## The house style, from Honkela's recent output

Antti Honkela's 2026 papers are the clearest template on the committee:
- *On Choosing the μ Parameter in Gaussian Differential Privacy* (arXiv 2606.09582, Kulynych &
  Honkela) — one parameter, one principled mapping, done.
- *Accuracy-First Rényi DP and Post-Processing Immunity* (arXiv 2509.22213, Räisä, Koskela,
  Honkela) — which definitions survive post-processing, which don't.
- *Privacy Leakage via Output Label Space and DP Continual Learning* (arXiv 2411.04680 / Apr 2026,
  Tobaben et al.) — **identifies the output label space as an unaccounted privacy side-channel.**

That third one is the archetype to imitate: *"here is a channel the accounting silently omits,
here is where it bites, here is the fix."* Small, exact, surprising, cheap to verify.

## What is already occupied by the people in the room

Do not propose these. Each is an organizer's or speaker's own current line.

| Territory | Owner | Artifact |
|---|---|---|
| Private Evolution + all its extensions | Zinan Lin (speaker) | PE-1/2, APIs-3 simulators, **Tab-PE (ICML 2026)**; **adopted by Apple** |
| Multi-query private RAG, Rényi filters | Ruihan Wu, Erchi Wang, Yu-Xiang Wang (organizers) | Private-RAG, arXiv 2511.07637 |
| LLM reasoning about DP | Erchi Wang, Chaudhuri, Yu-Xiang Wang, Ruihan Wu (organizers) | DPrivBench, arXiv 2604.15851 |
| Contextual integrity of persistent agent memory | Mireshghallah + Chaudhuri (organizers) | **CIMemories, ICLR 2026**; ConfAIde |
| Agent guardrails, LLM privacy benchmarking | Chulin Xie (speaker) | LLM-PBE, PriGuardAgent, GuardAgent |
| Unlearning + DP, per-instance privacy | Eli Chien (organizer) | Langevin Unlearning; *Do LLMs Really Forget?* |
| DP reconstruction bounds | Saeed Mahloujifar (speaker) | Bounding Training Data Reconstruction in DP-SGD |
| PE metadata augmentation | Eli Chien (organizer) | MAPLE, arXiv 2603.19258 |
| Private RAG / retrieval top-k — **the whole line** | Ruihan Wu + Kamalika Chaudhuri (organizers) | arXiv **2412.04697** (in addition to 2511.07637) — round-8 finding |
| DP-ICL with nearest-neighbour retrieval | Antti Koskela (organizer) | arXiv **2511.04332** (Koskela, Kulkarni, Zumot) |
| "LLM helps humans implement DP" (scaffolding) | Yu-Xiang Wang (organizer) | **DPCheatSheet**, arXiv **2509.12590** |

**Operating rule:** the good ideas adjacent to these lines are already theirs. Aim one step to the
side — close enough that they care, far enough that they are not writing it.

## Scoring rubric used in the portfolio

- **Novelty** — verified against the literature, not assumed.
- **Scoop risk** — is it the obvious next paper someone has already announced?
- **Outcome-robust** — does the paper still exist if the headline measurement comes out the
  boring way? With a 7-day clock this is the single most valuable property.
- **Resource honesty** — dataset access friction is the usual hidden killer, not GPU hours.
