"""
Test Cases for Day14
"""
# pylint: disable=C0104, E0602, W0602
from os.path import isfile
from unittest import TestCase, skip
from day14 import *
from config_day14 import *
import random

class TestDay14(TestCase):
    """ Test Cases for Day 14 Advent of Code """
    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        global dummy_input_file, sample_file, full_file
        global sample_rules, part1_sample_answer, part2_sample_answer

        # -- input file setup
        dummy_input_file = "foo.file"
        full_file = FULL_FILE
        sample_file = SAMPLE_FILE

        # verified data
        sample_rules = {'CH': 'B', 'HH': 'N', 'CB': 'H', 'NH': 'C'
                        ,'HB': 'C', 'HC': 'B', 'HN': 'C', 'NN': 'C'
                        ,'BH': 'H', 'NC': 'B', 'NB': 'B', 'BN': 'B'
                        ,'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C'}

        part1_sample_answer = 1588
        part2_sample_answer = 0

    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_class_setup(self):
        """ Testing nosetest class setup"""
        self.assertTrue(isfile(full_file))
        self.assertTrue(isfile(sample_file))

    def test_day14_object_creation(self):
        """ Test day14 object creation"""
        test01=Day14()
        self.assertIsInstance(test01,Day14)
        #-------------------------------------
        test02=Day14(dummy_input_file)
        self.assertIsInstance(test02,Day14)
        self.assertEqual(dummy_input_file,test02.input_file)
        #-------------------------------------
        test03=Day14(sample_file)
        self.assertIsInstance(test03,Day14)
        # -------------------------------------


    def test_load_from_file(self):
        """ Testing load_data_from_file() """
        test10=Day14()
        self.assertRaises(TypeError,test10.load_data_from_file,dummy_input_file)

        test11=Day14(SAMPLE_FILE)
        expected_polymer_template = 'NNCB'
        self.assertEqual(expected_polymer_template,test11.polymer_template)
        
        #--test a random dict values
        key,val = random.choice(list(test11.insertion_rules.items()))
        self.assertEqual(test11.insertion_rules[key],val)
    
    def test_process_polymer(self):
        """ Testing process_polymer()"""
        test20 = Day14(SAMPLE_FILE)
        step1_polymer = "NCNBCHB"
        #--run 1 step of polymerization
        test20.process_polymer(1)
        self.assertEqual(step1_polymer,test20.polymer)
        
        test21 = Day14(SAMPLE_FILE)
        step4_polymer="NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
        #--run 4 steps of polymerization
        test21.process_polymer(4)
        self.assertEqual(step1_polymer,test21.polymer)
        


    @skip("Skipping answer testing")
    def test_get_answer_key(self):
        """ Testing get_answer_key() """
        test90 = Day14()
        test_result = test90.get_answer_key()
        self.assertIsInstance(test_result,dict)

        test91 = Day14(sample_file)
        results = test91.solve_part1()
        self.assertEqual(results,part1_sample_answer)

        test92 = Day14(sample_file)
        results = test92.solve_part2()
        self.assertEqual(results,part2_sample_answer)

