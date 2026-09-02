from folio._mcp.client import call_tools
from folio.config import convert_args

def run_agent_1(payload: dict):
    data = payload
    task = data["query"]
    tool_name = data["tool_name"]
    
    print(f"> [Agent 1] calling.......")
    if tool_name == "send_message":
        args = {"channel": "#new-channel", "message": task}
    elif tool_name == "read_message":
        args = {"channel": task if task.startswith("#") else "#new-channel"}
    elif tool_name == "upload_file":
        args = {"channel": "#new-channel", "title": task}
    elif tool_name == "generate_pdf":
        args = {"title": "Report", "text": task}
    elif tool_name == "show_map":
        args = {"places": task.split(" to ")}
    else:
        args = convert_args(task)

    try:
        result = call_tools(tool_name = tool_name, args = args)

        print(f"> [Agent 1] → [Success]")

        return result
    except Exception as e:
        print(f"> [Agent 1] Failed '{tool_name}' for {task}")
        return "TOOL FAIL"

