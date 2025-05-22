from flask import Response, jsonify, request
from flask_restx import Resource, Namespace

from src.dto.User.UserCreateDTO import UserDTO

from src.dto.User import UserCreateDTO, UserResponseDTO

from src.dto.User.CreateUser import UserStatus
from src.service.UserService import UserService

import json

api = Namespace("Users", description="Users blueprint", path="/api/user")

userService = UserService()

@api.route("/create")
class CreateUser(Resource):
    @api.expect(UserCreateDTO.doc_model(api))
    def post(self):
        body = request.get_json()
        user = UserDTO.from_dict(body)
        result, user = userService.create(user)

        if result.status == UserStatus.CREATED:
            return jsonify(user)

        if result.status == UserStatus.INVALID:
            return Response(json.dumps({"erros": result.message}), 400)

@api.route("/getall")
class GetAllUsers(Resource):
    @api.response(200, "Return all registered users", UserResponseDTO.doc_model(api))
    def get(self):
        return jsonify(userService.find_all_dict())
