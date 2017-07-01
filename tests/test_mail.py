import unittest
from mail import Mail


class TestMail(unittest.TestCase):
    def setUp(self):
        self.mail = Mail()
        self.mail.from_address = 'test1@test.com'
        self.mail.to_address = 'test2@test.com'
        self.mail.subject = 'subject'
        self.mail.message = 'message'

    def test_valid(self):
        self.assertTrue(self.mail.valid())

    def test_valid_from_address(self):
        self.mail.from_address = None
        self.assertFalse(self.mail.valid())

    def test_valid_to_address(self):
        self.mail.to_address = None
        self.assertFalse(self.mail.valid())

    def test_valid_subject(self):
        self.mail.subject = None
        self.assertFalse(self.mail.valid())

    def test_valid_message(self):
        self.mail.message = None
        self.assertFalse(self.mail.valid())
