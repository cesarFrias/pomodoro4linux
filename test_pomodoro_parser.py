from unittest import TestCase, main
from optparse import OptionValueError

from pomodoro_parser import check_positive_integer

class TestParse(TestCase):

    def test_raise_with_negative(self):
        number = -5
        self.assertRaises(OptionValueError, check_positive_integer, number)


if __name__ == '__main__':
    main()
