""" 2021 Advent of Code: Day {NUM}"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103, C0123
from os.path import isfile
import numpy as np

class Day{NUM}():
    """ 2021 Advent of Code puzzle for Day{NUM} """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.answer_key = {}

        if input_file is not None and isfile(input_file):
            #TODO: self.{XXX} = self.load_data_from_file(input_file)
        else:
            #TODO: fill code

        if len(self.{XXX}) > 0:
            #TODO: fill code
        else:
            #TODO: fill code



    def load_data_from_file (self,input_file):
        """ loads the #TODO from file """
        # load logic:
        #  - 
        # 

        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # -- parse input file
        with open(input_file,'r',encoding="utf-8") as input_stream:
            raw_data=input_stream.readlines()
        input_stream.close()
        
        #TODO

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


