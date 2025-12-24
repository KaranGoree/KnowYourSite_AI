import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def retrieve(query, vectorizer, vectors, chunks, top_k=5):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, vectors)[0]
    top_idx = np.argsort(scores)[-top_k:]
    return [chunks[i] for i in top_idx]
