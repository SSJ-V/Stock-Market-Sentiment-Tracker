# sentiment_analyzer.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(headlines):
    sentiments = []

    for headline in headlines:
        score = analyzer.polarity_scores(headline)['compound']
        sentiment = "Positive" if score > 0.05 else "Negative" if score < -0.05 else "Neutral"
        sentiments.append((headline, score, sentiment))

    return sentiments
