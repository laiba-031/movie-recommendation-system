from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, df):
        self.df = df
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.similarity = self._build_similarity()

    def _build_similarity(self):
        vectors = self.vectorizer.fit_transform(self.df['tags'])
        return cosine_similarity(vectors)

    def recommend(self, title, top_n=5, threshold=0.15):
        index = self.df[self.df['title'] == title].index[0]
        scores = list(enumerate(self.similarity[index]))
        
        filtered = [
            (i, s) for i, s in scores
            if s > threshold and i != index
        ]
        
        filtered = sorted(filtered, key=lambda x: x[1], reverse=True)
        return [self.df.iloc[i[0]].title for i in filtered[:top_n]]