"""
Test Cases for Day4
"""
# pylint: disable=C0104, E0602, W0602
from unittest import TestCase
import numpy as np
import sys
sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day4')

from day4 import *

dummy_input_file = "foo"
real_input_file = '/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day4/day4_raw_input.txt'
dummy_input_draws = [1,2,3,25,35,99]


class TestDay4(TestCase):
    """ Test Cases for Day 4 Advent of Code """
    global dummy_input_file,real_input_file, dummy_input_draws

    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_day4_object_creation(self):
        """ Test Day4 object creation"""
        test01=Day4()
        self.assertIsInstance(test01,object)

        test02=Day4(dummy_input_file)
        self.assertIsInstance(test02,object)
        self.assertEqual(dummy_input_file,test02.input_file)

        test03=Day4(real_input_file)
        self.assertIsInstance(test03,object)
        self.assertEqual(real_input_file,test03.input_file)

    def test_set_bingo_draws(self):
        """ Test setting the bingo draws """
        single_val = random.randrange(0,100)
        test04=Day4()
        test04.set_bingo_draws(single_val)
        self.assertEqual([single_val],test04.bingo_draws)

        input_values = ["Random","RANDOM","random"]
        for i in input_values:
            test05=Day4()
            self.assertEqual(0,len(test05.bingo_draws))
            test05.set_bingo_draws(i)
            self.assertEqual(100,len(test05.bingo_draws))
            self.assertNotEqual(list(range(100)),test05.bingo_draws)

        test06=Day4()
        self.assertEqual([],test06.bingo_draws)
        test06.set_bingo_draws(dummy_input_draws)
        self.assertEqual(dummy_input_draws,test06.bingo_draws)

        bad_input_vals = [{1:2,3:4}, 123.45, "foo", "randommmm"]

        for bad_i in bad_input_vals:
            test07=Day4()
            self.assertRaises(TypeError
                              ,test07.set_bingo_draws
                              ,bad_i)
        
        # test08 load/re-load from the input_file specified at object
        # creation time.
