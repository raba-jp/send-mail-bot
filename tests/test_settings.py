import os
from app import settings
from nose.tools import eq_, ok_


class TestSettings:
    def setup(self):
        os.environ['ENV'] = 'local'

    def test_env(self):
        expect = 'local'
        eq_(settings.env(), expect)

    def test_env_local(self):
        ok_(settings.env_local())

    def test_env_prod(self):
        os.environ['ENV'] = 'prod'
        ok_(settings.env_prod())

    def test_local_secret_key(self):
        expect = '1234567890123456'
        eq_(settings.secret_key(), expect)

    def test_prod_secret_key(self):
        expect = '0987654321098765'
        os.environ['ENV'] = 'prod'
        os.environ['SECRET_KEY'] = expect

        eq_(settings.secret_key(), expect)

    def test_slack_api_token(self):
        expect = 'test_token'
        os.environ['SLACK_API_TOKEN'] = expect
        eq_(settings.slack_api_token(), expect)
