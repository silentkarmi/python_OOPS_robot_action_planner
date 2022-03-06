"""Base class of the RobotCeiling and RobotFloor described here
"""

#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass
from typing import Any

@dataclass
class Robot:
    """Robot class

    Returns:
        Robot(): returns a robot object
    """
    gripper_object : Any

    def __init__(self) -> None:
        self.gripper_object = None

    def is_gripper_empty(self):
        """ Returns, if the gripper holding the object is empty or full

        Returns:
            bool: false = gripper is empty
        """
        return self.gripper_object is None
    