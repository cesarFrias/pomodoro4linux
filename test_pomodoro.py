"""
    Test all the classes of pomodoro4linux.
"""

from unittest import TestCase, main
from optparse import OptionValueError

from pomodoro import Timer, UserInterface
from pomodoro_parser import check_positive_integer
from utils import seconds_to_minutes


class TestParse(TestCase):
    """
        Checks exclusively cases of parsing command-line.
    """
    def test_raise_with_negative(self):
        """
            Test if check_positive_integer returns a raise with
            negative number.
        """
        number = -5
        self.assertRaises(
            OptionValueError,
            check_positive_integer,
            '-w',
            '-r',
            number
        )


    def test_raise_with_0(self):
        """
            Test if check_positive_integer returns a raise with
            a neutral number.
        """
        number = 0
        self.assertRaises(
            OptionValueError,
            check_positive_integer,
            '-w',
            '-r',
            number
        )


    def test_returns_the_value_5(self):
        """
            Test if check_positive_integer returns the correct number.
        """
        number = 5
        expected = 5
        returned = check_positive_integer('-w', '-r', number)
        self.assertEqual(expected,  returned)


    def test_returns_the_value_500(self):
        """
            Test if check_positive_integer returns the correct number.
        """
        number = 500
        expected = 500
        returned = check_positive_integer('-w', '-r', number)
        self.assertEqual(expected, returned)



class TestUI(TestCase):
    """
        Checks exclusively user interface.
    """
    def setUp(self):
        """
            Override the method setUp of TestCase.
            I cannot take this name better :(
        """
        timer = Timer(300, 200)
        self.user_interface = UserInterface(timer)

    def test_seconds_to_minutes_1500(self):
        """
            Test if returns 25 minutes and zero seconds.
        """
        time_left = 1500
        returned = seconds_to_minutes(time_left)
        self.assertEqual((25, 0), returned)


    def test_seconds_to_minutes_1000(self):
        """
            Test if returns 16 minutes and 40 seconds.
        """
        time_left = 1000
        returned = seconds_to_minutes(time_left)
        self.assertEqual((16, 40), returned)


    def test_seconds_to_minutes_900(self):
        """
            Test if returns 15 minutes and zero seconds.
        """
        time_left = 900
        returned = seconds_to_minutes(time_left)
        self.assertEqual((15, 0), returned)


    def test_seconds_to_minutes_005(self):
        """
            Test if returns zero minutes and 5 seconds.
        """
        time_left = 005
        returned = seconds_to_minutes(time_left)
        self.assertEqual((0, 5), returned)


if __name__ == '__main__':
    main()
