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
LONG_REST_ICON = os.path.join(IMAGE_DIR, 'long-rest.png')


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
        self.break_count = 0

        self.status_icon = gtk.StatusIcon()
        self.status_icon.set_from_file(WORK_ICON)
        self.menu = gtk.Menu()
        self.quit_item = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        self._create_menu()
        self.status_icon.set_visible(True)

        self.dialog = gtk.MessageDialog(
            parent=None,
            flags=gtk.DIALOG_MODAL,
            type=gtk.MESSAGE_WARNING,
            buttons=gtk.BUTTONS_CLOSE)

        self.image = gtk.Image()
        self.image.set_from_file(REST_ICON)
        self.dialog.set_title('Pomodoro4linux')
        self.dialog.set_image(self.image)
        self.dialog.set_keep_above(True)
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
            if self.break_count == 0:
                icon = LONG_REST_ICON
            else:
                icon = REST_ICON
        self.status_icon.set_title(icon.split('/')[-1])
        self.status_icon.set_from_file(icon)

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
            if self.break_count < self.timer.max_break_count:
                self.image.set_from_file(REST_ICON)
                self.break_count += 1
                self.warn_coffee_break()
            else:
                self.image.set_from_file(LONG_REST_ICON)
                self.break_count = 0
                self.warn_long_break()

        # Keep breaking
        elif self.current_status == 1 and self.timer.time_left:
            self._set_icon()
            time_left = seconds_to_minutes(self.timer.time_left)
            if self.break_count == 0:
                label_str = 'Long Break\nRest for %02d:%02d minutes.' % \
                    (time_left)
            else:
                label_str = 'Coffee Break\nRest for %02d:%02d minutes. (%d/%d)' % \
                    (time_left[0],time_left[1],self.break_count,self.timer.max_break_count)
            self.dialog.set_markup(label_str)

        # Come back to work, lazy boy
        elif self.current_status == 1 and not self.timer.time_left:
            label_str = 'You should be working now!'
            self.image.set_from_file(WORK_ICON)
            self.dialog.set_markup(label_str)
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
        time_left = seconds_to_minutes(self.timer.time_left)
        label_str = 'Coffee Break\nRest for %02d:%02d minutes. (%d/%d)' % \
            (time_left[0],time_left[1],self.break_count,self.timer.max_break_count)
        self.dialog.set_markup(label_str)
        self.dialog.show_all()
        timeout_add(1000, self.update_timer)
        self.dialog.run()
        self.dialog.hide()
        self.timer.time_left = self.timer.work_time
        self.start_timer()

    def warn_long_break(self):
        """
           The dialog.
        """
        self.current_status = 1
        self.timer.time_left = self.timer.long_rest_time
        time_left = seconds_to_minutes(self.timer.time_left)
        label_str = 'Long Break\nRest for %02d:%02d minutes.' % \
            (time_left)
        self.dialog.set_markup(label_str)
        self.dialog.show_all()
        timeout_add(1000, self.update_timer)
        self.dialog.run()
        self.dialog.hide()
        self.timer.time_left = self.timer.work_time
        self.start_timer()
