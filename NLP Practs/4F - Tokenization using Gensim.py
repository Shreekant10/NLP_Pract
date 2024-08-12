# pip install gensim
from gensim.utils import tokenize

input_str = "I love to study Natural Language Processing in Python"
tokens = list(tokenize(input_str))
print("Tokens:")
print("=======")
for token in tokens:
    print(token)