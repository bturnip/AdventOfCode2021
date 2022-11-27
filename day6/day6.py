""" 2021 Advent of Code: Day 6"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103
from os.path import isfile
import numpy as np

class Day6():
    """ 2021 Advent of Code puzzle for Day 6 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.answer_key = {}
        
        if input_file is not None and isfile(input_file):
            self.fish = self.load_fish_from_file(input_file)
        else:
            self.fish = []
        
    def load_fish_from_file (self,input_file):
        """ loads the lantern fish from file """
        # fish load logic:
        #  - input file a series of numbers that represent each current
        #    fish's countdown timer
        #  - entry lines look like "1,4,1,2,1,1,4"
        #
        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # -- parse input file
        with open(input_file,'r') as input_stream:
            raw_data=input_stream.readlines()
        input_stream.close()
        
        fish_data = list(map(int,raw_data[0].split(',')))

        self.fish=np.array(fish_data)
        return self.fish

        
            
    
    def get_answer_key(self):
        """ return answer key"""

