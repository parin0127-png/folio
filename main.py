import os
from folio._mcp.client import ready
from folio.core.compressor import compress
from folio.core.agent_executor import run_agent

ready.wait()

from folio.core.brain import _brain, convert_json
history = []
try:
    while True:
        task = input("> ")
        if task.lower() == "exit":
            os._exit(0)
        if len(history) >= 8:
            print("> Compressing history........")
            summary = compress(history)
            history = [{"user": "summary", "agent": summary}]
            print(f"> Compressed:\n{summary}")
        
        result = _brain(task)
        print(f"> Result: {result}")
        convert_ = convert_json(result)
        # print("> JSON: ", convert_)
        run_agent(convert_, task)

        history.append({"user": task, "agent": result})


except KeyboardInterrupt:
    os._exit(0)
except Exception as e:
    import traceback
    traceback.print_exc()
    os._exit(0)
    