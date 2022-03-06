#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from planner import Planner
from utility import ask_for_order
    
def main_func():
    planner = Planner()
    order = ask_for_order(planner)
    planner.generate_plan(order)

if __name__ == '__main__':
    main_func()