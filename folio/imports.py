_cache = {}

def get(name):
    if name not in _cache:
        _cache[name] = _load(name)
    return _cache[name]

def _load(name):
    if name == "spacy":
        import spacy
        return spacy.load("en_core_web_sm")

    if name == "sentence_transformer":
        from sentence_transformers import SentenceTransformer
        return SentenceTransformer("all-MiniLM-L6-v2")

    if name == "bm25":
        from rank_bm25 import BM25Okapi
        return BM25Okapi

    if name == "kuzu":
        import kuzu
        return kuzu

    if name == "nltk_stopwords":
        from nltk.corpus import stopwords
        import nltk
        nltk.download("stopwords", quiet = True)
        return stopwords.words("english")

    if name == "numpy":
        import numpy as np
        return np

    if name == "cosine_similarity":
        from sklearn.metrics.pairwise import cosine_similarity
        return cosine_similarity


    raise ValueError(f"Unknown import: {name}")