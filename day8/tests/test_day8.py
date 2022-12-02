"""
Test Cases for Day8
"""
# pylint: disable=C0104, E0602, W0602
from os.path import isfile
from unittest import TestCase
from day8 import *
from config_day8 import *
import random

class TestDay8(TestCase):
    """ Test Cases for Day 8 Advent of Code """
    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        global dummy_input_file, sample_file, full_file
        global sample_line_count
        global sample_val_L3_P0_C3,sample_val_L4_P1_C2
        global sample_val_L5_P0_C7,sample_val_L6_P1_C0 
        
        # -- input file setup        
        dummy_input_file = "foo.file"
        full_file = FULL_FILE
        sample_file = SAMPLE_FILE
        
        # verified data
        sample_line_count = 10
        # random values cherry picked from sample file
        # line 3, part 1, col 3
        sample_val_L3_P0_C3 = 'bgaef'
        sample_val_L4_P1_C2 = 'bdfgeca'
        sample_val_L5_P0_C7 = 'fbedcg'
        sample_val_L6_P1_C0 = 'dgbac'

    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_class_setup(self):
        """ Testing nosetest class setup"""
        self.assertTrue(isfile(full_file))
        self.assertTrue(isfile(sample_file))

    def test_day8_object_creation(self):
        """ Test day8 object creation"""
        test01=Day8()
        self.assertIsInstance(test01,object)
        #-------------------------------------
        test02=Day8(dummy_input_file)
        self.assertIsInstance(test02,object)
        self.assertEqual(dummy_input_file,test02.input_file)
        #-------------------------------------
        test03=Day8(sample_file)
        self.assertIsInstance(test02,object)
        # -------------------------------------     


    def test_load_from_file(self):
        """ Testing load_data_from_file() """
        test11=Day8(sample_file)
        test_result = len(test11.segment_observations)
        self.assertEqual(sample_line_count, test_result)
        
        test_result = test11.segment_observations[3][0][3]
        self.assertEqual(sample_val_L3_P0_C3,test_result)

        test_result = test11.segment_observations[4][1][2]
        self.assertEqual(sample_val_L4_P1_C2,test_result)

        test_result = test11.segment_observations[5][0][7]
        self.assertEqual(sample_val_L5_P0_C7,test_result)

        test_result = test11.segment_observations[6][1][0]
        self.assertEqual(sample_val_L6_P1_C0,test_result)

