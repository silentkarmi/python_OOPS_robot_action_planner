#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass
from gc import callbacks
from typing import Any, Dict
from agv import AGV
from assembly_station import AssemblyStation
from bin import Bin
from constants import Const
from robot_ceiling import RobotCeiling
from robot_floor import RobotFloor

from table import Table
from tray import Tray
from utility import print_partition
from utility import print_success
from utility import print_error

@dataclass
class Planner:
    
    table_yellow: Any
    table_gray: Any
    robot_gantry : Any
    robot_ground : Any
    bins: list()
    agvs: list()
    as_stations : list()
    callbacks: list()
    args_callbacks: list()
    
    def __init__(self) -> None:
        self.robot_gantry = RobotCeiling()
        self.robot_ground = RobotFloor()
        
        self.table_yellow = Table(Tray(Const.TRAY_YELLOW))
        self.table_gray = Table(Tray(Const.TRAY_GRAY))
        
        self.agvs = []
        self.bins = []
        self.as_stations = []
        for i in range(1, 5):
            self.agvs.append(AGV(i))
            self.bins.append(Bin(i))
            self.as_stations.append(AssemblyStation(i))
            
    def store_callback(self, callback, arg):
        self.callbacks.append(callback)
        self.args_callbacks.append(arg)
        
    def execute_plan(self):
        for (callback, arg) in zip(self.callbacks, self.args_callbacks):
            print(callback.__qualname__, arg)
            callback(arg)
            
    def select_robot(self, id):
        if id == 1 or id == 2:
            return self.robot_ground
        elif id == 3 or id == 4:
            return self.robot_gantry

    def find_plan(self, order):
        index = lambda id : id - 1
        self.callbacks = []
        self.args_callbacks = []
            
        solution_found = True
        
        if order.tray_type == Const.TRAY_GRAY:
            self.store_callback(self.robot_gantry.pickup_tray, self.table_gray)
        elif order.tray_type == Const.TRAY_YELLOW:
            self.store_callback(self.robot_gantry.pickup_tray, self.table_yellow)
            
        
        agv_order = self.agvs[index(order.agv_id)]
        self.store_callback(self.robot_gantry.place_tray, agv_order)
    
        while order.red_parts:
            if order.red_parts != 0:
                bin = self.search_bins_for(Const.PART_RED)
                
                if bin == None:
                    solution_found = False
                    return solution_found
                else:
                    robot = self.select_robot(bin.id)
                    self.store_callback(robot.pickup_part, bin)
                    self.store_callback(robot.place_part, agv_order)
                    order.red_parts -= 1
                    
        while order.green_parts:
            if order.green_parts != 0:
                bin = self.search_bins_for(Const.PART_GREEN)
                
                if bin == None:
                    solution_found = False
                    return solution_found
                else:
                    robot = self.select_robot(bin.id)
                    self.store_callback(robot.pickup_part, bin)
                    self.store_callback(robot.place_part, agv_order)
                    order.green_parts -= 1
                    
        while order.blue_parts:
            if order.blue_parts != 0:
                bin = self.search_bins_for(Const.PART_BLUE)
                
                if bin == None:
                    solution_found = False
                    return solution_found
                else:
                    robot = self.select_robot(bin.id)
                    self.store_callback(robot.pickup_part, bin)
                    self.store_callback(robot.place_part, agv_order)
                    order.blue_parts -= 1
                    
        self.store_callback(agv_order.ship, self.as_stations[order.as_id - 1])
                        
        return solution_found
    
    def generate_plan(self, order):
        print_partition()
        solution = self.find_plan(order)
        if solution:
            print_success("SOLUTION FOUND!")
            print_partition()
            self.execute_plan()            
        else:
            print_error("NO SOLUTION FOUND!")
            
        print_partition()
        
    def search_bins_for(self, part_type):
        for bin in self.bins:
            if bin.type == part_type:
                return bin   
    
    def which_bins_are_empty(self):
        bins_availabe = []
        for bin in self.bins:
            if not bin.parts:
                bins_availabe.append(bin.id)
        
        return bins_availabe
        