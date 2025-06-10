from textblob import TextBlob
import re

def clean_text(text):
    """Remove special characters and extra spaces"""
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return ' '.join(text.split())

def detect_emotion(text):
    """
    Detects emotion using TextBlob sentiment analysis
    Returns emotion label and confidence score
    """
    text = clean_text(text)
    analysis = TextBlob(text)
    
    # Get polarity (-1 to 1) and subjectivity (0 to 1)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity
    
    # Determine emotion based on polarity
    if polarity >= 0.5:
        label = "happy"
    elif 0 <= polarity < 0.5:
        label = "neutral"
    elif -0.5 <= polarity < 0:
        label = "sad"
    else:
        label = "angry"
    
    return {
        "label": label,
        "score": round(abs(polarity) * subjectivity, 2)
    }