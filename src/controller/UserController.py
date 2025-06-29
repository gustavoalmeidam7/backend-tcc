from fastapi import APIRouter

from src.schema.User.UserCreateSchema import UserCreateSchema
from src.schema.User.UserResponseSchema import UserResponseSchema

from src.service.UserService import UserService

userService = UserService()

userRouter = APIRouter(
    prefix="/user",
    tags=["user"]
)

@userRouter.post("/create")
async def create_user(user: UserCreateSchema) -> 'UserResponseSchema':
    user = userService.create(user)

    return user

@userRouter.get("/getusers")
async def get_users(page: int = 1, pagesize: int = 15) -> 'list[UserResponseSchema]':
    return userService.find_all_page_dict(int(page), int(pagesize))
