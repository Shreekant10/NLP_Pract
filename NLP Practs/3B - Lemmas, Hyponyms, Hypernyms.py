import nltk
from nltk.corpus import wordnet
from tabulate import tabulate

car_synsets = wordnet.synsets("car")
synset_data = []
for synset in car_synsets:
    synset_data.append([synset.name(), ', '.join(synset.lemma_names())])
    # Print synsets and lemma names in a table
print("Synsets and Lemma Names for 'car':")
print(tabulate(synset_data, headers=['Synset', 'Lemma Names'], tablefmt='pretty'))
# Print all lemmas for 'car.n.01'
car_lemmas = wordnet.synset('car.n.01').lemmas()
lemma_data = [lemma.name() for lemma in car_lemmas]
print("\nLemmas for 'car.n.01':")
print(', '.join(lemma_data))
# Get the synset corresponding to the lemma 'car.n.01.automobile'
automobile_synset = wordnet.lemma('car.n.01.automobile').synset()
print("\nSynset for 'car.n.01.automobile':")
print(automobile_synset.name())
# Get the name of the lemma 'car.n.01.automobile'
print("\nName of the lemma 'car.n.01.automobile':")
print(wordnet.lemma('car.n.01.automobile').name())
# Hyponyms of 'car.n.01' (specific types of cars)
car_synset = wordnet.synset('car.n.01')
car_hyponyms = car_synset.hyponyms()
hyponym_data = [lemma.name() for synset in car_hyponyms for lemma in synset.lemmas()]
print("\nHyponyms of 'car.n.01':")
print(', '.join(hyponym_data))
# Hypernyms (general concepts) shared between 'car.n.01' and 'vehicle.n.01'
vehicle_synset = wordnet.synset('vehicle.n.01')
common_hypernyms = car_synset.lowest_common_hypernyms(vehicle_synset)
hypernym_data = [hypernym.name() for hypernym in common_hypernyms]
print("\nLowest Common Hypernyms between 'car.n.01' and 'vehicle.n.01':")
print(', '.join(hypernym_data))