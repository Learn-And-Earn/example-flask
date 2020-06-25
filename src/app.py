from flask import Flask

from .config import app_config
from .controllers.controller import controller


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    app.register_blueprint(controller, url_prefix='/api/v1/model')

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'Welcome to Python Flask Microservice API'

    return app
