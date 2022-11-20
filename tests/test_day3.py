"""
Test Cases for Day3
"""
# pylint: disable=C0104, E0602
import sys

sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day3')
from unittest import TestCase
import numpy as np
from day3 import *



class TestDay3(TestCase):
    """ Test Cases for Day 3 Advent of Code """
    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_create_2D_numpy_array_bad_input(self):
        """ Test create_2D_numpy_array() with bad input """
        foo = "I'm a string, not a list"
        self.assertRaises(ValueError,create_2D_numpy_array,foo)

        bar = []
        self.assertRaises(ValueError,create_2D_numpy_array,bar)

    def test_create_2D_numpy_array(self):
        """ Test creation of 2D numpy array """
        foo = ['12345','12345','12345','12345']
        expected_shape = (4,5)
        bar = create_2D_numpy_array(foo)

        self.assertIsInstance(bar,np.ndarray)
        self.assertEqual(expected_shape, bar.shape)

    def test_calculate_aoc_day3_bad_data(self):
        """ Test calculate_aoc_day3() with bad data"""
        # send a 2d list instead of numpy array
        wrong_type_foo = [[x] for x in range(10)]
        empty_foo = np.array([])
        bad_data_foo = np.array([[1,0,1],[1,0,0],[1,0,0],[1,1,9]])

        self.assertRaises(ValueError,calculate_aoc_day3,wrong_type_foo)
        self.assertRaises(ValueError,calculate_aoc_day3,empty_foo)
        self.assertRaises(ValueError,calculate_aoc_day3,bad_data_foo)

        bar = np.array([])
        self.assertRaises(ValueError,calculate_aoc_day3,bar)

    def test_calculate_aoc_day3_gamma_only(self):
        """ Test gamma rate calculation only """
        foo = ['111','000','110']
        expected_gamma = '110'
        bar = create_2D_numpy_array(foo)

        baz = calculate_aoc_day3(bar)
        self.assertEqual(expected_gamma, baz["gamma"])

    def test_calculate_aoc_day3(self):
        """ Test gamma and epsilon rate calculation """
        foo = ['111','000','110']
        expected_gamma = '110'
        expected_epsilon = '001'
        bar = create_2D_numpy_array(foo)

        baz = calculate_aoc_day3(bar)
        self.assertEqual(expected_gamma, baz["gamma"])
        self.assertEqual(expected_epsilon,baz["epsilon"])

    def test_calculate_aoc_day3_binary_conversion(self):
        """ Test conversion of binary rates to ints"""
        foo = ['111','000','110']
        expected_gamma = 6   #'110'
        expected_epsilon = 1 #'001'

        bar = create_2D_numpy_array(foo)
        baz = calculate_aoc_day3(bar)
        self.assertEqual(expected_gamma, baz["gamma_int"])
        self.assertEqual(expected_epsilon,baz["epsilon_int"])

    def test_calculate_gamma_and_espilon_power_consumption(self):
        """ Test power consumption calculation """
        foo = ['111','000','110']
        expected_gamma = 6   #'110'
        expected_epsilon = 1 #'001'
        expected_power_consumption = 6 #(6*1 = 6)

        bar = create_2D_numpy_array(foo)
        baz = calculate_aoc_day3(bar)
        self.assertEqual(expected_power_consumption, baz["power_consumption"])

    def test_calculate_power_consumption_bad_input(self):
        """ Test calculate_power_consumption with bad input """
        bad_input_type = "I'm a string, not a dict!"
        empty_input = {}
        too_small_input = {"a":1,}

        bad_keys1 = {"x":1, "epsilon":2}
        bad_keys2 = {"gamma":1, "y":2}

        self.assertRaises(ValueError,calculate_power_consumption,bad_input_type)
        self.assertRaises(ValueError,calculate_power_consumption,empty_input)
        self.assertRaises(ValueError,calculate_power_consumption,too_small_input)

        self.assertRaises(ValueError,calculate_power_consumption,bad_keys1)
        self.assertRaises(ValueError,calculate_power_consumption,bad_keys2)

    def test_calculate_power_consumption_dummy(self):
        """ test the stubbed return value for calculate_power_consumption() """
        self.assertEqual(0,calculate_power_consumption({"gamma":1, "epsilon":2}))

    def test_calculate_aoc_day3_pt2(self):
        """ Test calculate_aoc_day3_pt2() """
        dummy_dict={}

        wrong_type_foo = [[x] for x in range(10)]
        empty_foo = np.array([])
        bad_data_foo = np.array([[1,0,1],[1,0,0],[1,0,0],[1,1,9]])

        self.assertRaises(ValueError,calculate_aoc_day3_pt2,wrong_type_foo,dummy_dict)
        self.assertRaises(ValueError,calculate_aoc_day3_pt2,empty_foo,dummy_dict)
        self.assertRaises(ValueError,calculate_aoc_day3_pt2,bad_data_foo,dummy_dict)

    def test_calculate_aoc_day3_pt2_good_data(self):
        """ Test calculate_aoc_day3_pt2() with known data """
        dummy_dict={}
        expected_oxygen_generation = '110011110011'
        expected_oxygen_generation_int = 3315
        expected_co2_scrubber = '011011110010'
        expected_co2_scrubber_int = 1778
        expected_life_support =  5894070

        #set up
        this_file = '/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day3/sample3.txt'
        this_data = load_input_file_into_list(this_file, strip_newline = True)
        test_arr = create_2D_numpy_array(this_data)

        results_dict = calculate_aoc_day3_pt2(test_arr,dummy_dict)

        self.assertIsInstance(results_dict,dict)
        self.assertEqual(expected_oxygen_generation,results_dict["oxygen_generation"])
        self.assertEqual(expected_oxygen_generation_int,results_dict["oxygen_generation_int"])
        self.assertEqual(expected_co2_scrubber,results_dict["co2_scrubber"])
        self.assertEqual(expected_co2_scrubber_int,results_dict["co2_scrubber_int"])
        self.assertEqual(expected_life_support,results_dict["life_support"])









