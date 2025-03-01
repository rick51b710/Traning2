from flask import Flask, jsonify, request

app = Flask(__name__)

# 模擬的訓練課表數據
workouts = [
    {"id": 1, "name": "全身訓練", "duration": "60 min"},
    {"id": 2, "name": "胸背腿", "duration": "75 min"},
    {"id": 3, "name": "上肢下肢", "duration": "60 min"}
]

# 模擬的學員數據
students = [
    {"id": 1, "name": "王國安", "progress": "第4週"},
    {"id": 2, "name": "潘聰毅", "progress": "第6週"}
]

# 根路由
@app.route('/')
def home():
    return jsonify({"message": "Hello, Vercel! Your Flask API is running."})

# 查詢所有訓練課表
@app.route('/workouts', methods=['GET'])
def get_workouts():
    return jsonify(workouts)

# 查詢特定課表
@app.route('/workouts/<int:workout_id>', methods=['GET'])
def get_workout(workout_id):
    workout = next((w for w in workouts if w["id"] == workout_id), None)
    if workout:
        return jsonify(workout)
    return jsonify({"error": "Workout not found"}), 404

# 查詢所有學員
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# 查詢特定學員
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

# 更新學員進度
@app.route('/students/<int:student_id>/progress', methods=['POST'])
def update_progress(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.json
    if "progress" not in data:
        return jsonify({"error": "Missing 'progress' field"}), 400

    student["progress"] = data["progress"]
    return jsonify({"message": f"學員 {student_id} 進度更新為 {data['progress']}"})

if __name__ == '__main__':
    app.run(debug=True)