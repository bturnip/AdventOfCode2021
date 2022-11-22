""" 2021 Advent of Code: Day 4"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=C0104, C0123, C0413, E0602, W0511
import sys
import random

from os.path import exists as file_exists # one liner to check file

sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/advent_tools')
from advent_tools import *



class Day4(object):
    """ Object that contains the methods to compute/store
        the 2021 Advent Of Code puzzle for Day 4"""

    def __init__(self, input_file=None):
        self.bingo_draws = []
        self.valid_bingo_draw_keywords = ["random"]
        self.input_file = input_file
        self.bingo_cards = np.array([[[]]])
        self.best_card = 0

    def set_bingo_draws(self,input_draws):
        """ set bingo_draws from list, single value integer, or keyword"""
        if type(input_draws) == list:
            self.bingo_draws = input_draws

        elif type(input_draws) == int:
            self.bingo_draws = [input_draws]

        elif file_exists(input_draws):
            self.load_bingo_draws_from_file(input_draws)

        elif type(input_draws) == str:
            if input_draws.lower() not in self.valid_bingo_draw_keywords:
                err = f"+++ERROR: \"{input_draws}\" not a valid keyword, " \
                      f"valid key words are {self.valid_bingo_draw_keywords}"
                raise TypeError(err)
            if input_draws.lower() == "random":
                self.bingo_draws = list(range(100))
                random.shuffle(self.bingo_draws)

        else:
            err = "+++ERROR: valid inputs are a valid file path, a " \
                  "list of ints, a single int value or a keyword in " \
                  f"{self.valid_bingo_draw_keywords}"
            raise TypeError(err)

    def load_bingo_draws_from_file(self,input_draws):
        """ loads first line from input_draws file to bingo_draws """
        if not file_exists(input_draws):
            err_mssg = f"+++ERROR: input file [{input_draws}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # load Bingo Draw data into list
        # note that we only read one line
        with open(input_draws,'r') as file_stream:
            draw_data = file_stream.readline()
            file_stream.close()
            
        self.bingo_draws = list(map(int,draw_data.rstrip().split(',')))


        #  - extend this to the init:
        #    - if the file is not null
        #    - if the file is valid
        #    - do the function steps listed here
