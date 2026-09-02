from task.planner import build_flow
from task.selector import select_tool
from folio.core.agent_router import route_agent


def build_plan(tasks):

    plan = build_flow(tasks)
    
    selected = select_tool(plan)

    flow = []

    for item in selected:

        if item["status"] != "selected":
            continue

        tool = item.get("tool")

        if not tool:
            continue

        agent = route_agent({
            tool: item["description"]
        })

        flow.append({
            "task": item["task"],
            "tool": tool,
            "agent": agent
        })

    return flow


def flow_to_text(flow):

    lines = []

    for item in flow:
        lines.append(
            f'{item["task"]} -> '
            f'{item["tool"]} ({item["agent"]})'
        )

    return "\n".join(lines)