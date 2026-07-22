import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk

resources = [
    ("corpora/stopwords", "stopwords"),
    ("tokenizers/punkt", "punkt"),
    ("tokenizers/punkt_tab", "punkt_tab"),
]

for path, resource in resources:
    try:
        nltk.data.find(path)
    except LookupError:
        nltk.download(resource)


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

