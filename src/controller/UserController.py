from flask import Blueprint, Response, jsonify, request
from src.dto.User.UserCreateDTO import UserDTO
from src.dto.User.CreateUser import UserStatus

from src.service.UserService import UserService

import json

userBlueprint = Blueprint("Users", __name__, static_url_path="/user")

userService = UserService()

@userBlueprint.route("/create", methods=["POST"])
def create_user():
    body = request.get_json()

    user = UserDTO.from_dict(body)

    result, user = userService.create(user)

    if result.status == UserStatus.CREATED:
        return jsonify(user)

    if result.status == UserStatus.INVALID:
        return Response(json.dumps({"erros": result.message}) , 400)

@userBlueprint.route("/getall", methods=["GET"])
def get_all_users():
    return jsonify(userService.find_all_dict())
