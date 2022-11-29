""" 2021 Advent of Code: Day 7"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103, C0123
from os.path import isfile
import numpy as np

class Day7():
    """ 2021 Advent of Code puzzle for Day 6 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.answer_key = {}
        

        if input_file is not None and isfile(input_file):
            self.starting_crabs = self.load_data_from_file(input_file)
        else:
            self.starting_crabs = []

        if len(self.starting_crabs) > 0:
            pass
        else:
            pass



    def load_data_from_file (self,input_file):
        """ loads the #TODO from file """
        # load logic:
        #  - input file a series of numbers that represent each current
        #    crab's horizontal location
        #  - entry lines look like "1101,1,29,67,1102,0,1,65,1008,65,35"
        # note that this list won't change once created

        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # -- parse input file
        with open(input_file,'r') as input_stream:
            raw_data=input_stream.readlines()
        input_stream.close()
        
        crab_data = list(map(int,raw_data[0].split(',')))

        self.starting_crabs=np.array(crab_data)
        return self.starting_crabs
        
        
    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key


