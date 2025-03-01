from flask import Flask, jsonify

app = Flask(__name__)

# 根路由
@app.route('/')
def home():
    return jsonify({"message": "Hello, Vercel! Your Flask app is running."})

# 測試狀態 API
@app.route('/status')
def status():
    return jsonify({"status": "OK", "message": "Flask API is running smoothly."})

# 假設的數據 API
@app.route('/data')
def data():
    return jsonify({
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ],
        "message": "Sample data returned."
    })

if __name__ == '__main__':
    app.run(debug=True)