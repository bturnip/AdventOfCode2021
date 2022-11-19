"""
Test Cases for Day3
"""
import sys
sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day3')
from day3 import *
from unittest import TestCase
import numpy as np


class testDay3(TestCase):
    """ Test Cases for Day 2 Advent of Code """
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

    def test_calculate_gamma_and_espilon_rate_bad_data(self):
        """ Test calculate_gamma_and_espilon_rate() with bad data"""
        # send a 2d list instead of numpy array
        foo = [[x] for x in range(10)]
        self.assertRaises(ValueError,calculate_gamma_and_espilon_rate,foo)

        bar = np.array([])
        self.assertRaises(ValueError,calculate_gamma_and_espilon_rate,bar)

    def test_calculate_gamma_and_espilon_rate_gamma_only(self):
        """ Test gamma rate calculation only """
        foo = ['111','000','110']
        expected_gamma = '110'
        bar = create_2D_numpy_array(foo)

        baz = calculate_gamma_and_espilon_rate(bar)
        self.assertEqual(expected_gamma, baz["gamma"])

    def test_calculate_gamma_and_espilon_rate(self):
        """ Test gamma and epsilon rate calculation """
        foo = ['111','000','110']
        expected_gamma = '110'
        expected_epsilon = '001'
        bar = create_2D_numpy_array(foo)

        baz = calculate_gamma_and_espilon_rate(bar)
        self.assertEqual(expected_gamma, baz["gamma"])
        self.assertEqual(expected_epsilon,baz["epsilon"])

    def test_calculate_gamma_and_espilon_rate_binary_conversion(self):
        """ Test conversion of binary rates to ints"""
        foo = ['111','000','110']
        expected_gamma = 6   #'110'
        expected_epsilon = 1 #'001'

        bar = create_2D_numpy_array(foo)
        baz = calculate_gamma_and_espilon_rate(bar)
        self.assertEqual(expected_gamma, baz["gamma_int"])
        self.assertEqual(expected_epsilon,baz["epsilon_int"])

    def test_calculate_gamma_and_espilon_power_consumption(self):
        """ Test power consumption calculation """
        foo = ['111','000','110']
        expected_gamma = 6   #'110'
        expected_epsilon = 1 #'001'
        expected_power_consumption = 6 #(6*1 = 6)

        bar = create_2D_numpy_array(foo)
        baz = calculate_gamma_and_espilon_rate(bar)
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


