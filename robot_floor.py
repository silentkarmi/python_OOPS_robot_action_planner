#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass
from utility import print_error

from robot import Robot  

@dataclass
class RobotFloor(Robot):
    _bins_supported = (1, 2)
    
    def __init__(self) -> None:
        super().__init__()
    
    def is_this_bin_supported(self, id):
        return id in RobotFloor._bins_supported
    
    def pickup_part(self, bin):
        if self.isGripperEmpty() and self.is_this_bin_supported(bin.id):
            self.gripper_object = bin.get_part()
        else:
            print_error("Gripper is holding a object already.")
            
    def place_part(self, agv):
        if self.gripper_object == None:
            print_error("Nothing to place")
        else:
            if agv == None or agv.tray == None:
                print_error("No Tray Found!")
            else:
                agv.tray.parts.append(self.gripper_object)
                self.gripper_object = None