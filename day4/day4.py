""" 2021 Advent of Code: Day 4"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=C0104, C0123, C0413, E0602, W0511
import sys
import random
from os.path import isfile

sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/advent_tools')
from advent_tools import *



class Day4(object):
    """ Object that contains the methods to compute/store
        the 2021 Advent Of Code puzzle for Day 4"""

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.valid_bingo_draw_keywords = ["random"]
        scored_cards = []
        self.best_card = None

        if input_file is not None and isfile(input_file):
            self.bingo_draws = self.load_bingo_draws_from_file(input_file)
            self.bingo_cards = self.load_bingo_cards_from_file(input_file)
        else:
            self.bingo_draws = []
            self.bingo_cards = []

    def set_bingo_draws(self,input_draws):
        """ set bingo_draws from list, single value integer, or keyword"""

        if type(input_draws) == list:
            self.bingo_draws = intify_list(input_draws)

        elif type(input_draws) == int:
            self.bingo_draws = [input_draws]

        elif type(input_draws) == str and not isfile(input_draws):
            if input_draws.lower() not in self.valid_bingo_draw_keywords:
                err = f"+++ERROR: \"{input_draws}\" not a valid keyword, " \
                      f"valid key words are {self.valid_bingo_draw_keywords}"
                raise TypeError(err)
            if input_draws.lower() == "random":
                self.bingo_draws = list(range(100))
                random.shuffle(self.bingo_draws)

        elif type(input_draws) == str and isfile(input_draws):
            self.load_bingo_draws_from_file(input_draws)

        else:
            err_mssg = "+++ERROR: valid inputs are a valid file path, "\
                       "a list of ints, a single int value or a keyword "\
                       f"in {self.valid_bingo_draw_keywords}"
            raise TypeError(err_mssg)

    def load_bingo_draws_from_file(self,input_draws):
        """ loads first line from input_draws file to bingo_draws """
        if not isfile(input_draws):
            err_mssg = f"+++ERROR: input file [{input_draws}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # load Bingo Draw data into list
        # note that we only read one line
        with open(input_draws,'r') as file_stream:
            draw_data = file_stream.readline()
            file_stream.close()

        data = list(map(int,draw_data.rstrip().split(',')))
        self.bingo_draws = data
        return data

    def load_bingo_cards_from_file(self,input_cards):
        """ loads bingo cards from file"""
        # bingo card lines are rows of number, no commas
        # assumption is that all bingo cards are square grids, i.e,
        # 4x4, 5x5, etc.
        #
        # When a qualifying line is read:
        #  - add that line to the bingo card
        #  - keep adding subsequent lines to the bingo card until the
        #    len of the bingo card list is the same as the number of
        #    elements in each line.
        #
        # Once the bingo card is the correct size (rows = num of columns):
        #  - Add the completed card to the deck of cards
        #  - Clear the existing bingo card and repeat process until the
        #  - end of the file
        # --------------------------------------------------------------
        if not isfile(input_cards):
            err_mssg = f"+++ERROR: input file [{input_cards}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        this_deck = []
        this_bingo_card = []

        text_file = open(input_cards)
        for this_line in text_file:

            line = this_line.rstrip()

            if len(line) > 0 and line.find(',') == -1:
                add_row =(line.split())
                this_bingo_card.append(add_row)

                if len(this_bingo_card) == len(add_row):
                    this_deck.append(this_bingo_card)
                    this_bingo_card = []

        text_file.close()

        # assign deck of cards
        deck_of_cards = np.array(this_deck)
        self.bingo_cards = deck_of_cards

        return deck_of_cards

    def pick_best_bingo_card(self):
        """ Checks all bingo cards for the quickest win """
        num_draws = len(self.bingo_draws)
        num_cards = len(self.bingo_cards)
        best_card_number = None
        
        if num_draws == 0 or num_cards == 0:
            err_mssg = f"+++ERROR: To calculate the winning care, there " \
                       f"must be  a non-zero number of draws " \
                       f"(loaded {num_draws}) and a non-zero number of " \
                       f"bingo cards to score (loaded {num_cards})"
            raise ValueError(err_mssg)
        
        for i in range(len(self.bingo_cards)):
            min_draws_to_win = self.bingo_cards[i].shape[0]
            this_card = self.bingo_cards[i].copy
            ### need to make a better copy here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
            card_wins = False
            draws_used = 0
            
            print(f"+++ Scoring card #{i}")
            #print(f"min_draws_to_win:{min_draws_to_win}")
            #print(f"+++ This card start:\n{this_card}")
            
            # score card until it wins or runs out of draws
            for j in range(len(self.bingo_draws)):
                this_draw = str(self.bingo_draws[j])
                draws_used +=1
                
                #print(f"+++ draw #{draws_used}: {this_draw}")
                this_card[this_card == this_draw] = 'X'
                
                if draws_used >= min_draws_to_win:
                    #check for win condition
                    card_wins = self.check_for_win(this_card)
                    if card_wins:
                        pass
                        # set stats
                        # break loop, scorne next card

                
            print(f"+++ This card scored:\n{this_card}")
            print(f"+++ Original card:\n{self.bingo_cards[i]}")
        print("+++INFO: function exiting with return best_card_number")
        return best_card_number
    
    def check_for_win(self,bingo_card):
        """ Check card for bingo """
        print("+++ check_for_win")
        target = bingo_card.shape[0]
        check_columns = True
        
        # check first row, if no 'X' values, no need to check columns
        x_count = np.count_nonzero(bingo_card[0] == 'X')
        if x_count == 0:
            check_columns = False
        if x_count == target:
            print("+++ check_for_win--> WINNER!")
            return True
        
        for i in range (1,target):
            x_count = np.count_nonzero(bingo_card[0] == 'X')
            if x_count == 0 and check_columns:
                check_columns = False
            if x_count == target:
                print("+++ check_for_win--> WINNER!")
                return True
        
        if check_columns:
            pass
            
        return False
