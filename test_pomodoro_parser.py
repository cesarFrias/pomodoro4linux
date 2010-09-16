from unittest import TestCase, main
from optparse import OptionValueError

from pomodoro_parser import check_positive_integer

class TestParse(TestCase):

    def test_raise_with_negative(self):
        number = -5
        self.assertRaises(OptionValueError, check_positive_integer, number)

    def test_raise_with_0(self):
        number = 0
        self.assertRaises(OptionValueError, check_positive_integer, number)

    def test_returns_the_value_5(self):
        number = 5
        expected = 5
        returned = check_positive_integer(number)
        self.assertEqual(expected,  returned)

    def test_returns_the_value_500(self):
        number = 500
        expected = 500
        returned = check_positive_integer(number)
        self.assertEqual(expected, returned)

if __name__ == '__main__':
    main()
