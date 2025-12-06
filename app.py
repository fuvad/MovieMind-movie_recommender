import streamlit as st
import pandas as pd
import math
from fetch_movies import fetch, poster_url, save_to_db
from recommender import build_model, recommend
from db_utils import get_db_engine

st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬", layout="centered")

st.title("🎬 Movie Recommendation System (TMDB API + PostgreSQL Hybrid)")
st.markdown("""
This app recommends movies based on similarity of their content (title + overview).
It uses both **TMDB API** and **PostgreSQL** to fetch and store movie data efficiently.
""")

MOVIES_PER_PAGE = 20

#Helper function to load Data From DB or API
@st.cache_data(show_spinner=False)
def load_or_fetch_movies(pages=5):
    engine = get_db_engine()
    query = "SELECT * FROM movies;"
    
    try:
        df = pd.read_sql(query, engine)
    except Exception as e:
        st.warning(f"⚠️ Database not initialized. Fetching from TMDB...")
        df = pd.DataFrame()

    pages_in_db = math.ceil(len(df) / MOVIES_PER_PAGE) if not df.empty else 0

    if pages_in_db < pages:
        st.warning(f"⚠️ Only {pages_in_db} pages found in DB. Fetching {pages} pages from TMDB...")
        new_df = fetch(pages=pages)
        save_to_db(new_df)
        st.success(f"✅ Saved {len(new_df)} movies ({pages} pages) to database.")
        return new_df
    else:
        st.info(f"✅ Loaded {len(df)} movies ({pages_in_db} pages) from database.")
        return df
    

#Use Session State to persist data across reruns
if "movies_df" not in st.session_state:
    st.session_state.movies_df = None
if "similarity_matrix" not in st.session_state:
    st.session_state.similarity_matrix = None


#Added button to control when fetching happens
pages = st.number_input("Enter number of pages to load", min_value=1, max_value=10, value=5, step=1, key="num_pages_input")

if st.button("🚀 Load Movies"):  #prevents auto-fetch before user input
    with st.spinner("Loading movie data..."):
        st.session_state.movies_df = load_or_fetch_movies(pages=pages)

    with st.spinner("Building recommendation model..."):
        st.session_state.similarity_matrix = build_model(st.session_state.movies_df)

    st.success("✅ Movie data loaded and model built successfully!")

#Show recommendation section only after data is loaded
if st.session_state.movies_df is not None:
    movie_list = sorted(st.session_state.movies_df['title'].tolist())

    st.subheader("🔎 Search for a movie")
    selected_movie = st.selectbox("Choose a movie title", movie_list)

    if st.button("Get Recommendations"):
        with st.spinner("Finding similar movies..."):
            result, error = recommend(selected_movie, st.session_state.movies_df, st.session_state.similarity_matrix)
            if error:
                st.error(error)
            else:
                st.subheader(f"🎥 Movies similar to **{selected_movie}**:")
                
                for _, row in result.iterrows():
                    poster = poster_url(row.get("poster_path", ""), size="w342")
                    
                    cols = st.columns([1, 3])
                    with cols[0]:
                        if poster:
                            st.image(poster, width=150)
                        else:
                            st.write("🖼️ *No poster available*")
                            
                    with cols[1]:
                        st.markdown(f"**{row['title']}**")
                        st.write(f"(⭐ {row['vote_average']}) — Popularity: {round(row['popularity'], 2)}")
else:
    # 🟢 NEW: Friendly message instead of loading prematurely
    st.info("👆 Enter the number of pages and click **Load Movies** to begin.")

st.markdown("---")
st.caption("Built using TMDB API, Scikit-learn, and Streamlit.")
