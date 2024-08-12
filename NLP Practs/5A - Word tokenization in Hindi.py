# pip install spacy
# python -m spacy download xx_ent_wiki_sm
import spacy


nlp = spacy.load("xx_ent_wiki_sm")
hindi_text = "प्राकृ तिक भाषा सीखना बहुि रोमाांचक है।"
doc = nlp(hindi_text)
tokens = [token.text for token in doc]
print("Tokens:")
print(tokens)
