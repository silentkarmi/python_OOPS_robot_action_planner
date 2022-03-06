#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from constants import Const
from typing import Any
from utility import print_success

class AGV:
    id : int
    tray : Any
    
    def __init__(self, id) -> None:
        self.id = id
        self.tray = None
    
    def is_assembly_supported(self, station):
        if id == 1 or id == 2:
            return station == Const.AS1 or station == Const.AS2
        elif id == 3 or id == 4:
            return station == Const.AS3 or station == Const.AS4
    
    def ship(self, station):
        print_success(f"AGV={self.id} contains {self.tray}")
        print_success(f"{self.tray.type} contains following items: {self.tray.parts}")
        print_success(f"Shipped to Assembly Station: {station.id}")
        
    def __str__(self) -> str:
        return f"AGV(id={str(self.id)})"
            