from folio.config import mistral
from folio._mcp.client import call_tools, get_schema
import json, time


def agent_3(payload: dict, model = "mistral-large-latest"):
    try:
        time.sleep(8)
        data = payload
        task = data["query"]
        mode = data["mode"]
        tool = data["tool_name"]

        if mode == "code":
            system = "You are an expert coding assistant. Write clean, readable code in any language. Add brief inline comments. Return only code and a short explanation."
        else:
            system = "You are an expert system and UI/UX designer. For system design, provide architecture, components, and data flow. For UI/UX, describe layout and interactions. Be concise."

        schema = get_schema(tool)

        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": task}
        ]

        for i in range(3):
            response = mistral.chat.completions.create(
                model = model,
                messages = messages,
                tools = schema
            )
            print("> TOKENS: ", response.usage.total_tokens)
            message = response.choices[0].message

            if message.tool_calls:
                tool_name = message.tool_calls[0].function.name
                args = json.loads(message.tool_calls[0].function.arguments)

                print(f"> [Agent 3] Calling {tool_name} with {args}")

                result = call_tools(tool_name, args)
                time.sleep(6)

                messages = [
                    {"role": "system", "content": system},
                    {"role": "user", "content": f"Here is the result:\n\n{str(result)[:1000]}"}
                ]
                schema = None
            else:
                return message.content

        return None
    except Exception as e:
        return f'> [Unexcpected Error] as [{e}]'
