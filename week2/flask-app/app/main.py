import os

from flask import Flask, jsonify
from flask_restx import Api, Resource

import libs.logs as logs
from configs.Config import Config

from controllers.hello_controller import welcome_api

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object('config.DevelopmentConfig')


@app.errorhandler(400)
def payload_incomplete(e):
    return jsonify(error=str(e)), 400


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify(error='method is not allowed'), 405


@app.before_request
def clear_trailing():
    from flask import redirect, request

    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])


# register API controllers
app.register_blueprint(welcome_api)

api = Api(app)

cfg = Config().get_env(app.config['ENV'])

logger = logs.get_logger()


@api.route('/health')
class Health(Resource):
    def get(self):
        return jsonify({
            'status': 'Active',
            'environment': os.environ.get('DEPLOYMENT', 'development')
        })


@api.route('/api/v1/config')
class Configs(Resource):
    def get(self):
        return jsonify({
            "title": cfg['title'],
        })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
