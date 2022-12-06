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
        self.basin_map = {}
        self.hm_num_rows = 0
        self.hm_num_cols = 0
        self.hm_last_row = 0
        self.hm_last_col = 0

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
        self.heightmap = string_arr.astype(int)

        #--set status on loaded height map
        self.hm_num_rows, self.hm_num_cols = self.heightmap.shape
        self.hm_last_col = self.hm_num_cols-1
        self.hm_last_row = self.hm_num_rows-1


        return self.heightmap

    def set_low_point_coords (self):
        """ Create a dict with coords and value of low points for heightmap """
        #--sanity checks
        if self.heightmap.size == 0:
            print("+++ERROR: no data in the heightmap, nothing to do...")
            return {}

        row_wise_results = {}

        for r in range(0,self.hm_num_rows):
            #--calculate low points row-wise: consider left or right only
            this_row = self.heightmap[r]

            for c in range(0,self.hm_num_cols):
                this_value = this_row[c]

                #--check vals in 1st column, no check to the left
                if c == 0:
                    if this_value < this_row[c+1]:
                        row_wise_results[r,c]=this_value
                #--compare the 2nd through next to last cols
                if c < self.hm_last_col:
                    if this_value < this_row[c+1]:
                        if this_value < this_row[c-1]:
                            row_wise_results[r,c]=this_value
                #--check vals in last col, no check to the right
                if c == self.hm_last_col:
                    if this_value < this_row[c-1]:
                        row_wise_results[r,c]=this_value

        #--take the row wise calculations and compare the up or down coords
        temp_coords={}
        for coord, coord_height in row_wise_results.items():
            rownum = coord[0]
            colnum = coord[1]
            #--check vals in first row, no check above
            if rownum == 0:
                if coord_height < self.heightmap[rownum + 1][colnum]:
                    temp_coords[coord] = coord_height
            #--check vals for the value in the column above + below
            if rownum < self.hm_last_row:
                if coord_height < self.heightmap[rownum + 1][colnum]:
                    if coord_height < self.heightmap[rownum - 1][colnum]:
                        temp_coords[coord] = coord_height
            if rownum == self.hm_last_row:
                if coord_height < self.heightmap[rownum - 1][colnum]:
                    temp_coords[coord] = coord_height

        self.low_point_coords = temp_coords
        return self.low_point_coords

    def map_basins(self):
        """ maps all basins connected to each low point """
        #--start with each low point
        #  - row wise, add each element to the left or right until a value of 9 is
        #    reached. elements to the left, right, up, and down
        #--sanity checks
        if self.heightmap.size == 0:
            print("+++ERROR: no data in the heightmap, nothing to do...")
            return set()

        row_wise_results = set()
        for this_coord in self.low_point_coords.keys():
            print(f'+++DEBUG: this_coord: {this_coord}++++++++++++++++')
            row_wise_results = set()
            
            rownum = this_coord[0]
            colnum = this_coord[1]
            
            #--go right, add elements that go in this basin
            next_val = -1
            for c in range (colnum,self.hm_num_cols):
                if self.heightmap[rownum][c] == 9:
                    break
                row_wise_results.add((rownum,c))
                print(f'+++DEBUG: adding: {(rownum,c)}')
            
            #--go left, do not count starting point
            if colnum > 0:
                for c in range (colnum-1, -1,-1):
                    if self.heightmap[rownum][c] == 9:
                        break
                    row_wise_results.add((rownum,c))
                    print(f'+++DEBUG: adding: {(rownum,c)}')
 
                    
            print(f'+++DEBUG: row_wise_results: {row_wise_results}')
            #TODO go column wise down, then check left/right
            #TOOD go column wise up, then check for left right
        
                
                 
            
            
            
            
            
            
            




    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key

    def solve_part1(self):
        """ What is sum(risk levels) of all low points on heightmap? """
        #--risk level is height of the low point +1
        low_pt_risk_lvl_sum =sum(self.low_point_coords.values()) \
                            +len(self.low_point_coords)

        part1_answer = f"Low point risk level sum:[{low_pt_risk_lvl_sum}]"
        print(f"+++ANSWER: {part1_answer}" )
        self.answer_key["part 1"]= part1_answer

        return self.answer_key
