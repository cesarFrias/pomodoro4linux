# -*- coding: utf-8 -*-

from copy import copy
from optparse import Option, OptionParser, OptionValueError


def check_positive_integer(option, opt, value):
    try:
        value = int(value)
        if value > 0:
            return value
        else:
            not_positive_integer()
    except ValueError:
        not_positive_integer()

def not_positive_integer():
    raise OptionValueError("Both arguments must be Positive Integers")

def option_parser():
    usage = "%prog [OPTIONS]"
    description = """
        %prog to better manage your time, as soon as your work time ends
        starts your rest time. 
    """

    parser = OptionParser(usage, description=description,
        option_class=PositiveInteger)
    parser.add_option(
        '-w',
        '--work',
        action = 'store',
        type = 'positiveInteger',
        dest = 'work_time',
        help = 'Define the time of each work round',
        default = 1500
    )

    parser.add_option(
        '-r',
        '--rest',
        action = 'store',
        type = 'positiveInteger',
        dest = 'rest_time',
        help = 'Define the time of each rest round',
        default = 300
    )
    return parser.parse_args()

class PositiveInteger(Option):
    TYPES = Option.TYPES + ("positiveInteger",)
    TYPE_CHECKER = copy(Option.TYPE_CHECKER)
    TYPE_CHECKER["positiveInteger"] = check_positive_integer
