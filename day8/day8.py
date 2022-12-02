""" 2021 Advent of Code: Day 8"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103, C0123
from os.path import isfile
import numpy as np

class Day8():
    """ 2021 Advent of Code puzzle for Day 8 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.answer_key = {}

        if input_file is not None and isfile(input_file):
            self.segment_observations = self.load_data_from_file(input_file)
        else:
            self.segment_observations = []

        """
        if len(self.{XXX}) > 0:
            #TODO: fill code
        else:
            #TODO: fill code
        """

    def load_data_from_file (self,input_file):
        """ loads the #TODO from file """
        # load logic:
        #  - split the incoming line on the "|", and further split each
        #    half of the result into lists
        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # -- parse input file
        with open(input_file,'r') as input_stream:
            raw_data=input_stream.readlines()
        input_stream.close()

        self.segment_observations = [[y[0].split(),y[1].split()] for y in
                                         [x.split('|') for x in raw_data]
                                    ]
        return self.segment_observations
    
    def solve_part1(self):
        """ how many times do digits 1, 4, 7, or 8 appear in output? """
        
        target_count = 0
        
        if len(self.segment_observations) > 1:
            part1_outputs = [x[1] for x in self.segment_observations ]
            
            for x in part1_outputs:
                this_count=len([y for y in x if (len(y) ==7 or \
                                             len(y) ==2  or \
                                             len(y) ==3  or \
                                             len(y) ==4)]
                              )
                target_count += this_count
        else:
            print("+++WARNING: empty segment_observations data, nothing to do...")
            return 0
        


        part1_answer = f"Total count of 1,4,7,8 in outputs:[{target_count}]"
        print(f"+++ANSWER: {part1_answer}" )
        self.answer_key["part 1:"]= part1_answer

        return self.answer_key        

    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key
