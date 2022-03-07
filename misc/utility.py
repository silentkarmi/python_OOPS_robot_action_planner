""" This is a utility file containg functions to structure the code.

It contatins functions used to ask for order.
It also contains functions related to printing used throughout the code
"""

from colorama import Fore
from misc.constants import Const
from objects.part import Part
from order import Order

def print_error(text):
    """prints error

    Args:
        text (str): text error message
    """
    print(Fore.RED, text)

def print_success(text):
    """prints success messages

    Args:
        text (str): text message for the success
    """
    print(Fore.GREEN, text)

def print_normal(text):
    """normal prints

    Args:
        text (str): text message to be printed
    """
    print(Fore.WHITE, text, end="")

def print_partition():
    """To create the partition line
    """
    print(Fore.WHITE, "="*75)
    
def ask_for_order(planner):
    """This is the user interface which asks details about the orders

    Example of the UI:
    ===========================================================================
    How many red_parts in the workcell [0, 4 - 9]? 5
    In which bin are these red_parts located [1, 2, 3, 4]? 4
    How many green_parts in the workcell [0, 4 - 9]? 4
    In which bin are these green_parts located [1, 2, 3]? 3
    How many blue_parts in the workcell [0, 4 - 9]? 4
    In which bin are these blue_parts located [1, 2]? 2
    ===========================================================================
    Which tray to use? [(y)ellow, (g)ray]? y
    ===========================================================================
    Which AGV to use [1, 2, 3, 4] ? 2
    Which assembly station to ship agv2 [1, 2]? 1
    ===========================================================================
    How many red_parts in tray [0, 1, 2]? 2
    How many green_parts in tray [0, 1, 2]? 2
    How many blue_parts in tray [0, 1, 2]? 2
    ===========================================================================

    Args:
        planner (Planner()): The planner object

    Returns:
        Order(): returns an object containig the order which has all the necessary details
    """
    print_partition()
    red_parts_in_workcell = ask_part(Const.PART_RED, planner)
    green_parts_in_workcell = ask_part(Const.PART_GREEN, planner)
    blue_parts_in_workcell = ask_part(Const.PART_BLUE, planner)

    print_partition()
    tray_type = ask_order_tray()
    print_partition()
    agv_id, as_id = ask_which_agv_for_order()
    print_partition()
    red_parts_in_kit = 0
    green_parts_in_kit = 0
    blue_parts_in_kit = 0

    if red_parts_in_workcell:
        red_parts_in_kit = ask_how_many_parts_in_tray(Const.PART_RED)

    if green_parts_in_workcell:
        green_parts_in_kit = ask_how_many_parts_in_tray(Const.PART_GREEN)

    if blue_parts_in_workcell:
        blue_parts_in_kit = ask_how_many_parts_in_tray(Const.PART_BLUE)

    print_partition()

    order = Order(agv_id, as_id, tray_type, 
                  red_parts_in_kit, green_parts_in_kit, blue_parts_in_kit)

    return order

def create_parts(num_of_parts, part_type):
    """It creates the number of parts for a given type

    Args:
        num_of_parts (int): total parts to be created
        part_type (str): part type declared in constants.py

    Returns:
        list: list of parts of that type
    """
    # pylint: disable=unused-variable
    parts = []
    for i in range(num_of_parts):
        parts.append(Part(part_type))

    return parts

def ask_part(part_type, obj_planner):
    """Its asks for the number of part in the workcell and also the bin where they are located.

    Args:
        part_type (str): part type declared in constants.py
        obj_planner (Planner()): Planner Object

    Returns:
        int: number of parts created
    """
    # pylint: disable=no-else-break
    # pylint: disable=no-else-return
    # pylint: disable=chained-comparison

    total_parts = 0

    while True:
        print_normal("How many " + part_type + "s in the workcell [0, 4 - 9]? ")
        total_parts = int(input())

        if total_parts == 0 or (total_parts > 3 and total_parts < 10):
            if total_parts != 0:
                parts = create_parts(total_parts, part_type)

                success = False
                lst_empty_bin_ids = obj_planner.which_bins_are_empty()
                while not success:
                    print_normal("In which bin are these " +
                                 part_type + "s located " +
                                 ids_to_string(lst_empty_bin_ids) + "? ")
                    bin_id = int(input())
                    if bin_id in lst_empty_bin_ids:
                        success = obj_planner.bins[bin_id - 1].store_parts(parts)
                        return len(parts)
                    else:
                        print_error("Invalid Bin Id")
            break
        else:
            print_error("Alteast 4 parts are stored, but not more than 9")

def ask_order_tray():
    """Ask for the tray type for the order

    Returns:
        str: Tray type declared in constants.py
    """
    # pylint: disable=no-else-return
    while True:
        print_normal("Which tray to use? [(y)ellow, (g)ray]? ")
        tray_type = input()
        if tray_type == 'y':
            return Const.TRAY_YELLOW
        elif tray_type == 'g':
            return Const.TRAY_GRAY
        else:
            print_error("Invalid Tray Type")

def ask_which_agv_for_order():
    """asks for which agv to be used for the order

    With the agv id, it also asks for the assembly station id,
    to which the order would be shipped

    Returns:
        int: the agv id for the order
        int: the assembly station id for the order
    """
    # pylint: disable=no-else-return
    # pylint: disable=consider-using-in
    lst_agv_ids = [1, 2, 3, 4]

    while True:
        print_normal("Which AGV to use " + ids_to_string(lst_agv_ids) +" ? ")
        agv_id = int(input())
        if agv_id in lst_agv_ids:
            while True:
                lst_as_stations = []
                if agv_id == 1 or agv_id == 2:
                    lst_as_stations = [1, 2]
                elif agv_id == 3 or agv_id == 4:
                    lst_as_stations = [3,4]

                print_normal("Which assembly station to ship agv" + str(agv_id)
                             + " " + ids_to_string(lst_as_stations) + "? ")

                as_id = int(input())

                if as_id in lst_as_stations:
                    return agv_id, as_id
                else:
                    print_error("Invalid Assembly Station")
        else:
            print_error("Invalid AGV Id")

def ask_how_many_parts_in_tray(part_type):
    """it asks number of total parts for a particular part type

    It adheres to the rules:
    • The number of red_part to put in the tray: Maximum is 2.
    • The number of green_part to put in the tray: Maximum is 2.
    • The number of blue_part to put in the tray: Maximum is 2.

    Args:
        part_type (_type_): _description_

    Returns:
        _type_: _description_
    """
    # pylint: disable=no-else-return

    parts_total = [0, 1, 2]

    while True:
        print_normal("How many " + part_type + "s in tray " + ids_to_string(parts_total) + "? ")
        parts_in_kit = int(input())
        if parts_in_kit in parts_total:
            return parts_in_kit
        else:
            print_error("Invalid Number of Parts in Kit")

def ids_to_string(lst):
    """It takes integer list and converts into a printable string

    Args:
        lst (list): integer list

    Returns:
        str: printable string for the list of ids
    """
    string_ids = ""
    for id_int in lst:
        string_ids = string_ids + str(id_int) + ", "

    string_ids = "[" + string_ids[0:-2:1] + "]"

    return string_ids
