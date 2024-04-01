from flask import Blueprint
import json

health_blueprint = Blueprint("health", __name__)


@health_blueprint.route("/", methods=["GET"])
def health_check():
    return "Hello, from the middleware, I am healthy."
