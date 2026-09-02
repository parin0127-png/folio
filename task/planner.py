from task.tool_matcher import match_tool

def build_flow(tasks):
    flow = []

    for task in tasks:
        result = match_tool(task)

        if result["status"] != "matched":
            flow.append({
                "task": task,
                "status": "unresolvable",
                "tools": []
            })

            continue

        flow.append({
            "task": task,
            "status": "matched",
            "tools": result["candidates"]
        })

    return flow