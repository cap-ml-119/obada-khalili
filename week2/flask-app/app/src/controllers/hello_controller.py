
from flask import request, jsonify, Blueprint, abort

from models.hello import Hello

welcome_api = Blueprint('welcome_api', __name__, url_prefix='/api/v1/welcome')


@welcome_api.route('', methods=['GET'])
def get_welcome_message():
    message = Hello(firstname='unknown', lastname='unknown', age=0)
    return jsonify(message.to_dict())


@welcome_api.route('/<firstname>/<lastname>/<age>', methods=['GET'])
def serve_the_welcome_package(firstname: str, lastname: str, age: int):
    message = Hello(firstname=firstname, lastname=lastname, age=age)
    return jsonify(message.to_dict())


@welcome_api.route('', methods=['POST'])
def set_welcome_message():

    req_body = request.get_json(force=True)
    if not req_body:
        return abort(400, description="payload is missing or not in json format")

    if req_body is not None:
        firstname = req_body.get('firstname', None)
        lastname = req_body.get('lastname', None)
        age = req_body.get('age', None)

        if firstname and lastname and age:
            message = Hello(firstname=firstname, lastname=lastname, age=age)
            return jsonify(message.to_dict())
        return abort(400, description="payload is missing or incomplete")

    else:
        abort(400, description="payload is missing or incomplete")
