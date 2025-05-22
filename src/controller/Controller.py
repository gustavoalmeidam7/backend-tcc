from flask import Flask
from flask_restx import Api
from src.controller import UserController

def init():
    app = Flask(__name__)

    controllers = [UserController.api]

    api = Api(app, version="1.0.0", title="Api gerenciamento de ambulância TCC", prefix="/api", doc="/api/doc")

    for controller in controllers:
        api.add_namespace(controller, controller.path)

    app.run(threaded=True)

