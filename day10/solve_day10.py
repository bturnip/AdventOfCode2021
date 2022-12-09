""" Advent Of Code 2021 Day 10 driver """
from day10 import *
from config_day10 import *

# file chooser -----------------------------------

# -- uncomment one of these file choices below
this_file = FULL_FILE
#this_file = SAMPLE_FILE
print(f"+++INFO: using {this_file}...")

# puzzle runner ----------------------------------
print("+++INFO: starting puzzle...")
puzzle = Day10(this_file)

print("+++INFO: solving part 1:")
pt1= puzzle.solve_part1()

print("+++INFO: solving part 2:")
pt2= puzzle.solve_part2()

print(f"+++INFO: full answer key:\n{puzzle.get_answer_key()}")
