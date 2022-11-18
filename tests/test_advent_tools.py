"""
Test Cases for advent_tools module
"""
from unittest import TestCase
import unittest.mock as u

import sys
sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/advent_tools')
from advent_tools import *


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
        self.assertEqual(expected_file_name, get_input_file_name(day=2))

        # test with day as input parameter
        expected2 = expected_file_name.replace("day2","day3")
        self.assertEqual(expected2, get_input_file_name(3))

    def test_get_file_linecount(self):
        """ Get line count of input file"""
        expected_line_count = 1000
        self.assertEqual(expected_line_count,get_file_linecount(get_input_file_name(day=2)))

    def test_load_input_file_into_list_empty_file(self):
        """ Test that an empty file returns an empty list """
        # intercepting the file line count and returning a mocked value to
        # make the function think it has an empty file
        # the function needs a valid file, but it won't actually be counted
        this_file = get_input_file_name(day=2)
        with u.patch('advent_tools.get_file_linecount', return_value=0) as mocked_count:
            loaded_list =load_input_file_into_list(this_file)

        expected_list = []
        self.assertEqual(loaded_list,expected_list)


    def test_load_input_file_into_list(self):
        """ Test input file load """
        # load known test file from day 2 that has 1000 lines
        # check that list is the same length
        # check that output is actually a list
        foo = load_input_file_into_list(get_input_file_name(day=2))

        expected_len = 1000
        self.assertEqual(expected_len, len(foo))

        self.assertIsInstance(foo,list)


    def test_load_input_file_into_list_bad_load(self):
        """ Test that a failed file load is flagged """
        # intercepting the file line count and returning a mocked value
        # that should raise the ValueError
        this_file = get_input_file_name(day=2)
        with u.patch('advent_tools.get_file_linecount', return_value=12345) as mocked_count:
            self.assertRaises(ValueError, load_input_file_into_list, this_file)

    def test_intify_list(self):
        """ Test intify_list with known data"""
        foo = ["1","2",'3']
        expected_result = [1,2,3]
        bar = intify_list(foo)
        self.assertEqual(bar, expected_result)

    def test_intify_list_bad_input(self):
        """ Test intify_list with bad input"""
        foo = {}
        self.assertRaises(TypeError, intify_list, foo)

        bar =['x',1, '3']
        self.assertRaises(ValueError, intify_list, bar)

    def test_file_load_with_strip_newline(self):
        """ Test load_input_file_into_list() with strip_newline option """

        this_file = get_input_file_name(day=3)

        # first confirm that file load will have newlines
        foo = load_input_file_into_list(this_file)
        try:
            newline_found = next(x for x in foo if '\n' in x)
        except StopIteration:
            newline_found = None

        self.assertIsNotNone(newline_found)

        bar = load_input_file_into_list(this_file,strip_newline=True)
        try:
            newline_found = next(x for x in bar if '\n' in x)
        except StopIteration:
            newline_found = None

        self.assertIsNone(newline_found)
