from flask import Flask, Response

userController = Flask(__name__)

@userController.route("/hello")
def hello_world():
    return Response("Hello, world!", 200)
