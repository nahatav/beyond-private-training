# The plan — round 17: InfPriv Sep 7, *Authorship, not sabotage* Sep 12

Written 2026-09-03 (round 17), after [`ideas/29`](../ideas/29-round-17-three-axis-evaluation.md).
**Supersedes `notes/18`**, whose two killing checks have now run: K1 passed and dissolved its own premise
(one artifact, not two), K2 failed the round-16 framing and handed back a better one. `notes/18` is kept for
its §5 stopping-rule discipline and its November-window table, both of which survive.

Same discipline as `notes/09`, `notes/17` and `notes/18`: thresholds and stopping rules fixed **now**.

---

## 0. What changed, in one paragraph

Both September legs have **code and numbers** as of today (`experiments/`). InfPriv's decisive experiment
ran on the laptop in 34 seconds and its central figure is drawn; the only work left is prose. The Sep 12
paper is no longer "the metadata floor is above the published monitor" — that monitor number did not exist,
and the field already strips the leaks the round-16 version was going to announce. It is now: **the stored
honest/attack pairs behind the field's open code-backdoor monitoring numbers are human-written versus
LLM-written; a bag-of-words classifier that cannot read a backdoor scores above 20 of the 24 monitors ranked
on the field's own filtered split; a classifier that reads no code scores above 18; and five same-generator
agentic settings show what a floor looks like when authorship is removed.** The fresh-areas scan found
nothing that beats it on the three axes and one thing that broadens it (six corpora, two mechanisms).

## 1. The three tracks

| Deadline | Paper | State today |
|---|---|---|
| **Sep 7 AoE** | **InfPriv** — *Normalising Users Changes What Private Evolution Estimates* | E0/E1a/E1b done; figure drawn; bib resolved; scoop clean; G2 clear. **Writing only.** |
| **Sep 12 AoE** | ***Authorship, Not Sabotage*** — trivial baselines on AI-control monitoring benchmarks → **EvoRobust** (+ FLLMPT as a free dual) | Every CPU number exists. One control (same-generator honest code) and one figure set remain. |
| **Nov** | The authorship line across every stored-pair benchmark, or C9 | Decide Oct 2 against the AAAI-27 list. **No hours before Sep 13.** |

## 2. Schedule

The tracks are **serial for the human and trivial for the GPU**. Nothing below needs more than one rented
4090 for an afternoon.

| Day | InfPriv | Audit |
|---|---|---|
| **Sep 3 PM** | LaTeX skeleton; pre-flight items 2 and 6 (`notes/15`) | — |
| **Sep 4** | E4 widening (minutes); write §§1–3 | evening: draft the FLLMPT abstract (title + 150 words) from `ideas/29` §3.3 |
| **Sep 5** | Write §§4–6; figure polish | **Register the FLLMPT abstract before 23:00 GMT** — free, dual allowed. Not a target; an option. |
| **Sep 6** | Full draft; review against the unsubstantiated-claims policy | — |
| **Sep 7** | **Submit InfPriv** | — |
| **Sep 8** | — | **GATE S** (§3). Pull Jha's `runs/scores/` (24 monitors × 1,375 items, MIT); recompute the five agentic floors with task-grouped CV from `experiments/audit/scan/`. |
| **Sep 9** | — | Figures: protocol × baseline table; per-corpus floor bars with permutation nulls; monitor-vs-floor dot plot on the Koran split. Gate S result → headline branch. |
| **Sep 10–11** | — | Write four pages. First paragraph cites `2605.15377`, `2608.16190`, `2602.10153`, `2506.05296`, `2606.06529`, `2510.09462`; cites `1905.05778` against itself. |
| **Sep 12** | — | **Submit EvoRobust**; submit FLLMPT if the abstract was registered. |

## 3. GATE S — the same-generator control, Sep 8, and it decides the title

The APPS authorship claim needs honest code written by the *attack* model. Two routes, in order:

1. **Look first (R15).** `RoganInglis/vllm-control-arena` (HF, MIT, 200) holds model-generated APPS solutions
   with no labels — if those are honest LLM solutions to problems in the Koran filter, the control is free.
   Check its columns and generator before renting anything.
2. **Generate.** Rent one 4090; vLLM + `Qwen/Qwen2.5-Coder-7B-Instruct` (or the Llama-3.1-8B whose licence
   `notes/18` told us to accept); one solution per problem for the 3,420 problems with a passing human solution;
   run the shipped `inputs`/`outputs` tests on CPU; keep the passing ones. Order **1–2 GPU-hours, $5–10.**

