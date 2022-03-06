#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from constants import Const
from planner import Planner
from utility import print_partition
from utility import ask_part
from utility import ask_order_tray
from utility import ask_which_agv_for_order
from utility import ask_how_many_parts_in_tray


    
def main_func():
    planner = Planner()
    
    print_partition()
    red_parts_in_workcell = ask_part(Const.PART_RED, planner)
    blue_parts_in_workcell = 0
    green_parts_in_workcell = 0
    # ask_part(Const.PART_GREEN, planner)
    print_partition()
    tray_type = ask_order_tray()
    print_partition()
    agv_id, as_id = ask_which_agv_for_order()
    print_partition()
    red_parts_in_kit = 0
    blue_parts_in_kit = 0
    green_parts_in_kit = 0
    
    if red_parts_in_workcell:
        red_parts_in_kit = ask_how_many_parts_in_tray(Const.PART_RED)
    
    if blue_parts_in_workcell:
        blue_parts_in_kit = ask_how_many_parts_in_tray(Const.PART_BLUE)
    
    if green_parts_in_workcell:
        green_parts_in_kit = ask_how_many_parts_in_tray(Const.PART_GREEN)
    print_partition()
    
    
    planner.generate_plan()

if __name__ == '__main__':
    main_func()