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
        
        # -- input file setup        
        dummy_input_file = "foo.file"
        full_file = FULL_FILE
        sample_file = SAMPLE_FILE
        
        # verified data
        #TODO

    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_class_setup(self):
        """ Testing nosetest class setup"""
        self.assertTrue(isfile(full_file))
        self.assertTrue(isfile(sample_file))

    def test_day7_object_creation(self):
        """ Test day7 object creation"""
        test01=day7()
        self.assertIsInstance(test01,object)
        #-------------------------------------
        test02=day7(dummy_input_file)
        self.assertIsInstance(test02,object)
        self.assertEqual(dummy_input_file,test02.input_file)
        #-------------------------------------
        test03=day7(sample_file)
        self.assertIsInstance(test02,object)
        # -------------------------------------     


    def test_load_from_file(self):
        """ Testing () """
        #TODO
        pass
