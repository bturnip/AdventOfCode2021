""" Advent Of Code 2021 Day 3 driver """
import sys
import os.path
sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/advent_tools')
from advent_tools import *
from day3 import *
import numpy as np


# choose file ----------------------------------------------------------
# uncomment one of these lines to choose the file needed
# 1: true, full size data from AdventOfCode
# 2: top 10 lines from #1
# 3: ints 1-5 in 5x5 array
# 4: top 4 lines from #1

# --> #1: full file
this_file = get_input_file_name(day=3)
#this_file = '/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day3/sample.txt'
#this_file = '/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day3/sample2.txt'
#this_file = '/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day3/sample3.txt'


# load data ------------------------------------------------------------
this_data = load_input_file_into_list(this_file, strip_newline = True)
this_arr = create_2D_numpy_array(this_data)

# run calculations -----------------------------------------------------
results = calculate_aoc_day3(this_arr)
results = calculate_aoc_day3_pt2(this_arr,results)

# print results
print(f"+++ RESULTS:")
for k in results:
    print(f"{k}:{results[k]}")



