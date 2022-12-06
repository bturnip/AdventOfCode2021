"""
Test Cases for Day9
"""
# pylint: disable=C0104, E0602, W0602
from os.path import isfile
from unittest import TestCase
from day9 import *
from config_day9 import *
import random

class TestDay9(TestCase):
    """ Test Cases for Day 9 Advent of Code """
    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        global dummy_input_file, sample_file, full_file
        global sample_file_line_count, sample_pt1_answer
        
        # -- input file setup        
        dummy_input_file = "foo.file"
        full_file = FULL_FILE
        sample_file = SAMPLE_FILE
        
        # verified data
        sample_file_line_count = 5
        sample_pt1_answer = 15
        

    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_class_setup(self):
        """ Testing nosetest class setup"""
        self.assertTrue(isfile(full_file))
        self.assertTrue(isfile(sample_file))

    def test_day9_object_creation(self):
        """ Test day9 object creation"""
        test01=Day9()
        self.assertIsInstance(test01,object)
        #-------------------------------------
        test02=Day9(dummy_input_file)
        self.assertIsInstance(test02,object)
        self.assertEqual(dummy_input_file,test02.input_file)
        #-------------------------------------
        test03=Day9(sample_file)
        self.assertIsInstance(test03,object)
        # -------------------------------------     

    def test_load_from_file(self):
        """ Testing input file load """
        test10 = Day9(SAMPLE_FILE)
        test_result = len(test10.heightmap)
        self.assertEqual(sample_file_line_count,test_result)
        #sample file should have been loaded into 2D numpy array size=50
        self.assertEqual(50,test10.heightmap.size)
        self.assertEqual(2,test10.heightmap.ndim)
        
        test11=Day9()
        self.assertRaises(TypeError,test11.load_data_from_file,dummy_input_file)

    def test_set_low_point_coords(self):
        """ Testing set_low_point_coords() """
        #--an empty object should return an empty dict
        test21 = Day9()
        self.assertEqual(0,test21.heightmap.size)
        test_result= test21.set_low_point_coords()
        self.assertIsInstance(test_result,dict)
        self.assertEqual(len(test21.low_point_coords),0)
        
        #--testing the first row of the sample file should load two
        #  sets of coords in the low_point_coords dict
        #  dict should be:
        #  {(0,1):1, (0,9):0}
        test22 = Day9(SAMPLE_FILE)
        test22.set_low_point_coords()
        test_result = test22.low_point_coords
        self.assertIsInstance(test_result,dict)
        self.assertEqual(test_result[(0,1)],1)
        self.assertEqual(test_result[(0,9)],0)

    def test_solve_part1 (self):
        """ Testing solve_part1() """
        test31 = Day9(SAMPLE_FILE)
        test31.set_low_point_coords()
        test_result = test31.solve_part1()
        self.assertIsInstance(test_result, dict)
        
        #--test result looks like:
        #  answer_key["part 1"] = Low point risk level sum:[{nn}]
        #  extract and test just the "nn" numeric result
        foo = test_result["part 1"].split(":")[1]
        bar = int(foo.replace('[','').replace(']',''))
        self.assertEqual(bar,sample_pt1_answer )
        
        
    def test_get_answer_key(self):
        """ Testing get_answer_key() """
        test90 = Day9()
        test_result = test90.get_answer_key()
        self.assertIsInstance(test_result,dict)
    
    def test_map_basins(self):
        """ Testing maps_basins() """
        test41 = Day9()
        test_result = test41.map_basins()
        self.assertEqual(0,len(test_result))
        self.assertIsInstance(test_result, set)
        
        
        
        
        
        
