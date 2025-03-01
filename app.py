from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# 讓 Vercel 正確辨識
if __name__ == "__main__":
    app.run()
