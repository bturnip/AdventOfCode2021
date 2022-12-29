""" 2021 Advent of Code: Day 14"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103, C0123
from os.path import isfile
import numpy as np

class Day14():
    """ 2021 Advent of Code puzzle for Day14 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.answer_key = {}
        self.polymer_template = ''
        self.insertion_rules = {}
        self.polymer = ''


        if input_file is not None and isfile(input_file):
            self.load_data_from_file(input_file)


    def load_data_from_file (self,input_file):
        """ loads input data from file """
        # load logic:
        #  - This first line is the polymer template
        #  - Remaining lines populate the pair_insertion_rules dict

        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # -- parse input file
        with open(input_file,'r',encoding="utf-8") as input_stream:
            raw_data=input_stream.readlines()
        input_stream.close()
        
        self.polymer_template = raw_data[0].rstrip()
        
        rules = raw_data[2:]
        for r in rules:
            data = r.split(' -> ')
            self.insertion_rules[data[0]] = data[1].rstrip()



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


