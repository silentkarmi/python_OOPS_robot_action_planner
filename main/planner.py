"""This file has the Planner Class

Important Function calls to consider:

generate_plan : The algorithm is written in planner.py which in turn calls:
    >> find_plan (finds a solution, if its there) and then,
    >> execute_plan (it calls all the callbacks, if there is a plan)
"""

#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass
from typing import Any
from typing import List
from agvs.agv import AGV
from location.assembly_station import AssemblyStation
from objects.bin import Bin
from objects.table import Table
from objects.tray import Tray
from robot.gantry_robot import GantryRobot
from robot.linear_robot import LinearRobot
from utils.constants import Const
from utils.utility import print_normal, print_partition
from utils.utility import print_success
from utils.utility import print_error

@dataclass
class Planner:
    """This is the Planner class. It deals with the algorithm to shit the kit via AGV
    """
    # pylint: disable=too-many-instance-attributes
    table_yellow: Any
    table_gray: Any
    robot_gantry : Any
    robot_ground : Any
    bins: List[Any]
    agvs: List[Any]
    as_stations : List[Any]
    callbacks: List[Any]
    args_callbacks: List[Any]

    def __init__(self) -> None:
        self.robot_gantry = GantryRobot("Gantry", 200, 50)
        self.robot_ground = LinearRobot("UR10", 150, 50)
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
        """This stores the callbacks.

        These callbacks are synonymous with the actions robots have to take,
        if the solution is found.

        Args:
            callback (function): This is the function call.
            arg (Any): These are the argument objects required by the callbacks
        """
        self.callbacks.append(callback)
        self.args_callbacks.append(arg)

    def execute_plan(self):
        """This executes the plan of actions.

        This list of actions were created when find_plan was called.
        """
        for (callback, arg) in zip(self.callbacks, self.args_callbacks):
            # print_normal(f"{callback.__qualname__}({arg})\n")
            if arg == "":
                callback()
            else:
                callback(arg)

    def select_robot(self, bin_id):
        """This selects the desired robot in accordance with bin_id

        • bin1 and bin2 can only be reached by robot_floor
        • bin3 and bin4 can only be reached by robot_ceiling

        Args:
            bin_id (int): id of the bin

        Returns:
            Robot(): Return the right robot which can be robot_ground or robot_gantry
        """
        robot = None
        if bin_id in (1, 2):
            robot = self.robot_ground
        elif bin_id in (3, 4):
            robot = self.robot_gantry

        return robot

    def find_plan(self, order):
        """This finds the plan for this particular order

        Args:
            order (Order): _description_

        Returns:
            bool : For a particular order, a solution is found or not
        """

        # pylint: disable=too-many-branches
        # store_callback is called repeatedly to store the callbacks
        
        # pylint: disable=no-else-return
        # necessary to stop formulation plan and return to improve execution of the code

        index = lambda id : id - 1
        self.callbacks = []
        self.args_callbacks = []

        solution_found = True

        self.store_callback(self.robot_gantry.gripper.activate_gripper, "")
        if order.tray_type == Const.TRAY_GRAY:
            self.store_callback(self.robot_gantry.pickup_tray, self.table_gray)
        elif order.tray_type == Const.TRAY_YELLOW:
            self.store_callback(self.robot_gantry.pickup_tray, self.table_yellow)

        agv_order = self.agvs[index(order.agv_id)]
        self.store_callback(self.robot_gantry.gripper.deactivate_gripper, "")
        self.store_callback(self.robot_gantry.place_tray, agv_order)
        
        def plan_for_part(local_bin):
            obj_robot = self.select_robot(local_bin.id)
            self.store_callback(obj_robot.gripper.activate_gripper, "")
            self.store_callback(obj_robot.pickup_part, local_bin)
            self.store_callback(obj_robot.gripper.deactivate_gripper, "")
            self.store_callback(obj_robot.place_part, agv_order)

        while order.red_parts:
            if order.red_parts != 0:
                obj_bin = self.search_bins_for(Const.PART_RED)

                if obj_bin is None:
                    solution_found = False
                    return solution_found
                else:
                    plan_for_part(obj_bin)
                    order.red_parts -= 1

        while order.green_parts:
            if order.green_parts != 0:
                obj_bin = self.search_bins_for(Const.PART_GREEN)

                if obj_bin is None:
                    solution_found = False
                    return solution_found
                else:
                    plan_for_part(obj_bin)
                    order.green_parts -= 1

        while order.blue_parts:
            if order.blue_parts != 0:
                obj_bin = self.search_bins_for(Const.PART_BLUE)

                if obj_bin is None:
                    solution_found = False
                    return solution_found
                else:
                    plan_for_part(obj_bin)
                    order.blue_parts -= 1

        self.store_callback(agv_order.ship, self.as_stations[order.as_id - 1])

        return solution_found
    
    def generate_plan(self, order):
        """Generates the plan, if plan is found then executes as well.

        Args:
            order (Order): Receives the order, for which the plan needs to be formulated
        """
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
        """This searches in all bins to find the necessary part

        Args:
            part_type (str): This is the part type for which the bins would be searched

        Returns:
            Bin(): Returns the bin object where the part is located
        """
        for obj_bin in self.bins:
            if obj_bin.type == part_type:
                return obj_bin
    
    def which_bins_are_empty(self):
        """This searches for bins which are empty

        Returns:
            list: It returns a list of bins which are empty.
        """
        bins_availabe = []
        for obj_bin in self.bins:
            if not obj_bin.parts:
                bins_availabe.append(obj_bin.id)
        
        return bins_availabe
        