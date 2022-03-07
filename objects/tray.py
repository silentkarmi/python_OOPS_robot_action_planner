"""Tray file for the class
"""
#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass
from typing import Any
from typing import List

@dataclass
class Tray:
    """Tray Class

    Returns:
        Tray(type_tray): Returns the object of that type of tray
    """
    parts : List[Any]
    type : str = ""

    def __init__(self, type_tray) -> None:
        self.type = type_tray
        self.parts = []

    def __str__(self) -> str:
        return f"Tray(type = {self.type})"
    