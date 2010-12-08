"""
    Some functions that not make sense in other files.
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-

def seconds_to_minutes(time_left):
    """
        Transforms seconds in minutes.
    """
    minutes_left = time_left / 60
    seconds_left = time_left % 60

    return minutes_left, seconds_left

def show_menu(status_icon, button, time, data, widget=None):
    """
        This method is just for display the menu 
    """
    data.show_all()
    data.popup(None, None, widget, button, time, status_icon)
