"""
Test Cases for Day4
"""
# pylint: disable=C0104, E0602, W0602
from unittest import TestCase
import sys
import numpy as np

sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day4')

from day4 import *


dummy_input_file = "foo"

day4_path = "/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/day4"

sample_input_draws =[]
sample_bingo_cards =[]

sample_input_file  = f"{day4_path}/day4_raw_sample.txt"
sample_file_winner = f"{day4_path}/day4_raw_sample_winner.txt"
real_input_file    = f"{day4_path}/day4_raw_input.txt"

class TestDay4(TestCase):
    """ Test Cases for Day 4 Advent of Code """
    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        # these values sync up with what is in the sample_input_file
        # listed above
        global sample_bingo_cards,sample_input_draws
        global y,z,r,c # specific bingo cards
        sample_input_draws = [14,30,18,8,3,52]

        y = np.array([ ['13','62','38','10','41']
                      ,['93','59','60','74','75']
                      ,['79','18','57','90','28']
                      ,['56','76','34','96','84']
                      ,['78','42','69','14','19']])

        z= np.array([ ['26','70','3','5','89']
                     ,['94','49','35','43','99']
                     ,['82','36','62','78','37']
                     ,['90','73','9','38','40']
                     ,['60','68','8','2','53']])

        # row winner(last row) with sample_input_draws
        r = np.array([ ['13','62','38','10','41']
                      ,['93','59','60','74','75']
                      ,['79','18','57','90','28']
                      ,['56','76','34','96','84']
                      ,['8','30','18','14','52']])
        # col winner (last col) with sample_input_draws
        c = np.array([ ['13','62','38','10','14']
                      ,['93','59','60','74','30']
                      ,['79','18','57','90','18']
                      ,['56','76','34','96','3']
                      ,['60','68','48','12','52']])

        sample_bingo_cards.append(y)
        sample_bingo_cards.append(z)

    def test_test(self):
        """ Dummy Test to test nosetests"""
        self.assertEqual(1,1)

    def test_day4_object_creation(self):
        """ Test Day4 object creation"""
        test01=Day4()
        self.assertIsInstance(test01,object)
        #-------------------------------------
        test02=Day4(dummy_input_file)
        self.assertIsInstance(test02,object)
        self.assertEqual(dummy_input_file,test02.input_file)
        #-------------------------------------
        test03=Day4(real_input_file)
        self.assertIsInstance(test03,object)
        self.assertEqual(real_input_file,test03.input_file)
        #-------------------------------------
        test04=Day4(sample_input_file)
        self.assertEqual(sample_input_draws,test04.bingo_draws)
        #-------------------------------------
        test05=Day4(sample_file_winner)
        self.assertIsInstance(test05,object)

    def test_set_bingo_draws(self):
        """ Test setting the bingo draws """
        single_val = random.randrange(0,100)
        test10=Day4()
        test10.set_bingo_draws(single_val)
        self.assertEqual([single_val],test10.bingo_draws)
        #-------------------------------------
        input_values = ["Random","RANDOM","random"]
        for i in input_values:
            test11=Day4()
            self.assertEqual(0,len(test11.bingo_draws))
            test11.set_bingo_draws(i)
            self.assertEqual(100,len(test11.bingo_draws))
            self.assertNotEqual(list(range(100)),test11.bingo_draws)
        #-------------------------------------
        test12=Day4()
        self.assertEqual([],test12.bingo_draws)
        test12.set_bingo_draws(sample_input_draws)
        self.assertEqual(sample_input_draws,test12.bingo_draws)

        #-------------------------------------
        bad_input_vals = [{1:2,3:4}, 123.45, "foo", "randommmm"]

        for bad_i in bad_input_vals:
            test13=Day4()
            self.assertRaises(TypeError
                              ,test13.set_bingo_draws
                              ,bad_i)
        #-------------------------------------
        test14=Day4()
        test14.set_bingo_draws(sample_input_file)
        self.assertEqual(sample_input_draws
                         ,test14.bingo_draws)

    def test_load_bingo_draws_from_file(self):
        """ Test loading bingo_draws from an input file """
        test20=Day4(sample_input_file)
        test20.load_bingo_draws_from_file(sample_input_file)
        self.assertEqual(sample_input_draws,test20.bingo_draws)
        #-------------------------------------
        test21=Day4()
        self.assertRaises(TypeError
                          ,test21.load_bingo_draws_from_file
                          ,dummy_input_file)

    def test_load_bingo_cards_from_file(self):
        """ Test loading bingo_cards from an input file """

        #-----------------------------------------
        test30=Day4()

        self.assertRaises(TypeError
                          ,test30.load_bingo_cards_from_file
                          ,dummy_input_file)
        #-----------------------------------------
        test31=Day4()

        # starting with empty value?
        self.assertEqual([],test31.bingo_cards)

        # call method to load cards from known sample file
        test31.load_bingo_cards_from_file(sample_input_file)

        # correct number of cards?
        self.assertEqual(2,len(test31.bingo_cards))

        # each card is correct type?
        for this_card in test31.bingo_cards:
            self.assertIsInstance(this_card,np.ndarray)

        # test random card against known data
        test_index = random.randrange(0,len(test31.bingo_cards))

        expected = sample_bingo_cards[test_index]
        actual = test31.bingo_cards[test_index]

        self.assertTrue(np.array_equal(expected,actual))

        #-----------------------------------------
        test32=Day4(sample_input_file)
        # each card is correct type?
        for this_card in test32.bingo_cards:
            self.assertIsInstance(this_card,np.ndarray)

        # correct number of cards?
        self.assertEqual(2,len(test32.bingo_cards))

        # test random card against known data
        test_index = random.randrange(0,len(test32.bingo_cards))

        expected = sample_bingo_cards[test_index]
        actual = test32.bingo_cards[test_index]

        self.assertTrue(np.array_equal(sample_bingo_cards[test_index]
                                       ,test32.bingo_cards[test_index]))
        #-----------------------------------------

    def test_score_all_cards(self):
        """ Test scoring the deck of bingo cards """

        test40=Day4()
        # test empty bingo_draws will cause ValueError on pick function
        self.assertEqual([],test40.bingo_draws)
        self.assertRaises(ValueError,test40.score_all_cards)

        # test empty bingo_cards will cause ValueError on pick function
        test40.load_bingo_draws_from_file(sample_file_winner)
        self.assertEqual(sample_input_draws,test40.bingo_draws)
        self.assertEqual([],test40.bingo_cards)
        self.assertRaises(ValueError,test40.score_all_cards)

    def test_mark_bingo_card(self):
        """ Test marking the bingo cards"""
        
        # -- test with known data (winning row)
        test50=Day4()
        test50.set_bingo_draws(sample_input_draws)
        self.assertEqual(sample_input_draws,test50.bingo_draws)
        
        # for bingo card r the last row has 5 marks
        expected_result = ['X','X','X','X','X']

        test50.bingo_cards.append(r)
        test50.score_all_cards() # call to have the cards marked
        
        test_result = list(test50.bingo_cards[0][4])
        self.assertEqual(expected_result,test_result)
        
        # -- test with known data (winning col)
        test51=Day4()
        test51.set_bingo_draws(sample_input_draws)
        
        # for bingo card c the last column has 5 marks
        expected_result = ['X','X','X','X','X']
        
        test51.bingo_cards.append(c)
        test51.score_all_cards()
        
        test_result= list(test51.bingo_cards[0][:,4])
        self.assertEqual(expected_result,test_result)
        
        # -- test with known data (non-winner)
        test52=Day4()
        test52.set_bingo_draws(sample_input_draws)
        
        # for bingo card y there are only 2 marks on the card
        expected_result = 2
        
        test52.bingo_cards.append(y)
        test52.score_all_cards()
        test_result=(np.count_nonzero(test52.bingo_cards[0] == 'X'))
        self.assertEqual(expected_result, test_result)

    def test_check_for_win(self):
        """ Test checking for winning card """
        #test60=Day4()
    
    def test_stats(self):
        """ Test the stat calculation and recording """
        test70=Day4(sample_file_winner)
        test70.score_all_cards()
        
        num_stats = len(test70.bingo_card_stats)
        num_cards = len(test70.bingo_cards)
        self.assertEqual(num_stats,num_cards)
        #-----------------------------------------
        # card 2 known stats
        # unmarked_sum = 1099
        # last_draw = 52
        # pt1 score = 571148
        
        



