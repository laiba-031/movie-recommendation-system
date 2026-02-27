# Movie Recommendation App

A content-based movie recommendation application that suggests similar movies based on genre similarity using the MovieLens dataset.

---

## Overview
This project implements a content-based recommendation system that analyzes movie genres and recommends movies that are similar to a selected movie. The application uses TF-IDF vectorization and cosine similarity to compute similarity scores and displays recommendations through an interactive Streamlit web interface.

---

## Tech Stack
- Python  
- Pandas  
- Scikit-learn  
- Streamlit  

---

## Dataset
- **MovieLens Dataset (ml-latest-small)**
- Contains movie titles and genres
- Publicly available dataset used for research and learning purposes

---

## How It Works
1. Movie genre data is preprocessed and cleaned.
2. Feature engineering is performed by weighting genre information.
3. TF-IDF vectorization converts text data into numerical vectors.
4. Cosine similarity is used to find similar movies.
5. Top movie recommendations are displayed in the Streamlit app.

---

## Features
- Content-based movie recommendation
- Genre-weighted similarity computation
- Modular and readable code structure
- Interactive web interface using Streamlit

---

## Limitations
- Recommendations are based only on genre metadata
- Does not handle cold-start problems for new users
- Limited by the granularity of the MovieLens dataset

---

## Future Improvements
- Add collaborative filtering using user ratings
- Build a hybrid recommendation system
- Improve recommendation quality using richer metadata

---

## How to Run the App
```bash
pip install -r requirements.txt
streamlit run app.py
