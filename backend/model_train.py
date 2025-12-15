import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Load movies
movies = pd.read_csv("data/movies.csv")
movies = movies.reset_index(drop=True)  # 🔑 CRITICAL

# TF-IDF on genres
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["genres"])

# Similarity matrix
content_sim = cosine_similarity(tfidf_matrix)

# Save model
os.makedirs("models", exist_ok=True)
pickle.dump(content_sim, open("models/content_sim.pkl", "wb"))

print(f"Model trained successfully on {len(movies)} movies")
