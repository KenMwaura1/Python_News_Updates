from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    """
    Base class for general configuration settings
    """
    API_KEY = os.getenv('API_KEY')
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}'
    NEWS_ARTICLES_APL_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_SOURCES_URL = 'https://newsapi.org/v2/top-headlines/sources?category={}&apiKey={}'
    NEWS_SOURCES_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    ALL_NEWS_SOURCES = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'


class DevConfig(Config):
    """
    Dev config class
    """
    DEBUG = True


class ProdConfig(Config):
    """
    Production config class
    """
    DEBUG = False


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
