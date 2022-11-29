"""
Test Cases for Day7
"""
# pylint: disable=C0104, E0602, W0602
from os.path import isfile
from unittest import TestCase
from day7 import *
from config_day7 import *
import random

class TestDay7(TestCase):
    """ Test Cases for Day 7 Advent of Code """
    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        global dummy_input_file, sample_file, full_file
        global sample_record_count
        
        # -- input file setup        
        dummy_input_file = "foo.file"
        full_file = FULL_FILE
        sample_file = SAMPLE_FILE
        
        # verified data
        sample_record_count=108
        

    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_class_setup(self):
        """ Testing nosetest class setup"""
        self.assertTrue(isfile(full_file))
        self.assertTrue(isfile(sample_file))

    def test_day7_object_creation(self):
        """ Test day7 object creation"""
        test01=Day7()
        self.assertIsInstance(test01,object)
        #-------------------------------------
        test02=Day7(dummy_input_file)
        self.assertIsInstance(test02,object)
        self.assertEqual(dummy_input_file,test02.input_file)
        #-------------------------------------
        test03=Day7(sample_file)
        self.assertIsInstance(test02,object)
        # -------------------------------------     

    def test_load_from_file(self):
        """ Testing load_data_from_file() """
        test11=Day7(sample_file)
        expected_value=sample_record_count
        test_value = len(test11.starting_crabs)
        
        test12=Day7()
        self.assertRaises(TypeError,test12.load_data_from_file,dummy_input_file)

    def test_get_answer_key(self):
        test21=Day7()
        self.assertIsInstance(test21.answer_key,dict)
        self.assertEqual(0,len(test21.answer_key))
        
