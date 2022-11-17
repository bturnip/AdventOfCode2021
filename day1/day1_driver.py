""" Advent Of Code 2021 Day1 driver """
from day1 import *

# load file
d1_data = load_input_file_into_list(INPUT_FILE)

# part 1: count the number of times a depth measurement increases
print(f"Day 1, Part1: number of depth increases:"\
      f" {count_depth_increases(d1_data)}")

# part 2: count number of times sliding window sums increase
d1_part2 = create_windowed_list(d1_data,3)
print(f"Day 1, Part2: number of windowed depth increases:"\
      f" {count_depth_increases(d1_part2)}")
