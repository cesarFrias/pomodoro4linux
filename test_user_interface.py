from unittest import TestCase, main
from optparse import OptionParser

from user_interface import UserInterface
from pomodoro import Timer
from pomodoro_parser import PositiveInteger, option_parser

class TestUI(TestCase):

    def setUp(self):
        timer = Timer(300, 200)
        self.ui = UserInterface(timer)

    def test_seconds_to_minutes_300(self):
        time_left = 300
        returned = self.ui.seconds_to_minutes(time_left)
        self.assertEqual((5, 0), returned)

    def test_seconds_to_minutes_1500(self):
        time_left = 1500
        returned = self.ui.seconds_to_minutes(time_left)
        self.assertEqual((25, 0), returned)

    def test_seconds_to_minutes_1000(self):
        time_left = 1000
        returned = self.ui.seconds_to_minutes(time_left)
        self.assertEqual((16, 40), returned)

    def test_seconds_to_minutes_900(self):
        time_left = 900
        returned = self.ui.seconds_to_minutes(time_left)
        self.assertEqual((15, 0), returned)

    def test_seconds_to_minutes_005(self):
        time_left = 005
        returned = self.ui.seconds_to_minutes(time_left)
        self.assertEqual((0, 5), returned)

    def test_seconds_to_minutes_150(self):
        time_left = 150
        returned = self.ui.seconds_to_minutes(time_left)
        self.assertEqual((2, 30), returned)

if __name__ == '__main__':
    main()
