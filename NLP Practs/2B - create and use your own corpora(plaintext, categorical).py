import nltk 
from nltk.corpus import PlaintextCorpusReader
nltk.download('punkt')

corpus_root = '/content/sample_data'
filelist = PlaintextCorpusReader(corpus_root, '.*')
print('\n File list: \n')
print(filelist.fileids()) 
print(filelist.root) 
print('\n\nStatistics for each text:\n')
print('AvgWordLen\tAvgSentenceLen\tno.ofTimesEachWordAppearsOnAvg\tFileName')
for fileid in filelist.fileids():
    num_chars = len(filelist.raw(fileid))
    num_words = len(filelist.words(fileid))
    num_sents = len(filelist.sents(fileid))
    num_vocab = len(set([w.lower() for w in filelist.words(fileid)]))
    avg_word_len = int(num_chars / num_words)
    avg_sent_len = int(num_words / num_sents)
    avg_word_freq = int(num_words / num_vocab)
    print(avg_word_len, '\t\t\t', avg_sent_len, '\t\t\t', avg_word_freq, '\t\t', fileid)