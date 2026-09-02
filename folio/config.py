from groq import Groq
from openai import OpenAI 
from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

groq = Groq(api_key = os.getenv("GROQ"))

mistral = OpenAI(api_key = os.getenv("MISTRAL"),
                 base_url = "https://api.mistral.ai/v1")

slack = os.getenv("SLACK")
search_client = TavilyClient(api_key = os.getenv("SEARCH"))
github_token = os.getenv("GITHUB")

def convert_args(args):
    if isinstance(args, dict):
        return args
    return {"query": args}