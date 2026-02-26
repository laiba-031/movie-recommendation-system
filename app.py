import streamlit as st
from preprocess import load_and_clean_data
from recommender import MovieRecommender
from config import DATA_PATH, TOP_N
from utils import safe_recommend

st.set_page_config(page_title="Movie Recommendation App")

st.title("🎬 Movie Recommendation App")

movies_df = load_and_clean_data(DATA_PATH)
recommender = MovieRecommender(movies_df)

selected_movie = st.selectbox(
    "Select a movie you like 👇",
    movies_df['title'].values
)

if st.button("Recommend"):
    results = safe_recommend(recommender, selected_movie)

    if results:
        st.subheader("Recommended Movies:")
        for movie in results:
            st.write("👉", movie)
    else:
        st.warning("No recommendations found")