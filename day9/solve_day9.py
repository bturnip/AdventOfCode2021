""" Advent Of Code 2021 Day 9 driver """
from day9 import *
from config_day9 import *

# file chooser -----------------------------------

# -- uncomment one of these file choices below
this_file = FULL_FILE
#this_file = SAMPLE_FILE
print(f"+++INFO: using {this_file}...")

# puzzle runner ----------------------------------
print("+++INFO: starting puzzle...")
puzzle = Day9(this_file)

puzzle.set_low_point_coords()

print("+++INFO: solving part 1:")
puzzle.solve_part1()
print(puzzle.get_answer_key())

    
print("+++INFO: solving part 2:")
puzzle.solve_part2()











