import os


def env():
    return os.getenv('ENV', 'local')


def env_local():
    return env() == 'local'


def env_prod():
    return env() == 'prod'


def secret_key():
    if env() == 'local':
        return '1234567890123456'
    else:
        return os.getenv('SECRET_KEY')


def slack_api_token():
    return os.getenv('SLACK_API_TOKEN')
