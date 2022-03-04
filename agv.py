#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from constants import Const

class AGV:
    id : int
    
    def __init__(self, id) -> None:
        self.id = id
    
    def is_assembly_supported(station):
        if id == 1 or id == 2:
            return station == Const.AS1 or station == Const.AS2
        elif id == 3 or id == 4:
            return station == Const.AS3 or station == Const.AS4
    
    def ship(the_tray, to_the_station):
        print(f"agv{str(id)}, {the_tray.type}, {to_the_station}")
        print(f"{the_tray.type} contains following items: {the_tray.parts}")
            