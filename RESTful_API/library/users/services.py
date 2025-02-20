import bcrypt
from library.extension import db
from library.library_ma import UserSchema
from library.model import User
from flask import request, jsonify
import json
from sqlalchemy import func


# sign up service
def signup(data):
    schema = UserSchema()
    errors = schema.validate(data)
    if errors:
        return {"error": errors}, 400

    existing_user = User.query.filter_by(username=data["username"]).first()
    if existing_user:
        return {"error": "Username already exists"}, 400

    existing_email = User.query.filter_by(email=data["email"]).first()
    if existing_email:
        return {"error": "Email is already in use"}, 400

    try:
        new_user = User(
            username=data["username"],
            password=data["password"],
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"]
        )

        db.session.add(new_user)
        db.session.commit()

        return {"message": "Sign up successful"}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500

