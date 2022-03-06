#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass

from robot import Robot  

@dataclass
class RobotCeiling(Robot):
    _bins_supported = (3, 4)
    
    def __init__(self) -> None:
        super().__init__()
    
    def is_this_bin_supported(self, id):
        return id in RobotCeiling._bins_supported
    
    def pickup_part(self, bin):
        if self.isGripperEmpty() and self.is_this_bin_supported(bin.id):
            self.gripper_object = bin.get_part()
        else:
            print("Gripper is holding a object already.")
            
    def pickup_tray(self, table):
        if self.isGripperEmpty():
            self.gripper_object = table.get_tray()
        else:
            print("Gripper is holding a object already.")
        
    def place(self, obj):
        obj = self.gripper_object
        self.gripper_object = None
        return obj