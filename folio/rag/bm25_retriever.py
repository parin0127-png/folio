from folio.imports import get

STOPWORDS = set(get("nltk_stopwords"))

def tokenize(text):
    tokens = text.lower().split()
    filtered = [t for t in tokens if t not in STOPWORDS]
    return filtered if filtered else tokens
class BM25Retriever:
    def __init__(self, chunks):
        self.chunks = chunks
        self.bm25 = get("bm25")([tokenize(chunk["text"]) for chunk in chunks])

    def search(self, query, k = 5):
        np = get("numpy")
        scores = self.bm25.get_scores(tokenize(query))
        top_k = np.argsort(scores)[::-1][:k]
        return [self.chunks[i] for i in top_k]

    