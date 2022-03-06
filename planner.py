#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass
from typing import Any
from agv import AGV
from bin import Bin
from constants import Const
from order import Order
from robot_ceiling import RobotCeiling
from robot_floor import RobotFloor

from table import Table
from tray import Tray

import inspect as i
import sys

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
    
    def generate_plan(self, order):
        print("Generating Plan")
        
        callbacks = {}
        if isinstance(order, Order):
            if order.tray_type == Const.TRAY_GRAY:
                callbacks.update({self.robot_gantry.pickup_tray :
                    self.table_gray})
                
                for key, value in callbacks.items():
                    function_source = (i.getsource(key)).split('\n')
                    function_defintion = function_source[0]
                    print(function_defintion, value)
                    key(value)
        # pick_tray_yellow
        # place_tray_yellow
        # search_part_in_bins
        # get part from the bin according to robot type
        # place part in agv
        # ship agv
        
        
    
    def which_bins_are_empty(self):
        bins_availabe = []
        for bin in self.bins:
            if not bin.parts:
                bins_availabe.append(bin.id)
        
        return bins_availabe
        