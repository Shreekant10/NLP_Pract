import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
print("Synsets for 'car':")
print(wordnet.synsets("car"))
print("\nDefinition of 'car':")
print(wordnet.synset("car.n.01").definition())
print("\nExamples of 'car':")
print("Examples:", wordnet.synset("car.n.01").examples())
print("\nAntonyms of 'buy':")
print(wordnet.lemma('buy.v.01.buy').antonyms())