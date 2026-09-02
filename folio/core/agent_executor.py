from folio.core.data_clean import cleaner
from folio.core.agent1 import run_agent_1
from folio.core.agent2 import agent_2
from folio.core.agent3 import agent_3
from folio.core.observer import Observer
import json

observer = Observer()
memory = {}

def execute_agent(agent_name, payload, model, system_prompt = None):
    try:
        if agent_name == "agent_1":
            return run_agent_1(payload)

        elif agent_name == "agent_2":
            if system_prompt is None:
                return agent_2(payload, model = model)
            
            return agent_2(payload,
            model=model,
            prompt=system_prompt) 

        elif agent_name == "agent_3":
            return agent_3(payload)

        return None
    except Exception as e:
        return f"> [ERROR] - [{e}]"


def run_agent(data, user_task, model = None, system_prompt = None):
    try:
        memory.clear()
        memory["task"] = user_task

        if isinstance(data, str):
            data = json.loads(data)

        for agent_name, step in data.items():
            for s in step:
                tool_name = s["tool_name"]
                job = s.get("job", "")
                input_key = s.get("input_key", "task").strip()
                output_key = s.get("output_key", "result").strip()

                if input_key == "task":
                    query = s.get("input", "") or user_task
                else:
                    keys = [k.strip() for k in input_key.replace(";", ",").split(",")]
                    
                    previous = "\n\n".join(str(memory.get(k, "")) for k in keys)
                    explicit_input = s.get("input", "")
                    query = f"{user_task}\n\n{explicit_input}\n\n{previous}"

                # print("> MEMORY:", memory)

                payload = {
                    "tool_name" : tool_name,
                    "query" : query
                } 
                result = execute_agent(agent_name, payload, model, system_prompt)

                result, used_tool = observer.watch(tool_name, job, query, result, memory)


                if used_tool != tool_name:
                    print(f"> [Observer] Switching {tool_name} -> {used_tool}")

                    payload = {
                        "tool_name": used_tool,
                        "query" : query
                    }
                    print(f"> EXECUTING: {agent_name} -> {tool_name}")

                    result = execute_agent(agent_name, payload, model, system_prompt)
                     

                result = cleaner(used_tool, result)
                memory[output_key] = result

                print(result)
                print("<>" + "--" * 30 + "--------" + "<>")

    except Exception as e:

        import traceback
        traceback.print_exc()

        return f"> [Error] in running agents please try again: [{e}]"