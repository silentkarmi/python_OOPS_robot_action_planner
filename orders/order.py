"""order file for the Order class
"""
#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass

@dataclass
class Order:
    """Order Class which contains details of the order needed to be shipped
    """
    agv_id : int
    as_id : int
    tray_type : str
    red_parts : int = 0
    green_parts : int = 0
    blue_parts : int = 0
    