import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import os

movies = pd.read_csv("data/movies.csv")
movies = movies.reset_index(drop=True)

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["genres"])

os.makedirs("models", exist_ok=True)

pickle.dump(tfidf, open("models/tfidf.pkl", "wb"))
pickle.dump(tfidf_matrix, open("models/tfidf_matrix.pkl", "wb"))

print("TF-IDF model saved successfully")
