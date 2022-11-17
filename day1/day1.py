"""
2021 Advent of Code: Day 1
"""
import sys
sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/')
from advent_tools import *

def create_windowed_list(input_list,chunk_size):
    """
    returns an output list by creating each list element
    as the sum of the chunk_size windows of the input list
    """
    # sanity checks
    if (len(input_list) <= 0 or len(input_list) < chunk_size):
        err_mssg = (f"length of input list({len(input_list)}) "\
                   f"cannot be zero or less than "\
                   f"chunk_size ({chunk_size})")

        raise ValueError(err_mssg)

    # start building windowed sums
    i = 0
    last_index = chunk_size
    max_index = len(input_list)
    int_list = list(map(int,input_list))
    output_list = []

    while last_index <= max_index:
        output_list.append( sum(int_list[i:last_index]) )
        #print(f'i:{i},last_index:{last_index}, elements: {input_list[i:last_index]}')
        i+=1
        last_index +=1

    return output_list

def count_depth_increases(input_list):
    """
    takes a list and counts the number of increases from one measurement
    to the next.
    """
    i = 1
    increase_count = 0

    while i < len(input_list):
        prev = int(input_list[i-1])
        curr = int(input_list[i])
        #print(f'prev: {prev}\tcurr:{curr}')
        if prev < curr:
            increase_count += 1
        i += 1

    return increase_count
