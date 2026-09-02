from folio.rag.loader import DocumentLoader
from folio.rag.chunk import RecursiveSplitter
from folio.rag.embedder import Embedder
from folio.rag.vector_store import VectorStore
from folio.rag.hybrid_retriever import HybridRetriever
from folio.rag.reranker import Reranker

class RAGPipeline:
    def __init__(self, db_path = "rag_db"):
        self.embedder = Embedder()
        self.store = VectorStore(db_path)
        self.reranker = Reranker(self.embedder)
        self.retriever = None


    def ingest(self, file_path, chunk_size = 500, overlap = 50):
        text = DocumentLoader().load(file_path)
        chunks = RecursiveSplitter(chunk_size, overlap).split(text, source = file_path)
        embedding = self.embedder.embed_many([c["text"] for c in chunks])
        self.store.add(chunks, embedding)
        self._build_retriever()


    def _build_retriever(self):
        stored_chunks = self.store.get_all()
        self.retriever = HybridRetriever(stored_chunks, self.embedder)

    def search(self, query, k = 10, top_k = 3):
        if self.retriever is None:
            self._build_retriever()
        results = self.retriever.search(query, k = k)
        return self.reranker.rerank(query, results, top_k = top_k)
    