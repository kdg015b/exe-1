"""
Performs sentiment analysis on text data.
"""

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text and returns a numeric score.
    """
    text_lower = text.lower()
    if "positive" in text_lower or "bullish" in text_lower:
        return 1
    elif "negative" in text_lower or "bearish" in text_lower:
        return -1
    else:
        return 0
