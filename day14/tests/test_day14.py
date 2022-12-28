"""
Test Cases for Day14
"""
# pylint: disable=C0104, E0602, W0602
from os.path import isfile
from unittest import TestCase
from day14 import *
from config_day14 import *
import random

class TestDay14(TestCase):
    """ Test Cases for Day 14 Advent of Code """
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

    def test_day14_object_creation(self):
        """ Test day14 object creation"""
        test01=Day14()
        self.assertIsInstance(test01,Day14)
        #-------------------------------------
        test02=Day14(dummy_input_file)
        self.assertIsInstance(test02,Day14)
        self.assertEqual(dummy_input_file,test02.input_file)
        #-------------------------------------
        test03=Day14(sample_file)
        self.assertIsInstance(test03,Day14)
        # -------------------------------------     


    def test_load_from_file(self):
        """ Testing load_data_from_file() """
        test10=Day14()
        self.assertRaises(TypeError,test10.load_data_from_file,dummy_input_file)
        
        
        
    
    
    def test_get_answer_key(self):
        """ Testing get_answer_key() """
        test90 = Day14()
        test_result = test90.get_answer_key()
        self.assertIsInstance(test_result,dict)
        
        test91 = Day14(sample_file)
        results = test91.solve_part1()
        self.assertEqual(results,part1_sample_answer)
        
        test92 = Day14(sample_file)
        results = test92.solve_part2()
        self.assertEqual(results,part2_sample_answer)
        
