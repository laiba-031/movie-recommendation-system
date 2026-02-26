def precision_at_k(recommended, relevant, k=5):
    recommended_k = recommended[:k]
    hit_count = len(set(recommended_k) & set(relevant))
    return hit_count / k