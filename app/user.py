from flask_login import UserMixin
from simple_aes_cipher import AESCipher, generate_secret_key
from app import settings


class User(UserMixin):
    SECRET_KEY = generate_secret_key(settings.secret_key())
    cipher = AESCipher(SECRET_KEY)

    def __init__(self, name, password, encrypted=False):
        self.name = name
        self.password = password
        self.encrypted = encrypted

    def encrypt(self):
        self.password = self.cipher.encrypt(self.password)
        self.encrypted = True
        return self

    def decrypt(self):
        self.password = self.cipher.decrypt(self.password)
        self.encrypted = False
        return self

    def to_dict(self):
        return {
            'name': self.name,
            'password': self.password
        }


class UserRepository:
    prefix = 'user_'

    def __init__(self, store):
        self.store = store

    def save(self, user):
        key = self.prefix + user.name
        self.store.dict_set(key, user.to_dict())

    def find_by_name(self, name):
        user = self.store.dict_get(self.prefix + name)
        return User(user.name, user.password, encrypted=True)
