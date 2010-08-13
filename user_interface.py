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
        self.status_icon.set_from_file(REST_ICON)
        self.timer.pause()

    def start_timer(self, widget=None):
        self._set_icon()
        self.timer.start()

    def warn_coffe_break(self):
        dialog = gtk.Dialog('Pomodoro4linux')
        dialog.set_default_size(180, 120)
        dialog.set_keep_above(True)
        dialog.set_sensitive(False)
        dialog.set_icon_from_file(WORK_ICON)
        label = gtk.Label('Coffee Break\nRest for 5 minutes.')
        dialog.vbox.pack_start(label)
        label.show_now()
        dialog.show_now()
        #Só funciona quando quer :(
        #Only works when it wants
        self.wait_5_minutes()

        dialog.set_sensitive(True)
        dialog.run()
        dialog.destroy()

    def update_timer(self):
        if self.timer.time_left:
            time_str = 'Pomodoro4linux - %02d:%02d' % (self.timer.time_left / 60, self.timer.time_left % 60)
            self.status_icon.set_tooltip(time_str)
        else:
            self.pause_timer()
            self.warn_coffe_break()
            self.start_timer()

        return True

    def wait_5_minutes(self):
        # Sleep for five minutes till de warn goes clickable 
        sleep(300)
