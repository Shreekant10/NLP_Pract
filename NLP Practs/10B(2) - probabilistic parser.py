import nltk

grammar = nltk.PCFG.fromstring('''
NP -> NNS [0.5] | JJ NNS [0.3] | NP CC NP [0.2]
NNS -> "men" [0.1] | "women" [0.2] | "children" [0.3] | NNS CC NNS [0.4]
JJ -> "old" [0.4] | "young" [0.6]
CC -> "and" [0.9] | "or" [0.1]
''')
print("Grammar:")
print(grammar)
viterbi_parser = nltk.ViterbiParser(grammar)
sentence = "old men and women".split()
print("\nParsing Output:")
for tree in viterbi_parser.parse(sentence):
    print(tree)