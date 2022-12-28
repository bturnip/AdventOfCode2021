""" 2021 Advent of Code: Day 13"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103, C0123
from os.path import isfile
import numpy as np

class Day13():
    """ 2021 Advent of Code puzzle for Day13 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.answer_key = {}
        self.fold_instructions = []
        self.whole_sheet = np.array([])
        self.folded_sheet = np.array([])

        if input_file is not None and isfile(input_file):
            self.whole_sheet = self.load_whole_sheet_from_file(input_file)
            self.fold_instructions = self.load_fold_instructions_from_file(input_file)


    def load_fold_instructions_from_file (self,input_file):
        """ loads the fold_instructions from file """
        #--load logic:
        #  - discard all lines that do not start with "f"
        #  - instruction lines look like "fold along y=7"
        #  - store just the axis and index, ie ["y=7"]

        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # -- parse input file
        with open(input_file,'r',encoding="utf-8") as input_stream:
            raw_data = [line
                          .rstrip()
                          .split()[2]
                        for line in input_stream
                        if line.startswith('f')]

        input_stream.close()
        self.fold_instructions = raw_data
        return raw_data


    def get_sheet_bounds(self, input_file):
        """ determine the max grid size needed in input file """
        #--find max x-coord and max y-coord, round up to next
        max_x = 0
        max_y = 0
        with open(input_file,'r',encoding="utf-8") as input_stream:
            raw_data = [line.rstrip()
                        for line in input_stream
                        if line[0].isdigit()]
        input_stream.close()

        for this_coord in raw_data:
            x, y = this_coord.split(',')
            if int(x) > max_x:
                max_x = int(x)
            if int(y) > max_y:
                max_y = int(y)

        max_min_data = {"x":max_x+1, "y":max_y+1}
        return max_min_data


    def load_whole_sheet_from_file(self, input_file=None):
        """ Loads all coord pairs as a True/False matrix """
        #--x=
        #--NB: ignores all folding instructions
        #--sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        #--determine the size of the sheet, fill with 0
        sheet_bounds = self.get_sheet_bounds(input_file)
        sheet = np.full((sheet_bounds["y"], sheet_bounds["x"]),0)

        #--populate blank sheet using coords from input file
        with open(input_file,'r',encoding="utf-8") as input_stream:
            raw_data = [line.rstrip()
                        for line in input_stream
                        if line[0].isdigit()]
        input_stream.close()

        for i in range (0,len(raw_data)):
            x,y = raw_data[i].split(',')
            coord =(int(y),int(x))
            sheet[coord] = 1

        self.whole_sheet = sheet
        return sheet


    def fold(self,fold_instruction):
        """
        Folds the folded sheet (or a copy of the whole sheet if this
        the first fold)  according to the fold instruction
        """
        # -- conceptual diagram
        # +---+---+---+---+---+
        # | 1 | 2 | 3 | 4 | 5 |
        # +---+---+---+---+---+
        # | A | B | C | D | E |
        # +---+---+---+---+---+ <--- fold here
        # | 6 | 7 | 8 | 9 | 0 |
        # +---+---+---+---+---+
        # | G | H | I | J | K |
        # +---+---+---+---+---+
        #
        # the folded section gets row flipped
        # +---+---+---+---+---+
        # | G | H | I | J | K |
        # +---+---+---+---+---+
        # | 6 | 7 | 8 | 9 | 0 |
        # +---+---+---+---+---+
        instructions = []
        if type(fold_instruction) in (str,list):
            if len(fold_instruction) == 0:
                err_mssg = "+++ERROR: must have non-empty fold instructions, nothing to do"
                raise ValueError(err_mssg)
            if type(fold_instruction) == str:
                instructions.append(fold_instruction)
            elif type(fold_instruction) == list:
                instructions.extend(fold_instruction)
        else:
            err_mssg = "+++ERROR: fold_instruction must be a str or list of strings"
            raise TypeError(err_mssg)

        if self.folded_sheet.size == 0:
            self.folded_sheet = self.whole_sheet

        for this_i in instructions:
            print(f'+++FOLDING: {this_i}')

            axis, idx = this_i.split('=')
            idx = int(idx)
            if axis not in ("x","y"):
                err_mssg =f"+++ERROR: fold instructions must look like "\
                          f"'y=3' or 'x=16', etc.  Bad instruction: {this_i}"
                raise ValueError(err_mssg)

            if axis == 'y':
                fixed_portion = self.folded_sheet[0:idx:]
                folding_portion = np.flipud(self.folded_sheet[idx+1::])
            else:
                fixed_portion = self.folded_sheet[:,0:idx]
                folding_portion = np.fliplr(self.folded_sheet[:,idx+1:])

            self.folded_sheet = fixed_portion + folding_portion
            print(self.folded_sheet)


    def solve_part1(self):
        """
        How many dots are visible after completing just the first
        fold instruction on your transparent paper?
        """
        part1_score = 0
        self.fold(self.fold_instructions[0])
        part1_score = np.count_nonzero(self.folded_sheet > 0)
        self.answer_key["part1"] = part1_score
        return part1_score

    def solve_part2(self):
        """ TODO: enter part 2 question here """
        part2_score = 0
        return part2_score

    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key
