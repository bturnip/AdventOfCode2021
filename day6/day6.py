""" 2021 Advent of Code: Day 6"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103
from os.path import isfile
import numpy as np

class Day6():
    """ 2021 Advent of Code puzzle for Day 6 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.answer_key = {}
        
    def get_answer_key(self):
        """ return answer key"""

