import json
import urllib.request

def fetch_news(api_key, query="business"):
    """
    Fetches top business headlines from NewsAPI.
    """
    url = f"https://newsapi.org/v2/top-headlines?category={query}&apiKey={api_key}"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            return json.loads(data)
    except urllib.error.URLError as e:
        print(f"Error fetching news: {e}")
        return None
