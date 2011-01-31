"""
    User interface.
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import gtk
from gobject import timeout_add

from utils.utils import seconds_to_minutes, show_menu

__all__ = ['UI']
IMAGE_DIR = os.path.join(os.path.abspath(
    os.path.dirname(__file__)),
    '../images/'
)
WORK_ICON = os.path.join(IMAGE_DIR, 'work.png')
REST_ICON = os.path.join(IMAGE_DIR, 'rest.png')


class UI(object):
    """
        Here is the main class of the program.
    """
    def __init__(self, timer):
        """
            Initiate the interface
        """
        self.timer = timer
        self.current_status = 0

        self.status_icon = gtk.StatusIcon()
        self.status_icon.set_from_file(WORK_ICON)
        self.menu = gtk.Menu()
        self.quit_item = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        self._create_menu()
        self.status_icon.set_visible(True)

        self.dialog = gtk.Dialog('Pomodoro4linux')
        self.label = gtk.Label()
        self.start_timer()

        timeout_add(1000, self.update_timer)

    def _create_menu(self):
        """
            This method will disappear and will be engaged in __init__
        """

        self.quit_item.connect('activate', gtk.main_quit, gtk)

        self.menu.append(self.quit_item)
        self.status_icon.connect('popup-menu', show_menu, self.menu)

    def _set_icon(self):
        """
            Sets the correct icon according to the status.
        """
        if self.current_status == 0:
            icon = WORK_ICON
        else:
            icon = REST_ICON
        #self.status_icon.set_title(icon.split('/')[-1])
        self.status_icon.set_from_file(icon)

    def _set_label(self, label_str):
        """
            Updates the label of the dialog
        """
        self.label.set_text(label_str)

    def pause_timer(self):
        """
            Pauses the timer.
        """
        self.current_status = 1
        self._set_icon()
        self.timer.pause()

    def start_timer(self):
        """
            Starts the timer.
        """
        self.current_status = 0
        self._set_icon()
        self.timer.start()

    def update_timer(self):
        """
            Updates the timer, sets the tooltip and calls the dialog.
            Refactor this function.
        """
        # Keep working
        if self.current_status == 0 and self.timer.time_left:
            time_left = seconds_to_minutes(self.timer.time_left)
            time_str = 'Pomodoro4linux - %02d:%02d' % (time_left)

            self.status_icon.set_tooltip(time_str)

        # Go get some coffee
        elif self.current_status == 0 and not self.timer.time_left:
            self.warn_coffee_break()

        # Keep breaking
        elif self.current_status == 1 and self.timer.time_left:
            self._set_icon()
            time_left = seconds_to_minutes(self.timer.time_left)
            label_str = 'Coffee Break\nRest for %02d:%02d minutes.' % \
                (time_left)

            self._set_label(label_str)

        # Come back to work, lazy boy
        elif self.current_status == 1 and not self.timer.time_left:
            label_str = 'You should be working now!'
            self._set_label(label_str)
            self.pause_timer()
            self.current_status = 0
            self.timer.time_left = self.timer.work_time

        return True

    def warn_coffee_break(self):
        """
           The dialog.
        """
        self.current_status = 1
        self.timer.time_left = self.timer.rest_time
        self.dialog.set_default_size(180, 120)
        self.dialog.set_keep_above(True)
        self.dialog.set_icon_from_file(WORK_ICON)
        time_left = seconds_to_minutes(self.timer.time_left)
        label = 'Coffee Break\nRest for %02d:%02d minutes.' % (time_left)
        self.label.set_text(label)
        self.label.show_now()
        self.dialog.show_now()
        timeout_add(1000, self.update_timer)
        self.dialog.run()
        self.dialog.destroy()
        self.timer.time_left = self.timer.work_time
        self.start_timer()
