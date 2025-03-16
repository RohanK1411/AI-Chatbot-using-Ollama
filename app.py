from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_BASE_URL = "http://localhost:11434/api/generate"  # Ollama API endpoint
OLLAMA_MODEL = "llama3"  # Change to your installed model (e.g., llama3, mistral, etc.)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    # Prepare payload for Ollama
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": user_message,
        "stream": False  # Set True if you handle streaming in frontend
    }

    try:
        response = requests.post(OLLAMA_BASE_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        bot_response = data.get('response', 'No response from model.')

        return jsonify({'response': bot_response})

    except requests.RequestException as e:
        print(f"Error communicating with Ollama: {e}")
        return jsonify({'response': 'Error communicating with AI model.'})


if __name__ == '__main__':
    app.run(debug=True)