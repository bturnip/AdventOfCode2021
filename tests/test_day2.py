"""
Test Cases for Day2
"""
from unittest import TestCase

import sys
sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day2')
from day2 import *


class testDay2(TestCase):
    """ Test Cases for Day 2 Advent of Code """
    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)
        
    def test_calculate_position_empty_list(self):
        """ Test calculate_position() with empty list """
        expected_result = {"horiz":0,"depth":0}
        foo = calculate_position()
        self.assertEqual(foo, expected_result)
        
    def test_calculate_position(self):
        """ Test calculate_position() with known data """
        foo = ['forward 5\n', 'down 6\n', 'forward 5\n', 'up 2\n']
        expected_horizontal = 10
        expected_depth = 4
 
        # test 1: test horizontal position only
        result = calculate_position(foo)
        bar = result["horiz"]
        self.assertEqual(bar, expected_horizontal)
        
        #test 2: test depth position only
        baz = result["depth"]
        self.assertEqual(baz, expected_depth)
        
        #test 3: test dict result correctness
        expected_result = {"horiz":10,"depth":4}
        self.assertEqual(result,expected_result)

    def test_calc_postion_with_aim(self):
        """ Test calc_postion_with_aim() with known data """
        # Forward adds to *Horizontal* direction
        # Up or Down subtracts or adds to *Aim*
        # When *Aim* !=0, multiply *Aim* by *Forward* and add value to *Depth*
        foo = ['forward 5\n', 'down 5\n', 'forward 8\n', 'up 3\n', 'down 8\n', 'forward 2\n']
        expected_results={"horiz":15,"depth":60}
        bar = calc_postion_with_aim(foo)
        self.assertEqual(bar,expected_results)
       
        


        
        
        

