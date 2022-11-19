""" Advent Of Code 2021 Day 3 driver """
import sys
import os.path
sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/advent_tools')
from advent_tools import *
from day3 import *
import numpy as np

# load file -----------------------------------------------------------
this_file = get_input_file_name(day=3)
this_data = load_input_file_into_list(this_file, strip_newline = True)


# load data into numpy -------------------------------------------------
this_arr = create_2D_numpy_array(this_data)

# run calculations -----------------------------------------------------
results = calculate_gamma_and_espilon_rate(this_arr)


gamma = results['gamma']
epsilon = results['epsilon']
power_consumption = results['power_consumption']

# print results --------------------------------------------------------
print(f"+++ RESULTS:")
for k in results:
    print(f"{k}:{results[k]}")
