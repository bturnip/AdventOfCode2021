""" 2021 Advent of Code: Day 10"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103, C0123
from os.path import isfile
import numpy as np

class Day10():
    """ 2021 Advent of Code puzzle for Day 6 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.answer_key = {}

        self.bracket_dict = {')':'(', ']':'[', '}':'{', '>':'<'}
        self.part1_points_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}


        if input_file is not None and isfile(input_file):
            self.input_data = self.load_data_from_file(input_file)
        else:
            self.input_data = []


    def load_data_from_file (self,input_file):
        """ loads the #TODO from file """
        # load logic:
        #  - raw load, only process in other functions defs

        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # -- parse input file
        with open(input_file,'r') as input_stream:
            raw_data=input_stream.readlines()
        input_stream.close()

        self.input_data = raw_data
        return raw_data


    def parse_line(self,line):
        """ parse line using a stack to catch illegal chars"""
        stack=[]

        open_b = ['(', '[', '{', '<']
        close_b = [')', ']', '}', '>']
        all_b = open_b + close_b


        for c in line:
            #--is this a bracket?
            if c in all_b:
                #--an opening bracket? push
                if c in open_b:
                    stack.append(c)
                    # ~ print(f'+++DEBUG: stacking: {c}')

                #--a closing bracket?
                if c in close_b:
                    #--matching bracket?  pop and carry on
                    if len(stack) > 0 and stack[-1] == self.bracket_dict[c]:
                        # ~ print(f'+++DEBUG: popping: {stack[-1]}')
                        stack.pop()
                    else:
                        # ~ print(f'+++DEBUG: illegal char: {c}')
                        return c
        return ''



    def solve_part1(self):
        """ What is the total syntax error score? """
        #-- take the first illegal character on the line
        #   score each line according to the part1 points dict
        
        part1_score = 0
        
        for this_line in self.input_data:
            illegal_char = self.parse_line(this_line)
            if len(illegal_char) > 0:
                part1_score += self.part1_points_dict[illegal_char]
        
        part1_answer = f"Syntax error score:[{part1_score}]"
        print(f"+++ANSWER: {part1_answer}" )
        self.answer_key["part 1"]= part1_answer



    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key


