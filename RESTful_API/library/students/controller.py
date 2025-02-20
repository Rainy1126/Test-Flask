from flask import Blueprint
from .services import (add_student_service, get_student_by_id_service, get_all_students_service, 
                        update_student_by_id_service, delete_student_by_id_service)

student = Blueprint("student", __name__)


# add new student
@student.route("/student-management/student", methods=["POST"])
def add_student():
    return add_student_service()


# get student by id
@student.route("/student-management/student/<int:id>", methods=["GET"])
def get_student_by_id(id):
    return get_student_by_id_service(id)


# get all students
@student.route("/student-management/students", methods=["GET"])
def get_all_students():
    return get_all_students_service()


# update student by id
@student.route("/student-management/student/<int:id>", methods=["PUT"])
def update_student_by_id(id):
    return update_student_by_id_service(id)


# delete student by id
@student.route("/student-management/student/<int:id>", methods=["DELETE"])
def delete_student_by_id(id):
    return delete_student_by_id_service(id)