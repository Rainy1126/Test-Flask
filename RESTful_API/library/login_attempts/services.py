import jwt
import datetime
from library.extension import db
from library.library_ma import UserSchema, LoginAttemptSchema
from library.model import User, Login_attempt
from flask import request, jsonify
import json
from sqlalchemy import func
from library.session.services import create_session


# log in service
def create_login_attempt(data, user, login_status):
    new_login_attempt = Login_attempt(
        email=data["email"],
        password=data["password"],
        ip_address=request.remote_addr,
        login_status=login_status
    )
    if user:
        new_login_attempt.user = user
    db.session.add(new_login_attempt)
    db.session.commit()

def login(data):
    schema = LoginAttemptSchema()
    errors = schema.validate(data)
    if errors:
        return {"error": errors}, 400

    user = User.query.filter_by(email=data["email"]).first()
    if not user:
        create_login_attempt(data, None, "failed")
        return {"error": "Invalid email or password"}, 401

    if not user.check_password(data["password"]):
        create_login_attempt(data, user, "failed")
        return {"error": "Invalid email or password"}, 401

    create_login_attempt(data, user, "success")


    # Create a new session
    create_session(user.id)


    # Generate JWT token
    payload = {
        "user_id": user.id,
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1)
    }
    SECRET_KEY = "8cckiv8mJaxjujkiQJ9UPzlH7wjffhDM9ULFeiUqOp0="
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    # Create response
    response = {
        "user": {
            "id": user.id,
            "name": user.first_name + " " + user.last_name,
            "email": user.email,
            "is_active": user.is_active,
            "is_superuser": user.is_superuser,
        },
        "token": token,
        "token_type": "jwt",
    }

    return response, 200
