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

        if len(self.vent_coords) > 0:
            self.marked_map = self.map_coords(self.vent_coords)
        else:
            self.marked_map = []

    def load_all_coords_from_file(self,input_file):
        """ loads the map of coords from file """
        # coordinates load logic:
        #  - input file a series of coordinate entries
        #  - entry lines look like "777,778 -> 777,676"
        #  - these are the "start" and "stop" points on a line segment
        #    on a grid
        #  - output is a 2D np array that looks like this:
        #    [[777 778 777 676]
        #     [500 510 378 510]
        #     [...]
        #     [623 450 623 616]]
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

        self.vent_coords = np.empty((0,4), int)

        coord_pairs =np.array([x.rstrip().split(' -> ') for x in raw_data])

        for this_pair in coord_pairs:
            start_pt = this_pair[0]
            stop_pt = this_pair[1]
            xstart, ystart = start_pt.split(',')
            xend, yend = stop_pt.split(',')
            
            this_row = np.array([[xstart,ystart,xend,yend]])
            
            #print(f"{xstart}|{ystart}|{xend}|{yend}")
            self.vent_coords = np.r_[self.vent_coords ,this_row.astype(int)]

        return self.vent_coords

    def get_all_coords(self):
        """ get the list of loaded coords """
        return self.vent_coords

    def map_coords(self,coords):
        """ maps a set of coords to self.marked_map """
        #-- find the boundaries of the map
        #   - entries are a np array of two element ndarrays
        #   - example:
        x1_max, y1_max, x2_max, y2_max = coords.max(axis=0)
        print("+++INFO:map_coords, column maxes")
        print(x1_max, y1_max, x2_max, y2_max)
        
        return 0


