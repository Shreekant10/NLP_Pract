# pip install gensim

import gensim
from gensim.parsing.preprocessing import remove_stopwords
from nltk.tokenize import word_tokenize
from tabulate import tabulate
text = "Ben likes to play football, however he is not too fond of tennis."
filtered_sentence = remove_stopwords(text)
all_stopwords = gensim.parsing.preprocessing.STOPWORDS
from gensim.parsing.preprocessing import STOPWORDS
all_stopwords_gensim = STOPWORDS.union(set(['likes', 'play']))
text_tokens = word_tokenize(text)
tokens_without_sw1 = [word for word in text_tokens if not word in all_stopwords_gensim]
all_stopwords_gensim = STOPWORDS.difference({"not"})
text_tokens = word_tokenize(text)
tokens_without_sw2 = [word for word in text_tokens if not word in all_stopwords_gensim]
data = [
    ["1. Remove stopwords using Gensim's default stopwords list:", filtered_sentence],
    ["2. Gensim's default stopwords list:", '\n'.join(all_stopwords)],
    ["3. Remove 'likes' and 'play' from Gensim's default stopwords list:", tokens_without_sw1],
    ["4. Remove 'not' from Gensim's default stopwords list:", tokens_without_sw2],
    ["Explanation:", "Using Gensim: Adding and Removing Stop Words in Default Gensim Stop Words List"]
]
print(tabulate(data, headers=['Output Section', 'Content'], tablefmt='grid'))