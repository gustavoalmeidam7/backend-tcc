from flask import Flask, Response, jsonify, request
from src.model.User import UserDTO
from src.dto.CreateUser import UserStatus

from src.service.UserService import UserService

userController = Flask(__name__)

userService = UserService()

@userController.route("/user/create")
def create_user():
    body = request.get_json()
    result, user = userService.create((body["username"]), body["email"])

    if result.status == UserStatus.CREATED:
        return jsonify(user)
    
    return Response(result.message, 200)

@userController.route("/user/getall")
def get_all_users():
    dictUsers = userService.find_all()

    print("a: ", dictUsers)

    return jsonify(dictUsers)
