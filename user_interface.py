#!/usr/bin/python
# -*- coding: utf-8 -*-
# Desenvolvido por: César Frias
# Data: 02/08/2010


import os
import gtk
from time import sleep
from gobject import timeout_add

IMAGE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images/')
WORK_ICON = os.path.join(IMAGE_DIR, 'work.png')
REST_ICON = os.path.join(IMAGE_DIR, 'rest.png')

class UserInterface(object):

    def __init__(self, timer):
        self.timer = timer
        self.current_status = 0

        self.status_icon = gtk.StatusIcon()
        self.status_icon.set_from_file(WORK_ICON)
        self._create_menu()
        self.status_icon.set_visible(True)

        self.start_timer()

        timeout_add(1000, self.update_timer)

    def _create_menu(self):
        self.menu = gtk.Menu()

        self.quit_item = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        self.quit_item.connect('activate', gtk.main_quit, gtk)

        self.menu.append(self.quit_item)
        self.status_icon.connect('popup-menu', self._show_menu, self.menu)

    def _show_menu(self, widget, button, time, data):
        data.show_all()
        data.popup(None, None, None, button, time)

    def _set_icon(self):
        if self.current_status == 0:
            icon = WORK_ICON
        else:
            icon = REST_ICON
        self.status_icon.set_from_file(icon)

    def pause_timer(self, widget=None):
        self.current_status = 1
        self._set_icon()
        self.timer.pause()

    def start_timer(self, widget=None):
        self._set_icon()
        self.timer.start()

    def update_timer(self):
        if self.current_status == 0 and self.timer.time_left:
            time_str = 'Pomodoro4linux - %02d:%02d' % (
                                                     self.timer.time_left / 60,
                                                     self.timer.time_left % 60)
            self.status_icon.set_tooltip(time_str)

        elif self.current_status == 0 and not self.timer.time_left:
            self.warn_coffe_break()

        elif self.current_status == 1 and self.timer.time_left:
            self._set_icon()
            label_str = 'Coffee Break\nRest for %02d:%02d minutes.' % (
                                self.timer.time_left / 60,
                                self.timer.time_left % 60)
            self.label.set_text(label_str)

        elif self.current_status == 1 and not self.timer.time_left:
            label_str = 'You should be working now!'
            self.label.set_text(label_str)
            self.current_status = 0
            self.timer.time_left = self.timer.work_time

        return True

    def warn_coffe_break(self):
        self.current_status = 1
        self.timer.time_left = self.timer.rest_time
        self.dialog = gtk.Dialog('Pomodoro4linux')
        self.dialog.set_default_size(180, 120)
        self.dialog.set_keep_above(True)
        self.dialog.set_icon_from_file(WORK_ICON)
        self.label = gtk.Label('Coffee Break\nRest for %02d:%02d minutes.'
                                % (self.timer.time_left / 60,
                                self.timer.time_left % 60))
        self.dialog.vbox.pack_start(self.label)
        self.label.show_now()
        self.dialog.show_now()
        timeout_add(1000, self.update_timer)
        self.dialog.run()
        self.dialog.destroy()
        self.start_timer()
