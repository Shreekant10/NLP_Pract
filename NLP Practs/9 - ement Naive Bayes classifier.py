import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# Step 1: Load the SMS spam dataset
sms_data = pd.read_csv("spam.csv", encoding='latin-1')
stemming = PorterStemmer()
corpus = []
for i in range(0, len(sms_data)):
    s1 = re.sub('[^a-zA-Z]', repl=' ', string=sms_data['v2'][i])
    s1 = s1.lower()
    s1 = s1.split()
    s1 = [stemming.stem(word) for word in s1 if word not in set(stopwords.words('english'))]
    s1 = ' '.join(s1)
    corpus.append(s1)
countvectorizer = CountVectorizer()
x = countvectorizer.fit_transform(corpus).toarray()
y = sms_data['v1'].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, stratify=y, random_state=2)
multinomialnb = MultinomialNB()
multinomialnb.fit(x_train, y_train)
y_pred = multinomialnb.predict(x_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))