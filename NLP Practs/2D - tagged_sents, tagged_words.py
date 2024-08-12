import nltk
from nltk import tokenize
nltk.download('punkt')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
para = "Hello! My name is Pikachu. Today you'll be learning NLTK."
sents = tokenize.sent_tokenize(para)
print("\nSentence Tokenization\n===================\n", sents)
print("\nWord Tokenization and POS Tagging\n===================\n")
tagged_sents = []
tagged_words = []
for index in range(len(sents)):
    words = tokenize.word_tokenize(sents[index])
    tagged = nltk.pos_tag(words)
    tagged_sents.append(tagged)
    tagged_words.extend(tagged)
print(words)
print(tagged)
print("\nTagged Sentences\n===================\n", tagged_sents)
print("\nTagged Words\n===================\n", tagged_words)