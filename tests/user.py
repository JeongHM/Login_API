import unittest
from services.internals.user import UserService


class TestUserMethods(unittest.TestCase):
    def setUp(self):
        self._body = {
            'name': 'asd안',
            'nick_name': 'nickname',
            'email': 'email@email.com',
            'phone': '01099999999',
            'password': 'asdj1fklASD!@#'
        }
        self._user = UserService(body=self._body)

    def test_name(self):
        self.assertEqual(True, self._user.validate_name())

    def test_nick_name(self):
        self.assertEqual(True, self._user.validate_nick_name())

    def test_email(self):
        self.assertEqual(True, self._user.validate_email())

    def test_phone(self):
        self.assertEqual(True, self._user.validate_phone())

    def test_password(self):
        self.assertEqual(True, self._user.validate_password())


if __name__ == '__main__':
    unittest.main()
