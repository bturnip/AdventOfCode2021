""" 2021 Advent of Code: Day 4"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=C0104, C0123, C0413, E0602, W0511
import sys
import random
sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/advent_tools')
from advent_tools import *



class Day4(object):
    """ Object that contains the methods to compute/store
        the 2021 Advent Of Code puzzle for Day 4"""

    def __init__(self, input_file=None):
        self.bingo_draws = []
        self.valid_bingo_draw_keywords = ["random","input_file"]
        self.input_file = input_file
        self.bingo_cards = np.array([[[]]])
        self.best_card = 0

    def set_bingo_draws(self,input_draws):
        """ set bingo_draws from list, single value integer, or keyword"""
        if type(input_draws) == list:
            self.bingo_draws = input_draws

        elif type(input_draws) == int:
            self.bingo_draws = [input_draws]

        elif type(input_draws) == str:
            if input_draws.lower() not in self.valid_bingo_draw_keywords:
                err = f"+++ERROR: \"{input_draws}\" not a valid keyword, " \
                      f"valid key words are {self.valid_bingo_draw_keywords}"
                raise TypeError(err)
            if input_draws.lower() == "random":
                self.bingo_draws = list(range(100))
                random.shuffle(self.bingo_draws)
            elif input_draws.lower() == "input_file":
                #TODO: implement the file extract
                self.bingo_draws = [1,2,3,25,35,99]
                # call a function:
                #  - confirm we have a file that can be opened
                #  - open a file
                #  - read one line
                #  - close the file
                #  - strip the newline
                #  - load read line into list
                #  - set self.bingo_draws to list
                #  - extend this to the init:
                #    - if the file is not null
                #    - if the file is valid
                #    - do the function steps listed here
        else:
            err = f"+++ERROR: valid inputs are a list of ints, a single "\
                  f"int value or a keyword in {self.valid_bingo_draw_keywords}"
            raise TypeError(err)
