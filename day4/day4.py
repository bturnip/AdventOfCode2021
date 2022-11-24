""" 2021 Advent of Code: Day 4"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=C0104, C0123, C0413, E0602, W0511
# --------------------------------------------------------------
# Card scoring logic
# --------------------------------------------------------------
# Cycle through each card stored in self.bingo_cards
#   - For each card:
#     - Cycle bingo draws: For each draw:
#         - Mark card
#         - If we have at least the min # draws for a bingo
#           - Check for Win:
#             - If a Win:
#                 - Set stats:
#                   - Mark card as Winner
#                   - Record last draw
#                   - Record draw number
#                 - Record stats
#                 - Break out of loop, GO to next card
#     - If all draws processed, mark card as non winner,
#       GO to the next card
#   - After all cards processed:
#     - process stat_log
#       - pick winner
#       - record objects final part 1 score
# --------------------------------------------------------------
import sys
import random
from os.path import isfile

sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/advent_tools')
from advent_tools import *

class BingoCardStat(object):
    def __init__(self,card_num,win_status,num_draws=None,last_draw=None):
        self.card_num = card_num
        self.win_status = win_status
        self.num_draws = num_draws

        if last_draw is not None:
            self.last_draw = int(last_draw)
        self.unmarked_sum = 0
        self.pt1_final_score = 0
        self.pt2_final_score = 0

    def get_stats(self):
        """ report stats """
        return vars(self)
    def get_card_num(self):
        """ returns card num """
        return self.card_num
    def is_winner(self):
        """ True/False for win status"""
        return self.win_status
    def get_num_draws(self):
        """ returns number of draws"""
        return self.num_draws
    def get_pt1(self):
        """ returns the final answer for Part 1 of Puzzle """
        return self.pt1_final_score
    def get_pt2(self):
        """ returns the final answer for Part 2 of Puzzle """
        return self.pt2_final_score

class Day4(object):
    """ Object that contains the methods to compute/store
        the 2021 Advent Of Code puzzle for Day 4"""

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.valid_bingo_draw_keywords = ["random"]


        if input_file is not None and isfile(input_file):
            self.bingo_draws = self.load_bingo_draws_from_file(input_file)
            self.bingo_cards = self.load_bingo_cards_from_file(input_file)
        else:
            self.bingo_draws = []
            self.bingo_cards = []

        self.bingo_card_stats = []

        self.part1_answer ={}

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

    def mark_bingo_card(self,card, draw):
        """ Marks bingo card with given draw """
        card[card == draw] = 'X'
        return card

    def set_card_stats(self,card_number,is_winner,num_draws=None,last_draw=None):
        """ records the stats for each scored card """
        # sanity checks
        if is_winner and (num_draws is None or last_draw is None):
            err_mssg = "+++ERROR: set_card_stats().  If card is a winner, "\
                       "num_draws ({num_draws}) and last_draw ({last_draw}) "\
                       "must be populated."
            raise ValueError(err_mssg)

        this_stat = BingoCardStat(card_number,is_winner,num_draws,last_draw)

        if is_winner:
            # -- calculate unmarked_sum and pt1_final_score
            this_card = self.bingo_cards[card_number].copy()
            this_card[this_card == 'X'] = 0
            this_stat.unmarked_sum = np.sum(this_card.astype(int))

            this_stat.pt1_final_score = this_stat.unmarked_sum * this_stat.last_draw

        # load stat
        self.bingo_card_stats.append(this_stat)

        return 0

    def score_all_cards(self):
        """ Scores all bingo cards """

        num_draws = len(self.bingo_draws)
        num_cards = len(self.bingo_cards)

        # -- sanity checks
        if num_draws == 0 or num_cards == 0:
            err_mssg = f"+++ERROR: To calculate the winning care, there " \
                       f"must be  a non-zero number of draws " \
                       f"(loaded {num_draws}) and a non-zero number of " \
                       f"bingo cards to score (loaded {num_cards})"
            raise ValueError(err_mssg)

        # -- cycle through all bingo cards
        for i in range(num_cards):
            # -- set vars
            card_wins = False
            draws_used = 0

            # -- load card
            this_card = self.bingo_cards[i]
            min_draws_to_win = self.bingo_cards[i].shape[0]

            # -- cycle through the draws, marking and checking card
            for j in range(num_draws):
                this_draw = str(self.bingo_draws[j])
                draws_used +=1

                # -- mark card
                self.mark_bingo_card(this_card,this_draw)

                # -- check for winner
                if draws_used >= min_draws_to_win:
                    card_wins = self.check_for_win(this_card)
                    # -- calculate winner stats
                    if card_wins:
                        self.set_card_stats(i,True,draws_used,this_draw)
                        break

            if not card_wins:
                # -- mark card as non-winner
                self.set_card_stats(i,False)

            #print(f"+++ Card #{i} scored")

        # -- determine best card and set dict for part 1
        self.set_part1_answer()


        # TODO: find_best_card()
        return 0

    def set_part1_answer(self):
        """ calculates the answer for part 1"""
        best_card_num = -1
        quickest_win_draws = 1000

        for i in range(len(self.bingo_card_stats)):
            this_card = self.bingo_card_stats[i]
            if this_card.is_winner():
                this_num_draws = this_card.get_num_draws()
                if this_num_draws < quickest_win_draws:
                    best_card_num = i
                    quickest_win_draws = this_num_draws

        winning_card = self.bingo_card_stats[best_card_num]
        final_pt1_score = winning_card.get_pt1()
        self.part1_answer["card number"] = best_card_num
        self.part1_answer["score"] = final_pt1_score

    def get_part1_answer(self):
        """ returns the answer for part 1 of Day4 puzzle """
        answer = f"+++ Part 1 results:\n "\
                 f"\tBest Card Number: {self.part1_answer['card number']} \n"\
                 f"\tAnswer: {self.part1_answer['score']}"
        print(answer)

    def check_for_win(self,bingo_card):
        """ Check card for bingo """
        target = bingo_card.shape[0]
        check_columns = True

        # -- check 1st row, if no 'X' values, no need to check columns
        x_count = np.count_nonzero(bingo_card[0] == 'X')
        if x_count == 0:
            check_columns = False
        if x_count == target:
            return True

        # -- if 1st row wasn't a winner, check rows
        for i in range (1,target):
            x_count = np.count_nonzero(bingo_card[i] == 'X')
            if x_count == 0 and check_columns:
                check_columns = False
            if x_count == target:
                return True

        # -- check columns if needed
        if check_columns:
            for j in range(0,target):
                x_count = np.count_nonzero(bingo_card[:,j] == 'X')
                if x_count == target:
                    return True

        return False
