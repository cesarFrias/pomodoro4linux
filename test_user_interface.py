from unittest import TestCase, main

from user_interface import UserInterface
from pomodoro import Timer

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


if __name__ == '__main__':
    main()
