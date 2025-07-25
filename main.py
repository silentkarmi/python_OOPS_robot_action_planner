"""main file
"""

#!/usr/bin/env python3
# Author @ Kartikeya Mishra

# pylint: disable=no-name-in-module
# pylint: disable=import-error

from planner.planner import Planner
from utils.utility import ask_for_order

def main_func():
    """This is the starting point of the program
    """
    planner = Planner()
    order = ask_for_order(planner)
    planner.generate_plan(order)

if __name__ == '__main__':
    main_func()
    