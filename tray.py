#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass

@dataclass
class Tray:
    parts : list()
    type : str = ""
    
    def __init__(self, type) -> None:
        self.type = type