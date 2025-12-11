# 🎬 Movie Recommendation System (TMDB + PostgreSQL + Streamlit)

An interactive web app that recommends movies using **content-based filtering**.  
It fetches real movie data from the **TMDB API**, stores it in a **PostgreSQL** database,  
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
- **PostgreSQL** – local relational database for persistence 
- **SQLAlchemy + Psycopg2** – ORM and connection drivers
- **Pandas, Scikit-learn** – data manipulation and similarity modeling  

---

## 🚀 Features
- Fetches live movie data directly from TMDB  
- Saves and reuses data via PostgreSQL 
- Dynamically switches between API and database based on requested pages
- Builds a **TF-IDF-based similarity matrix** for recommendations  
- Uses **Streamlit session state** for caching and performance  
- Provides a clear and responsive UI  

---

## 🧩 Architecture Flow
1. **Fetch Movies** – retrieves data from TMDB API.  
2. **Store Data** – movies are saved locally using SQLAlchemy and PostgreSQL.
3. **Build Model** – computes similarity between movies.
4. **Hybrid Data Loader Func** – decides between database and API. 
5. **Run App** – (Streamlit) displays recommendations interactively.

---

## 📊 Example Workflow
1. User selects number of pages to load (1 page = 20 movies).  
2. The app checks if the movies exist in the database.  
3. If not, it fetches new ones and saves them.  
4. A similarity model is built and cached.  
5. User searches for a movie -> app shows similar ones instantly.

---

## 💡 Future Enhancements
- Add hybrid (content + collaborative) recommendations  
- Include poster previews and TMDB links  
- Deploy with a shared online database for real-time access  

---

## 🧰 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/fuvad/MovieMind-movie_recommender.git
cd movie-recommendation
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Add Environment Variables
- Follow the .env.example format

### 4️⃣ Run the App
```
streamlit run app.py
```
---

## 🖼️ Screenshots
<img width="873" height="837" alt="image" src="https://github.com/user-attachments/assets/348a87cf-88e0-4ea6-a994-4c7c4ffd2b83" />
