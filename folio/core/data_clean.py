import re
import json

CLEAN_TOOLS = {
    "web_search",
    "web_scraper",
    "wikipedia_search",
    "get_news",
    "youtube_search",
    "trend_search",
    "linkedin_jobs",
    "startups_find",
    "remote_and_eu_jobs",
    "_arxiv_search",
    "stack_search",
    "search_github",
    "info_medicine",
    "search_flights",
    "search_hotels",
    "search_visa_info",
}

def clean_raw(text: str):
    text = re.sub(r"#{1,6} ", "", text)
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[*_~`>|\\]", "", text)
    text = re.sub(r"Image \d+:.*?(?:\n|$)", "", text)
    text = re.sub(r"\[\.{3}\]", "", text)
    text = re.sub(r"Avatar of [^\n]+", "", text)
    text = re.sub(r"Abstract Wikipedia.*?(?=\n|[A-Z])", "", text)
    text = re.sub(r"Archived from the original.*?(?:\d{4}\.?)", "", text)
    text = re.sub(r"Retrieved [A-Z][a-z]+ \d+, \d{4}\.?", "", text)
    text = re.sub(r"Milestones(\s+\d{4}[^\n]+)+", "", text)
    text = re.sub(r"Wiki\w+\s+", "", text)
    text = re.sub(r"\(.*?\)", "", text)  
    text = re.sub(r"[()]", "", text)     
    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip()

def cleaner(tool_name: str, result):
    if tool_name not in CLEAN_TOOLS:
        return result
    
    if result is None:
        return f"> [{tool_name}] No result."

    if isinstance(result , list):
        parts = []
        for item in result:
            if isinstance(item , dict):
                text_parts = []
                for k, v in item.items():
                    if k.lower() in ["url", "image", "thumbnail", "icon"]:
                        continue
                    if isinstance(v ,str):
                        text_parts.append(clean_raw(v))
                parts.append(" | ".join(filter(None, text_parts)))    
            elif isinstance(item, str):
                parts.append(clean_raw(item))
        cleaned = "\n\n".join(filter(None, parts))

    elif isinstance(result, dict):
        text_parts = []
        for k , v in result.items():
            if k.lower() in ["url", "image", "thumbnail", "icon"]:
                continue
            if isinstance(v,str):
                text_parts.append(clean_raw(v))
        cleaned = " | ".join(filter(None, text_parts))

    elif isinstance(result, str):
        cleaned = clean_raw(result)
    else:
        cleaned = str(result).strip()
    if not cleaned:
        return f"[{tool_name}] Result was empty after cleaning."
    print("<>" + "--" * 15 + "[ANSWER]" + "--" * 15 + "<>")
    return f"{cleaned}"
