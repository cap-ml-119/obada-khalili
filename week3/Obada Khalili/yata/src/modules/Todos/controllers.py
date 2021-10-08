"""
Controllers of the Todos module
"""

from flask import Blueprint, request
from json import dumps as to_json
from .model import TodosModel

blueprint = Blueprint("todo", __name__)
todos_model = TodosModel()


@blueprint.route("/")
def get_all_todos():
    """Returns all TO-Do's."""

    return to_json(todos_model.todos)


@blueprint.route("/", methods=["POST"])
def add_todo():
    """Adds a new To-Do."""

    try:
        todos_model.add_todo(request.json["title"])
        return ""
    except KeyError:
        return "Invalid JSON body. Should contain 'title'", 400
    except Exception:
        return "Internal server error", 500


@blueprint.route("/<uid>", methods=["PATCH"])
def update_todo(uid):
    """Updates a To-Do by UID."""

    try:
        todos_model.update_todo(
            uid, {
                "title": request.json.get("title"),
                "status": request.json.get("status"),
            })
        return ""
    except todos_model.TodoDNE as e:
        return e.message, 400
    except Exception:
        return "Internal server error", 500


@blueprint.route("/<uid>", methods=["DELETE"])
def delete_todo(uid):
    """Deletes a To-Do by UID."""

    try:
        todos_model.delete_todo(uid)
        return ""
    except todos_model.TodoDNE as e:
        return e.message, 400
    except Exception:
        return "Internal server error", 500
