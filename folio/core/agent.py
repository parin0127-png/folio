from folio.rag.pipeline import RAGPipeline
from folio.config import mistral
class Agent:
    def __init__(self, enable_rag = False, enable_mcp = False, 
                 verbose = False, agent_prompt = None, 
                 brain_model="openai/gpt-oss-20b",
                 agent_model="mistral-small-latest"):
        
        self.enable_rag = enable_rag
        self.enable_mcp = enable_mcp
        self.rag = RAGPipeline() if enable_rag else None
        self.verbose = verbose
        self.history = []
        self._loaded = {}
        self.brain_model = brain_model
        self.agent_model = agent_model
        self.agent_prompt = agent_prompt

    def _load(self):
        if "core" in self._loaded:
            return

        try:
            from folio.core.brain import _brain, convert_json
            from folio.core.agent_executor import run_agent
            from folio.core.compressor import compress

        except ImportError as e:
            raise ImportError(
                f"Folio is missing a required dependency: {e}\n"
                "Run: pip install folio[full]"
            )

        self._loaded["core"] = (_brain, convert_json, run_agent, compress)

    def ingest(self, file_path: str = None):
        if not self.enable_rag:
            raise ValueError("enable_rag=True required.")
        self.rag.ingest(file_path)

    def run(self, task):
        self._load()
        _brain, convert_json, run_agent, compress = self._loaded["core"]

        if self.enable_rag and self.rag.retriever is not None:
            results = self.rag.search(task)
            if results:
                context = "\n\n".join([r["text"] for r in results])
                res = mistral.chat.completions.create(
                model="mistral-small-latest",
                messages=[
                    {"role": "system", "content": "Answer the user question using only the context provided."},
                    {"role": "user", "content": f"Question: {task}\n\nContext: {context[:500]}"}
                ]
            )
                print(res.choices[0].message.content)
                return

        if len(self.history) >= 8:
            summary = compress(self.history)
            self.history = [{"user": "summary", "agent": summary}]

        plan = _brain(task,model = self.brain_model)

        if self.verbose:
            print(f"> Plan: {plan}")

        converted = convert_json(plan)
        # print("> PLAN:\n", plan)    
        run_agent(converted, task, model=self.agent_model, system_prompt = self.agent_prompt)
        self.history.append({"user": task, "agent": plan})
        