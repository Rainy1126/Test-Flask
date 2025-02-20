import uuid
import jwt
import datetime
from library.extension import db
from library.library_ma import UserSchema, LoginAttemptSchema
from library.model import User, Login_attempt, Session
from flask import request, jsonify
import json
from sqlalchemy import func


# create session
def create_session(user_id):
    new_session = Session(user_id=user_id, session_id=str(uuid.uuid4()))
    db.session.add(new_session)
    db.session.commit()
    return new_session