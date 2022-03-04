#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass

from robot import Robot  

@dataclass
class RobotFloor(Robot):
    _bins_supported = (1, 2)
    
    def is_this_bin_supported(self, id):
        return id in RobotFloor._bins_supported
    
    def pickup_part(self, bin):
        if self.isGripperEmpty() and self.is_this_bin_supported(bin.id):
            self.gripper_object = bin.get_part()
        else:
            print("Gripper is holding a object already.")