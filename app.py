from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, Vercel! Your Flask app is running."})

@app.route('/status')
def status():
    return jsonify({"status": "OK", "message": "API is working properly"})

# 確保 Vercel 能正確找到 Flask 應用
if __name__ == "__main__":
    app.run()