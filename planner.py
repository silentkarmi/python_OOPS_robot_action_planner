#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass
from typing import Any
from agv import AGV
from bin import Bin
from constants import Const
from robot_ceiling import RobotCeiling
from robot_floor import RobotFloor

from table import Table
from tray import Tray

@dataclass
class Planner:
    
    table_yellow: Any
    table_gray: Any
    robot_gantry : Any
    robot_ground : Any
    bins: list()
    agvs: list()
    
    def __init__(self) -> None:
        self.robot_gantry = RobotCeiling()
        self.robot_ground = RobotFloor()
        
        self.table_yellow = Table(Tray(Const.TRAY_YELLOW))
        self.table_gray = Table(Tray(Const.TRAY_GRAY))
        
        self.agvs = []
        self.bins = []
        for i in range(1, 5):
            self.agvs.append(AGV(i))
            self.bins.append(Bin(i))
    
    def generate_plan(self):
        print("Generating Plan")