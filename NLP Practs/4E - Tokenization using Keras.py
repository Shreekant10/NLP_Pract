# pip install keras
# pip install tensorflow

import keras
from keras.preprocessing.text import text_to_word_sequence
# Create a string input
input_str = "I love to study Natural Language Processing in Python"
# Tokenize the text
tokens = text_to_word_sequence(input_str)
# Print the tokens
print("Tokens:")
print("=======")
print(tokens)