from flask import Flask, request, jsonify
from chatbot import find_best_response
from flask_cors import CORS  

app = Flask(__name__)

CORS(app) 

@app.route('/chat', methods=['POST'])
def chat():
    
    data = request.get_json()
    user_message = data.get('message')

    if not user_message:
        return jsonify({'response': 'Please send a message!'}), 400

    bot_response = find_best_response(user_message)

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
