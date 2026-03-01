from textblob import TextBlob

print("AI Sentiment Analyzer")
print("---------------------")

text = input("Enter a sentence: ")

analysis = TextBlob(text)
polarity = analysis.sentiment.polarity

if polarity > 0:
    print("Result: Positive 😊")
elif polarity < 0:
    print("Result: Negative 😠")
else:
    print("Result: Neutral 😐")
    