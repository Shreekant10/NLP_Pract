import nltk
from collections import defaultdict
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
text = nltk.word_tokenize("Shreekant likes to play Cricket. Shreekant does not like to play Football.")
tagged = nltk.pos_tag(text)
print(tagged)
addNounWords = []
for word, tag in tagged:
    if tag in ('NN', 'NNS', 'NNPS', 'NNP'):
        addNounWords.append(word)
print(addNounWords)
temp = defaultdict(int)
for noun in addNounWords:
    temp[noun] += 1
res = max(temp, key=temp.get)
print("Word with maximum frequency : " + str(res))