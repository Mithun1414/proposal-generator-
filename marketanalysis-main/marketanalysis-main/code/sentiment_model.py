import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download necessary data
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """Analyze the sentiment of a given text using VADER."""
    scores = sia.polarity_scores(text)
    if scores['compound'] > 0.05:
        return 'Positive'
    elif scores['compound'] < -0.05:
        return 'Negative'
    else:
        return 'Neutral'
