# pip install spacy
# python -m spacy download en_core_web_sm
# python -m spacy download en

import spacy
from nltk.tokenize import word_tokenize
from tabulate import tabulate

sp = spacy.load('en_core_web_sm')
all_stopwords = sp.Defaults.stop_words
all_stopwords.add("play")
text = "Sara likes to play football, however he is not too fond of tennis."
text_tokens = word_tokenize(text)
tokens_without_sw1 = [word for word in text_tokens if not word in all_stopwords]
if 'not' in all_stopwords:
    all_stopwords.remove('not')
tokens_without_sw2 = [word for word in text_tokens if not word in all_stopwords]
data = [
    ["1. Remove stopwords including 'play' from Spacy's default stop words list:", tokens_without_sw1],
    ["2. Remove stopwords excluding 'not' from Spacy's default stop words list:", tokens_without_sw2],
    ["Explanation:", "Using Spacy: Adding and Removing Stop Words in Default Spacy Stop Words List"]
]
print(tabulate(data, headers=['Output Section', 'Content'], tablefmt='grid'))