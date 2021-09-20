
class Config(object):
    DEBUG = False
    TESTING = False

    def __init__(self):
        pass


class ProductionConfig(Config):
    DEBUG = True
    ENV = 'prod'


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'dev'


class TestingConfig(Config):
    TESTING = True
    ENV = 'test'
