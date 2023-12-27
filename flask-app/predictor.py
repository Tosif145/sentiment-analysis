import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import joblib

# Download stopwords
nltk.download('stopwords')

# Import dataset from a specific folder (modify as needed)
dataset = pd.read_csv('a2_RestaurantReviews_FreshDump.tsv', delimiter='\t', quoting=3)

# Data cleaning
ps = PorterStemmer()
all_stopwords = stopwords.words('english')
all_stopwords.remove('not')

corpus = []

for i in range(0, 100):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)
    corpus.append(review)

# Data transformation (using the saved BoW dictionary)
# Load the BoW model
cvFile = 'c1_BoW_Sentiment_Model.pkl'
cv = pickle.load(open(cvFile, 'rb'))

X_fresh = cv.transform(corpus).toarray()
print(X_fresh.shape)

# Predictions (using the saved sentiment classifier)
# Load the classifier model
classifierFile = 'c2_Classifier_Sentiment_Model.joblib'
classifier = joblib.load(classifierFile)

y_pred = classifier.predict(X_fresh)
print(y_pred)

# Add predicted labels to the dataset
dataset['predicted_label'] = y_pred.tolist()

# Save the dataset with predicted labels
dataset.to_csv("c3_Predicted_Sentiments_Fresh_Dump.tsv", sep='\t', encoding='UTF-8', index=False)

# Return the predicted labels (y_pred) in the response
response_data = {'sentiment_predictions': y_pred.tolist()}
# print(response_data)

# Save the predicted labels to a file
np.savetxt('predicted_labels.txt', y_pred, fmt='%d')