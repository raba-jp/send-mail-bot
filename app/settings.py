import os


def env():
    return os.getenv('ENV', 'local')


def secret_key():
    if env() == 'local':
        return '12345678901234567890123456789012'
    else:
        return os.getenv('SECRET_KEY')
