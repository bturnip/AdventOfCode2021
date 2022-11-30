""" Advent Of Code 2021 Day day7 driver """
from day7 import *
from config_day7 import *

# file chooser -----------------------------------

# -- uncomment one of these file choices below
this_file = FULL_FILE
#this_file = SAMPLE_FILE
this_file = TINY_SAMPLE
print(f"+++INFO: using {this_file}...")

# puzzle runner ----------------------------------
print("+++INFO: starting puzzle...")
puzzle = Day7(this_file)

#print(f'+++DEBUG: starting_crabs: {puzzle.starting_crabs}')
#print(f'+++DEBUG: crab positions: {puzzle.crab_horiz_pos}')

print("+++INFO: solving part 1:")
puzzle.solve_part1()

print("+++INFO: solving part 2:")
puzzle.solve_part2()


#print(puzzle.get_answer_key())










