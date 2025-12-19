from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import os
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

movies_path = os.path.join(BASE_DIR, "data", "movies.csv")
tfidf_path = os.path.join(BASE_DIR, "models", "tfidf.pkl")
tfidf_matrix_path = os.path.join(BASE_DIR, "models", "tfidf_matrix.pkl")

movies = pd.read_csv(movies_path)
movies = movies.reset_index(drop=True)

tfidf = pickle.load(open(tfidf_path, "rb"))
tfidf_matrix = pickle.load(open(tfidf_matrix_path, "rb"))

@app.route("/")
def home():
    return "Backend is running successfully"

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    if not data or "movie" not in data:
        return jsonify({"error": "Invalid input"})

    movie = data["movie"]

    if movie not in movies["title"].values:
        return jsonify({"error": "Movie not found"})

    idx = movies.index[movies["title"] == movie][0]

    scores = cosine_similarity(
        tfidf_matrix[idx],
        tfidf_matrix
    ).flatten()

    similar_indices = scores.argsort()[::-1][1:11]
    recommendations = movies.iloc[similar_indices]["title"].tolist()

    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
