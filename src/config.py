from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = False
    TESTING = False


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False


class Testing(object):
    """
    Development environment configuration
    """
    DEBUG = False
    TESTING = True


app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}
