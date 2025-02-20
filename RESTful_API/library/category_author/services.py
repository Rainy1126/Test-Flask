from library.extension import db
from library.library_ma import AuthorSchema, CategorySchema
from library.model import Author, Category
from flask import request, jsonify
import json

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)


def add_author_service():
    data = request.json
    if data and all(key in data for key in ['name']):
        name = data['name']
        if Author.query.filter_by(name=name).first():
            return jsonify({"message": "Author name already exists"}), 400
        try:
            new_author = Author(name)
            db.session.add(new_author)
            db.session.commit()
            return jsonify({"message": "Add author success"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Add author failed"}), 400

    else:
        return jsonify({"message": "Request error"}), 400
    


def get_author_by_id_service(id):
    author = Author.query.filter_by(id=id).first()
    if author:
        return author_schema.dump(author)
    else:
        return jsonify({"message": "Author not found"}), 404
    

def get_all_authors_service():
    authors = Author.query.all()
    if authors:
        return authors_schema.dump(authors)
    else:
        return jsonify({"message": "No author found"}), 404
    

def update_author_by_id_service(id):
    author = Author.query.get(id)
    data = request.json
    if author:
        if data and 'name' in data:
            try:
                author.name = data['name']
                db.session.commit()
                return jsonify({"message": "Update success"}), 200
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Update author failed"}), 400
    else:
        return jsonify({"message": "Author not found"}), 404
    

def delete_author_by_id_service(id):
    author = Author.query.get(id)
    if author:
        try:
            db.session.delete(author)
            db.session.commit()
            return jsonify({"message": "Delete success"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Delete author failed"}), 400
    else:
        return jsonify({"message": "Author not found"}), 404
    

def add_category_service():
    data = request.json
    if data and all(key in data for key in ['name']):
        name = data['name']
        if Category.query.filter_by(name=name).first():
            return jsonify({"message": "Category name already exists"}), 400
        try:
            new_category = Category(name)
            db.session.add(new_category)
            db.session.commit()
            return jsonify({"message": "Add category success"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Add category failed"}), 400

    else:
        return jsonify({"message": "Request error"}), 400
    

def get_category_by_id_service(id):
    category = Category.query.filter_by(id=id).first()
    if category:
        return category_schema.dump(category)
    else:
        return jsonify({"message": "Category not found"}), 404
    

def get_all_categories_service():
    categories = Category.query.all()
    if categories:
        return categories_schema.dump(categories)
    else:
        return jsonify({"message": "No category found"}), 404
    

def update_category_by_id_service(id):
    category = Category.query.get(id)
    data = request.json
    if category:
        if data and 'name' in data:
            try:
                category.name = data['name']
                db.session.commit()
                return jsonify({"message": "Update success"}), 200
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Update category failed"}), 400
    else:
        return jsonify({"message": "Category not found"}), 404
    

def delete_category_by_id_service(id):
    category = Category.query.get(id)
    if category:
        try:
            db.session.delete(category)
            db.session.commit()
            return jsonify({"message": "Delete success"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Delete category failed"}), 400
    else:
        return jsonify({"message": "Category not found"}), 404
