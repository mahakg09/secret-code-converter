from flask import Flask, request, jsonify
from flask_cors import CORS  
import random
import string  

app = Flask(__name__)
CORS(app) 

@app.route('/encode', methods=['POST'])
def encode():
    data = request.get_json()
    word = data.get("message", "").split()
    nword = []

    for words in word:
        if len(words) >= 3:
            words = words[1:] + words[0] 
            a = "".join(random.choices(string.ascii_letters, k=3)) 
            b = "".join(random.choices(string.ascii_letters, k=3))  
            nword.append(a + words + b)
        else:
            nword.append(words[::-1]) 

    return jsonify({"encoded": " ".join(nword)})

@app.route('/decode', methods=['POST'])
def decode():
    data = request.get_json()
    decoded = data.get("message", "").split()
    decoded_words = []

    for items in decoded:
        if len(items) < 3:
            decoded_words.append(items[::-1])  
        else:
            ogword = items[3:-3]  
            oggword = ogword[-1] + ogword[:-1]  
            decoded_words.append(oggword)

    return jsonify({"decoded": " ".join(decoded_words)})
@app.route('/')
def home():
    return "Flask server is running!"

if __name__ == '__main__':
    app.run(debug=True)
