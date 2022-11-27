"""
Test Cases for Day6
"""
# pylint: disable=C0104, E0602, W0602
from os.path import isfile
from unittest import TestCase
from day6 import *
from config_day6 import *
import random

class TestDay6(TestCase):
    """ Test Cases for Day 6 Advent of Code """
    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        global dummy_input_file, sample_file, full_file, sample_file_count
        
        # -- input file setup        
        dummy_input_file = "foo.file"
        full_file = FULL_FILE
        sample_file = SAMPLE_FILE
        sample_file_count = 50

    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_class_setup(self):
        """ Testing nosetest class setup"""
        self.assertTrue(isfile(full_file))
        
        self.assertTrue(isfile(sample_file))

    def test_day6_object_creation(self):
        """ Test Day6 object creation"""
        test01=Day6()
        self.assertIsInstance(test01,object)
        #-------------------------------------
        test02=Day6(dummy_input_file)
        self.assertIsInstance(test02,object)
        self.assertEqual(dummy_input_file,test02.input_file)
        #-------------------------------------
        test03=Day6(sample_file)
        self.assertIsInstance(test02,object)


    def test_load_fish_from_file(self):
        """ Testing load_fish_from_file() """
        test11=Day6(dummy_input_file)
        self.assertRaises(TypeError,test11.load_fish_from_file,dummy_input_file)
        
        test12=Day6(sample_file)
        expected_result = sample_file_count
        actual_result = len(test12.fish)
        self.assertEqual(expected_result,actual_result)
        
        test13=Day6()
        self.assertEqual(0,len(test13.fish))

