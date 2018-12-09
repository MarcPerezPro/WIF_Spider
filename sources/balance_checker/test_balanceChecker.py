from unittest import TestCase
from balance_checker import BalanceChecker

VALID_WIF = "5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ"


class TestBalanceChecker(TestCase):
    def test_is_valid(self):
        balance_checker = BalanceChecker()
        if not balance_checker.is_valid(VALID_WIF):
            self.fail()

    def test_get_key_info(self):
        self.fail()
