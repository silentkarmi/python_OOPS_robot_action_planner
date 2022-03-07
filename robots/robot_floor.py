"""contains the RobotFloor class
"""
#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass
from misc.utility import print_error
from robots.robot import Robot

@dataclass
class RobotFloor(Robot):
    """This is the ground robot

    this is a robot that can move on a linear rail attached to the ﬂoor. This
    robot can only pick up parts from bin1 and bin2 . This robot cannot pick up trays
    from tables

    Args:
        Robot (): Base Class for all the robots

    Returns:
        RobotFloor(): creates an instance of RobotFloor
    """
    # pylint: disable=useless-super-delegation

    _bins_supported = (1, 2)

    def __init__(self) -> None:
        """call the base constructor for the Robot()
        """
        super().__init__()

    @classmethod
    def is_this_bin_supported(cls, bin_id):
        """checks what bin it can take parts from

        Args:
            bin_id (int): id of the bin

        Returns:
            bool: returns True if the robot can reach to the bin
        """
        return bin_id in RobotFloor._bins_supported

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
                