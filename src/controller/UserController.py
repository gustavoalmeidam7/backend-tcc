from flask import request, make_response
from flask_restx import Resource, Namespace

from src.dto.User.UserCreateDTO import UserDTO

from src.dto.User import UserCreateDTO, UserResponseDTO

from src.dto.User.CreateUser import UserStatus
from src.service.UserService import UserService

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
            return make_response(user, 200)

        if result.status == UserStatus.INVALID:
            return make_response({"erros": result.message}, 400)

@api.route("/getusers")
class GetUsers(Resource):
    @api.response(200, "Return all registered users", UserResponseDTO.doc_model(api))
    @api.response(400, "When receive error parsing parameters")
    @api.param("page", "Page number")
    @api.param("pagesize", "Page size (between 1 and 50)")
    def get(self):
        page = request.args.get("page")
        pagesize = request.args.get("pagesize")

        if not page.isnumeric() or not pagesize.isnumeric():
            return make_response({"error": "Error parsing parameters!"}, 400)

        return make_response(userService.find_all_page_dict(int(page), int(pagesize)), 200)
