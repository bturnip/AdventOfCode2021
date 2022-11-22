""" 2021 Advent of Code: Day 4"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=C0104, C0123, C0413, E0602, W0511
import sys
import random
from os.path import isfile

sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/advent_tools')
from advent_tools import *



class Day4(object):
    """ Object that contains the methods to compute/store
        the 2021 Advent Of Code puzzle for Day 4"""

    def __init__(self, input_file=None):
        self.input_file = input_file

        if input_file is not None and isfile(input_file):
            self.bingo_draws = self.load_bingo_draws_from_file(input_file)
        else:
            self.bingo_draws = []

        self.valid_bingo_draw_keywords = ["random"]

        self.bingo_cards = np.array([[[]]])
        self.best_card = 0

    def set_bingo_draws(self,input_draws):
        """ set bingo_draws from list, single value integer, or keyword"""

        if type(input_draws) == list:
            self.bingo_draws = intify_list(input_draws)

        elif type(input_draws) == int:
            self.bingo_draws = [input_draws]

        elif type(input_draws) == str and not isfile(input_draws):
            if input_draws.lower() not in self.valid_bingo_draw_keywords:
                err = f"+++ERROR: \"{input_draws}\" not a valid keyword, " \
                      f"valid key words are {self.valid_bingo_draw_keywords}"
                raise TypeError(err)
            if input_draws.lower() == "random":
                self.bingo_draws = list(range(100))
                random.shuffle(self.bingo_draws)

        elif type(input_draws) == str and isfile(input_draws):
            self.load_bingo_draws_from_file(input_draws)

        else:
            err_mssg = "+++ERROR: valid inputs are a valid file path, "\
                       "a list of ints, a single int value or a keyword "\
                       f"in {self.valid_bingo_draw_keywords}"
            raise TypeError(err_mssg)


    def load_bingo_draws_from_file(self,input_draws):
        """ loads first line from input_draws file to bingo_draws """
        if not isfile(input_draws):
            err_mssg = f"+++ERROR: input file [{input_draws}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # load Bingo Draw data into list
        # note that we only read one line
        with open(input_draws,'r') as file_stream:
            draw_data = file_stream.readline()
            file_stream.close()

        data = list(map(int,draw_data.rstrip().split(',')))
        self.bingo_draws = data
        return data

    def load_bingo_cards_from_file(self,input_cards):
        """ loads bingo cards from file"""
        if not isfile(input_cards):
            err_mssg = f"+++ERROR: input file [{input_cards}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        with open(input_cards) as file_stream:
            full_file = file_stream.readlines()
            file_stream.close()

        
        card_started = False
        card_dimension = 0
        for this_line in full_file:
            if (this_line.rstrip() =="" or this_line.find(',') > -1):
                #print(f"skipping line:{this_line.rstrip()}")
                pass
            else:
                # first card found
                card_started = True
                card_line = intify_list(this_line   \
                                          .rstrip() \
                                          .split())
                print(f"+++INFO card line:{card_line}")

