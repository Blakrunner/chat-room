from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route for the chat room page
@app.route('/')
def chat_room():
    return render_template('chat.html')

# Route to handle chat messages (mock interaction for now)
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data.get('message', '')
    # Placeholder response for the AI (you can replace this with your AI logic)
    ai_response = f"Echo: {user_message}"
    return jsonify({"user_message": user_message, "ai_response": ai_response})

if __name__ == '__main__':
    app.run(debug=True)
