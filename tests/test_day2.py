"""
Test Cases for Day2
"""
from unittest import TestCase
import unittest.mock as u
from day2.day2 import *

class testDay2(TestCase):
    """ Test Cases for Day 2 Advent of Code """
    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    # NB: these test cases are testing code that was moved to the
    # NB: advent_tools module, since they are likely to be used in
    # NB: following day's puzzles
    def test_get_input_file_name(self):
        """ Test automated file name generation"""
        expected_file_name = ("/home/bturnip/Documents/Code/python/"\
                              "advent_of_code/AdventOfCode2021/"\
                              "day2/day2_input.txt")

        # test with no argument
        print(get_input_file_name())
        self.assertEqual(expected_file_name, get_input_file_name())

        # test with day as input parameter
        expected2 = expected_file_name.replace("day2","day3")
        self.assertEqual(expected2, get_input_file_name(3))

    def test_get_file_linecount(self):
        """ Get line count of input file"""
        expected_line_count = 1000
        self.assertEqual(expected_line_count,get_file_linecount(get_input_file_name()))

    def test_load_input_file_into_list(self):
        """ Test input file load """
        foo = load_input_file_into_list(get_input_file_name())

        expected_len = 1000
        self.assertEqual(expected_len, len(foo))


    def test_load_input_file_into_list_bad_load(self):
        """ Test that a failed file load is flagged """
        x=get_file_linecount(get_input_file_name())
        print(x)
        
        y=load_input_file_into_list(get_input_file_name())
        print(y)
        
#        with u.patch('get_file_linecount',100):
#            get_file_linecount(get_input_file_name())
#            load_input_file_into_list(get_input_file_name())



