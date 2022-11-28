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
        global dummy_input_file, sample_file, full_file
        global sample_file_count, sample_file_freqs
        
        # -- input file setup        
        dummy_input_file = "foo.file"
        full_file = FULL_FILE
        sample_file = SAMPLE_FILE
        
        # verified data
        sample_file_count = 50
        sample_file_freqs = {1: 37, 2: 3, 3: 4, 4: 4, 5: 2}

    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_class_setup(self):
        """ Testing nosetest class setup"""
        self.assertTrue(isfile(full_file))
        self.assertTrue(isfile(sample_file))
        
        test00 = Day6(sample_file)
        self.assertEqual(len(test00.starting_fish),sample_file_count)
        self.assertEqual(len(test00.fish_status),len(sample_file_freqs))
        #-------------------------------------
        # -- get random key in status dict and compare to the known data
        key_num = random.randrange(0,len(test00.fish_status))
        # don't use this on large dicts
        random_key = list(test00.fish_status)[key_num]
        expected_result = sample_file_freqs[random_key]
        actual_result = sample_file_freqs[random_key]
        self.assertEqual(expected_result,actual_result)

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
        # -------------------------------------     


    def test_load_fish_from_file(self):
        """ Testing load_fish_from_file() """
        test11=Day6(dummy_input_file)
        self.assertRaises(TypeError,test11.load_fish_from_file,dummy_input_file)
        
        test12=Day6(sample_file)
        expected_result = sample_file_count
        actual_result = len(test12.starting_fish)
        self.assertEqual(expected_result,actual_result)
        self.assertEqual(expected_result,test12.total_fish_count)
        
        test13=Day6()
        self.assertEqual(0,len(test13.starting_fish))
        self.assertEqual(0,test13.total_fish_count)
    
    def test_initialize_fish_status(self):
        """ Testing the fish status tracker """
        test21=Day6(sample_file)
        pass
        #raise ValueError("+++TODO: implement the initialize_fish_status test here")

