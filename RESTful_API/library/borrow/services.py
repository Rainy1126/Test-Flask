from library.extension import db
from library.library_ma import BorrowSchema
from library.model import Borrow, Books, Category, Author, Students
from flask import request, jsonify
import json
from sqlalchemy import func
from datetime import datetime

borrow_schema = BorrowSchema()
borrows_schema = BorrowSchema(many=True)


def add_borrow_service():
    data = request.json
    if data and all(key in data for key in ['book_id', 'student_id', 'borrow_date', 'return_date']):
        book_id = data['book_id']
        student_id = data['student_id']
        borrow_date = datetime.strptime(data['borrow_date'], '%Y-%m-%d').date()
        return_date = datetime.strptime(data['return_date'], '%Y-%m-%d').date()
        try:
            new_borrow = Borrow(book_id, student_id, borrow_date, return_date)
            db.session.add(new_borrow)
            db.session.commit()
            return jsonify({"message": "Add borrow success"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Add borrow failed"}), 400

    else:
        return jsonify({"message": "Request error"}), 400
    

def get_all_borrows_service():
    borrows = Borrow.query.all()
    if borrows:
        return borrows_schema.dump(borrows)
    else:
        return jsonify({"message": "No borrow found"}), 404
    

def get_borrow_by_id_service(id):
    borrow = Borrow.query.filter_by(id=id).first()
    if borrow:
        return borrow_schema.dump(borrow)
    else:
        return jsonify({"message": "Borrow not found"}), 404
    

def update_borrow_by_id_service(id):
    borrow = Borrow.query.get(id)
    data = request.json
    if borrow:
        if data and 'return_date' in data:
            try:
                borrow.return_date = datetime.strptime(data['return_date'], '%Y-%m-%d').date()
                db.session.commit()
                return jsonify({"message": "Update success"}), 200
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Update borrow failed"}), 400
    else:
        return jsonify({"message": "Borrow not found"}), 404
    

def delete_borrow_by_id_service(id):
    borrow = Borrow.query.get(id)
    if borrow:
        try:
            db.session.delete(borrow)
            db.session.commit()
            return jsonify({"message": "Delete success"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Delete borrow failed"}), 400
    else:
        return jsonify({"message": "Borrow not found"}), 404
    
    
def get_borrow_author_category_service(student_name):
    borrow = db.session.query(Borrow.id, Books.name, Category.name, Author.name).join(
        Books, Borrow.book_id == Books.id).join(
        Category, Books.category_id == Category.id).join(
        Author, Books.author_id == Author.id).join(
        Students, Borrow.student_id == Students.id).filter(
        func.lower(Students.name) == student_name.lower()).all()
    
    if borrow:
        return jsonify(f"{student_name} borrowed: {borrow}"), 200
    else:
        return jsonify({"message": "No borrow found"}), 404