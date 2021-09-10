class Config:
    """
    Base class for general configuration settings
    """
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}'
    NEWS_ARTICLES_APL_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_SOURCE_ARTICLES_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey='


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
