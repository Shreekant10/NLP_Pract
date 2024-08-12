import nltk
from nltk.tokenize import word_tokenize

input_str = "I love to study Natural Language Processing in Python"
tokens = word_tokenize(input_str)
print("Tokenized Output:")
print("=================")
print(tokens)