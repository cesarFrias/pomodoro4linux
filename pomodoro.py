#!/usr/bin/python
# -*- coding: utf-8 -*-
# Desenvolvido por: César Frias
# Data: 03/08/2010

"""
Pomodoro4linux - tool for better manage your time.

Copyright (C) 2010 César Frias <cagfrias@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 2 dated June, 1991.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Library General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see <http://www.gnu.org/licenses/>.

If you find any bugs or have any suggestions email: cagfrias@gmail.com
"""

from gtk import main
from gobject import timeout_add

from user_interface import UserInterface
from pomodoro_parser import option_parser

class Timer(object):
    """ Clock of the software """
    def __init__(self, work_time=1500, rest_time=300):
        self.work_time = work_time
        self.rest_time = rest_time
        self.time_left = self.work_time

        timeout_add(1000, self.update)
        self.running = False

    def start(self):
        """ Starts the clock """
        self.running = True

    def pause(self):
        """ Pauses the clock """
        self.running = False

    def update(self):
        """ Updates the clock """
        if self.running:
            if self.time_left:
                self.time_left = self.time_left - 1
            else:
                self.time_left = self.work_time

        return True

if __name__ == '__main__':
    OPTIONS, ARGS = option_parser()
    TIMER = Timer(OPTIONS.work_time, OPTIONS.rest_time)
    UI = UserInterface(TIMER)
    main()

