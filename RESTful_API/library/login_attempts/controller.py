from flask import Blueprint, request, jsonify
from .services import login

logins = Blueprint("logins", __name__)

# login route
@logins.route("/login", methods=["POST"])
def login_route():
    data = request.get_json()
    result, status = login(data)
    return jsonify(result), status