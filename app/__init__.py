from flask import Flask

from config import config_options


def create_app(config_name):
    """

    :param config_name:
    :return:
    """
    # register app
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    # register blueprint
    from .main import main
    app.register_blueprint(main)
    # register the request
    from .news_requests import request_config
    request_config(app)

    return app
