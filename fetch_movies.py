import requests
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import os
import time
import streamlit as st
from db_utils import get_db_engine

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"


def save_to_db(df, table_name='movies'):
    engine = get_db_engine()
    with engine.begin() as conn:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"✅ Saved {len(df)} records to '{table_name}' table.")
    
@st.cache_data(show_spinner=False)
def fetch(pages=5):
    all_movies = []
    for page in range(1, pages+1):
        url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page={page}"
        
        for attempt in range(3):  # try up to 3 times
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                data = response.json()
                break  # success, exit retry loop
            except requests.exceptions.RequestException as e:
                print(f"Attempt {attempt+1} failed: {e}")
                time.sleep(2)  # wait a bit before retrying
        else:
            print(f"Failed to fetch page {page} after 3 attempts.")
            continue

        
        for movie in data.get('results', []):
            all_movies.append({
                'id': movie.get('id'),
                'title': movie.get('title'),
                'overview': movie.get('overview',''),
                'genre_ids': movie.get('genre_ids', []),
                'vote_average': movie.get('vote_average', 0),
                'popularity': movie.get('popularity', 0),
                'poster_path': movie.get('poster_path', ""),
                'release_date': movie.get('release_date', "")
            })
        time.sleep(0.5)  # pause between pages
            
    df = pd.DataFrame(all_movies)
    return df

def poster_url(poster_path: str, size="w500"):
    if not poster_path:
        return ""
    return f"https://image.tmdb.org/t/p/{size}{poster_path}"

if __name__ == "__main__":
    df = fetch(pages=2)  # Try fetching 2 pages (~40 movies)
    print("✅ Data fetched successfully!")
    print(df.head())
    print(f"\nTotal movies fetched: {len(df)}")
    
    save_to_db(df)
