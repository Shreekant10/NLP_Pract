import spacy
from spacy import displacy

# Load the spaCy model
sp = spacy.load('en_core_web_sm')
sen = sp(u"I like to play football. I hated it in my childhood though")
print("Original Sentence:")
print(sen.text)
word_index = 7
print("\nDetails of a specific word:")
print(f'Text: {sen[word_index].text}')
print(f'POS: {sen[word_index].pos_}')
print(f'Tag: {sen[word_index].tag_}')
print(f'Explanation: {spacy.explain(sen[word_index].tag_)}')
print("\nPOS tags for all words:")
for word in sen:
    print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')
sen = sp(u'Can you google it?')
word = sen[2]
print("\nDetails of the word 'google':")
print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')
sen = sp(u'Can you search it on google?')
word = sen[5]
print("\nDetails of the word 'google' in a different context:")
print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')
sen = sp(u"I like to play football. I hated it in my childhood though")
num_pos = sen.count_by(spacy.attrs.POS)
print("\nNumber of POS tags in the sentence:")
for k, v in sorted(num_pos.items()):
    print(f'{k}. {sen.vocab[k].text:{8}}: {v}')
sen = sp(u"I like to play football. I hated it in my childhood though")
print("\nVisualizing Parts of Speech Tags (serving in the browser):")
displacy.serve(sen, style='dep', options={'distance': 120})