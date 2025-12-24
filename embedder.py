from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def chunk_text(pages, chunk_size=500, overlap=100):
    chunks = []
    for page in pages:
        text = page.strip()
        for i in range(0, len(text), chunk_size - overlap):
            chunk = text[i:i + chunk_size]
            if chunk.strip():
                chunks.append(chunk)
    return chunks


def create_vector_store(chunks):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(chunks)
    return (vectorizer, vectors), chunks


def retrieve_top_chunks(query, vector_data, chunks, top_k=6):
    vectorizer, vectors = vector_data
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, vectors)[0]

    top_indices = similarities.argsort()[-top_k:][::-1]
    top_chunks = [chunks[i] for i in top_indices if similarities[i] > 0]

    return "\n\n".join(top_chunks)
