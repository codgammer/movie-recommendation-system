🎬 Movie Recommendation System (Machine Learning)

A Movie Recommendation System built using Machine Learning and Flask, which suggests similar movies based on content similarity.
The system uses TF-IDF Vectorization and Cosine Similarity to recommend movies and provides a clean, interactive frontend for users.

📌 Project Overview

Recommender systems are widely used in platforms like Netflix, Amazon, and YouTube.
This project implements a Content-Based Movie Recommendation System that recommends movies based on their genres.

The application is built as a full-stack ML web application with:

A Flask backend API

A modern frontend (HTML, CSS, JavaScript)

Dataset-based movie recommendations

🚀 Features

🔍 Search movies by title

🎯 Get top similar movie recommendations

⚡ Fast recommendations using precomputed similarity matrix

🧠 Machine Learning with TF-IDF & Cosine Similarity

🎨 Modern and responsive frontend UI

🧪 Error handling for invalid movie names

📦 GitHub version-controlled project

🛠️ Tech Stack
Frontend

HTML5

CSS3

JavaScript

Backend

Python

Flask

Flask-CORS

Machine Learning

Pandas

Scikit-learn

TF-IDF Vectorizer

Cosine Similarity

Tools

Git & GitHub

VS Code

📂 Project Structure
movie-recommendation-system/
│
├── backend/
│   ├── app.py
│   ├── model_train.py
│   ├── evaluate.py
│   ├── requirements.txt
│   ├── data/
│   │   ├── movies.csv
│   │   └── ratings.csv
│   └── models/
│       └── content_sim.pkl
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── README.md
└── .gitignore

⚙️ How It Works

Movie genres are vectorized using TF-IDF

Cosine similarity is calculated between movies

Similarity scores are stored in a matrix

When a user enters a movie name:

The system finds similar movies

Returns the top recommendations via API

The frontend displays recommendations dynamically

▶️ How to Run the Project Locally
1️⃣ Clone the Repository
git clone https://github.com/codgammer/movie-recommendation-system.git
cd movie-recommendation-system

2️⃣ Setup Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Train the Model
python model_train.py

4️⃣ Run Flask Server
python app.py


Backend will run at:

http://127.0.0.1:5000/

5️⃣ Run Frontend

Open frontend/index.html using Live Server

Enter a movie name (example: Toy Story (1995))

Click Recommend

📊 Evaluation Metrics

The system can be evaluated using:

RMSE (Root Mean Square Error)

MAE (Mean Absolute Error)

Graphs included:

Rating distribution

Accuracy comparison

🧠 Use Case

Movie recommendation platforms

OTT applications

Learning recommender system concepts

Placement-ready ML project

🏆 Resume Description

Developed a Movie Recommendation System using Machine Learning techniques such as TF-IDF and Cosine Similarity, implemented with Flask REST APIs and an interactive frontend.

🧠 Viva / Interview Explanation

“This project uses content-based filtering where movies are recommended based on genre similarity. TF-IDF vectorization converts text data into numerical form, and cosine similarity is used to find similar movies efficiently.”

🔮 Future Enhancements

Hybrid recommendation (Content + Collaborative Filtering)

Movie poster integration using TMDB API

User login and personalized recommendations

Deployment using Render and Netlify

React-based frontend

👨‍💻 Author

Kishan Harishchandra Prabhu
GitHub: https://github.com/codgammer

