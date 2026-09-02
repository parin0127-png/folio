from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

def web_scraper(url: str):
    """scrape and extract all text content and data from any website url"""
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless = True)
            page = browser.new_page(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                java_script_enabled=True
            )
            page.goto(url)
            page.wait_for_timeout(4000)
            html = page.content()
            browser.close()

        soup = BeautifulSoup(html, "html.parser")

        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        text = soup.get_text(separator = "\n", strip = True)
        return text[:3000]
    except Exception as e:
        return f"> Web scraper failed: {str(e)}"

