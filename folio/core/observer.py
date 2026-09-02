from folio.config import groq


TOOL_SUBSTITUTES = {
    "wikipedia_search": ["web_search", "trend_search"],
    "web_search": ["wikipedia_search", "web_scraper"],
    "get_news": ["web_search", "trend_search"],
    "arxiv_search": ["_arxiv_search", "web_search"],
    "search_github": ["web_search", "stack_search"],
    "stack_search": ["web_search", "search_github"],
    "trend_search": ["web_search", "get_news"],
    "web_scraper": ["web_search"],
    "get_stocks": ["web_search"],
    "get_crypto": ["web_search"],
    "linkedin_jobs": ["web_search", "startups_find", "remote_and_eu_jobs"],
    "startups_find": ["web_search", "linkedin_jobs", "remote_and_eu_jobs"],
    "remote_and_eu_jobs": ["web_search", "linkedin_jobs", "startups_find"],
    "country_info": ["wikipedia_search", "web_search"],
    "info_medicine": ["web_search", "wikipedia_search"],
    "search_flights": ["web_search"],
    "search_hotels": ["web_search"],
    "search_visa_info": ["web_search", "country_info"],
    "ip_check": ["web_search"],
    "check_whois": ["web_search"],
    "check_status": ["web_scraper"],
    "show_map": ["web_search"],
    "score": ["web_search", "get_news"],
    "youtube_search": ["web_search"],
    "packages_info": ["web_search", "stack_search"],
    "timezone_check": ["web_search"],
    "convert_currency": ["web_search"],
    "_weather": ["web_search"],
    "save_history": ["write_file"],
}

FAIL_SIGNALS = ["error", "failed", "unavailable", "tool fail", "{}", "[]", "unknown tool"]

class Observer:
    def is_failed(self, result):
        
        if not result:
            return True
        if isinstance(result , str):
            return any(s in result.lower() for s in FAIL_SIGNALS)
        return False

    def get_substitues(self, tool_name):
        return TOOL_SUBSTITUTES.get(tool_name, [])

    def ai_fix(self, tool_name, job, memory, available_tools):
        prompt = f"Tool '{tool_name}' failed for job: '{job}'. Available tools: {available_tools}. Current data: {memory}. Which tool can complete this job? Return ONLY: tool_name|input"

        res = groq.chat.completions.create(
            model = "openai/gpt-oss-20b",
            reasoning_effort = "low",
            messages = [{"role" : "user", "content": prompt}]
        )
        print("> TOKENS: ", res.usage.total_tokens)
        return res.choices[0].message.content
    
    def watch(self, tool_name, job, query, result, memory):
        
        
        available_tools = list(TOOL_SUBSTITUTES.keys())
        if not self.is_failed(result):
            return result, tool_name

        print(f"> [Observer] '{tool_name}' failed. Finding fix......")
        print("=="*30)
        substitutes = self.get_substitues(tool_name)

        for sub in substitutes:
            if sub:
                print(f"> [Observer] Trying substitute: '{sub}'")
                print("=="*30)
                return None, sub

        # print(f"> [Observer] No substitute. Calling AI fix...")
        ai_solution = self.ai_fix(tool_name, job, memory, available_tools)
        new_tool = ai_solution.split("|")[0].strip()
        return None, new_tool

    