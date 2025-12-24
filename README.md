# KnowYourSite_AI
# 🌐 Website AI Chatbot (RAG-Based)

An AI-powered chatbot that answers questions **strictly using data from a given website**.  
Users can enter **any public website URL**, ask questions, and get accurate responses generated using **Retrieval-Augmented Generation (RAG)**.

---

## 🚀 Features

- Works with **any public website**
- Website-wide content extraction (same domain)
- Retrieval-Augmented Generation (RAG)
- TF-IDF + cosine similarity based retrieval
- Local LLM inference using **Ollama**
- Uses **llama3.2:1b** (low memory friendly)
- Prevents hallucinations
- Clean and simple web UI

---

## 🏗️ Architecture

Website URL → Web Scraper → Text Chunking
→ Vector Store (TF-IDF)
→ Relevant Chunk Retrieval
→ LLM (Ollama)
→ Answer

yaml
Copy code

---

## 🛠️ Tech Stack

**Backend**
- Python
- Flask
- BeautifulSoup
- Requests

**AI / NLP**
- Ollama
- llama3.2:1b
- Scikit-learn (TF-IDF)

**Frontend**
- HTML
- CSS
- JavaScript

---

## 📁 Project Structure

website-rag-chatbot/
├── app.py
├── embedder.py
├── templates/
│ └── index.html
├── static/
│ └── style.css
├── requirements.txt
└── README.md

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

```
pip install -r requirements.txt
requirements.txt
flask
requests
beautifulsoup4
scikit-learn
```
### 2️⃣ Install Ollama
Download from:
https://ollama.com/

Verify installation:

ollama --version
3️⃣ Pull the Model

ollama pull llama3.2:1b
Recommended for systems with low RAM.

4️⃣ Run the Application
```
python app.py
```
Open in browser:
```
http://127.0.0.1:5000
```
🔐 Accuracy & Safety
Answers only from website data

No external knowledge usage

Domain-restricted crawling

Prevents hallucinations

⚡ Performance
First query may take 30–60 seconds (website crawling)

Subsequent queries are faster

Large websites may take longer

Max pages crawl limit applied

🚫 Limitations
Static HTML websites only

No JavaScript-rendered pages

No login-protected sites

CPU-based inference

🎯 Use Cases
College or university website chatbot

Company documentation assistant

Product support chatbot

Hackathon AI project

Portfolio project

🔮 Future Enhancements
Vector caching

FAISS integration

Streaming responses

Multi-language support

Better embeddings

👨‍💻 Author
Karan
B.Tech CSE
AI & ML Enthusiast
