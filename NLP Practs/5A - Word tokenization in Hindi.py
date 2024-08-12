# pip install torch==3.3.1
# pip install inltk
# pip install tornado==4.5.3

from inltk.inltk import setup
from inltk.inltk import tokenize

setup('hi') # 'hi' is the language code for Hindi
hindi_text = "प्राकृतिक भाषा सीखना बहुि रोमाांचक है।"
tokens = tokenize(hindi_text, "hi")
print("Tokens:")
print(tokens)
print("Print Tokens:")
print(['प्राकृतिक', 'भाषा', 'सीखना', 'बहुि', 'रोमाांचक', 'है', '।'])