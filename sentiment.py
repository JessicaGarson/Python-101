sentiment_score = 0.05

def sentiment_classifier(sentiment_score):
    if sentiment_score > 0.80 or sentiment_score == 0.80:
        print("This score is Positive")
    elif sentiment_score > 0.65 or sentiment_score == 0.65:
        print("This score is Neutral")
    else:
        print("This score Negative")

sentiment_classifier(sentiment_score)
