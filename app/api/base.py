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


def get_json_file(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


class Infratoken(Resource):
    def get(self):
        styles = get_json_file("app/styles/colors-infra.json")
        images = get_json_file("app/styles/images-infratoken.json")
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
