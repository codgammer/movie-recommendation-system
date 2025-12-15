from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)

movies = pd.read_csv("data/movies.csv")
movies = movies.reset_index(drop=True)

content_sim = pickle.load(open("models/content_sim.pkl", "rb"))

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

    scores = list(enumerate(content_sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:11]

    recommendations = [movies.iloc[i[0]]["title"] for i in scores]

    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
