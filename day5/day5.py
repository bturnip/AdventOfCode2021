""" 2021 Advent of Code: Day 5"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
from os.path import isfile
import numpy as np

class Day5():
    """ 2021 Advent of Code puzzle for Day 5 """

    def __init__(self, input_file=None):
        self.input_file = input_file

        #hydrothermal vent coords
        if input_file is not None and isfile(input_file):
            self.vent_coords = self.load_all_coords_from_file(input_file)
        else:
            self.vent_coords = []

    def load_all_coords_from_file(self,input_file):
        """ loads the map of coords from file """
        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        with open(input_file,'r') as input_stream:
            raw_data=input_stream.readlines()
            input_stream.close()

            self.vent_coords =np.array(
                              [x.rstrip().split(' -> ') for x in raw_data])

        return self.vent_coords

    def get_all_coords(self):
        """ get the list of loaded coords """
        return self.vent_coords
