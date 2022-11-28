""" Advent Of Code 2021 Day 6 driver """
from day6 import *
from config_day6 import *

# file chooser -----------------------------------

# -- uncomment one of these file choices below
this_file = FULL_FILE
#this_file = SAMPLE_FILE
print(f"+++INFO: using {this_file}...")

# puzzle runner ----------------------------------
print(f"+++INFO: starting puzzle...")
puzzle = Day6(this_file)
puzzle.solve_part1()
print(puzzle.get_answer_key())






