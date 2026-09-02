from folio.rag.vector_retriever import VectorRetriever
from folio.rag.bm25_retriever import BM25Retriever

class HybridRetriever:
    def __init__(self, chunks, embedder):
        self.bm25 = BM25Retriever(chunks)
        self.vector = VectorRetriever(chunks, embedder)

    def search(self, query, k = 5):
        bm25_search = self.bm25.search(query, k = k)
        vector_search = self.vector.search(query, k = k)

        scores = {}
        for rank, chunk in enumerate(bm25_search):
            chunk_id = chunk["chunk_id"]
            scores[chunk_id] = scores.get(chunk_id, 0) + 1 / (rank + 1)

        for rank, chunk in enumerate(vector_search):
            chunk_id = chunk["chunk_id"]
            scores[chunk_id] = scores.get(chunk_id, 0) + 1 / (rank + 1)


        all_chunks = {c["chunk_id"]: c for c in bm25_search + vector_search}
        ranked = sorted(scores, key = scores.get, reverse = True)[:k]
        return [all_chunks[chunk_id] for chunk_id in ranked]

    