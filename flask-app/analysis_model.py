# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
import pickle
import joblib

# Download stopwords
nltk.download('stopwords')

# Import dataset from the local file
csv_file_path = 'a1_RestaurantReviews_HistoricDump.tsv'
dataset = pd.read_csv(csv_file_path, delimiter='\t', quoting=3)

# Data Preprocessing
ps = PorterStemmer()
all_stopwords = stopwords.words('english')
all_stopwords.remove('not')
corpus = []

for i in range(len(dataset)):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)
    corpus.append(review)

# Data transformation (BoW)
cv = CountVectorizer(max_features=1420)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, -1].values

# Save BoW dictionary
bow_path = 'c1_BoW_Sentiment_Model.pkl'
pickle.dump(cv, open(bow_path, 'wb'))

# Dividing dataset into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Model fitting (Naive Bayes)
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Export NB Classifier
classifier_path = 'c2_Classifier_Sentiment_Model.joblib'
joblib.dump(classifier, classifier_path)

# Model performance
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)


score = round( accuracy_score(y_test, y_pred) * 100)
print(f'Accuracy Score: {score}')

def perform_analysis():
    
    return score 