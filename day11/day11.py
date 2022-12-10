""" 2021 Advent of Code: Day 11"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103, C0123
from os.path import isfile
import numpy as np

class Day11():
    """ 2021 Advent of Code puzzle for Day11 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.answer_key = {}

        if input_file is not None and isfile(input_file):
            self.orig_input = self.load_data_from_file(input_file)
            self.input_working_copy = self.orig_input.copy()
        else:
            self.orig_input = np.array([[]])

        if len(self.orig_input) > 0:
            #TODO: fill code
            pass
        else:
            #TODO: fill code
            pass

    def load_data_from_file(self,input_file):
        """ loads the #TODO from file """

        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # -- parse input file
        with open(input_file,'r') as input_stream:
            raw_data=input_stream.readlines()
        input_stream.close()

        data_out = [list(x.rstrip()) for x in raw_data]

        return np.array(data_out)

    def model_turn(self,):
        """ Function doc """

    def solve_part1(self):
        """ TODO: enter part 1 question here """
        part1_score = 0
        return part1_score

    def solve_part2(self):
        """ TODO: enter part 2 question here """
        part2_score = 0
        return part2_score

    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key


