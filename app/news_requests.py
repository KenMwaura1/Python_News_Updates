import requests

from .models import Articles, NewsSources

news_sources_url = None
news_articles_url = None
news_base_url = None
api_key = None


def request_config(app):
    """
    function to assign proper values to variables required to make requests to the Api
    :param app:
    :return: values from the config file
    """
    global news_sources_url, news_articles_url, news_base_url, api_key
    news_sources_url = app.config.get('NEWS_SOURCES_URL')
    news_articles_url = app.config.get('NEWS_ARTICLES_APL_URL')
    news_base_url = app.config.get('NEWS_API_BASE_URL')
    api_key = app.config.get('api_key')
