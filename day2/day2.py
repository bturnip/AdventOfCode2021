"""
2021 Advent of Code: Day 2
"""
import sys
sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/advent_tools')
from advent_tools import *

DUMMY_LIST = []
def calculate_position(input_list = DUMMY_LIST):
    """ Calculate the horizontal and depth readings """
    # initialize counters
    horiz = 0
    depth = 0
    result_dict = {"horiz":horiz,"depth":depth}

    if len(input_list) == 0:
        return result_dict

    # Calculate the forward (horizontal) position
    # -----------------------------------------------------
    # entries look like "forward 5\n", "up 2\n", "down 3\n"
    # make a list comprehension that filters for "forward""

    forward_values = [x.rstrip().split()[1] for x in input_list \
                      if x.rstrip().split()[0]=="forward"]

    result_dict["horiz"] = sum(intify_list(forward_values))

    # Calculate the depth position
    # -----------------------------------------------------
    # entries look like "forward 5\n", "up 2\n", "down 3\n"
    # make a list comprehension that filters for "up" or "down"
    # up entries are negative, down entries "add" to the depth
    down_values = [x.rstrip().split()[1] for x in input_list \
                   if x.rstrip().split()[0]=="down"]
    up_values = [x.rstrip().split()[1] for x in input_list \
                 if x.rstrip().split()[0]=="up"]

    result_dict["depth"] = (sum(intify_list(down_values))
                            - sum(intify_list(up_values)))
    return result_dict

def calc_postion_with_aim(input_list = DUMMY_LIST):
    """ Calculate positions accounting for aim """
    # initialize counters
    horiz = 0
    depth = 0
    aim = 0
    result_dict = {"horiz":horiz,"depth":depth}

    if len(input_list) == 0:
        return result_dict
    
    for x in input_list:
        this_entry = x.rstrip().split()
        if this_entry[0] == "forward":
            horiz += int(this_entry[1])
            depth += int(this_entry[1]) * aim
        elif this_entry[0] == "down":
            aim += int(this_entry[1])
        elif this_entry[0] == "up":
            aim -= int(this_entry[1])
        #print(f"---> hda:{horiz}|{depth}|{aim}, entry was {this_entry}")
    
    result_dict["horiz"]= horiz
    result_dict["depth"]= depth
    
    return result_dict
        
        
    
    


    
