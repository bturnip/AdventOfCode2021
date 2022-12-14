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
print(f'+++DEBUG: pt1: {pt1}') 
print(f"+++INFO: full answer key:\n{puzzle.get_answer_key()}") 

print("+++INFO: solving part 2:")
puzzle2=Day11(this_file)
pt2= puzzle2.solve_part2()
print(f'+++DEBUG: pt2: {pt2}') 

print(f"+++INFO: full answer key:\n{puzzle2.get_answer_key()}")

print("#=============================================================")




