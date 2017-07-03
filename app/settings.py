import os


def env():
    return os.getenv('ENV', 'local')


def secret_key():
    if env() == 'local':
        return '1234567890123456'
    else:
        return os.getenv('SECRET_KEY')
