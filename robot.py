#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass
from typing import Any

@dataclass
class Robot:
    # gripper_object : Any
    
    def __init__(self) -> None:
        self.gripper_object = None
        
    def isGripperEmpty(self):
        return self.gripper_object == None
        
