"""contains the LinearRobot class
"""
#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass
from utils.utility import print_error
from robot.base_robot import BaseRobot
from gripper.gripper import Gripper

@dataclass
class LinearRobot(BaseRobot):
    """This is the ground robot

    this is a robot that can move on a linear rail attached to the ﬂoor. This
    robot can only pick up parts from bin1 and bin2 . This robot cannot pick up trays
    from tables

    Args:
        Robot (): Base Class for all the robots

    Returns:
        LinearRobot(): creates an instance of LinearRobot
    """
    # pylint: disable=useless-super-delegation
    # pylint: disable=dangerous-default-value

    def __init__(self, name, payload, weight, bins = [1, 2], category="industrial") -> None:
        """call the base constructor for the Robot()
        """
        gripper = Gripper(name + "_gripper")
        super().__init__(name, payload, weight, gripper, bins, category="industrial")
        
        self._linear_rail_length = 10
        
    def __str__(self):
        return self._name