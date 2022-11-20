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

# --> #2: 10 line sample from full file
this_file = '/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day3/sample.txt'

# --> #3 ints 1-5 in 3x5 array
this_file = '/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day3/sample2.txt'

# --> #4 4 line sample from full file
this_file = '/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day3/sample3.txt'


# load data ------------------------------------------------------------
this_data = load_input_file_into_list(this_file, strip_newline = True)
this_arr = create_2D_numpy_array(this_data)

value_check_passes = check_np_array_values(this_arr,[0,1])

if value_check_passes is False:
    err_mssg = "+++ERROR: only values in [0,1] allowed in input array"
    raise ValueError(err_mssg)
else:
    print("+++INFO: check_np_array_values(this_arr,[0,1]) passed... ")


""" <DISABLE CODE>
# run calculations -----------------------------------------------------
results = calculate_aoc_day3(this_arr)

gamma = results['gamma']
epsilon = results['epsilon']
power_consumption = results['power_consumption']
exi
# print results --------------------------------------------------------
print(f"+++ RESULTS:")
for k in results:
    print(f"{k}:{results[k]}")
#<END DISABLE CODE>"""

# ----------------------------------------------------------------------

oxy_gen = this_arr.copy()
# get arr stats
num_cols = oxy_gen.shape[1]
print(f"this_arr:\n{oxy_gen}\n--->num_cols:{num_cols}")


for c in range(num_cols):    
    if len(oxy_gen) == 1:        
        oxy_value = list(oxy_gen[0].astype(int).astype(str))
        
        oxygen_generation = ''.join(oxy_value)
        print(f"+++RESULTS:final answer found in {c} bits: {oxygen_generation}")
        break
    
           
    test_col = oxy_gen[:,c]
    print(f"PASS #{c}--->{test_col}---------------------------")
    keep_bit = binary_frequency_select(test_col)
    
    print(f"keep_bit:{keep_bit}")
    # now remove the rows that don't match

    filter_arr = oxy_gen[:,c] == keep_bit
    oxy_gen=oxy_gen[filter_arr]
    
    print(f"filter_arr is now:{filter_arr}")
    print(f"oxy_gen is now:\n{oxy_gen}")

    

#<END DISABLE CODE>"""


