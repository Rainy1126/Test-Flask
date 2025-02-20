from flask import Blueprint, request, jsonify
from .services import signup

users = Blueprint("users", __name__)

# sign up route
@users.route("/signup", methods=["POST"])
def signup_route():
    data = request.get_json()
    result, status = signup(data)
    return jsonify(result), status