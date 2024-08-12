import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
text = "Nobita enjoys playing football, but he isn't particularly fond of tennis."
text_tokens = word_tokenize(text)
tokens_without_sw_default = [word for word in text_tokens if not word in stopwords.words('english')]
print("Using default NLTK stopwords:")
print("Word Tokens:", text_tokens)
print("Tokens without Stopwords:", tokens_without_sw_default)
print()

all_stopwords = stopwords.words('english')
all_stopwords.append('play')
tokens_without_sw_with_play = [word for word in text_tokens if not word in all_stopwords]
print("Adding 'play' to NLTK stopwords:")
print("Word Tokens:", text_tokens)
print("Tokens without Stopwords (including 'play'):", tokens_without_sw_with_play)
print()

all_stopwords.remove('not')
tokens_without_sw_without_not = [word for word in text_tokens if not word in all_stopwords]
print("Removing 'not' from NLTK stopwords:")
print("Word Tokens:", text_tokens)
print("Tokens without Stopwords (excluding 'not'):", tokens_without_sw_without_not)
