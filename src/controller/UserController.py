from flask import Blueprint, Response, jsonify, request
from src.model.User import UserDTO
from src.dto.CreateUser import UserStatus

from src.service.UserService import UserService

userBlueprint = Blueprint("Users", __name__, static_url_path="/user")

userService = UserService()

@userBlueprint.route("/create", methods=["POST"])
def create_user():
    body = request.get_json()
    result, user = userService.create((body["username"]), body["email"])

    if result.status == UserStatus.CREATED:
        return jsonify(user)
    
    return Response(result.message, 200)

@userBlueprint.route("/getall", methods=["GET"])
def get_all_users():
    dictUsers = userService.find_all()

    return jsonify(dictUsers)
