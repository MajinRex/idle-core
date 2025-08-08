from textblob import TextBlob

def analyze_sentiment(data):
    results = []
    for item in data:
        analysis = TextBlob(item["text"])
        score = round(analysis.sentiment.polarity, 3)  # -1.0 to +1.0
        results.append({
            "pair": item["pair"],
            "source": item["source"],
            "text": item["text"],
            "sentiment": score,
            "timestamp": item["timestamp"]
        })
    return results
