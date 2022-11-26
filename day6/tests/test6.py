"""
Test Cases for Day6
"""
# pylint: disable=C0104, E0602, W0602
from os.path import isfile
from unittest import TestCase
from day6 import *
from config_day6 import *
import random

class TestDay5(TestCase):
    """ Test Cases for Day 5 Advent of Code """
    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        global dummy_input_file, ten_line_sample_file, full_file
        
        # -- input file setup        
        dummy_input_file = "foo.file"
        full_file = FULL_FILE
        sample_file = SAMPLE_FILE

    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

