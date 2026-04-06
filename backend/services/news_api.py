
import requests

NEWS_API_KEY = "YOUR_API_KEY"  # https://newsapi.org


def fetch_news(query="crypto OR stock", page_size=20):
    url = "https://newsapi.org/v2/everything"

    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": NEWS_API_KEY
    }

    res = requests.get(url, params=params)
    data = res.json()

    articles = []

    for a in data.get("articles", []):
        articles.append({
            "title": a["title"],
            "content": a.get("description", "") or "",
            "url": a["url"],
            "publishedAt": a["publishedAt"]
        })

    return articles
