# 🎬 Movie Recommendation System (TMDB + PostgreSQL + Streamlit)

An interactive web app that recommends movies using **content-based filtering**.  
It fetches real movie data from the **TMDB API**, stores it in a **PostgreSQL (Supabase)** database,  
and uses a **TF-IDF similarity model** to suggest movies based on content similarity.

---

## 🧠 Overview
This project demonstrates an end-to-end data pipeline and recommendation system built with Python.  
The app integrates external APIs, databases, and machine learning into a single user-friendly interface.

---

## ⚙️ Tech Stack
- **Python** – backend logic and data processing  
- **Streamlit** – web-based UI for interaction  
- **TMDB API** – real movie metadata source  
- **PostgreSQL (Supabase)** – cloud database for storage  
- **SQLAlchemy + Psycopg2** – database connectivity  
- **Pandas, Scikit-learn** – data manipulation and similarity modeling  

---

## 🚀 Features
- Fetches live movie data directly from TMDB  
- Stores movie data in PostgreSQL for persistence  
- Dynamically loads movie pages on demand  
- Builds a **TF-IDF-based similarity matrix** for recommendations  
- Uses **Streamlit session state** for caching and performance  
- Provides a clear and responsive UI  

---

## 🧩 Architecture Flow
1. **Fetch Movies** – `fetch_movies.py` retrieves data from TMDB API.  
2. **Save to Database** – data stored using SQLAlchemy and Supabase PostgreSQL.  
3. **Build Model** – `recommender.py` computes similarity between movies.  
4. **Run App** – `app.py` (Streamlit) displays recommendations interactively.

---

## 📊 Example Workflow
1. User selects number of pages to load (e.g., 5 pages = 100 movies).  
2. The app checks if the movies exist in the database.  
3. If not, it fetches new ones and saves them.  
4. A similarity model is built and cached.  
5. User searches for a movie → app shows similar ones instantly.

---

## 💡 Future Enhancements
- Add hybrid (content + collaborative) recommendations  
- Include poster previews and TMDB links  
- Deploy with a shared online database for real-time access  

---

## 🧰 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/movie-recommendation.git
cd movie-recommendation
