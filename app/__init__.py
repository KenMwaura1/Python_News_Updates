from flask import Flask
from config import config_options
from commands import test


def create_app(config_name):
    """

    :param config_name:
    :return:
    """
    # register app
    app = Flask(__name__)
    # app.config.from_object(config_options[config_name])

    # register blueprint
    from .main import main
    app.register_blueprint(main)

    @app.cli.command('tests')
    def run_tests():
        test()

    return app


create_app('development').config.from_object(config_options['development'])
