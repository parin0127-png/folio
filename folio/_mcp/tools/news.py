from newspaper import Article
import requests
import xml.etree.ElementTree as e

def get_news(query: str):
    """fetch latest breaking news, headlines, and articles by topic, keyword, or category"""
    try :
        url = f"https://news.google.com/rss/search?q={query}&hl=en"
        response = requests.get(url)
        articles = []

        root = e.fromstring(response.content)

        for r in root.findall(".//item")[:5]:
            url = r.find("link").text
            try:
                a = Article(url)
                a.download()
                a.parse()
                text = a.text[:1000]
            except:
                text = ""
            articles.append(f"{r.find('title').text} | {r.find('pubDate').text}\n{text}")

        return articles
    except:
        return "> News unavailable !"
    
