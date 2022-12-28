""" Advent Of Code 2021 Day 13 driver """
import argparse
from day13 import *
from config_day13 import *
import random

#-- parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--samplefile"\
                    ,help = "run the solver script with the SAMPLE_FILE"\
                    , action = "store_true")
parser.add_argument("-f", "--fullfile"
                    ,help = "run the solver script with the FULL_FILE"\
                    ,action="store_true")

args = parser.parse_args()

# file chooser -----------------------------------
if args.samplefile:
    this_file = SAMPLE_FILE
elif args.fullfile:
    this_file = FULL_FILE
else:
    print("+++INFO: No file option specified, default is SAMPLE_FILE")
    this_file = SAMPLE_FILE

print(f"+++INFO: using {this_file}...")


# puzzle runner ----------------------------------
print("+++INFO: starting puzzle...")
puzzle = Day13(this_file)

print("+++INFO: solving part 1:")
pt1= puzzle.solve_part1()
'''
print("+++INFO: solving part 2:")
pt2= puzzle.solve_part2()
'''
print(f"+++INFO: full answer key:\n{puzzle.get_answer_key()}")

