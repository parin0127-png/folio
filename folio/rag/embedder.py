from folio.imports import get


class Embedder:
    def __init__(self, model_name = "all-miniLM-L6-v2"):
        self.model_name = model_name
        self._model = None  

    def _get_model(self):
        if self._model is None:
            self._model = get("sentence_transformer")
        return self._model
    
    def embed(self, text):
        return self._get_model().encode([text])[0]

    def embed_many(self, texts):
        return self._get_model().encode(texts)