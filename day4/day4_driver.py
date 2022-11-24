""" Advent Of Code 2021 Day 4 driver """
import sys
sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/advent_tools')
from day4 import *

day4_path = "/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day4"

sample_input_draws = [14,30,18,8,3,52]
sample_input_file = f"{day4_path}/day4_raw_sample.txt"
full_file= f"{day4_path}/day4_raw_input.txt"
sample_file_winner = f"{day4_path}/day4_raw_sample_winner.txt"


print("+++ DAY 4 DRIVER STARTING:")

puzzle=Day4(full_file)

puzzle.score_all_cards()
puzzle.get_part1_answer()
