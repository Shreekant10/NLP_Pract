# 1 - Default Tagger
'''
import nltk
from nltk.tag import DefaultTagger
from nltk.corpus import treebank
nltk.download('treebank')
exptagger = DefaultTagger('NN')
testsentences = treebank.tagged_sents()[1000:]
evaluation_score = exptagger.evaluate(testsentences)
print("Evaluation score of the default tagger on test sentences:")
print(evaluation_score)
tagged_sentences = exptagger.tag_sents([['Hi', ','], ['How', 'are', 'you', '?']])
print("\nTagged sentences:")
print(tagged_sentences)
'''


# 2 - Regular Expression Tagger
'''
import nltk
from nltk.corpus import brown
from nltk.tag import RegexpTagger
test_sent = brown.sents(categories='news')[0]
regexp_tagger = RegexpTagger([
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
    (r'(The|the|A|a|An|an)$', 'AT'), # articles
    (r'.*able$', 'JJ'), # adjectives
    (r'.*ness$', 'NN'), # nouns formed from adjectives
    (r'.*ly$', 'RB'), # adverbs
    (r'.*s$', 'NNS'), # plural nouns
    (r'.*ing$', 'VBG'), # gerunds
    (r'.*ed$', 'VBD'), # past tense verbs
    (r'.*', 'NN') # nouns (default)
    ])
# Print the RegexpTagger object
print("RegexpTagger object:")
print(regexp_tagger)
# Tag the sample sentence using the RegexpTagger
tagged_sentence = regexp_tagger.tag(test_sent)
# Print the tagged sentence
print("\nTagged sentence:")
print(tagged_sentence)
'''