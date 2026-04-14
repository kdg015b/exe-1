"""
Main entry point for the investment automation agent.
"""

import json
from collectors.news_collector import fetch_news
from analyzers.sentiment_analyzer import analyze_sentiment
from evaluators.scoring_engine import calculate_score
from portfolio.portfolio_builder import build_portfolio

def main():
    """
    Main function to run the investment automation agent.
    """
    # 1. Data Collection
    news_api_key = "7f0f28591a554080ba2d4f7f96b2b729"
    news_data = fetch_news(api_key=news_api_key)

    if not news_data or 'articles' not in news_data or not news_data['articles']:
        print("No news data found.")
        # Create an empty portfolio file
        with open('portfolio.json', 'w') as f:
            json.dump([], f, indent=4)
        return

    # 2. Insight Analysis
    total_sentiment_score = 0
    for article in news_data['articles']:
        description = article['description'] or ""
        title = article['title'] or ""
        total_sentiment_score += analyze_sentiment(title + " " + description)
    
    average_sentiment = total_sentiment_score / len(news_data['articles']) if news_data['articles'] else 0
    momentum_score = (average_sentiment + 1) * 50

    # 3. Investment Evaluation
    scores = [
        {'asset': 'BTC', 'score': calculate_score(momentum_score, 80, 90, 60)},
        {'asset': 'ETH', 'score': calculate_score(momentum_score, 85, 80, 70)},
        {'asset': 'SOL', 'score': calculate_score(momentum_score, 70, 75, 65)},
        {'asset': 'ADA', 'score': calculate_score(momentum_score, 60, 65, 55)},
        {'asset': 'XRP', 'score': calculate_score(momentum_score, 50, 55, 45)},
        {'asset': 'DOGE', 'score': calculate_score(momentum_score, 30, 40, 50)},
    ]

    # 4. Portfolio Generation
    portfolio = build_portfolio(scores)

    # 5. Save portfolio to JSON file
    with open('portfolio.json', 'w') as f:
        json.dump(portfolio, f, indent=4)

    print("Portfolio data has been successfully saved to portfolio.json")

if __name__ == "__main__":
    main()
