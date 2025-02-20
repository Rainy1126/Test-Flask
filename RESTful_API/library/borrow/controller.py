from flask import Blueprint
from .services import (add_borrow_service, get_borrow_by_id_service, get_all_borrows_service, 
                        update_borrow_by_id_service, delete_borrow_by_id_service, get_borrow_author_category_service)

borrow = Blueprint("borrow", __name__)


# add new borrow
@borrow.route("/borrow-management/borrow", methods=["POST"])
def add_borrow():
    return add_borrow_service()


# get borrow by id
@borrow.route("/borrow-management/borrow/<int:id>", methods=["GET"])
def get_borrow_by_id(id):
    return get_borrow_by_id_service(id)


# get all borrows
@borrow.route("/borrow-management/borrows", methods=["GET"])
def get_all_borrows():
    return get_all_borrows_service()


# update borrow by id
@borrow.route("/borrow-management/borrow/<int:id>", methods=["PUT"])
def update_borrow_by_id(id):
    return update_borrow_by_id_service(id)


# delete borrow by id
@borrow.route("/borrow-management/borrow/<int:id>", methods=["DELETE"])
def delete_borrow_by_id(id):
    return delete_borrow_by_id_service(id)


# get borrow by student name
@borrow.route("/borrow-management/borrow/<string:student_name>", methods=["GET"])
def get_borrow_by_student_name(student_name):
    return get_borrow_author_category_service(student_name)