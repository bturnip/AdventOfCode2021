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
        self.basin_sizes = {}
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
        #--start with each low point coord
        #  send the height map and low point to the flood fill function
        #  - count the -1 values after flood fill has completed
        #    record the low point coord and connected points
        for this_coord in self.low_point_coords.keys():
            this_basin = self.heightmap.copy()
            self.flood_fill(field = this_basin \
                            ,x = this_coord[1] \
                            ,y = this_coord[0] \
                            ,border_value =  9 \
                            ,fill_value = -1)
            basin_count = np.count_nonzero(this_basin == -1)
            self.basin_sizes[this_coord] = basin_count


    def flood_fill(self,field, x, y, border_value, fill_value):
        """ Take a given field and start point, flood fill with fill value  """
        #--Flood fill algorithm example from here:
        #--https://github.com/ramza/PythonTuts

        #--this version needs to fill any value that isn't a 9, instead
        #  of a "bucket fill" method original algoritm solved

        #--the flood fill has 4 parts
        #--firstly, make sure the x and y are inbounds
        if x < 0 or x >= len(field[0]) or y < 0 or y >= len(field):
            return

        #--secondly, check if the current position equals the old value
        if field[y][x] == border_value or field[y][x] == fill_value:
            return

        #--thirdly, set the current position to the new value
        field[y][x] = fill_value

        #--fourthly, attempt to fill the neighboring positions
        self.flood_fill(field,x+1, y, border_value, fill_value)
        self.flood_fill(field,x-1, y, border_value, fill_value)
        self.flood_fill(field,x, y+1, border_value, fill_value)
        self.flood_fill(field,x, y-1, border_value, fill_value)


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


    def solve_part2(self):
        """ What is the product of the 3 largest basin sizes? """
        self.map_basins()
        sizes = np.array(sorted(self.basin_sizes.values(),reverse=True))
        top3_product = np.prod(sizes[0:2])

        part2_answer = f"Product of 3 largest basin sizes:[{top3_product}]"
        print(f"+++ANSWER: {part2_answer}" )
        self.answer_key["part 2"]= part2_answer

        return self.answer_key

