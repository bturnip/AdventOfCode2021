"""
Test Cases for advent_tools module
"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=C0104, E0602

from unittest import TestCase
import unittest.mock as u

import sys
sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/advent_tools')
from advent_tools import *
import numpy as np


class TestAdventTools(TestCase):
    """ Test Cases for Advent Tools """
    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)


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

    def test_check_dict_keys_bad_input(self):
        """ Test check_dict_keys() with bad input """
        foo = ["a","b"]
        bar = {"a":1,"b":2}

        bad_foo = "I'm a string instead of a list"
        bad_bar = "I'm  string instead of a dict"

        empty_foo = []
        empty_bar ={}

        missing_bar = {"a":1,"c":3}

        self.assertRaises(TypeError,check_dict_keys, bad_foo, bar)
        self.assertRaises(TypeError,check_dict_keys, foo, bad_bar)
        self.assertRaises(ValueError,check_dict_keys,empty_foo, bar)
        self.assertRaises(ValueError,check_dict_keys,foo,empty_bar)
        self.assertFalse(check_dict_keys(foo, missing_bar))

    def test_check_dict_keys(self):
        """ Test check_dict_keys with known data """
        foo = ["a","b"]
        bar = {"a":1,"b":2}
        self.assertTrue(check_dict_keys(foo,bar))

    def test_bin_str_to_int(self):
        """ Test bin_str_to_int() """
        bad_inputs = [11,{'10101'},'123','']
        for b in bad_inputs:
            self.assertRaises(ValueError,bin_str_to_int, b)

        good_inputs = {'110':6, '001100001011':779 , '110011110100':3316}
        for k in good_inputs:
            self.assertEqual(good_inputs[k],bin_str_to_int(k))

    def test_check_np_array_values(self):
        """ test check_np_array_values()"""
        foo = np.array([[1,0,1,1],[1,1,0,0],[0,0,1,0]])
        valid_values = [0,1]

        empty_foo = np.array([])
        empty_values = []

        bad_foo = np.array([[2,0,1,1],[1,1,0,0],[0,0,1,0]])

        wrong_foo = "I'm a string instead of getting numpy!"
        wrong_values = "valid values"

        single_row_foo = np.array([1,1,0,0,1,1])

        # Check for empty input or wrong types
        self.assertRaises(ValueError,check_np_array_values,foo,empty_values)
        self.assertRaises(ValueError,check_np_array_values,empty_foo,valid_values)
        self.assertRaises(TypeError,check_np_array_values,foo,wrong_values)
        self.assertRaises(TypeError,check_np_array_values,wrong_foo,valid_values)

        # Check return values
        self.assertTrue(check_np_array_values(foo,valid_values))
        self.assertFalse(check_np_array_values(bad_foo,valid_values))
        self.assertTrue(check_np_array_values(single_row_foo,valid_values))

    def test_binary_frequency_select(self):
        """ test binary_frequency_select() """
        bad_type_foo = "I'm a string instead of getting numpy!"
        empty_foo = np.array([])
        bad_data_foo = np.array([1,0,1,2])

        # test sanity checks
        self.assertRaises(ValueError,binary_frequency_select,bad_type_foo)
        self.assertRaises(ValueError,binary_frequency_select,empty_foo)
        self.assertRaises(ValueError,binary_frequency_select,bad_data_foo)

        #test return values
        foo_pick_one_pt1 = np.array([1,0,1,1])
        foo_pick_one_pt2 = np.array([1,1,0,0])
        foo_pick_zero = np.array([0,1,0,0])

        self.assertEqual(1,binary_frequency_select(foo_pick_one_pt1))
        self.assertEqual(1,binary_frequency_select(foo_pick_one_pt2))
        self.assertEqual(0,binary_frequency_select(foo_pick_zero))

