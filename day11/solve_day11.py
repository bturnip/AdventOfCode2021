""" Advent Of Code 2021 Day 11 driver """
from day11 import *
from config_day11 import *

# file chooser -----------------------------------

# -- uncomment one of these file choices below
this_file = FULL_FILE
this_file = SAMPLE_FILE
print(f"+++INFO: using {this_file}...")

# puzzle runner ----------------------------------
print("+++INFO: starting puzzle...")
puzzle = Day11(this_file)

print("+++INFO: solving part 1:")
pt1= puzzle.solve_part1()


print("+++INFO: solving part 2:")
pt2= puzzle.solve_part2()

print(f"+++INFO: full answer key:\n{puzzle.get_answer_key()}")

#======================================================================
test01=Day11(this_file)
print(f'+++DEBUG: test01.orig_input:\n{test01.orig_input}')
print(f'+++DEBUG: should be 1: {test01.orig_input[0][9]}')
