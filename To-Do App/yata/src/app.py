"""yata - Yet Another To-Do App.
Server entry point.
"""

from flask import Flask
from modules import Todos


def main():
    """
    Creates a flask instance, registers necessary blueprints, and runs app.
    """

    app = Flask(__name__)

    app.register_blueprint(Todos.blueprint, url_prefix="/api/v1/todos")

    @app.errorhandler(404)
    def page_not_found(e):
        return "Page not found", 404

    app.run(port=8081, host='0.0.0.0')


if __name__ == "__main__":
    main()
