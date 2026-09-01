# Permissibility, data, and compute

Constraints: **public datasets only · one local GPU · no experiments involving real people.**
Everything below is checked against those.

## Is this research allowed?

**Yes, and it stays that way under the plan in `ideas/09`.** Specifically:

- **No human-subjects research.** No recruitment, no intervention, no interaction with people, no
  new collection of data about anyone. Everything is secondary analysis of already-public corpora.
  This is not human-subjects research under the Common Rule and needs no IRB.
- **No attack on any real person's privacy.** We are not re-identifying anyone, not linking across
  datasets, not inferring sensitive attributes about individuals, and not publishing anything about
  a specific person.
- **No third-party systems touched.** No probing of live APIs, no auditing of anyone's production
  service. Local models on local hardware, reading public corpora.

### The one thing that deserves an honest flag

The lead idea needs records **grouped by person** in order to measure how one person's
contributions behave. A privacy paper doing identity-grouping should say why that is fine:

1. The groupings are already published as part of the corpus (authorship on arXiv), so no linkage
   is being created that did not exist.
2. Nothing person-specific is reported. The output is an aggregate distribution over a
   *structural* statistic (vote concentration). No individual appears in any result.
3. **The controlled arm needs no real identities at all** (see below), and it carries the
   scientific weight. Real-data grouping only anchors one point on the curve.

That third point is the important one, and it is a design improvement rather than a concession —
see "Why the controlled design is also better science."

## Dataset licences — checked

| Corpus | Licence / access | Verdict |
|---|---|---|
| **arXiv metadata + abstracts** | **CC0 1.0 Universal public-domain dedication.** arXiv distributes all metadata *including abstracts* under CC0. Bulk access via OAI-PMH, GCS bucket, or the Kaggle mirror. No agreement, no restrictions. | **Use this.** Cleanest option available. |
| **PubMed abstracts** | Free via NCBI E-utilities; authorship is public bibliographic record. Abstract copyright varies by publisher, so avoid redistributing text — derive statistics only. | Usable as a second anchor. |
| **Yelp Open Dataset** | "Intended for educational use", behind a click-through **Dataset Terms of Use**. Real individuals' reviews with pseudonymous `user_id`. Widely used academically (Aug-PE itself uses it). | **Avoid.** Adds a licence agreement and is data about real individuals, for no scientific gain over arXiv. |
| **OpenReview ICLR 2023** | Public reviews. | **Cannot support the user-level arm** — reviewers are anonymous, so there is no person to group by. |
| MIMIC / PhysioNet | Credentialed; CITI training required | **Excluded.** Timeline alone rules it out. |

**Decision: arXiv (CC0) as the primary corpus, PubMed as an optional second anchor. Yelp dropped.**

## Why the controlled design is also better science

The claim under test is a *relationship*: within-person semantic similarity → vote concentration →
user-level sensitivity. Observing that relationship on one corpus is a single data point, and it
confounds the effect with whatever that corpus happens to look like.

Better: **construct groups with a controlled within-group similarity parameter** and sweep it.
That produces a curve — sensitivity as a function of intra-user coherence — which is a stronger and
more general result, needs no real identities, and lets a reader place *their own* deployment on
the axis. The real-data anchor then answers one question only: where does naturally-occurring
authorship sit on that curve?

So the constraint and the better methodology point the same way.

## Compute — fits one GPU comfortably

| Stage | Cost | Notes |
|---|---|---|
| Vote-concentration sweep (the central figure) | **~1 GPU-hour** | Embeddings + FAISS nearest-neighbour only. No generation. Arguably CPU-feasible. |
| Real-data anchor (arXiv by author) | ~1 GPU-hour | Same pipeline, real groupings. |
| Utility curves for user-level PE | ~2–4 GPU-hr per run × ~12 runs → **1–2 GPU-days** | Local 8B generator under vLLM. Only needed for the full paper, not the core claim. |
| Downstream utility eval | minutes | BERT-base fine-tune. |

Embedding model is <1 GB. FAISS has a GPU index (aug-pe already uses
`faiss.index_cpu_to_gpu`). **Nothing here needs more than one workstation GPU, and the decisive
experiment needs an hour of it.**

## Confirmed from reading aug-pe source (not from a summary)

Downloaded `main.py`, `dpsda/dp_counter.py`, `dpsda/data_loader.py` and read them directly.

- The noise is exactly one line, `dp_counter.py:53`:
  ```python
  count += (np.random.normal(size=len(count)) * np.sqrt(num_nearest_neighbor)
            * noise_multiplier)
  ```
  Each private sample votes for its `num_nearest_neighbor` closest candidates, contributing ℓ₂ norm
  √k, and the noise scales by √k to match. **This is direct code-level confirmation of the
  record-level assumption my lead idea is about**: the sensitivity is a per-*sample* quantity, with
  nothing anywhere that accounts for one person contributing several samples.
- Thresholding (`np.clip(count, a_min=threshold); count -= threshold`) is post-processing on the
  noisy count — fine, no issue.
- `np.random.normal` is the standard insecure float sampler (Mironov). Already-worked territory;
  footnote at most.

## Open check worth an hour, not yet a claim

`dp_counter.py:46` folds votes by modulo when `num_packing > 1`:
```python
count[k % num_true_public_features] += counter[k]
```
If a sample's `k` nearest neighbours can fold onto the *same* bin, its ℓ₂ contribution would be up
to `k` rather than `√k`, while the noise only scales by `√k`. That would be a sensitivity
under-estimate. **This is a hypothesis, not a finding** — the intended semantics may preclude
collisions, and `num_packing` may be 1 throughout the text pipeline. It needs the packing path read
end-to-end before anyone says a word about it publicly, and if it were real it would warrant private
disclosure to the authors before publication, not a workshop paper.
