""" Advent Of Code 2021 Day1 driver """
import sys
sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/advent_tools')
from advent_tools import *
from day1 import *

# load file
d1_data = load_input_file_into_list(get_input_file_name(day=1))

# part 1: count the number of times a depth measurement increases
print(f"Day 1, Part1: number of depth increases:"\
      f" {count_depth_increases(d1_data)}")

# part 2: count number of times sliding window sums increase
d1_part2 = create_windowed_list(d1_data,3)
print(f"Day 1, Part2: number of windowed depth increases:"\
      f" {count_depth_increases(d1_part2)}")
