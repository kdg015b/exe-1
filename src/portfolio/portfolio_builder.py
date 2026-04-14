"""
Builds a portfolio of assets based on their scores.
"""

def build_portfolio(scores):
    """
    Builds a portfolio of the top 5 assets based on their scores.
    """
    sorted_assets = sorted(scores, key=lambda x: x['score'], reverse=True)
    top5 = sorted_assets[:5]

    total_score = sum([x['score'] for x in top5])
    if total_score == 0:
        # Avoid division by zero if all scores are 0
        return top5

    for asset in top5:
        asset['weight'] = round(asset['score'] / total_score * 100, 2)

    return top5
