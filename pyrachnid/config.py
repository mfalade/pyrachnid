import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(24)


class DevelopmentConfiguration(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True


class TestingConfiguration(Config):
    TESTING = True


class ProductionConfiguration(Config):
    pass


app_config = dict(
    dev=DevelopmentConfiguration,
    production=ProductionConfiguration,
    test=TestingConfiguration
)