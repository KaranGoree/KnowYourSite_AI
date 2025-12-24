from embedder import chunk_text, create_vector_store, retrieve_top_chunks

texts = [
    "This website provides scholarship information for students.",
    "Application process requires Aadhaar and income certificate.",
    "Last date for submission is 31st July."
]

chunks = chunk_text(texts)
vectors, stored_chunks = create_vector_store(chunks)

context = retrieve_top_chunks("What documents are required?", vectors, stored_chunks)
print(context)
