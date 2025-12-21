# register the request
from app.news_requests import request_config


def config_app(app):
    request_config(app)


def test():
    """
    function to run tests
    :return:
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
