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
from optparse import OptionParser

from user_interface import UserInterface

class Timer(object):
    def __init__(self, work_time=1500, rest_time=300):
        self.work_time = work_time
        self.rest_time = rest_time
        self.time_left = self.work_time

        timeout_add(1000, self.update)
        self.running = False

    def start(self):
       self.running = True

    def pause(self):
        self.running = False

    def update(self):
        if self.running:
            if self.time_left:
                self.time_left = self.time_left - 1
            else:
                self.time_left = self.work_time

        return True

def option_parser():
    usage = "%prog [OPTIONS]"
    description = """
%prog to better manage your time, as soon as your work time ends
starts your rest time. 
    """

    parser = OptionParser(usage, description=description)
    parser.add_option(
        '-w',
        '--work',
        action = 'store',
        type = 'int',
        dest = 'work_time',
        help = 'Define the time of each work round',
        default = 1500
    )

    parser.add_option(
        '-r',
        '--rest',
        action = 'store',
        type = 'int',
        dest = 'rest_time',
        help = 'Define the time of each rest round',
        default = 300
    )
    return parser.parse_args()

if __name__ == '__main__':
    options, args = option_parser()
    timer = Timer(options.work_time, options.rest_time)
    ui = UserInterface(timer)
    main()

