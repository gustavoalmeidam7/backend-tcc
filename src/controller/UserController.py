from flask import Blueprint, Response, jsonify, request
from src.dto.UserDTO import UserDTO
from src.dto.CreateUser import UserStatus

from src.service.UserService import UserService

import json

userBlueprint = Blueprint("Users", __name__, static_url_path="/user")

userService = UserService()

@userBlueprint.route("/create", methods=["POST"])
def create_user():
    body = request.get_json()

    user = UserDTO.fromDict(body)

    result, user = userService.create(user)

    if result.status == UserStatus.CREATED:
        return jsonify(user)
    
    return Response(json.dumps({"erro": result.message}) , 409)

@userBlueprint.route("/getall", methods=["GET"])
def get_all_users():
    dictUsers = userService.find_all()

    return jsonify(dictUsers)
