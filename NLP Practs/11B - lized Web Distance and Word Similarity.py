# pip install textdistance
import numpy as np
import re
import textdistance
from sklearn.cluster import AgglomerativeClustering

texts = [
    'Reliance supermarket', 'Reliance hypermarket', 'Reliance', 'Reliance',
    'Reliance downtown', 'Relianc market',
    'Mumbai', 'Mumbai Hyper', 'Mumbai dxb', 'mumbai airport',
    'k.m trading', 'KM Trading', 'KM trade', 'K.M. Trading', 'KM.Trading'
]

def normalize(text):
    """ Keep only lower-cased text and numbers"""
    return re.sub('[^a-z0-9]+', ' ', text.lower())

def group_texts(texts, threshold=0.4):
    """ Replace each text with the representative of its cluster"""
    normalized_texts = np.array([normalize(text) for text in texts])
    distances = 1 - np.array([
        [textdistance.jaro_winkler(one, another) for one in normalized_texts]
        for another in normalized_texts
    ])
    clustering = AgglomerativeClustering(
        n_clusters=None, linkage="complete", compute_full_tree=True, distance_threshold=threshold
    ).fit(distances)
    centers = dict()
    for cluster_id in set(clustering.labels_):
        index = clustering.labels_ == cluster_id
        centrality = distances[:, index][index].sum(axis=1)
        centers[cluster_id] = normalized_texts[index][centrality.argmin()]
    return [centers[i] for i in clustering.labels_]
clustered_texts= group_texts(texts)
cluster_dict = {}
for idx, (text, clustered_text) in enumerate(zip(texts, clustered_texts)):
    cluster_id = clustered_texts.index(clustered_text)
    if cluster_id not in cluster_dict:
        cluster_dict[cluster_id] = []
    cluster_dict[cluster_id].append(text)
    for cluster_id, cluster_texts in cluster_dict.items():
        print(f"Cluster {cluster_id + 1}:")
        for text in cluster_texts:
            print(f" - {text}")

print(group_texts(texts))