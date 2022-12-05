""" Advent Of Code 2021 Day 9 driver """
from day9 import *
from config_day9 import *

# file chooser -----------------------------------

# -- uncomment one of these file choices below
this_file = FULL_FILE
this_file = SAMPLE_FILE
print(f"+++INFO: using {this_file}...")

# puzzle runner ----------------------------------
print("+++INFO: starting puzzle...")
puzzle = Day9(this_file)

print(f'+++DEBUG: puzzle.heightmap:\n {puzzle.heightmap}')
puzzle.set_low_point_coords()

print(f'+++DEBUG: : {puzzle.low_point_coords}')





'''
print("\tsolving part 1:")
puzzle.solve_part1()
print(puzzle.get_answer_key())
'''










