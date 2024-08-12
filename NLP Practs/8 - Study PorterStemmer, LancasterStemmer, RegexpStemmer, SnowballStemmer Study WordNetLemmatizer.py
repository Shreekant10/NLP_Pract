import nltk
from nltk.stem import PorterStemmer, LancasterStemmer, RegexpStemmer, SnowballStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
word_stemmer = PorterStemmer()
print("PorterStemmer: 'writing' ->", word_stemmer.stem('writing'))
Lanc_stemmer = LancasterStemmer()
print("LancasterStemmer: 'writing' ->", Lanc_stemmer.stem('writing'))
Reg_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)
print("RegexpStemmer: 'writing' ->", Reg_stemmer.stem('writing'))
english_stemmer = SnowballStemmer('english')
print("SnowballStemmer: 'writing' ->", english_stemmer.stem('writing'))
lemmatizer = WordNetLemmatizer()
print("\nWordNetLemmatizer:")
print("word :\tlemma")
print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))
print("better :", lemmatizer.lemmatize("better", pos="a"))