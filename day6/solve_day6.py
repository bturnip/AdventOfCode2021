""" Advent Of Code 2021 Day 6 driver """
from day6 import *
from config_day6 import *

# file chooser -----------------------------------

# -- uncomment one of these file choices below
this_file = FULL_FILE
#this_file = SAMPLE_FILE
print(f"+++INFO: using {this_file}...")

# puzzle runner ----------------------------------
print("+++INFO: starting puzzle...")
puzzle = Day6(this_file)

print("\tsolving part 1:")
puzzle.solve_part1()
print(puzzle.get_answer_key())

# need to create a new object so that the status is 
# original input
print("\tsolving part 2:")
puzzle2=Day6(this_file)
puzzle2.solve_part2()
print(puzzle2.get_answer_key())









