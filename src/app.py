from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def chat_room():
    return render_template('chat.html')  # This will link to an HTML file we'll create next

if __name__ == '__main__':
    app.run(debug=True)
