"""
Calculates investment scores based on various factors.
"""

def calculate_score(momentum, fundamental, onchain, technical):
    """
    Calculates the total investment score based on weighted factors.
    """
    total_score = (
        0.35 * momentum +
        0.30 * fundamental +
        0.20 * onchain +
        0.15 * technical
    )
    return total_score
