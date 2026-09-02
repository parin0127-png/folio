AGENT2_TOOLS = [
    "web_search", "wikipedia_search", "_arxiv_search", "trend_search",
    "stack_search", "web_scraper", "search_github", "info_medicine",
    "generate_pdf", "send_email", "file_organizer", "write_file",
    "write_excel"
]
AGENT_EXAMPLES = {
    "agent_1": "Example:\nTask: get weather of London\nagent_1|_weather|get weather of London|input=London|in=task|out=key1",
    "agent_2": "Example:\nTask: search wikipedia for AI and save to file\nagent_2|wikipedia_search|search wikipedia for AI|input=AI|in=task|out=key1\nagent_2|write_file|save research to file|input=key1|in=key1|out=key2\nTask: send email to parin12@gmail.com with AI news\nagent_2|web_search|search for AI news|input=AI news|in=task|out=key1\nagent_2|send_email|send to parin12@gmail.com|input=parin12@gmail.com|in=key1|out=key2",
    "agent_3": "Example:\nTask: run python script main.py\nagent_3|run_command|run python main.py|input=python main.py|in=task|out=key1",
}

def route_agent(selected_tool: dict):
    tool_dict = list(selected_tool.keys())

    if "run_command" in tool_dict:
        return "agent_3"

    for tool in tool_dict:
        if tool in AGENT2_TOOLS:
            return "agent_2"

    return "agent_1"

