""" Advent Of Code 2021 Day 6 driver """
from day6 import *
from config_day6 import *

# file chooser -----------------------------------

# -- uncomment one of these file choices below
this_file = FULL_FILE
this_file = SAMPLE_FILE
print(f"+++INFO: using {this_file}")


# puzzle runner ----------------------------------
puzzle = Day6(this_file)


x=puzzle.fish
print(x)
print(f"type(x):{type(x)}")
print(f"len(x):{len(x)}")


#puzzle = print(puzzle.get_answer_key())








