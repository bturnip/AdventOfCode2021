"""
Test Cases for Day1
"""
from unittest import TestCase

import sys
sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day1')
from day1 import *


class testDay1(TestCase):
    """ Test Cases for Day 1 Advent of Code """
    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_create_windowed_list_bad_data(self):
        """ Test sending bad data to create_windowed_list()"""
        foo = []
        self.assertRaises(ValueError, create_windowed_list, foo, 3)
        bar = [1,2,3,4,5]
        self.assertRaises(ValueError, create_windowed_list, foo, 5)

    def test_create_windowed_list(self):
        """ Test Windowed List Creation"""
        foo = [1,1,1,2,2,2,3,3,3]
        expected_bar = [3,4,5,6,7,8,9]
        bar = create_windowed_list(foo,3)
        self.assertEqual(bar,expected_bar)

    def test_count_depth_increases(self):
        """ Test counting the number of depth increases """
        foo = [1,2,3,4]
        expected_count = 3
        actual_count = count_depth_increases(foo)
        self.assertEqual(expected_count, actual_count)

        bar = [1,1,1,1]
        expected_count = 0
        actual_count = count_depth_increases(bar)
        self.assertEqual(expected_count, actual_count)

        baz = [1,0,1,2]
        expected_count = 2
        actual_count = count_depth_increases(baz)
        self.assertEqual(expected_count, actual_count)

        qux = [1,1,2,0]
        expected_count = 1
        actual_count = count_depth_increases(qux)
        self.assertEqual(expected_count, actual_count)


