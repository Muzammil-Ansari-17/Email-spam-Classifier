import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk

nltk.download("punkt")
nltk.download("stopwords")


ps = PorterStemmer()
stop_words = stopwords.words('english')
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []

    # Removing special character
    for i in text:
        if i.isalnum():
            y.append(i)


    text = y[:]
    y.clear()

    # Removing stop words and punctuation\
    for i in text:
        if i not in stop_words and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    #  Stemming
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


# Testing the method or function

output = transform_text("Hi, I'm Muzammil, and you're looking at code I wrote on 21 July 2026 at 5:03 PM.")
print(output)
