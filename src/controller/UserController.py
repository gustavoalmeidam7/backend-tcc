from flask import Response, jsonify, request, make_response
from flask_restx import Resource, Namespace

from src.dto.User.UserCreateDTO import UserDTO

from src.dto.User import UserCreateDTO, UserResponseDTO

from src.dto.User.CreateUser import UserStatus
from src.service.UserService import UserService

import json

api = Namespace("Users", description="Users blueprint", path="/user")

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

@api.route("/getusers")
class GetUsers(Resource):
    @api.response(200, "Return all registered users", UserResponseDTO.doc_model(api))
    @api.response(400, "When recive error parsing parameters")
    @api.param("page", "Page number")
    @api.param("pagesize", "Page size (between 1 and 50)")
    def get(self):
        page = request.args.get("page")
        pagesize = request.args.get("pagesize")

        if not page.isnumeric():
            return make_response({"error": "Error parsing page param!"}, 400)
        
        if not pagesize.isnumeric():
            return make_response({"error": "Error parsing pagesize param!"}, 400)

        return make_response(userService.find_all_page_dict(int(page), int(pagesize)), 200)
