from colorama import Fore
from constants import Const

from part import Part

def print_error(text):
    print(Fore.RED, text)
    
def print_normal(text):
    print(Fore.WHITE, text)
    
def print_partition():
    print_normal("="*75)

def create_parts(num_of_parts, part_type):
    parts = []
    for i in range(num_of_parts):
        parts.append(Part(part_type))
    
    return parts

def ask_part(part_type, obj_planner):
    total_parts = 0
    
    while True:
        print_normal("How many " + part_type + "s in the workcell [0, 4 - 9]?")
        total_parts = 5
                
        if total_parts == 0 or (total_parts > 3 and total_parts < 10):
            if total_parts != 0:
                parts = create_parts(total_parts, part_type)
                
                success = False
                lst_empty_bin_ids = obj_planner.which_bins_are_empty()
                while not success:
                    print_normal("In which bin are these " + part_type + "s located " + ids_to_string(lst_empty_bin_ids) + "?")
                    bin_id = 1
                    if bin_id in lst_empty_bin_ids:
                        success = obj_planner.bins[bin_id - 1].store_parts(parts)
                        return len(parts)
                    else:
                        print_error("Invalid Bin Id")
                
            break
        else:
            print_error("Alteast 4 parts are stored, but not more than 9")
            
def ask_order_tray():
    while True:
        print_normal("Which tray to use? [(y)ellow, (g)ray]?")
        tray_type = 'g'
        if tray_type == 'y':
            return Const.TRAY_YELLOW
        elif tray_type == 'g':
            return Const.TRAY_GRAY
        else:
            print_error("Invalid Tray Type")
            
def ask_which_agv_and_station():
    while True:
        print_normal("Which tray to use? [(y)ellow, (g)ray]?")
        tray_type = 'g'
        if tray_type == 'y':
            return Const.TRAY_YELLOW
        elif tray_type == 'g':
            return Const.TRAY_GRAY
        else:
            print_error("Invalid Tray Type")
            
def ask_which_agv_for_order():
    lst_agv_ids = [1, 2, 3, 4]
    
    while True:
        print_normal("Which AGV to use " + ids_to_string(lst_agv_ids) +" ?")
        agv_id = 3
        if agv_id in lst_agv_ids:
            while True:
                lst_as_stations = []
                if agv_id == 1 or agv_id == 2:
                    lst_as_stations = [1, 2]
                elif agv_id == 3 or agv_id == 4:
                    lst_as_stations = [3,4]
                    
                print_normal("Which assembly station to ship agv" + str(agv_id)
                             + " " + ids_to_string(lst_as_stations) + "?")
                
                as_id = 3
                
                if as_id in lst_as_stations:
                    return agv_id, as_id
                else:
                    print_error("Invalid Assembly Station")
        else:
            print_error("Invalid AGV Id")

def ask_how_many_parts_in_tray(part_type):
    parts_total = [0, 1, 2]
    
    while True:
        print_normal("How many " + part_type + "s in tray " + ids_to_string(parts_total) + "?")
        parts_in_kit = 2
        if parts_in_kit in parts_total:
            return parts_in_kit
        else:
            print_error("Invalid Number of Parts in Kit")

def ids_to_string(list):
    string_ids = ""
    for id in list:
        string_ids = string_ids + str(id) + ", "
            
    string_ids = "[" + string_ids[0:-2:1] + "]"
    
    return string_ids
        