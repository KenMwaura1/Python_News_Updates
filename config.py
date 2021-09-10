class Config:
    """
    Base class for general configuration settings
    """
    NEWS_API_BASE_URL = ''


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
