# app.py
from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup
import requests

from embedder import chunk_text, create_vector_store, retrieve_top_chunks

app = Flask(__name__)

# ---------------------------------------
# Crawl ONLY one page
# ---------------------------------------
def crawl_single_page(url):
    try:
        res = requests.get(url, timeout=8)
        soup = BeautifulSoup(res.text, "html.parser")

        # Remove unnecessary tags
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        text = soup.get_text(" ", strip=True)
        return [text]  # return as list (important for chunk_text)

    except Exception as e:
        print("Crawl error:", e)
        return []

# ---------------------------------------
# Ask LLM via Ollama
# ---------------------------------------
def ask_llm(prompt):
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:1b",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.2,
                    "num_ctx": 1024
                }
            },
            timeout=60
        )
        return res.json().get("response", "")
    except Exception as e:
        return f"LLM Error: {e}"

# ---------------------------------------
# Home Page
# ---------------------------------------
@app.route("/")
def home():
    return render_template("index.html")

# ---------------------------------------
# Ask API
# ---------------------------------------
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    url = data.get("url")
    question = data.get("query")

    if not url or not question:
        return jsonify({"error": "URL and question required"}), 400

    try:
        # 1️⃣ Crawl only ONE page
        pages = crawl_single_page(url)

        # 2️⃣ Chunk text
        chunks = chunk_text(pages)

        # 3️⃣ Create vector store
        vector_data, chunks = create_vector_store(chunks)

        # 4️⃣ Retrieve relevant context
        context = retrieve_top_chunks(question, vector_data, chunks)

        # 5️⃣ Prompt
        prompt = f"""
Answer ONLY using the content below.
If answer not found, say:
"Information not found on the website."

Website Content:
{context}

Question:
{question}

Answer:
"""

        answer = ask_llm(prompt)
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
