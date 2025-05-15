from flask import Flask
from src.controller import UserController

def init():
    app = Flask(__name__)

    blueprints = [UserController.userBlueprint]

    for blueprint in blueprints:
        app.register_blueprint(blueprint, url_prefix=blueprint.static_url_path)

    app.run()
