import nltk
from nltk.tokenize import MWETokenizer
from nltk import sent_tokenize, word_tokenize

s = '''Good cake cost Rs.1500/kg in Mumbai. Please buy me one of them.\n\nThanks.'''
mwe = MWETokenizer([('New', 'York'), ('Hong', 'Kong')], separator='_')
print("Tokenized Output:")
for sent in sent_tokenize(s):
    tokens = word_tokenize(sent)
    mwe_tokens = mwe.tokenize(tokens)
    print(mwe_tokens)