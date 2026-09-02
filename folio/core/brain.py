from folio.config import groq
from folio.core.agent_router import AGENT_EXAMPLES
from task.splitter import split_task
from task.validator import validate_tasks
from task.pipeline import build_plan, flow_to_text

import os
import json
import time

sys_prompt = """Use only the given flow.

Format:
agent|tool|job=description|input=value|in=key|out=key

Example:
agent_2|wikipedia_search|job=get information|input=Rohit Sharma|out=wiki

Rules:
- Use ONLY tools in Flow.
- Never add a tool.
- Follow Flow order.
- input= literal input.
- in= previous output.
- Return only the plan.
- Use ONLY tools in Flow.
- Never add a tool.

Flow: {flow}
Task: {task}"""

def count_tokens(text: str) -> int:
    return len(text.split())

def _brain(message, model = "openai/gpt-oss-20b"):
    retry = 0
    try: 
        tasks = split_task(message)

        tasks = validate_tasks(tasks, message)

        flow = build_plan(tasks)

        flow_text = flow_to_text(flow)
        

        prompt = sys_prompt.format(
            task=message,
            flow=flow_text,
        )
        # print(prompt)
        print("-----------------------------------------------")
        while retry < 3:
            try:
                res = groq.chat.completions.create(
                model = model,
                reasoning_effort = "low", 
                messages = [
                        {"role": "system" , "content" : prompt},
                        {"role": "user", "content": message}
                    ],
                )
                print("> TOKENS: ",res.usage.total_tokens)
                return res.choices[0].message.content
            except Exception as b:
                error_msg = str(b)
                if "429" in error_msg:
                    if "per minute" in error_msg or "tpm" in error_msg:
                        time.sleep(5)
                        retry += 1
                    else:
                        break
                else:
                    print(f"> LLM Error: {b}")
                    os._exit(0)
                


    except Exception as e:
        return f"> System error: {e}"
            
def convert_json(text):
    results = {}
    outputs = set()

    for line in text.strip().splitlines():
        p = line.split("|")

        if len(p) < 3:
            continue

        agent, tool, job = p[:3]
        data = {
            "job" : job,
            "tool_name" : tool
        }   

        input_value = None
        input_key = None

        for x in p[3:]:
            if x.startswith("input="):
                input_value = x[6:]

            elif x.startswith("in="):
                key = x[3:]
                if key in outputs:
                    input_key = key

            elif x.startswith("out="):
                key = x[4:]
                data["output_key"] = key
                outputs.add(key)

        if input_value in outputs:
            input_key = input_value

        elif input_value:
            data["input"] = input_value

        if input_key:
            data["input_key"] = input_key

        results.setdefault(agent, []).append(data)

    return json.dumps(results, indent=2)