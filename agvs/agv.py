""" AGV class
"""
#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from typing import Any
from utils.constants import Const
from utils.utility import print_partition, print_success

class AGV:
    """This class for Automated Guided Vehicles.

    Returns:
        AGV() : Returns an AGV instance when called AGV(agv_id = <int_value>)
    """
    agv_id : int
    tray : Any

    def __init__(self, agv_id) -> None:
        """initializer for AVG

        Args:
            agv_id (int): integer value to be provided
        """
        self.agv_id = agv_id
        self.tray = None

    def is_assembly_supported(self, station_id):
        """This tells us which AGV supports which Assembly station

        This is added for the sake completeness of the program. It's not used
        in the program because our user interface is robust enough to only give
        options which the agv supports

        Args:
            station_id (int): Takes assembly station id as integer

        Returns:
            Bool: Boolean true or false, if the station_id is supported or not
        """

        flag = False
        if self.agv_id in (1,2):
            flag = station_id in (Const.AS1, Const.AS2)
        elif self.agv_id in (3,4):
            flag = station_id in (Const.AS3, Const.AS4)

        return flag

    def ship(self, station):
        """Ships the tray contained in the AGV.

        The robot picks and place all the parts on the tray of AGV.
        And, when ship is called with the assembly station

        Args:
            station (int): It's the assembly station it will be shipped to
        """
        print_success("kit is complete\n")
        print_success(f"shipping agv{self.agv_id} to as{station.id}\n")
        print_partition()
        print_success(f"agv{self.agv_id} contains {self.tray}\n")
        if self.tray is not None:
            print_success(f"{self.tray.type} contains following items: {self.tray.parts}\n")

    def __str__(self) -> str:
        return f"AGV(id={str(self.agv_id)})"
            