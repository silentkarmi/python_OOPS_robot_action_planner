"""Base class of the GantryRobot and LinearRobot described here
"""

#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass
from utils.utility import print_error

@dataclass
class BaseRobot():
    """Robot class

    Returns:
        Robot(): returns a robot object
    """
    def __init__(self, name, payload, weight, gripper, bins, category="industrial") -> None:
        self._name = name
        self._category = category
        self._payload = payload
        self._weight = weight
        self._gripper = gripper
        self._accessible_bins = bins 
        
    @property
    def gripper(self):
        return self._gripper
    
    def _is_this_bin_supported(self, bin_id):
        """checks what bin it can take parts from

        Args:
            bin_id (int): id of the bin

        Returns:
            bool: returns True if the robot can reach to the bin
        """
        return bin_id in self._accessible_bins
    
    
    def pickup_part(self, bin_obj):
        """Picks up part from the bin

        Args:
            bin (Bin()): Bin object where the part is located
        """
        if (self.gripper.is_gripper_empty() and 
            self.gripper.enable and
            self._is_this_bin_supported(bin_obj.id)):
            self.gripper.object_held = bin_obj.get_part()
        else:
            print_error("Gripper is holding a object already or gripper not activated yet or bin not supported.")

    def place_part(self, agv):
        """Place part into the agv

        Args:
            agv (AGV()): Puts the part into AGV if the tray is already placed in it
        """
        if self.gripper.object_held is None:
            print_error("Nothing to place")
        else:
            if agv is None or agv.tray is None:
                print_error("No Tray Found!")
            else:
                agv.tray.parts.append(self.gripper.object_held)
                self.gripper.object_held = None