"""Shared helpers for the InfPriv E0/E1a hour-one measurements.

Everything here is synthetic and carries no real identities.
"""

import numpy as np
import pandas as pd

from pe.data import Data
from pe.embedding.embedding import Embedding
from pe.constant.data import CLIENT_ID_COLUMN_NAME, LABEL_ID_COLUMN_NAME

RAW_COLUMN = "RAW_EMBEDDING"


class PrecomputedEmbedding(Embedding):
    """Pass-through 'embedding' that copies an already-computed vector column.

    Lets us drive DPSDA's real ``NearestNeighbors.compute_histogram`` without
    loading any generative model.
    """

    def compute_embedding(self, data):
        df = data.data_frame.copy()
        df[self.column_name] = df[RAW_COLUMN]
        return Data(data_frame=df, metadata=data.metadata)


def unit(x, axis=-1):
    return x / np.linalg.norm(x, axis=axis, keepdims=True)


def make_corpus(U=200, m=10, d=64, c=0.5, V=2000, seed=0):
    """Build a controlled user-structured corpus.

    Each of ``U`` users has a random unit centroid; each of their ``m`` samples is
    ``c * centroid + (1 - c) * noise``, renormalised to the unit sphere.  ``c``
    is the within-user coherence knob.  The candidate pool is ``V`` random unit
    vectors in the same space.

    Returns (priv_emb [U*m, d], client_ids [U*m], syn_emb [V, d]).
    """
    rng = np.random.default_rng(seed)
    centroids = unit(rng.standard_normal((U, d)))
    noise = unit(rng.standard_normal((U, m, d)))
    samples = c * centroids[:, None, :] + (1.0 - c) * noise
    priv = unit(samples).reshape(U * m, d).astype(np.float32)
    client_ids = np.repeat(np.arange(U), m)
    syn = unit(rng.standard_normal((V, d))).astype(np.float32)
    return priv, client_ids, syn


def to_data(emb, client_ids=None):
    df = pd.DataFrame({RAW_COLUMN: list(emb)})
    df[LABEL_ID_COLUMN_NAME] = 0
    if client_ids is not None:
        df[CLIENT_ID_COLUMN_NAME] = client_ids
    return Data(data_frame=df, metadata={"iteration": 0})


def vote_matrix(ids, client_ids, n_syn):
    """Per-user aggregate vote vectors v_u, shape [U, n_syn], integer counts.

    ``ids`` is the [n_priv, k] array of nearest-neighbour candidate indices, i.e.
    exactly what DPSDA's backend ``search`` returns.
    """
    users = np.unique(client_ids)
    V = np.zeros((len(users), n_syn), dtype=np.float64)
    for i, u in enumerate(users):
        rows = ids[client_ids == u].ravel()
        np.add.at(V[i], rows, 1.0)
    return V


def user_stats(Vmat, k, m):
    """d_u, and user mass w_u(p) for the normalisation family."""
    l1 = np.abs(Vmat).sum(axis=1)
    l2 = np.linalg.norm(Vmat, axis=1)
    l15 = (np.abs(Vmat) ** 1.5).sum(axis=1) ** (1.0 / 1.5)
    d_u = (l1 / l2) ** 2
    return {
        "l1": l1,
        "l2": l2,
        "l1p5": l15,
        "d_u": d_u,
        "ratio": d_u / (k * m),
        "w_record": l1,                 # k * m_u  (DPSDA divides by sqrt(k) globally)
        "w_p1": l1 / l1,                # identically 1
        "w_p1p5": l1 / l15,
        "w_p2": l1 / l2,                # == sqrt(d_u)
    }
