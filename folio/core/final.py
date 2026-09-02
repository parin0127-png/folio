from folio._mcp.tools.email_sender import send_email
from folio.config import mistral
from folio.core.data_clean import clean_raw
import json, re

prompt = """You are a final output formatter. You receive results from multiple sources.
Your job:
- Merge all content into one clean, professional output
- If flight prices are in INR (₹), convert them to USD (use rate: 1 USD = 84 INR)
- Remove duplicates, placeholders, and noise
- Use short paragraphs and bullet points
- Use emojis only where they add clarity
- Max 600 words, only real content
- Return ONLY a JSON with two keys: subject (string) and body (plain text string, no nested JSON)"""

def final_ai(memory: dict, plan: dict, model = "mistral-small-latest"):
    skip = {"task"}
    content = "\n\n".join([f"[{k}]\n{v}" for k, v in memory.items() if k not in skip and not str(v).startswith("Written to") and not str(v).startswith("Email sent")])
    response = mistral.chat.completions.create(
        model = model,     
        messages = [
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": content}
                ],
        max_tokens = 500
    )
    tokens= response.usage.total_tokens
    print("> Tokens: ", tokens)
    raw = response.choices[0].message.content
    try:
        result = json.loads(raw)
    except:
        result = {"subject": memory.get("task", "Summary")[:60], "body" : raw}

    all_tools = [s["tool_name"] for steps in plan.values() for s in steps]

    body = result["body"] if isinstance(result["body"], str) else json.dumps(result["body"], indent = 2)
    clean_body = re.sub(r"```json|```", "", body)
    try:
        parsed = json.loads(clean_body)
        clean_body = parsed.get("body", clean_body)
    except:
        pass 
    if "write_file" in all_tools:
        from folio.core.agent1 import run_agent_1
        run_agent_1({"tool_name": "write_file", "query": clean_body})

    if "send_email" in all_tools:
        email = next((s["input"] for steps in plan.values() for s in steps if s["tool_name"] == "send_email"), None)
        if email:
            from folio._mcp.client import call_tools
            print(f"> [Final AI] Sending email to {email}")
            call_tools("send_email", {"to": email, "subject": result["subject"], "body": clean_body}).result()
            print("> [Final AI] Email sent!")

    return clean_body