Then rebuild the pairs (LLM-honest vs LLM-attack, comments stripped, Koran's filter) and rerun TF-IDF,
character-n-gram, length and the seven surface features.

**Routes, fixed now:**
- **Collapse** (TF-IDF ≤ 0.60 AUROC on same-generator pairs, having been 0.81 on stored pairs) → headline is
  **authorship**: *the benchmark as stored measures who wrote the code.* Title stands.
- **Partial** (0.60–0.72) → *authorship carries most of the signal; the remainder is surface content.* Title stands;
  abstract states the split.
- **No collapse** (> 0.72) → headline becomes **content**: *these backdoors are separable by surface features
  regardless of author, and LLM monitors underperform a linear model on them.* New title (*"A Linear Model Beats the
  Trusted Monitor"*), same figures, same recommendations. **Both directions are a paper.**
- **Route 2 fails by end of Sep 8** (generation or test harness will not run) → ship without the control. The
  transfer (99% across generators), inert-backdoor (95% on non-working backdoors) and style-marker evidence plus
  the five same-generator settings carry the authorship reading as *inference*, stated as such in Limitations.
  Do not spend Sep 9 debugging a generator.

**Never cut:** the exact-split comparison (train on Koran's paired train, score their 1,375); the metadata-only
floor on that split; permutation nulls beside every floor; the Feng self-citation; the six first-paragraph
citations; the release of the split and the scripts.

**Cut order if Sep 10–11 slips:** the CoT-regex paragraph (already a section, not a paper — `2607.09786`) →
the character-n-gram duplicate of TF-IDF → the fifth agentic setting.

## 4. What the paper is not

- Not *"nobody ran a trivial baseline"* — Jha's repo ships `--leak-check` with two of them. Credit it.
- Not *"the floor is above the published monitor"* — compare only on Koran's split with Jha's per-item scores.
- Not a CoT-monitoring paper — the 15-word scratchpad regex (AUROC 0.76–0.82 across five settings) is one
  paragraph; `2607.09786` owns the instrument.
- Not an AgentHarm paper — **excluded on G2**: Andriushchenko authored it and is an EvoRobust invited speaker.
- Not a claim that live ControlArena evals are wrong — they generate both classes; the artifact is in
  **training, selecting and benchmarking monitors on stored pairs**, which is what the cited papers and the
  reference tutorial do.

## 5. Stopping rules

- **InfPriv slips past Sep 6 without a full draft** → submit what exists on Sep 7: Propositions 1–3, the E0
  threshold finding, the E1 figure, and the arXiv anchor are already a complete 4-page note. There is no
  measurement left to wait for.
- **Gate S route 2 fails** → §3, ship without the control.
- **Sep 10–11 slip** → the Nov window (`notes/18` §7) takes the audit; InfPriv is already in. Nothing is lost
  but the slot — and the split, the scripts and the numbers are public either way.
- **Nothing about C9 is decided before Oct 2.**

## 6. Budget

| Item | Cost |
|---|---|
| InfPriv | **$0** (laptop). E4 widening on a rented GPU is optional and under $5. |
| Audit, Gate S generation | $5–10 |
| Audit, one same-harness prompted monitor on the regenerated pool (optional, strengthens the collapse claim) | $5–10 |
| **September total** | **≤ $25** of the $200–300 |

The surplus goes where `notes/11` says: a second task setting (done — five agentic settings), an adversarial arm
(not applicable — no adversary in a validity audit) and confidence intervals (permutation nulls and 5-fold folds,
done). Breadth buys nothing here.

## 7. Standing constraints, unchanged

Public datasets only · no experiments involving real people · nothing person-specific reported (`notes/08`).
Local open-weight models, no paid API. Verify every citation by fetching (**R1**); zeros with positive controls
(**R3**); read the setup sections, not just the greps (**R18**); recompute delegated numbers (**R17**).

## 8. Odds

| Path | P(submit) | P(accept ¦ submit) |
|---|---|---|
| InfPriv → Sep 7 | 0.95 | 0.55–0.70 |
| *Authorship, not sabotage* → EvoRobust Sep 12 | 0.80 | 0.45–0.55 |
| same → FLLMPT Sep 12 | 0.60 (only if the abstract is registered Sep 5) | 0.30–0.40 |

Ordering, not measurement. Both September legs clear `notes/17`'s single-track 0.15–0.22 on their own, and for
the first time the risk on both is the writing, not the science.
