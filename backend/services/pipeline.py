
from services.news_api import fetch_news

def run_pipeline():
    news_list = fetch_news()

    # 기존 로직 연결
    from skills.news_mapper.scripts.news_mapper import map_news_to_tickers
    from skills.news_quality.scripts.news_quality import compute_trust_score

    results = []

    for news in news_list:
        tickers = map_news_to_tickers(news["content"])

        for t in tickers:
            results.append({
                "ticker": t["ticker"],
                "score": t["relevance"],
                "source": news["url"]
            })

    return results
