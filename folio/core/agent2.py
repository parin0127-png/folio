from folio.config import mistral
from folio._mcp.client import call_tools, get_schema
import json, time

def agent_2(payload: dict, model, prompt="Return the tool result."):
    try:
        data = payload
        tool_name = data["tool_name"]
        task = data["query"]
        schema = get_schema(tool_name)

        messages = [
                    {"role" : "system", "content":"""Use the tool {tool_name}.
                    Use the provided input exactly when filling the tool arguments.
                    Do not replace, summarize, or invent the input.
                    Return the tool result.
                    For write_excel, format the data as CSV with headers."""},
                    {"role": "user", "content": task}
                ]
        for i in range(3):
            try:
                if schema:
                    response = mistral.chat.completions.create( 
                        model=model,
                        messages=messages,
                        tools=[schema],
                        tool_choice="any",
                        # reasoning_effort="low"
                    )
                else:
                    response = mistral.chat.completions.create(
                        model=model,
                        messages=messages,
                        # reasoning_effort="low"
                    )
            except Exception as e:
                if "429" in str(e):
                    print("> [Agent 2] Rate limited, waiting 5s...")
                    time.sleep(5)
                    continue
                return f"> [Agent 2] API error: {e}"
            
            print(f"> [Agent 2] Requesting model: {model}")
            tokens = response.usage.total_tokens
            print("> TOKENS: ", tokens)
            message = response.choices[0].message
            
                        
            if message.tool_calls:
                tool_name = message.tool_calls[0].function.name
                args = json.loads(message.tool_calls[0].function.arguments)
                if "max_result" in args:
                    args["max_result"] = int(args["max_result"])
                    
                print(f"> [Agent 2] Calling {tool_name}")
                result = call_tools(tool_name, args)
                summary = mistral.chat.completions.create(
                            model=model,
                            messages=[
                                {"role": "system", "content": prompt},
                                {"role": "user", "content": str(result)}
                                ]
                            )
                print("> [Agent 2] done.")
                return summary.choices[0].message.content 
            return message.content
        return None
    except Exception as e:
        return f'> [Unexpected Error] as [{e}]'