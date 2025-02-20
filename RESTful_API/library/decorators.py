import datetime
from functools import wraps
from flask import request, jsonify
import jwt
from RESTful_API.library.config import SECRET_KEY
from library.model import Session
from library.extension import db

def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token is None:
            return jsonify({'error': 'Missing JWT token'}), 401
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']
            # Verify the user ID and other claims in the token
            # ...other claims here
            # Check if the token has expired
            if datetime.datetime.now(datetime.timezone.utc) > payload['exp']:
                # Close the session
                session = Session.query.filter_by(user_id=user_id).first()
                if session:
                    db.session.delete(session)
                    db.session.commit()
                return jsonify({'error': 'JWT token has expired', 'message': 'Please log in again'}), 401
        except jwt.ExpiredSignatureError:
            # close the session
            session = Session.query.filter_by(user_id=user_id).first()
            if session:
                db.session.delete(session)
                db.session.commit()
            return jsonify({'error': 'JWT token has expired', 'message': 'Please log in again'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid JWT token', 'message': 'Please log in again'}), 401
        return f(*args, **kwargs)
    return decorated_function