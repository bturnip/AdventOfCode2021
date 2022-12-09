"""
Test Cases for Day11
"""
# pylint: disable=C0104, E0602, W0602
from os.path import isfile
from unittest import TestCase
from day11 import *
from config_day11 import *
import random

class TestDay11(TestCase):
    """ Test Cases for Day 11 Advent of Code """
    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        global dummy_input_file, sample_file, full_file
        global sample_file_line_count, part1_sample_answer, part2_sample_answer
        
        # -- input file setup        
        dummy_input_file = "foo.file"
        full_file = FULL_FILE
        sample_file = SAMPLE_FILE
        
        # verified data
        sample_file_line_count = 10
        part1_sample_answer = #TODO
        part2_sample_answer = #TODO

    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_class_setup(self):
        """ Testing nosetest class setup"""
        self.assertTrue(isfile(full_file))
        self.assertTrue(isfile(sample_file))

    def test_day11_object_creation(self):
        """ Test day11 object creation"""
        test01=Day11()
        self.assertIsInstance(test01,object)
        #-------------------------------------
        test02=Day11(dummy_input_file)
        self.assertIsInstance(test02,object)
        self.assertEqual(dummy_input_file,test02.input_file)
        #-------------------------------------
        test03=Day11(sample_file)
        self.assertIsInstance(test02,object)
        # -------------------------------------     


    def test_load_from_file(self):
        """ Testing () """
        #TODO
        pass
    
    
    def test_get_answer_key(self):
        """ Testing get_answer_key() """
        test90 = Day11()
        test_result = test90.get_answer_key()
        self.assertIsInstance(test_result,dict)
        
        test91 = Day11(sample_file)
        results = test91.solve_part1()
        self.assertEqual(results,part1_sample_answer)
        
        test92 = Day11(sample_file)
        results = test92.solve_part2()
        self.assertEqual(results,part2_sample_answer)
        
