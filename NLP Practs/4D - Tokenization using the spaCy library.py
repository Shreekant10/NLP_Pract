import spacy

nlp = spacy.blank("en")
input_str = "I love to study Natural Language Processing in Python"
doc = nlp(input_str)
words = [token.text for token in doc]
print("Tokens:")
print("=======")
print(words)