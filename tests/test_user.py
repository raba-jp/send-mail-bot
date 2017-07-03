import os
from nose.tools import eq_, ok_
from unittest.mock import MagicMock
from app.user import User, UserRepository


class TestUser:
    def setup(self):
        os.environ['ENV'] = 'local'
        self.user = User('sample_user', 'sample_password')

    def test_encrypt(self):
        self.user.encrypt()
        ok_(self.user.encrypted)

    def test_decrypt(self):
        self.user.encrypt().decrypt()
        ok_(not self.user.encrypted)

    def test_to_dict(self):
        expect = {'name': 'sample_user', 'password': 'sample_password'}
        eq_(self.user.to_dict(), expect)


class TestUserRepository:
    def setup(self):
        self.store_mock = MagicMock()
        self.repo = UserRepository(self.store_mock)

    def test_save(self):
        self.repo.save(User('user', 'pass'))
        self.store_mock.dict_set.assert_called_once()

    def test_find_by_name(self):
        self.repo.find_by_name('sample')
        self.store_mock.dict_get.assert_called_once()

