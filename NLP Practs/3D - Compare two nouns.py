import nltk
from nltk.corpus import wordnet
syn1 = wordnet.synsets('football')
syn2 = wordnet.synsets('soccer')
comparison_data = []
for s1 in syn1:
    for s2 in syn2:
        similarity = s1.path_similarity(s2)
        if similarity is not None:
            comparison_data.append({
                'Synset for Football': f"{s1} ({s1.pos()}) [{s1.definition()}]",
                'Synset for Soccer': f"{s2} ({s2.pos()}) [{s2.definition()}]",
                'Path Similarity': f"{similarity:.2f}"
                })
print("Comparison of synsets for 'football' and 'soccer':")
for idx, comparison in enumerate(comparison_data, start=1):
    print(f"Comparison {idx}:")
    print("Synset for Football:", comparison['Synset for Football'])
    print("Synset for Soccer:", comparison['Synset for Soccer'])
    print("Path Similarity:", comparison['Path Similarity'])
    print()