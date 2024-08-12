import nltk
from nltk import tokenize, tag, chunk
from tabulate import tabulate

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
para = "Hello! My name is Jack Reacher. Today you'll be learning NLTK."
sents = tokenize.sent_tokenize(para)
tokenized_words = []
pos_tags = []
for sent in sents:
    words = tokenize.word_tokenize(sent)
    tokenized_words.append(words)
    pos_tags.append(tag.pos_tag(words))

chunked_trees = []
for tags in pos_tags:
    chunked_trees.append(chunk.ne_chunk(tags))
print("\nSentence Tokenization\n===================")
print(tabulate([[sent] for sent in sents], headers=['Sentences']))
print("\nWord Tokenization\n===================")
for i, words in enumerate(tokenized_words):
    print(f"Sentence {i + 1}:")
    print(tabulate([words], headers=['Words']))
print("\nPOS Tagging\n===========")
for i, tags in enumerate(pos_tags):
    print(f"POS Tags for Sentence {i + 1}:")
    print(tabulate(tags, headers=['Word', 'POS Tag']))
print("\nChunking\n========")
for i, tree in enumerate(chunked_trees):
    print(f"Chunking for Sentence {i + 1}:")
    print(tree)
    print()