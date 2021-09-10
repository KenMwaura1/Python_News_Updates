from flask import Flask

from config import config_options


def create_app(config_name):
    """

    :param config_name:
    :return:
    """
    app = Flask(__name__, )
    app.config.from_object(config_options[config_name])
    from .main import main
    app.register_blueprint(main)

    return app
