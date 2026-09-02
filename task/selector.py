def select_tool(flow):
    selected = []
    for f in flow:
        if f["status"] != "matched":
            selected.append({
                "task": f["task"],
                "tool": None,
                "status": "unresolvable"
            })
            continue
        tools = f["tools"]

        if not tools:
            selected.append({
                "task": f["task"],
                "tool": None,
                "status": "unresolvable"
            })
            continue

        best_tool = tools[0]

        selected.append({
            "task": f["task"],
            "tool": best_tool["tool"],
            "description": best_tool["description"],
            "score": best_tool["score"],
            "status": "selected"
        })

    return selected
