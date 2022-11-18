""" Advent Of Code 2021 Day 2 driver """
import sys
sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/advent_tools')
from advent_tools import *
from day2 import *

# load file
d2_data = load_input_file_into_list(get_input_file_name(day=2))
print(f"[Data Loaded]")

# part 1
position_results = calculate_position(d2_data)
print(f"[Position Calculated]:{position_results}")

pt1_answer = position_results["horiz"] * position_results["depth"]
print(f"[Day2, Part 1 answer]:{pt1_answer}")


# part 2
improved_position_results = calc_postion_with_aim(d2_data)
pt2_answer = improved_position_results["horiz"] * improved_position_results["depth"]
print(f"[Day2, Part 2 answer]:{pt2_answer}")


