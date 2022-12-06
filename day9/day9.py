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
        self.low_point_coords ={}

        if input_file is not None and isfile(input_file):
            self.heightmap = self.load_data_from_file(input_file)
        else:
            self.heightmap = np.array([[]])

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

    def set_low_point_coords (self):
        """ Create a dict with coords and value of low points for heightmap """
        #--sanity checks
        if self.heightmap.size == 0:
            print("+++ERROR: no data in the heightmap, nothing to do...")
            return {}

        num_rows, num_cols = self.heightmap.shape
        last_col = num_cols-1
        last_row = num_rows-1

        row_wise_results = {}

        for r in range(0,num_rows):
            #--calculate low points row-wise: consider left or right only
            this_row = self.heightmap[r]

            print(f'+++DEBUG: this_row: {this_row}')

            for c in range(0,num_cols):
                this_value = this_row[c]

                #--check vals in 1st column, no check to the left
                if c == 0:
                    if this_value < this_row[c+1]:
                        row_wise_results[r,c]=this_value
                #--compare the 2nd through next to last cols
                if c < last_col:
                    if this_value < this_row[c+1]:
                        if this_value < this_row[c-1]:
                            row_wise_results[r,c]=this_value
                #--check vals in last col, no check to the right
                if c == last_col:
                    if this_value < this_row[c-1]:
                        row_wise_results[r,c]=this_value

        #--take the row wise calculations and compare the up or down coords
        temp_coords={}
        for coord, coord_height in row_wise_results.items():
            print(f'+++DEBUG: coord, coord_height: {coord},{coord_height}')
            rownum = coord[0]
            colnum = coord[1]
            #--check vals in first row, no check above
            if rownum == 0:
                if coord_height < self.heightmap[rownum + 1][colnum]:
                    temp_coords[coord] = coord_height
            #--check vals for the value in the column above + below
            if rownum < last_row:
                if coord_height < self.heightmap[rownum + 1][colnum]:
                    if coord_height < self.heightmap[rownum - 1][colnum]:
                        temp_coords[coord] = coord_height
            if rownum == last_row:
                if coord_height < self.heightmap[rownum - 1][colnum]:
                    temp_coords[coord] = coord_height
        
        self.low_point_coords = temp_coords
        return self.low_point_coords





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
