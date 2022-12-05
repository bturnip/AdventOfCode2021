""" 2021 Advent of Code: Day 9"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103, C0123
from os.path import isfile
import numpy as np

class Day9():
    """ 2021 Advent of Code puzzle for Day 6 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.answer_key = {}

        if input_file is not None and isfile(input_file):
            self.heightmap = self.load_data_from_file(input_file)
        else:
            self.heightmap = [[]]
        '''
        if len(self.{XXX}) > 0:
            #TODO: fill code
        else:
            #TODO: fill code
        '''



    def load_data_from_file (self,input_file):
        """ loads the heightmap from file """
        # load logic:
        #  - input data is a grid of numbers
        #  - load as 2D numpy array
        
        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # -- parse input file
        with open(input_file,'r') as input_stream:
            raw_data=input_stream.readlines()
        input_stream.close()
        
        #--convert strings to ints and return list
        string_arr = np.array([list(x.strip()) for x in raw_data])
        return string_arr.astype(int)
    
    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key

    def solve_part1(self):
        """ What is sum(risk levels) of all low points on heightmap? """

        low_pt_risk_lvl_sum = 0
        
        part1_answer = f"Low point risk level sum:[{low_pt_risk_lvl_sum}]"
        print(f"+++ANSWER: {part1_answer}" )
        self.answer_key["part 1:"]= part1_answer

        return self.answer_key

