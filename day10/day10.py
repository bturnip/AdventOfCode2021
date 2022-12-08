""" 2021 Advent of Code: Day 10"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103, C0123
from os.path import isfile
import numpy as np

class Day10():
    """ 2021 Advent of Code puzzle for Day 6 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.answer_key = {}

        if input_file is not None and isfile(input_file):
            self.input_data = self.load_data_from_file(input_file)
        else:
            self.input_data = []


    def load_data_from_file (self,input_file):
        """ loads the #TODO from file """
        # load logic:
        #  - raw load, only process in other functions defs

        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # -- parse input file
        with open(input_file,'r') as input_stream:
            raw_data=input_stream.readlines()
        input_stream.close()


    def solve_part1(self):
        """ TODO: enter part 1 question here """
        pass

    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key


