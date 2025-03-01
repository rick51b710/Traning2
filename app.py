from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, Vercel! Your Flask app is running."})

@app.route("/health")
def health_check():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run()