"""
Test Cases for Day13
"""
# pylint: disable=C0104, E0602, W0602
from os.path import isfile
from unittest import TestCase
from day13 import *
from config_day13 import *
import random

class TestDay13(TestCase):
    """ Test Cases for Day 13 Advent of Code """
    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        global dummy_input_file, sample_file, full_file
        global sample_fold_instructions, sample_sheet_shape,sample_sheet_starting_coords
        global sample_file_line_count, part1_sample_answer, part2_sample_answer

        # -- input file setup
        dummy_input_file = "foo.file"
        full_file = FULL_FILE
        sample_file = SAMPLE_FILE

        # verified data
        sample_file_line_count = 0 #TODO
        part1_sample_answer = 0 #TODO
        part2_sample_answer = 0 #TODO
        sample_fold_instructions = ['y=7','x=5']
        sample_sheet_shape = (15,11)
        sample_sheet_starting_coords = ['6,10', '0,14', '9,10', '0,3'
                                        ,'10,4', '4,11', '6,0', '6,12'
                                        ,'4,1', '0,13', '10,12', '3,4'
                                        ,'3,0', '8,4', '1,10', '2,14'
                                        ,'8,10', '9,0']

    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_class_setup(self):
        """ Testing nosetest class setup"""
        self.assertTrue(isfile(full_file))
        self.assertTrue(isfile(sample_file))

    def test_day13_object_creation(self):
        """ Test day13 object creation"""
        test01=Day13()
        self.assertIsInstance(test01,Day13)
        #-------------------------------------
        test02=Day13(dummy_input_file)
        self.assertIsInstance(test02,Day13)
        self.assertEqual(dummy_input_file,test02.input_file)
        #-------------------------------------
        test03=Day13(sample_file)
        self.assertIsInstance(test03,Day13)
        # -------------------------------------


    def test_load_fold_instructions_from_file(self):
        """ Testing load_fold_instructions_from_file() """
        test10=Day13()
        self.assertRaises(TypeError,test10.load_fold_instructions_from_file,dummy_input_file)

        #--test that a list of fold directions is created
        test10.load_fold_instructions_from_file(SAMPLE_FILE)
        for this_instr in sample_fold_instructions:
            self.assertTrue(this_instr in test10.fold_instructions)


    def test_load_whole_sheet_from_file(self):
        """ Testing load_whole_sheet_from_file() """
        test20 = Day13()
        test20.load_whole_sheet_from_file(SAMPLE_FILE)
        self.assertEqual(sample_sheet_shape, test20.whole_sheet.shape)
        
        #--test a few random values from the sample file, expected
        #  result is that each coord tested returns a 1
        for i in range (0,3):
            rand_idx = random.randrange(0,len(sample_sheet_starting_coords))
            x,y = sample_sheet_starting_coords[rand_idx].split(',')
            rand_coord =(int(y),int(x))
            self.assertEqual(1,test20.whole_sheet[rand_coord])
        

    def test_fold_horizontal(self):
        """ Testing folding on the y axis """
        test30 = Day13(SAMPLE_FILE)
        fold_instruction = 'y=7'
        test30.fold(fold_instruction)
        expected_shape =(7,11)
        self.assertEqual(expected_shape,test30.folded_sheet.shape)
        
        test31 = Day13(SAMPLE_FILE)
        self.assertRaises(TypeError,test31.fold(7))
        
    def test_get_answer_key(self):
        """ Testing get_answer_key() """
        test90 = Day13()
        test_result = test90.get_answer_key()
        self.assertIsInstance(test_result,dict)

        test91 = Day13(sample_file)
        results = test91.solve_part1()
        self.assertEqual(results,part1_sample_answer)

        test92 = Day13(sample_file)
        results = test92.solve_part2()
        self.assertEqual(results,part2_sample_answer)

