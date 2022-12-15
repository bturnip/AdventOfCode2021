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

        self.row_out_of_bounds = self.orig_input.shape[0]
        self.col_out_of_bounds = self.orig_input.shape[1]


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

    def model_turn(self, solve_part2=False):
        """ Model 1 turn of dumbo energy increasing """
        #--increase energy levels
        self.input_working_copy = self.input_working_copy + 1

        #--if we have energy levels to flash, process all flash chains
        if 10 in self.input_working_copy:
            self.model_flashes()

        #--for Part2, return when all grid points have flashed
        if solve_part2 is True:
            if (np.count_nonzero(self.input_working_copy == 0)\
                == self.orig_input.size):
                return 99999
        return 0


    def model_flashes(self):
        """ Process dumbo flashing """
        #--while enery level > 9 anywhere in grid:
        #  - gather list of coords and call_flash_coord on each one
        while np.count_nonzero(self.input_working_copy > 9):
            this_flash = np.where(self.input_working_copy>=10)
            flash_coords = list(zip(this_flash[0],this_flash[1]))

            for this_coord in flash_coords:
                 # ~ print(f'+++DEBUG: calling flash_coord({this_coord})')
                self.flash_coord(this_coord)

    def flash_coord (self, coord):
        """ Set coord to zero and increment all non-zero neighbors """
        row,col = coord
        if self.input_working_copy[row][col] != 0:
            self.total_flashes_100_turns +=1
            self.input_working_copy[row][col]=0

        for r in range(max(row-1,0) \
                       ,min(row+2,self.row_out_of_bounds)):
            for c in range(max(col-1,0) \
                           ,min(col+2, self.col_out_of_bounds)):
                if self.input_working_copy[r][c] > 0:
                    self.input_working_copy[r][c] += 1


    def solve_part1(self, num_turns=None):
        """ How many total flashes are there after 100 steps? """
        if num_turns is None or type(num_turns) != int:
            num_turns = 100

        for i in range(1,num_turns+1):
            self.model_turn()
            # ~ print(f"turn {i}: flashes:{self.total_flashes_100_turns}")

        part1_answer = f'Total flashes after 100 steps:[{self.total_flashes_100_turns}]'
        self.answer_key["part 1"]=part1_answer

        return self.total_flashes_100_turns

    def solve_part2(self):
        """ What is 1st step during which all octopuses flash? """
        part2_answer = 0
        turn_limit = 5000 #--don't run forever
        i = 0
        while part2_answer != 99999 and i <= turn_limit:
            i+=1
            
            part2_answer = self.model_turn(solve_part2=True)
            

        if i==turn_limit:
            print(f"+++WARNING: no all-flashing turn found after {turn_limit} turns...")
        else:

            part2_answer = f'Found all-flashing turn on turn #{i}'
            self.answer_key['part 2']=part2_answer
        return i

    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key
