from nose.tools import ok_
from unittest.mock import MagicMock
from app.mail import Mail


class TestMail:
    def setup(self):
        self.mail = Mail()
        self.mail.from_address = 'test1@test.com'
        self.mail.to_address = 'test2@test.com'
        self.mail.subject = 'subject'
        self.mail.message = 'message'

    def test_valid(self):
        ok_(self.mail.valid())

    def test_valid_from_address(self):
        self.mail.from_address = None
        ok_(not self.mail.valid())

    def test_valid_to_address(self):
        self.mail.to_address = None
        ok_(not self.mail.valid())

    def test_valid_subject(self):
        self.mail.subject = None
        ok_(not self.mail.valid())

    def test_valid_message(self):
        self.mail.message = None
        ok_(not self.mail.valid())

    def test_with_syntax(self):
        with Mail(MagicMock()) as mail:
            mail.from_address = "test1@test.com"
            mail.to_address = 'test2@test.com'
            mail.subject = 'subject'
            mail.message = 'message'
