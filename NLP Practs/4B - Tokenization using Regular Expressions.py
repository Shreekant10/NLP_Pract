import nltk
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer('\s+', gaps=True)
input_str = "I love to study Natural Language Processing in Python"
tokens = tokenizer.tokenize(input_str)
print("Tokenized Output:")
print("=================")
print(tokens)