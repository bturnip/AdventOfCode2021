""" Advent Of Code 2021 Day {DAY_NUM} driver """
from {DAY_NUM} import *
from config_{DAY_NUM} import *

# file chooser -----------------------------------

# -- uncomment one of these file choices below
this_file = FULL_FILE
this_file = SAMPLE_FILE
print(f"+++INFO: using {this_file}...")

# puzzle runner ----------------------------------
print("+++INFO: starting puzzle...")
puzzle = Day{NUM}(this_file)

print("\tsolving part 1:")
puzzle.solve_part1()
print(puzzle.get_answer_key())










