""" Advent Of Code 2021 Day day8 driver """
from day8 import *
from config_day8 import *

# file chooser -----------------------------------

# -- uncomment one of these file choices below
this_file = FULL_FILE
#this_file = SAMPLE_FILE
print(f"+++INFO: using {this_file}...")

# puzzle runner ----------------------------------
print("+++INFO: starting puzzle...")
puzzle = Day8(this_file)

print("\tsolving part 1:")
puzzle.solve_part1()
#print(puzzle.get_answer_key())










