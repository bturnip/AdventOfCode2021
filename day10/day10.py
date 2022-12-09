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

        self.open_b = ['(', '[', '{', '<']
        self.close_b = [')', ']', '}', '>']
        self.all_b = self.open_b + self.close_b

        self.bracket_dict = {')':'(', ']':'[', '}':'{', '>':'<' \
                            ,'(':')', '[':']', '{':'}', '<':'>'}
        self.part1_points_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
        self.part2_points_dict = {')': 1, ']': 2, '}': 3, '>': 4}

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

        for c in line:
            #--is this a bracket?
            if c in self.all_b:
                #--an opening bracket? push
                if c in self.open_b:
                    stack.append(c)
                    # ~ print(f'+++DEBUG: stacking: {c}')

                #--a closing bracket?
                if c in self.close_b:
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
        return part1_score

    def autocomplete_line(self,data_in):
        """ parses data_in, returns str that completes it bracket-wise """
        # if the parse line returns '', indicating an incomplete string:
        # process the string starting from the end, building the string
        # needed to close all brackets
        if self.parse_line(data_in) == '':
            data= data_in.strip()
            completion_data = []
            this_stack=[]
            #--reverse the string and start stack processing
            for c in data[::-1]:
                #--closing bracket
                if c in self.close_b:
                    #--does this match the top of the stack?
                    if len(this_stack) > 0:
                        if this_stack[-1] == self.bracket_dict[c]:
                            this_stack.pop()
                        else:
                            this_stack.append(c)
                    else:
                        this_stack.append(c)
                #--opening bracket
                if c in self.open_b:
                    #does this match the top of the stack?
                    if len(this_stack) > 0:
                        if c == self.bracket_dict[this_stack[-1]]:
                            this_stack.pop()
                    else:
                        completion_data.append(self.bracket_dict[c])
            return ''.join(completion_data)
        return


    def solve_part2(self):
        """ What is the middle score of the automcomplete series? """
        part2_score = 0
        part2_scores = []

        #--score all lines
        for this_line in self.input_data:
            this_score = 0
            completion_str = self.autocomplete_line(this_line)
            # ~ print(f'+++DEBUG: completion_str: {completion_str}')
            if completion_str is not None:
                
                for c in completion_str:
                    this_score *=5
                    this_score += self.part2_points_dict[c]
                part2_scores.append(this_score)
        
        #--sort scores and choose the middle value
        idx = len(part2_scores)//2
        part2_score = sorted(part2_scores)[idx]
        
        part2_answer = f"Autocomplete middle score:[{part2_score}]"
        print(f"+++ANSWER: {part2_answer}" )
        self.answer_key["part 2"]= part2_answer        

        return part2_score


    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key
