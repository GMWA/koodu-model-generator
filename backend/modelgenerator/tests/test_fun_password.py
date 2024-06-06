from modelgenerator.utils import check_password_policy
from unittest import TestCase


class TestPassword(TestCase):
    def test_check_password_policy(self):
        # Test password length
        self.assertFalse(check_password_policy("aB1$"))
        self.assertTrue(check_password_policy("aB1$2cD3"))

        # Test uppercase
        self.assertFalse(check_password_policy("ab1$2cd3"))
        self.assertTrue(check_password_policy("aB1$2cD3"))

        # Test lowercase
        self.assertFalse(check_password_policy("AB1$2CD3"))
        self.assertTrue(check_password_policy("aB1$2cD3"))

        # Test number
        self.assertFalse(check_password_policy("aB$cd"))
        self.assertTrue(check_password_policy("aB1$2cD3"))

        # Test special character
        self.assertFalse(check_password_policy("aB1cd3"))
        self.assertTrue(check_password_policy("aB1$2cD3"))