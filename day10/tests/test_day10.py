"""
Test Cases for Day10
"""
# pylint: disable=C0104, E0602, W0602
from os.path import isfile
from unittest import TestCase
from day10 import *
from config_day10 import *
import random

class TestDay10(TestCase):
    """ Test Cases for Day 10 Advent of Code """
    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        global dummy_input_file, sample_file, full_file
        global sample_file_line_count
        
        # -- input file setup        
        dummy_input_file = "foo.file"
        full_file = FULL_FILE
        sample_file = SAMPLE_FILE
        
        # verified data
        sample_file_line_count = 10

    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_class_setup(self):
        """ Testing nosetest class setup"""
        self.assertTrue(isfile(full_file))
        self.assertTrue(isfile(sample_file))

    def test_day10_object_creation(self):
        """ Test day10 object creation"""
        test01=Day10()
        self.assertIsInstance(test01,object)
        #-------------------------------------
        test02=Day10(dummy_input_file)
        self.assertIsInstance(test02,object)
        self.assertEqual(dummy_input_file,test02.input_file)
        #-------------------------------------
        test03=Day10(sample_file)
        self.assertIsInstance(test02,object)
        # -------------------------------------     


    def test_load_from_file(self):
        """ Testing load_data_from_file() """
        test10=Day10(sample_file)
        test_result = len(test10.input_data)
        self.assertEqual(test_result, sample_file_line_count)
        
    
    
    def test_get_answer_key(self):
        """ Testing get_answer_key() """
        test90 = Day10()
        test_result = test90.get_answer_key()
        self.assertIsInstance(test_result,dict)
