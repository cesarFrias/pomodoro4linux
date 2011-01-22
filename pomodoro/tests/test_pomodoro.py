"""
    Test all the classes of pomodoro4linux.
"""

from unittest import TestCase, main
from optparse import OptionValueError

from pomodoro.pomodoro import Timer
from pomodoro.ui import UI, seconds_to_minutes
from pomodoro.utils.parser import check_positive_integer
from pomodoro.utils.utils import seconds_to_minutes


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

class TestUtils(TestCase):
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


    def test_seconds_to_minutes(self):
        """
            Test if returns 8 minutes and 20 seconds.
        """
        time_left = 500
        returned = seconds_to_minutes(time_left)
        self.assertEqual((8, 20), returned)

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
        time_left = 1500
        returned = seconds_to_minutes(time_left)
        self.assertEqual((25, 0), returned)
        self.assertFalse(self.test_pomodoro.running)
        self.test_pomodoro.start()
        self.assertTrue(self.test_pomodoro.running)


    def test_pause(self):
        """
            When call the function pause the expected value is running = False
        """
        time_left = 1000
        returned = seconds_to_minutes(time_left)
        self.assertEqual((16, 40), returned)
        self.test_pomodoro.pause()
        self.assertFalse(self.test_pomodoro.running)


    def test_update_running(self):
        """
            When update is called with running = True the expected vale
            is time_left - 1
        """
        time_left = 900
        returned = seconds_to_minutes(time_left)
        self.assertEqual((15, 0), returned)
        self.test_pomodoro.time_left = 12
        self.test_pomodoro.running = True
        self.test_pomodoro.update()
        self.assertEqual(self.test_pomodoro.time_left, 11)


    def test_update_not_running(self):
        """
            When update is called with running = False the expected vale
            is work_time
        """
        time_left = 005
        returned = seconds_to_minutes(time_left)
        self.assertEqual((0, 5), returned)
        work_time = 1500
        self.test_pomodoro.running = False
        self.test_pomodoro.update()
        self.assertEqual(self.test_pomodoro.time_left, work_time)

class TestUI(TestCase):
    def setUp(self):
        timer = Timer()
        self.UI = UI(timer)

    def test_function_init(self):
        self.assertEqual(self.UI.current_status, 0)
        self.assertTrue(self.UI.menu)
        self.assertTrue(self.UI.quit_item)

    def test_pause_timer(self):
        current_status = 0
        self.UI.start_timer()
        self.assertEqual(current_status, self.UI.current_status)

    def test_rest_icon_with_status_1(self):
        """
        Only work icon has tooltip
        """
        self.UI.current_status = 1
        self.UI._set_icon()
        self.assertFalse(self.UI.status_icon.get_has_tooltip())

if __name__ == '__main__':
    main()
