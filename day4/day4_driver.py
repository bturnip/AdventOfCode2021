""" Advent Of Code 2021 Day 4 driver """
import sys
import os.path
sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/advent_tools')
from advent_tools import *
from day4 import *
import numpy as np


# load data ------------------------------------------------------------
# Input file 1st line is a list of bingo numbers to call out
input_file = get_input_file_name(4)
input_file = input_file.replace("_input","_raw_input")
#print(f"+++INFO: input_file: {os.path.basename(input_file)}")

# load Bingo Draw data into list 
with open(input_file,'r') as file_stream:
    draw_data = file_stream.readline()
file_stream.close()

bingo_draws = draw_data.rstrip().split(',')


puzzle = Day4(input_file)

#print(f"puzzle.input_file:{puzzle.input_file}")
print(f"puzzle.bingo_draws:{puzzle.bingo_draws}")



puzzle.set_bingo_draws("random")
print(f"bingo_draws:{puzzle.bingo_draws}")

puzzle.set_bingo_draws(29)

