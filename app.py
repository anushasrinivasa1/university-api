from flask import Flask, jsonify, request

app = Flask(__name__)

students = {}
courses = {}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Enhanced University API!"}), 200

@app.route('/students', methods=['POST'])
def create_student():
    if not request.json or not 'first_name' in request.json or not 'last_name' in request.json:
        return jsonify({"error": "First name and last name are required"}), 400
    
    student_id = len(students) + 1
    student = {
        "id": student_id,
        "first_name": request.json['first_name'],
        "last_name": request.json['last_name'],
        "courses": []
    }
    students[student_id] = student
    return jsonify(student), 201

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(list(students.values())), 200

@app.route('/courses', methods=['POST'])
def create_course():
    if not request.json or not 'course_name' in request.json or not 'course_code' in request.json:
        return jsonify({"error": "Course name and course code are required"}), 400
    
    course_id = len(courses) + 1
    course = {
        "id": course_id,
        "course_name": request.json['course_name'],
        "course_code": request.json['course_code'],
        "description": request.json.get('description', "")
    }
    courses[course_id] = course
    return jsonify(course), 201

@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(list(courses.values())), 200

@app.route('/students/<int:student_id>/courses', methods=['POST'])
def assign_course_to_student(student_id):
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404
    
    if not request.json or not 'course_id' in request.json:
        return jsonify({"error": "Course ID is required"}), 400
    
    course_id = request.json['course_id']
    if course_id not in courses:
        return jsonify({"error": "Course not found"}), 404
    
    students[student_id]['courses'].append(courses[course_id])
    return jsonify({"message": f"Course {course_id} assigned to student {student_id}"}), 200

@app.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404
    
    student_courses = students[student_id]['courses']
    return jsonify(student_courses), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
