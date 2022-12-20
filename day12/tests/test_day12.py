"""
Test Cases for Day12
"""
# pylint: disable=C0104, E0602, W0602
import random
from os.path import isfile
from unittest import TestCase
import unittest.mock as u
from day12 import *
from config_day12 import *



class TestDay12(TestCase):
    """ Test Cases for Day 12 Advent of Code """
    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        global dummy_input_file, sample_file, full_file
        global sample_file_line_count, part1_sample_answer, part2_sample_answer

        # -- input file setup
        dummy_input_file = "foo.file"
        full_file = FULL_FILE
        sample_file = SAMPLE_FILE

        # verified data
        sample_file_line_count = 7
        part1_sample_answer = 10
        part2_sample_answer = 0

    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_class_setup(self):
        """ Testing nosetest class setup"""
        self.assertTrue(isfile(full_file))
        self.assertTrue(isfile(sample_file))

    def test_day12_object_creation(self):
        """ Test day12 object creation"""
        test01=Day12()
        self.assertIsInstance(test01,Day12)
        #-------------------------------------
        test02=Day12(dummy_input_file)
        self.assertIsInstance(test02,Day12)
        self.assertEqual(dummy_input_file,test02.input_file)
        #-------------------------------------
        test03=Day12(sample_file)
        self.assertIsInstance(test03,Day12)


    def test_load_from_file(self):
        """ Testing load_data_from_file() """
        test10=Day12()
        self.assertRaises(TypeError,test10.load_data_from_file,dummy_input_file)

        test11=Day12(sample_file)
        self.assertEqual(sample_file_line_count,len(test11.input_data))


    def test_build_cave_list(self):
        """ Testing build_cave_list() """
        test_list = ['ABE-betty','betty-CARLA','CARLA-dave']
        test20=Day12()

        #-- should build a list of 4 caves
        test20.build_cave_list(test_list)
        expected_len = 4
        test_len = len(test20.cave_list)
        self.assertEqual(expected_len, test_len)

        #-- cave "ABE" should have a single connection "betty"
        idx=test20.get_cave_index_by_name('ABE')
        expected_result="betty"
        test_result=test20.cave_list[idx].connects_to[0]
        self.assertEqual(expected_result,test_result)

        expected_result = 1
        test_result = len(test20.cave_list[idx].connects_to)
        self.assertEqual(expected_result,test_result)


    def test_get_cave_index_by_name(self):
        """ Testing get_cave_index_by_name() """
        #--data setup for test
        data=[Cave('foo'),Cave('bar'),Cave('baz'),Cave('bat')]
        test_idx = random.randrange(0,len(data))
        test_name = data[test_idx].name

        with u.patch('day12.Day12.build_cave_list', return_value = data):
            test30=Day12(sample_file)
            result_idx = test30.get_cave_index_by_name(test_name)
        self.assertEqual(test_idx, result_idx)


    def test_build_cave_paths_pt1(self):
        """ Testing build_cave_paths_pt1() """
        
        

    def test_get_answer_key(self):
        """ Testing get_answer_key() """
        test90 = Day12()
        test_result = test90.get_answer_key()
        self.assertIsInstance(test_result,dict)

        test91 = Day12(sample_file)
        results = test91.solve_part1()
        self.assertEqual(results,part1_sample_answer)

        test92 = Day12(sample_file)
        results = test92.solve_part2()
        self.assertEqual(results,part2_sample_answer)

    def test_Cave_creation(self):
        """ Creating Cave objects """
        test100=Cave("sm")
        self.assertIsInstance(test100,Cave)
        self.assertEqual("sm",test100.name)

        test_result = repr(test100)
        self.assertEqual("sm",test_result)

        test101=Cave("XS")
        self.assertIsInstance(test101,Cave)
        self.assertEqual("XS",test101.name)

        test102=Cave("foo")
        self.assertEqual("foo",test102.get_name())

    def test_Cave_connections(self):
        """ Creating Cave connections """
        test110=Cave("A")
        self.assertIsInstance(test110.connects_to, list)
        self.assertEqual(0,len(test110.connects_to))

        test110.add_connection('foo')
        self.assertEqual(1,len(test110.connects_to))

        #--get_connections() test
        test_result = test110.get_connections()
        self.assertIsInstance(test_result, list)
        self.assertEqual(1,len(test_result))
        self.assertEqual('foo',test_result[0])

        test110.add_connection('Bar')
        test110.add_connection('foo')
        test110.add_connection('Bar')
        self.assertEqual(2,len(test110.connects_to))

        test111=Cave("foo", connection="bar")
        self.assertEqual(1,len(test111.connects_to))
        self.assertEqual("bar",test111.connects_to[0])

        test112=Cave("foo", connection=["bar","baz"])
        self.assertEqual(2,len(test112.connects_to))
        self.assertTrue("baz" in test112.connects_to)



