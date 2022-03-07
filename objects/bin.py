"""File for the Bin class
"""
#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from typing import Any
from typing import List
from dataclasses import dataclass
from misc.utility import print_error

@dataclass
class Bin:
    """Bin class which contains the parts

    Returns:
        Bin(): returns a bin object
    """
    # pylint: disable=invalid-name

    id: int
    parts: List[Any]
    type: str = None

    def __init__(self, bin_id) -> None:
        self.id = bin_id
        self.parts = []

    def get_part(self):
        """Removes the part from the bin, and give it to the robot

        Returns:
            Part(): Returna a part object contained in the bin
        """
        part = None
        if self.parts:
            part = self.parts.pop()

            # if list empty we change the bin type to None
            # now, it can store any part type
            if not self.parts:
                self.type = None

        return part

    def store_parts(self, parts):
        """store parts inside the bin

        • A bin can be empty, can have 4 parts to 9 parts
        • A bin can have only parts of the same color. For instance, you cannot have red_-
        part s and green_part s in the same bin.

        Args:
            parts (list): parts containing a list of part objects to be stored inside the bin

        Returns:
            bool: returns true, if it was able to store the parts
        """
        success = False
        if not self.parts and parts:
            self.type = parts[0].type

        if self.type == parts[0].type:
            if (len(self.parts) + len(parts) > 3 and
                len(self.parts) + len(parts) < 10):
                self.parts.extend(parts)
                success = True
            else:
                print_error("Alteast 4 parts are stored, but not more than 9")
        else:
            print_error("This part type can't be stored with parts of other type in the same bin.")

        return success

    def __str__(self) -> str:
        return f"Bin(id={str(self.id)}, part_type={self.type})"
    