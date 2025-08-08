import tweepy
import requests
import datetime
import os

def sentiment_scraper(pairs):
    data = []
    
    # Twitter API Setup
    twitter_client = tweepy.Client(bearer_token=os.getenv("TWITTER_BEARER"))
    
    for pair in pairs:
        # Fetch Tweets
        query = f"{pair} lang:en -is:retweet"
        tweets = twitter_client.search_recent_tweets(query=query, max_results=5)
        
        if tweets.data:
            for tweet in tweets.data:
                data.append({
                    "pair": pair,
                    "source": "twitter",
                    "text": tweet.text,
                    "timestamp": datetime.datetime.utcnow().isoformat()
                })
        
        # NewsAPI fetch
        news_url = f"https://newsapi.org/v2/everything?q={pair}&language=en&apiKey={os.getenv('NEWSAPI_KEY')}"
        news_resp = requests.get(news_url)
        if news_resp.status_code == 200:
            articles = news_resp.json().get("articles", [])
            for article in articles[:3]:
                data.append({
                    "pair": pair,
                    "source": "news",
                    "text": article["title"],
                    "timestamp": datetime.datetime.utcnow().isoformat()
                })
    
    return data
