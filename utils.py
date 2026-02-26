def safe_recommend(recommender, movie):
    try:
        return recommender.recommend(movie)
    except:
        return []