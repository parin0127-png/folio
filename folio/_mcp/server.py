import sys, os

log = open('debug.log', 'w', buffering=1)
sys.stderr = log

def d(msg):
    log.write(msg + '\n')
    log.flush()

d("started")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
d("sys.path ok")

try:
    from mcp.server.fastmcp import FastMCP
    d("FastMCP ok")
    from folio._mcp.tools.websearch import web_search
    d("websearch ok")
    from folio._mcp.tools.weather import _weather
    d("weather ok")
    from folio._mcp.tools.news import get_news
    d("news ok")
    from folio._mcp.tools.stocks import get_stocks
    d("stocks ok")
    from folio._mcp.tools.crypto import get_crypto
    d("crypto ok")
    from folio._mcp.tools.writer import write_file
    d("writer ok")
    from folio._mcp.tools.excel import write_excel
    d("excel ok")
    from folio._mcp.tools.pdf import generate_pdf
    d("pdf ok")
    from folio._mcp.tools.email_sender import send_email
    d("email ok")
    from folio._mcp.tools.youtube import youtube_search
    d("youtube ok")
    from folio._mcp.tools.translator import translate_text
    d("translator ok")
    from folio._mcp.tools.search_wikipedia import wikipedia_search
    d("wikipedia ok")
    from folio._mcp.tools.google_trends import trend_search
    d("trends ok")
    from folio._mcp.tools.job_search import linkedin_jobs, startups_find, remote_and_eu_jobs
    d("jobs ok")
    from folio._mcp.tools.arxiv_search import _arxiv_search
    d("arxiv ok")
    from folio._mcp.tools.math import math_solver
    d("math ok")
    from folio._mcp.tools.file_manager import file_organizer
    d("file_manager ok")
    from folio._mcp.tools.country import country_info
    d("country ok")
    from folio._mcp.tools.currency_convertor import convert_currency
    d("currency ok")
    from folio._mcp.tools.flight import search_flights
    d("flight ok")
    from folio._mcp.tools.hotels import search_hotels
    d("hotels ok")
    from folio._mcp.tools.github_search import search_github
    d("github ok")
    from folio._mcp.tools.ip import ip_check
    d("ip ok")
    from folio._mcp.tools.medicine_info import info_medicine
    d("medicine ok")
    from folio._mcp.tools.package import packages_info
    d("package ok")
    from folio._mcp.tools.password import password_generator
    d("password ok")
    from folio._mcp.tools.qr import qr_generator
    d("qr ok")
    from folio._mcp.tools.reminder import reminders
    d("reminder ok")
    from folio._mcp.tools.stackoverflow import stack_search
    d("stackoverflow ok")
    from folio._mcp.tools.sports import score
    d("sports ok")
    from folio._mcp.tools.time_zone import timezone_check
    d("timezone ok")
    from folio._mcp.tools.visa_info import search_visa_info
    d("visa ok")
    from folio._mcp.tools.webscraper import web_scraper
    d("webscraper ok")
    from folio._mcp.tools.website_status import check_status
    d("website_status ok")
    from folio._mcp.tools.whois_check import check_whois
    d("whois ok")
    from folio._mcp.tools.remember import remembers
    d("remember ok")
    from folio._mcp.tools.recall import recalls
    d("recall ok")
    from folio._mcp.tools.clear import clear_memory
    d("clear ok")
    from folio._mcp.tools.save import save_history
    d("save ok")
    from folio._mcp.tools.cmd_runner import run_command
    d("cmd_runner ok")
    from folio._mcp.tools.slack import send_message, read_message, upload_file, get_available_channel
    d("slack ok")

except Exception as e:
    import traceback
    d(f"FAILED: {e}")
    d(traceback.format_exc())
    sys.exit(1)

mcp = FastMCP("FOLIO")

mcp.tool()(web_search)
mcp.tool()(_weather)
mcp.tool()(get_news)
mcp.tool()(get_stocks)
mcp.tool()(get_crypto)
mcp.tool()(write_file)
mcp.tool()(write_excel)
mcp.tool()(generate_pdf)
mcp.tool()(send_email)
mcp.tool()(youtube_search)
mcp.tool()(translate_text)
mcp.tool()(wikipedia_search)
mcp.tool()(trend_search)
mcp.tool()(linkedin_jobs)
mcp.tool()(startups_find)
mcp.tool()(remote_and_eu_jobs)
mcp.tool()(_arxiv_search)
mcp.tool()(math_solver)
mcp.tool()(file_organizer)
mcp.tool()(country_info)
mcp.tool()(convert_currency)
mcp.tool()(search_flights)
mcp.tool()(search_hotels)
mcp.tool()(search_github)
mcp.tool()(ip_check)
mcp.tool()(info_medicine)
mcp.tool()(packages_info)
mcp.tool()(password_generator)
mcp.tool()(qr_generator)
mcp.tool()(reminders)
mcp.tool()(stack_search)
mcp.tool()(score)
mcp.tool()(timezone_check)
mcp.tool()(search_visa_info)
mcp.tool()(web_scraper)
mcp.tool()(check_status)
mcp.tool()(check_whois)
mcp.tool()(remembers)
mcp.tool()(recalls)
mcp.tool()(clear_memory)
mcp.tool()(save_history)
mcp.tool()(run_command)
mcp.tool()(send_message)
mcp.tool()(read_message)
mcp.tool()(upload_file)
d("all tools registered")

if __name__ == "__main__":
    d("starting mcp server...")
    mcp.run(transport="stdio")