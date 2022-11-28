"""
Test Cases for Day{NUM}
"""
# pylint: disable=C0104, E0602, W0602
from os.path import isfile
from unittest import TestCase
from day{NUM} import *
from config_day{NUM} import *
import random

class Testday{NUM}(TestCase):
    """ Test Cases for Day {NUM} Advent of Code """
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

    def test_day{NUM}_object_creation(self):
        """ Test day{NUM} object creation"""
        test01=day{NUM}()
        self.assertIsInstance(test01,object)
        #-------------------------------------
        test02=day{NUM}(dummy_input_file)
        self.assertIsInstance(test02,object)
        self.assertEqual(dummy_input_file,test02.input_file)
        #-------------------------------------
        test03=day{NUM}(sample_file)
        self.assertIsInstance(test02,object)
        # -------------------------------------     


    def test_load_from_file(self):
        """ Testing () """
        #TODO
        pass
