import unittest
from demo.calculator import Democalculator


class TestDemoCalculator(unittest.TestCase):

    def test_valid_user_password(self):
        print('test_valid_user_password')

    def test_invalid_user_password(self):
        print('test_invalid_user_password')

    def test_invalid_addition(self):
        demcal = Democalculator()
        result = demcal.addition(-100,-365)
        self.assertEqual(result,"Only Positive numbers are allowded")
        print('test_invalid_addition_ok')

    def test_valid_addition(self):
        print('test_valid_addition')

    def test_valid_addition_one_more(self):
        print('test_valid_addition_one_more')


if __name__ == '__main__':
    unittest.main()

