from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import streamlit as st

@st.cache_data(show_spinner=False)
def build_model(df):
    df['combined'] = df['title'].fillna('') + ' ' + df['overview'].fillna('')
    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    tfidf_matrix = tfidf.fit_transform(df['combined'])
    similarity = cosine_similarity(tfidf_matrix)
    return similarity

def recommend(movie_title, df, similarity, top_n=5):
    if movie_title not in df['title'].values:
        return None, "Movie Not found in the dataset"
    
    index = df[df['title'] == movie_title].index[0]
    distances = similarity[index]
    recommended_indices = distances.argsort()[::-1][1:top_n+1]

    recommendations = df.iloc[recommended_indices][['title', 'vote_average', 'popularity', 'poster_path']]
    return recommendations, None