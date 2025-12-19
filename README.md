# 🎬 Movie Recommendation System (Machine Learning)

A **full-stack Movie Recommendation System** built using **Machine Learning and Flask**, which suggests similar movies based on **content similarity**.  
The system uses **TF-IDF Vectorization** and **Cosine Similarity (computed at runtime)** to recommend movies and provides a clean, interactive frontend for users.

---

## 📌 Project Overview

Recommender systems are widely used in platforms like **Netflix, Amazon, and YouTube** to personalize user experience.

This project implements a **Content-Based Movie Recommendation System** that recommends movies based on their **genre similarity** using Natural Language Processing techniques.

The application is developed as a **production-ready full-stack ML web application** consisting of:

- 🧠 Machine Learning model for similarity computation  
- ⚙️ Flask REST API backend  
- 🎨 Responsive frontend using HTML, CSS, and JavaScript  
- ☁️ Cloud deployment using **Render (backend)** and **Vercel (frontend)**  

---

## 🚀 Features

- 🔍 Search movies by title  
- 🎯 Get top similar movie recommendations  
- ⚡ Fast recommendations using **runtime cosine similarity**  
- 🧠 Machine Learning with **TF-IDF Vectorization**  
- 🎨 Modern, responsive frontend UI  
- 🧪 Error handling for invalid movie names  
- 📦 GitHub version-controlled project  
- ☁️ Cloud-deployed and publicly accessible  

---

## 🛠️ Tech Stack

### Frontend
- HTML5  
- CSS3  
- JavaScript  

### Backend
- Python  
- Flask  
- Flask-CORS  

### Machine Learning
- Pandas  
- Scikit-learn  
- TF-IDF Vectorizer  
- Cosine Similarity  

### Tools & Platforms
- Git & GitHub  
- VS Code  
- Render (Backend Deployment)  
- Vercel (Frontend Deployment)  

---

## 📂 Project Structure

```text
movie-recommendation-system/
│
├── backend/
│   ├── app.py
│   ├── model_train.py
│   ├── evaluate.py
│   ├── requirements.txt
│   ├── Procfile
│   ├── data/
│   │   ├── movies.csv
│   │   └── ratings.csv
│   └── models/
│       ├── tfidf.pkl
│       └── tfidf_matrix.pkl
│
├── frontend/
│   └── index.html
│
├── README.md
└── .gitignore
```


## ⚙️ How It Works

- Movie genres are vectorized using **TF-IDF**
- TF-IDF vectors are stored as lightweight model files
- When a user enters a movie name:
  - The corresponding TF-IDF vector is retrieved
  - **Cosine similarity** is computed against all movies
  - Top similar movies are selected
- Recommendations are returned via a **Flask REST API**
- The frontend fetches and displays recommendations dynamically

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/codgammer/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2️⃣ Setup Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

### 3️⃣ Train the Model
python model_train.py


This generates:

- tfidf.pkl

- tfidf_matrix.pkl

### 4️⃣ Run Flask Server
python app.py

Backend runs at:

http://127.0.0.1:5000/

### 5️⃣ Run Frontend

- Open frontend/index.html in a browser

- Enter a movie name (example: Toy Story (1995))

- Click Recommend

---
## 📊 Evaluation Metrics


- The project includes an offline evaluation module using:

  - RMSE (Root Mean Square Error)

  - MAE (Mean Absolute Error)

- Generated visualizations:

  - Rating distribution

  - Accuracy comparison graphs

  - Evaluation scripts are executed locally only and are not part of production runtime.

---
## 🧠 Use Cases


- Movie recommendation platforms

- OTT applications

- Learning recommender system concepts

- Final-year engineering project

- Placement-ready ML portfolio project

---
## 🔮 Future Enhancements

- Hybrid recommendation (Content + Collaborative Filtering)

- Movie poster integration using TMDB API

- User authentication & personalized recommendations

- React-based frontend

- Caching for faster inference

Analytics dashboard
---
## 👨‍💻 Author

Kishan Harishchandra Prabhu
GitHub: https://github.com/codgammer

© 2025 Kishan Harishchandra Prabhu. All rights reserved.

