# model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("dataset.csv")

# Split data
X = data["text"]
y = data["label"]

# Convert text to numbers
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vectorized, y)

# Prediction function
def predict_email(email_text):
    email_vector = vectorizer.transform([email_text])
    prediction = model.predict(email_vector)[0]
    probability = model.predict_proba(email_vector).max()
    return prediction, round(probability * 100, 2)
