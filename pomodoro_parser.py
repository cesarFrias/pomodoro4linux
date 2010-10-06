# -*- coding: utf-8 -*-
"""
Parses the options passed by command-line
"""

from copy import copy
from optparse import Option, OptionParser, OptionValueError


def check_positive_integer(options, option_used, value):
    """ Verifies if the value passed is a number higher than zero """
    try:
        value = int(value)
        if value > 0:
            return value
        else:
            not_positive_integer(options, option_used)
    except OptionValueError:
        not_positive_integer(options, option_used)

def not_positive_integer(options, option_used):
    """ 
        Raises an OptionValueError if at least one of
        the values is not higher than zero
    """
    raise OptionValueError("""Both arguments {0} must be Positive Integers.
Option you have used {1}""".format(options, option_used))

def option_parser():
    """ Parses the option given by command-line """
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
    """ Class used to verify if the values are higher than zero """
    TYPES = Option.TYPES + ("positiveInteger",)
    TYPE_CHECKER = copy(Option.TYPE_CHECKER)
    TYPE_CHECKER["positiveInteger"] = check_positive_integer
