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

day4_path = "/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day4"

sample_input_draws = [14,30,18,8,3,52]
sample_input_file = f"{day4_path}/day4_raw_sample.txt"
real_input_file = f"{day4_path}/day4_raw_input.txt"



class TestDay4(TestCase):
    """ Test Cases for Day 4 Advent of Code """

    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_day4_object_creation(self):
        """ Test Day4 object creation"""
        test01=Day4()
        self.assertIsInstance(test01,object)
        #-------------------------------------
        test02=Day4(dummy_input_file)
        self.assertIsInstance(test02,object)
        self.assertEqual(dummy_input_file,test02.input_file)
        #-------------------------------------
        test03=Day4(real_input_file)
        self.assertIsInstance(test03,object)
        self.assertEqual(real_input_file,test03.input_file)
        #-------------------------------------
        test04=Day4(sample_input_file)
        self.assertEqual(sample_input_draws,test04.bingo_draws)

    def test_set_bingo_draws(self):
        """ Test setting the bingo draws """
        single_val = random.randrange(0,100)
        test10=Day4()
        test10.set_bingo_draws(single_val)
        self.assertEqual([single_val],test10.bingo_draws)
        #-------------------------------------
        input_values = ["Random","RANDOM","random"]
        for i in input_values:
            test11=Day4()
            self.assertEqual(0,len(test11.bingo_draws))
            test11.set_bingo_draws(i)
            self.assertEqual(100,len(test11.bingo_draws))
            self.assertNotEqual(list(range(100)),test11.bingo_draws)
        #-------------------------------------
        test12=Day4()
        self.assertEqual([],test12.bingo_draws)
        test12.set_bingo_draws(sample_input_draws)
        self.assertEqual(sample_input_draws,test12.bingo_draws)

        #-------------------------------------
        bad_input_vals = [{1:2,3:4}, 123.45, "foo", "randommmm"]
        
        for bad_i in bad_input_vals:
            test13=Day4()
            self.assertRaises(TypeError
                              ,test13.set_bingo_draws
                              ,bad_i)
        #-------------------------------------
        test14=Day4()
        test14.set_bingo_draws(sample_input_file)
        self.assertEqual(sample_input_draws
                         ,test14.bingo_draws)
        
        

    def test_load_bingo_draws_from_file(self):
        """ Test loading bingo_draws from an input file """
        test20=Day4(sample_input_file)
        test20.load_bingo_draws_from_file(sample_input_file)
        self.assertEqual(sample_input_draws,test20.bingo_draws)
        #-------------------------------------
        test21=Day4()
        self.assertRaises(TypeError
                          ,test21.load_bingo_draws_from_file
                          ,dummy_input_file)
                          
    def test_load_bingo_cards_from_file(self):
        """ Test loading bingo_cards from an input file """
        test30=Day4()
        self.assertRaises(TypeError
                          ,test30.load_bingo_cards_from_file
                          ,dummy_input_file)
        
        
        
        
        
