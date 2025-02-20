from library.extension import db
from library.library_ma import StudentSchema
from library.model import Students
from flask import request, jsonify
import json
from datetime import datetime

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


def add_student_service():
    data = request.json
    if data and all(key in data for key in ['name', 'birth_date', 'gender', 'class_name']):
        name = data['name']
        birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d').date()
        gender = data['gender']
        class_name = data['class_name']
        try:
            new_student = Students(name, birth_date, gender, class_name)
            db.session.add(new_student)
            db.session.commit()
            return jsonify({"message": "Add student success"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Add student failed"}), 400

    else:
        return jsonify({"message": "Request error"}), 400
    

def get_all_students_service():
    students = Students.query.all()
    if students:
        return students_schema.dump(students)
    else:
        return jsonify({"message": "No student found"}), 404
    

def get_student_by_id_service(id):
    student = Students.query.filter_by(id=id).first()
    if student:
        return student_schema.dump(student)
    else:
        return jsonify({"message": "Student not found"}), 404
    
    

def update_student_by_id_service(id):
    student = Students.query.get(id)
    data = request.json
    if student:
        if data and all(key in data for key in ['name', 'birth_date', 'gender', 'class_name']):
            try:
                student.name = data['name']
                student.birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d').date()
                student.gender = data['gender']
                student.class_name = data['class_name']
                db.session.commit()
                return jsonify({"message": "Update success"}), 200
            except (ValueError, TypeError) as error:
                db.session.rollback()
                return jsonify({"message": "Update student failed", "error": str(error)}), 400
        else:
            return jsonify({"message": "Missing required fields"}), 400
    else:
        return jsonify({"message": "Student not found"}), 404
    


def delete_student_by_id_service(id):
    student = Students.query.get(id)
    if student:
        try:
            db.session.delete(student)
            db.session.commit()
            return jsonify({"message": "Delete success"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Delete student failed"}), 400
    else:
        return jsonify({"message": "Student not found"}), 404