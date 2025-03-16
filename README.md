# Ollama Chatbot in Python (Flask)

## Description
A simple chatbot using Python Flask as backend and Ollama as LLM backend. Frontend is HTML/JS.

## Setup Instructions

### 1. Install Ollama
Ensure Ollama is installed and running on your machine: https://ollama.com/

Start a model in Ollama:
```
ollama run llama3
```

### 2. Setup Python Flask app
```bash
pip install Flask requests
```

### 3. Run Flask app
```bash
python app.py
```

### 4. Access Chatbot
Open browser at `http://127.0.0.1:5000/`

## Notes
- Adjust `OLLAMA_MODEL` in `app.py` for your model (e.g., llama3, mistral).
- API runs on port 5000.