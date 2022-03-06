#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from constants import Const
from typing import Any

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
    
    def ship(self, to_the_station):
        print(f"agv{str(id)}, {self.tray.type}, {to_the_station}")
        print(f"{self.tray.type} contains following items: {self.tray.parts}")
            