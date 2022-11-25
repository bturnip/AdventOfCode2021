"""
Test Cases for Day5
"""
# pylint: disable=C0104, E0602, W0602
from os.path import isfile
from unittest import TestCase
from day5 import *
from config_day5 import *
import random

class TestDay5(TestCase):
    """ Test Cases for Day 5 Advent of Code """
    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        global dummy_input_file, ten_line_sample_file, full_file
        global test_vent_coords
        
        # -- input file setup        
        dummy_input_file = "foo.file"
        full_file = FULL_FILE
        ten_line_sample_file = TEN_LINE_SAMPLE
        
        # -- known data for test Day5.vent_coords
        # extracted from ten_line_sample_file
        test_vent_coords = np.array([
            [777,778,777,676]
            ,[500,510,378,510]
            ,[441,657,441,638]
            ,[724,480,724,778]
            ,[702,85,44,85]
            ,[973,961,28,16]
            ,[913,125,483,125]
            ,[714,895,870,739]
            ,[273,774,273,795]
            ,[623,450,623,616]
            ])


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
        
        test14=Day5(ten_line_sample_file)
        self.assertEqual(np.sum(test_vent_coords),np.sum(test14.vent_coords))
        self.assertEqual(test_vent_coords.shape, test14.vent_coords.shape)
        self.assertEqual(test_vent_coords.ndim,test14.vent_coords.ndim)
        
        random_row = random.randrange(0,len(test14.vent_coords))
        for r in range(len(test_vent_coords[random_row])):
            self.assertEqual(test_vent_coords[random_row][r]
                             ,test14.vent_coords[random_row][r])

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
        
        
        
        

