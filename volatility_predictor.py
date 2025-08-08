def predict_volatility(sentiment_scores):
    results = []
    for s in sentiment_scores:
        prob = abs(s["sentiment"]) * 0.8  # Placeholder calculation
        results.append({
            "pair": s["pair"],
            "sentiment": s["sentiment"],
            "volatility_prob": prob,
            "timestamp": s["timestamp"]
        })
    return results
