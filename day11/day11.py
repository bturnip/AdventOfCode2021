""" 2021 Advent of Code: Day 11"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103, C0123
from os.path import isfile
import numpy as np

class Day11():
    """ 2021 Advent of Code puzzle for Day11 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.answer_key = {}
        self.total_flashes_100_turns = 0

        if input_file is not None and isfile(input_file):
            self.orig_input = self.load_data_from_file(input_file)
            self.input_working_copy = self.orig_input.copy()
        else:
            self.orig_input = np.array([[]])

        if len(self.orig_input) > 0:
            self.row_out_of_bounds = self.orig_input.shape[0]
            self.col_out_of_bounds = self.orig_input.shape[1]
        else:
            self.last_row = 0
            self.last_col = 0

    def load_data_from_file(self,input_file):
        """ loads the #TODO from file """

        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # -- parse input file
        with open(input_file,'r') as input_stream:
            raw_data=input_stream.readlines()
        input_stream.close()

        data_out = [list(x.rstrip()) for x in raw_data]

        return np.array(data_out).astype(int)

    def model_turn(self):
        """ Model 1 turn of dumbo energy increasing """
        #--increase energy levels
        # ~ print(f'+++DEBUG: input array: {input}')
        self.input_working_copy = self.input_working_copy + 1
        #--if we have energy levels to flash, process all flash chains
        if 10 in self.input_working_copy:
            self.model_flashes()

    def model_flashes(self):
        """ Process dumbo flashing """
        while 10 in self.input_working_copy:
            this_flash = np.where(self.input_working_copy>=10)
            flash_coords = list(zip(this_flash[0],this_flash[1]))
            #print(f'+++DEBUG: flash_coords: {flash_coords}')
    
            #--for each flash coord
            #  - set coord to zero
            #  - for each neighbor <> 0, increment
            for this_coord in flash_coords:
                print(f'+++DEBUG: calling flash_coord({this_coord})')
                self.flash_coord(this_coord)

    def flash_coord (self, coord):
        """ Set coord to zero and increment all non-zero neighbors """
        #print(f'+++DEBUG: starting work:\n {self.input_working_copy}')
        row,col = coord
        self.input_working_copy[row][col]=0
        self.total_flashes_100_turns +=1
        
        for r in range(max(row-1,0) \
                       ,min(row+2,self.row_out_of_bounds)):
            for c in range(max(col-1,0) \
                           ,min(col+2, self.col_out_of_bounds)):
                #print(f'+++DEBUG: target coord: {r},{c}')
                if self.input_working_copy[r][c] > 0:
                    self.input_working_copy[r][c] += 1
        #print(f'+++DEBUG: flash_coord complete:\n {self.input_working_copy}')










    def solve_part1(self):
        """ TODO: enter part 1 question here """
        for i in range(0,100):
            self.model_turn()
            print(f"turn {i}:")
        return self.total_flashes_100_turns

    def solve_part2(self):
        """ TODO: enter part 2 question here """
        part2_score = 0
        return part2_score

    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key


