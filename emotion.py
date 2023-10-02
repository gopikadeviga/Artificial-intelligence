#used to perform sentiment analysis on data
from textblob import TextBlob

text = "Please pass me the book"
# object creation
tb = TextBlob(text)

# sentiment analysis
# .sentiment - attribute of TextBlob with 2 properties (polarity, subjectivity)
#.polarity - retrives the polarity score of the text
score = tb.sentiment.polarity

if score > 0:
    sentiment = "Positive"
elif score < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Sentiment: {sentiment}")
