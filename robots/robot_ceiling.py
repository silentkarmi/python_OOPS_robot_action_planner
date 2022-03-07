"""contains the RobotCeiling class
"""
#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass
from misc.utility import print_error
from robots.robot import Robot

@dataclass
class RobotCeiling(Robot):
    """This is the ceiling robot

    This is a gantry robot, which can move along rails attached to the ceiling.
    This robot can only pick up parts from bin3 and bin4 . robot_ceiling is also the only
    robot capable of picking up trays from a table tray ( yellow_tray_table or gray_tray_-
    table ) and placing them on AGVs

    Args:
        Robot (): Base Class for all the robots

    Returns:
        RobotCeiling(): creates an instance of RobotCeiling
    """
    # pylint: disable=useless-super-delegation

    _bins_supported = (3, 4)

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def is_this_bin_supported(cls, bin_id):
        """checks what bin it can take parts from

        Args:
            bin_id (int): id of the bin

        Returns:
            bool: returns True if the robot can reach to the bin
        """
        return bin_id in RobotCeiling._bins_supported

    def pickup_part(self, bin_obj):
        """Picks up part from the bin

        Args:
            bin (Bin()): Bin object where the part is located
        """
        if self.is_gripper_empty() and self.is_this_bin_supported(bin_obj.id):
            self.gripper_object = bin_obj.get_part()
        else:
            print_error("Gripper is holding a object already.")

    def place_part(self, agv):
        """Place part into the agv

        Args:
            agv (AGV()): Puts the part into AGV if the tray is already placed in it
        """
        if self.gripper_object is None:
            print_error("Nothing to place")
        else:
            if agv is None or agv.tray is None:
                print_error("No Tray Found!")
            else:
                agv.tray.parts.append(self.gripper_object)
                self.gripper_object = None

    def pickup_tray(self, table):
        """picks up tray from the table

        Args:
            table (Table()): Table object which contains the tray
        """
        if self.is_gripper_empty():
            self.gripper_object = table.get_tray()
        else:
            print_error("Gripper is holding a object already.")

    def place_tray(self, agv):
        """Places the tray into the agv

        Args:
            agv (AGV()): The agv object in which the tray has to be placed
        """
        if self.gripper_object is None:
            print_error("Nothing to place")
        else:
            agv.tray = self.gripper_object
            self.gripper_object = None
            