from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, Vercel! Your Flask app is running."})

@app.route('/api/test')
def test_api():
    return jsonify({"message": "Test API is working!"})

if __name__ == '__main__':
    app.run()