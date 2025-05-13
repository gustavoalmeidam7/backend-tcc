from src.controller import UserController

def init():
    controllers = [UserController.userController]

    for controller in controllers:
        controller.run()
