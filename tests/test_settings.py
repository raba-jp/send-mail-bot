import os
from app import settings
from nose.tools import eq_


class TestSettings:
    def setup(self):
        os.environ['ENV'] = 'local'

    def test_env(self):
        expect = 'local'
        eq_(settings.env(), expect)

    def test_local_secret_key(self):
        expect = '12345678901234567890123456789012'
        eq_(settings.secret_key(), expect)

    def test_prod_secret_key(self):
        expect = '09876543210987654321098765432109'
        os.environ['ENV'] = 'prod'
        os.environ['SECRET_KEY'] = expect

        eq_(settings.secret_key(), expect)
