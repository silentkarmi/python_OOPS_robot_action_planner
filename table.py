"""Table class file
"""
#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from typing import Any
from dataclasses import dataclass

@dataclass
class Table:
    """Table Class which contains the tray

    Returns:
        Table(tray): Returns a Table object containing that specific tray
    """
    tray: Any

    def get_tray(self):
        """It get's the tray from the Table.

        Note that, after the tray is given away, to the AGV
        The table will contain no tray

        Returns:
            Tray(): returns the tray object stored in the table
        """
        obj_tray = self.tray
        self.tray = None
        return obj_tray

    def __str__(self) -> str:
        return "Table(" + self.tray.type + ")"
    