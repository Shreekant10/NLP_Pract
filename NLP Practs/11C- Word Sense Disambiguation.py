from nltk.corpus import wordnet as wn

def get_first_sense(word, pos=None):
    if pos:
        synsets = wn.synsets(word, pos=pos)
    else:
        synsets = wn.synsets(word)
        return synsets[0]
word1 = 'bank'
best_synset1 = get_first_sense(word1)
print(f"Senses of '{word1}':")
print(f"{best_synset1.name()}: {best_synset1.definition()}")

word2 = 'set'
best_synset2 = get_first_sense(word2, 'n')
print(f"\nSenses of '{word2}' as a noun:")
print(f"{best_synset2.name()}: {best_synset2.definition()}")

best_synset3 = get_first_sense(word2, 'v')
print(f"\nSenses of '{word2}' as a verb:")
print(f"{best_synset3.name()}: {best_synset3.definition()}")