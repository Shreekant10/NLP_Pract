# pip install nltk
import nltk
from nltk.corpus import brown 
nltk.download('brown')
print ('File ids of brown corpus\n', brown.fileids())
ca01 = brown.words('ca01')
print('\nca01 has following words:\n', ca01[:10])
print('\nca01 has', len(ca01), 'words')
print ('\n\nCategories or file in brown corpus:\n')
print (brown.categories())
print ('\n\nStatistics for each text:\n')
print('AvgWordLen\tAvgSentenceLen\tno.ofTimesEachWordAppearsOnAvg\t\tFileName')
for fileid in brown.fileids():
    num_chars = len(brown.raw(fileid)) # Counting the number of characters
    num_words = len(brown.words(fileid)) # Counting the number of words
    num_sents = len(brown.sents(fileid)) # Counting the number of sentences
    num_vocab = len(set([w.lower() for w in brown.words(fileid)]))
    avg_word_len = int(num_chars / num_words)
    avg_sent_len = int(num_words / num_sents)
    avg_word_freq = int(num_words / num_vocab)
    print (avg_word_len, '\t\t\t', avg_sent_len, '\t\t\t', avg_word_freq, '\t\t\t', fileid)