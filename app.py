from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Hello, Vercel! Your Flask app is running."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)