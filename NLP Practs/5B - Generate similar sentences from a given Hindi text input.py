from inltk.inltk import setup, get_similar_sentences

setup('hi')
input_text = 'मैं आज बहुि खुश हां'
output = get_similar_sentences(input_text, 5, 'hi')
print("Similar Sentences:")
for sentence in output:
    print(sentence)
    print("Similar Sentences:\nमैं आज बहुि खुश हां\nमैं बहुि खुश हां\nमैं बहुि खुश हूँ\nमैं आज खुश हां\nमैं आज बहुि खुश हूँ")