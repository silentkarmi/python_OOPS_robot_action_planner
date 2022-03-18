"""contains the GantryRobot class
"""
#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass
from gripper.gripper import Gripper
from utils.utility import print_normal
from utils.utility import print_error
from robot.base_robot import BaseRobot

@dataclass
class GantryRobot(BaseRobot):
    """This is the ceiling robot

    This is a gantry robot, which can move along rails attached to the ceiling.
    This robot can only pick up parts from bin3 and bin4 . robot_ceiling is also the only
    robot capable of picking up trays from a table tray ( yellow_tray_table or gray_tray_-
    table ) and placing them on AGVs

    Args:
        Robot (): Base Class for all the robots

    Returns:
        GantryRobot(): creates an instance of GantryRobot
    """
    # pylint: disable=useless-super-delegation
    
    def __init__(self, name, payload, weight, bins = [3, 4], category="industrial") -> None:
        """call the base constructor for the Robot()
        """
        gripper = Gripper(name + "_gripper")
        super().__init__(name, payload, weight, gripper, bins, category="industrial")
        
        self._small_rail_length = 12
        self._long_rail_length = 20
        self._small_rail_height = 5
        self._long_rail_height = 4.75


    def pickup_tray(self, table):
        """picks up tray from the table

        Args:
            table (Table()): Table object which contains the tray
        """ 
        if (self.gripper.is_gripper_empty() and 
            self.gripper.enable):
            self.gripper.object_held = table.get_tray()
            print_normal(f"pickup_tray({self._name}, {self.gripper.object_held.type}, table)\n")
        else:
            print_error("Gripper is holding a object already or gripper not activated yet.")

    def place_tray(self, agv):
        """Places the tray into the agv

        Args:
            agv (AGV()): The agv object in which the tray has to be placed
        """
        if self.gripper.object_held is None:
            print_error("Nothing to place")
        else:
            print_normal(f"place_tray({self._name}, {self.gripper.object_held.type}, agv{agv.agv_id})\n")
            agv.tray = self.gripper.object_held
            self.gripper.object_held = None
            
    def __str__(self):
        return self._name
            