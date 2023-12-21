import os
import itertools
from datetime import datetime
from bson.objectid import ObjectId
from app.utils.slugify import slugify
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
from app.utils.return_url import return_url_file
from flask import request, jsonify, make_response, Blueprint
import json

api_todos = Blueprint("api_todos", __name__)
api = Api(api_todos)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_json_file(file_path):
    if not os.path.exists(file_path):
        return {"error": "File not found"}

    with open(file_path, "r") as file:
        return json.load(file)


class Infratoken(Resource):
    def get(self):
        styles = get_json_file(
            "/Users/rafaelricco/Documents/Emana/flask-mongodb/app/styles/colors-infra.json"
        )
        images = get_json_file(
            "/Users/rafaelricco/Documents/Emana/flask-mongodb/app/styles/images-infratoken.json"
        )

        if "error" in styles or "error" in images:
            return jsonify({"error": "One or more files not found"}), 404

        return jsonify({"styles": styles, "images": images})


class Dtvm(Resource):
    def get(self):
        styles = get_json_file("app/styles/colors-dtvmxpo.json")
        images = get_json_file("app/styles/images-dtvm.json")
        return jsonify({"styles": styles, "images": images})


class Invista(Resource):
    def get(self):
        styles = get_json_file("app/styles/colors-invista.json")
        images = get_json_file("app/styles/images-invista.json")
        return jsonify({"styles": styles, "images": images})


api.add_resource(Infratoken, "/infratoken")
api.add_resource(Dtvm, "/dtvm")
api.add_resource(Invista, "/invista")
