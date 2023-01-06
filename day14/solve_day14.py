""" Advent Of Code 2021 Day 14 driver """
import argparse
from day14 import *
from config_day14 import *
import time

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
puzzle = Day14(this_file)

'''
print("+++INFO: solving part 1:")
timer_start = time.perf_counter()
pt1= puzzle.solve_part1()
timer_stop = time.perf_counter()
print(f'+++INFO: pt1: {pt1}')
'''

foo = Day14(this_file)
foo.process_polymer_chunks(num_cycles=10, chunk_size=4)
print(f'+++DEBUG: final poly len: {len(foo.polymer)}')

'''
print("+++INFO: solving part 2:")
puzzle2 = Day14(this_file)
timer_start = time.perf_counter()
pt2= puzzle2.solve_part2()
timer_stop = time.perf_counter()
print(f'+++INFO: pt2: {pt2}')
print(f'+++INFO: seconds elapsed: {timer_stop - timer_start:0.4f}')
#'''


print(f"+++INFO: full answer key:\n{puzzle.get_answer_key()}")
