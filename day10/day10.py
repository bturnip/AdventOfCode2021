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

    def solve_part2(self):
        """ What is the middle score of the automcomplete series? """
        part2_score = 0
        # for all lines
        # parse line
        #if value returned is ''
        # figure out completion string
        # score and store completion string
        part2_scores = []
        for this_line in self.input_data:
            if self.parse_line(this_line) == '':
                data= this_line.strip()
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(f'+++DEBUG: incomplete_line: {data}')
                this_stack = []
                completion_data = []
                #--reverse the string and start stack processing
                for c in data[::-1]:
                    # ~ print(f'+++DEBUG: stack start of cycle: {this_stack}')
                    
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
                            
                    # ~ print(f'+++DEBUG: c: {c}')
                    # ~ print(f'+++DEBUG: stack end of cycle: {this_stack}')
                    # ~ print(f'+++DEBUG: completion_data: {completion_data}')
                    # ~ print("=========================================================")
                
                completion_str=''.join(completion_data)   
                print(f'+++DEBUG: completion_str: {completion_str}') 
                






        return part2_score


    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key


