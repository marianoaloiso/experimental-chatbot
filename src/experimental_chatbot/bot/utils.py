from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze sentiment of a text using TextBlob
    """
    blob = TextBlob(text)
    return blob.sentiment.polarity

def generate_glitch_text(text, intensity=0.3):
    """
    Generate glitch text based on reality_glitch_level
    """
    if random.random() < intensity:
        glitch_chars = "¯̮̮́́═̶̶░̴̴█̷̷▒̸̸▓̡̡"
        return "".join([c if random.random() < 0.7 else random.choice(glitch_chars) for c in text])
    return text

    