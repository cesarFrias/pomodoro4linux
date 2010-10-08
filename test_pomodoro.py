"""
    Test all the classes of pomodoro4linux.
"""

from unittest import TestCase, main
from optparse import OptionValueError

from pomodoro import Timer, UI
from pomodoro_parser import check_positive_integer


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


    def test_returns_the_correct_value(self):
        """
            Test if check_positive_integer returns the correct number.
        """
        number = 5
        expected = 5
        returned = check_positive_integer('-w', '-r', number)
        self.assertEqual(expected,  returned)

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
        self.user_interface = UI(timer)


    def test_seconds_to_minutes_1000(self):
        """
            Test if returns 16 minutes and 40 seconds.
        """
        time_left = 1000
        returned = self.user_interface.seconds_to_minutes(time_left)
        self.assertEqual((16, 40), returned)


    def test_seconds_to_minutes_005(self):
        """
            Test if returns zero minutes and 5 seconds.
        """
        time_left = 005
        returned = self.user_interface.seconds_to_minutes(time_left)
        self.assertEqual((0, 5), returned)

class TestTimer(TestCase):
    """
        Checks exclusively user interface.
    """
    def setUp(self):
        """
            Override the method setUp of TestCase.
            I cannot take this name better :(
        """
        self.test_pomodoro = Timer()


    def test_start(self):
        """
            When call the function start the expected value is running = True
        """
        self.assertFalse(self.test_pomodoro.running)
        self.test_pomodoro.start()
        self.assertTrue(self.test_pomodoro.running)


    def test_pause(self):
        """
            When call the function pause the expected value is running = False
        """
        self.test_pomodoro.pause()
        self.assertFalse(self.test_pomodoro.running)


    def test_update_running(self):
        """
            When update is called with running = True the expected vale
            is time_left - 1
        """
        self.test_pomodoro.time_left = 12
        self.test_pomodoro.running = True
        self.test_pomodoro.update()
        self.assertEqual(self.test_pomodoro.time_left, 11)


    def test_update_not_running(self):
        """
            When update is called with running = False the expected vale
            is work_time
        """
        work_time = 1500
        self.test_pomodoro.running = False
        self.test_pomodoro.update()
        self.assertEqual(self.test_pomodoro.time_left, work_time)



if __name__ == '__main__':
    main()
