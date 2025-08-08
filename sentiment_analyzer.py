def analyze_sentiment(data):
    # Simple scoring placeholder
    results = []
    for item in data:
        score = 0.2  # Replace with real NLP later
        results.append({
            "pair": item["pair"],
            "sentiment": score,
            "timestamp": item["timestamp"]
        })
    return results
