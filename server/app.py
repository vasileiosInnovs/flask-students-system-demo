from flask import Flask, send_file, request, jsonify, make_response
from models import db, Student, Enrollment, Course
from flask_migrate import Migrate
from dotenv import load_dotenv
import psycopg2

load_dotenv()

app = Flask(__name__)
app.config.from_prefixed_env()

db.init_app(app)
migration = Migrate(app, db)

@app.before_request
def beforerequest():
    authed = False
    if request.path.startswith("/uploads") and authed == False:
        return "Prouted route. you need to be logged in", 403


@app.route("/")
def home():
    return send_file("./static/index.html")

@app.route("/uploads/<string:filename>")
def uploads(filename):
    return send_file(f"./uploads/{filename}")

@app.route('/students', methods=['GET', 'POST'])
def students():

    if request.method == 'GET':
        students = Student.query.all()
        students_data = [student.to_dict() for student in students]

        return students_data, 200
    
    elif request.method == 'POST':
        new_student = Student(
            name=request.form.get("name"),
            age=request.form.get("age")
        )

        db.session.add(new_student)
        db.session.commit()

        student_dict = new_student.to_dict()

        response = make_response(
            jsonify(student_dict),
            201
        )

        return response

@app.route('/students/<int:id>')
def students_id(id):
    
    student = Student.query.filter(Student.id==id).first()

    return student.to_dict(), 200

@app.route('/students/<int:id>/courses', methods=['GET'])
def student_courses(id):
    student = Student.query.filter(Student.id == id).first_or_404()

    courses = [enrollment.course.to_dict() for enrollment in student.enrollments]

    return jsonify(courses), 200

#GET POST courses
@app.route('/courses', methods=['GET', 'POST'])
def courses():

    if request.method == "GET":
        courses = Course.query.all()
        courses_list = [course.to_dict() for course in courses]

        response = make_response(
            jsonify(courses_list),
            200
        )

        return response
    
    elif request.method == 'POST':
        new_course = Course(
            name=request.form.get("name")
        )

        db.session.add(new_course)
        db.session.commit()

        course_dict = new_course.to_dict()

        response = make_response(
            jsonify(course_dict),
            201
        )

        return response

#GET POST all enrollments
@app.route('/enrollments', methods=['GET', 'POST'])
def enrollments():

    if request.method == 'GET':
        enrollments = Enrollment.query.all()
        enrollments_list = [enrollment.to_dict() for enrollment in enrollments]

        response = make_response(
            jsonify(enrollments_list),
            200
        )

        return response
    
    elif request.method == 'POST':
        new_enrollment = Enrollment(
            student_id=request.form.get("student_id"),
            course_id=request.form.get("course_id"),
            grade=request.form.get("grade")
        )

        db.session.add(new_enrollment)
        db.session.commit()

        new_enrollment_dict = new_enrollment.to_dict()

        response = make_response(
            jsonify(new_enrollment_dict),
            201
        )

        return response
    
@app.route('/enrollments/<int:id>', methods=['PUT'])
def update_enrollment(id):
    enrollment = Enrollment.query.filter(Enrollment.id == id).first_or_404()
    grade = request.form.get('grade')

    if grade:
        enrollment.grade = grade
        db.session.commit()

        response = make_response(
            jsonify(enrollment.to_dict()),
            200
        )
        return response

    return jsonify({"message": "Grade is required"}), 400
    
@app.route('/enrollments/<int:id>')
def enrollment_by_id():
    enrollment = Enrollment.query.filter(Enrollment.id == id).first()

    db.session.delete(enrollment)
    db.session.commit()
    response_body = {
        "delete_successful": True,
        "message": "Review deleted."
    }
    response = make_response(
        jsonify(response_body),
        200
    )
    return response

# MISSING MODULE psycopg2

