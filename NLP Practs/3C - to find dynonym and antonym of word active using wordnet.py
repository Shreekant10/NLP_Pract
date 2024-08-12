from nltk.corpus import wordnet
from tabulate import tabulate
active_synsets = wordnet.synsets("active")
synset_data = []
for synset in active_synsets:
    synset_data.append([synset.name(), synset.definition()])
active_lemma = wordnet.lemma('active.a.01.active')
antonyms = active_lemma.antonyms()
antonym_names = ', '.join([antonym.name() for antonym in antonyms])
print("Synsets for 'active':")
print(tabulate(synset_data, headers=['Synset', 'Definition'], tablefmt='pretty'))
print("\nAntonyms:")
print(tabulate([[antonym_names]], headers=['Antonyms'], tablefmt='pretty'))