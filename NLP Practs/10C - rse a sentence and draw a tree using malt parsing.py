# JAVA should be installed

from nltk.parse import malt

maltparser_dir = 'C:/Users/schau/AppData/Local/Programs/Python/Python311/maltparser-1.7.2/maltparser-1.7.2'
model_file = 'C:/Users/schau/AppData/Local/Programs/Python/Python311/engmalt.linear-1.7.mco'
mp = malt.MaltParser(maltparser_dir, model_file)
sentence = 'I saw a bird from my window.'
parsed_sentence = mp.parse_one(sentence.split())
t = parsed_sentence.tree()
print(t)
t.draw()