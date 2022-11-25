"""
Test Cases for Day5
"""
# pylint: disable=C0104, E0602, W0602
from os.path import isfile
from unittest import TestCase
from day5 import *
from config_day5 import *

class TestDay5(TestCase):
    """ Test Cases for Day 5 Advent of Code """
    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        global dummy_input_file, ten_line_sample_file, full_file
        
        # -- input file setup        
        dummy_input_file = "foo.file"
        full_file = FULL_FILE
        ten_line_sample_file = TEN_LINE_SAMPLE

    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_class_setup(self):
        """ Testing nosetest class setup"""
        self.assertTrue(isfile(full_file))
        self.assertTrue(isfile(ten_line_sample_file))

    def test_day5_object_creation(self):
        """ Test Day5 object creation"""
        test01=Day5()
        self.assertIsInstance(test01,object)
        #-------------------------------------
        test02=Day5(dummy_input_file)
        self.assertIsInstance(test02,object)
        self.assertEqual(dummy_input_file,test02.input_file)
        #-------------------------------------
        test03=Day5(ten_line_sample_file)
        self.assertIsInstance(test02,object)

    def test_load_all_coords_from_file(self):
        """ Testing load_all_coords_from_file() """
        test11=Day5(dummy_input_file)
        self.assertRaises(TypeError,test11.load_all_coords_from_file,dummy_input_file)
        
        test12=Day5(ten_line_sample_file)
        expected_result = 10
        actual_result = len(test12.vent_coords)
        self.assertEqual(expected_result,actual_result)
        
        test13=Day5()
        self.assertEqual(0,len(test13.vent_coords))
        test13.load_all_coords_from_file(ten_line_sample_file)

    def test_get_all_coords(self):
        """ Testing get_all_coords() """
        dummy_inputs=['',dummy_input_file]
        
        for this_test in dummy_inputs:
            test21=Day5(this_test)
            test_result = test21.get_all_coords()
            self.assertIsInstance(test_result,list)
        
        test22=Day5(ten_line_sample_file)
        test_result = test22.get_all_coords()
        self.assertIsInstance(test_result,np.ndarray)
        
        
        
        

