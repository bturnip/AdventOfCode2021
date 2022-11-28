""" 2021 Advent of Code: Day 6"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103, C0123
from os.path import isfile
import numpy as np

class Day6():
    """ 2021 Advent of Code puzzle for Day 6 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.new_fish_status = 8
        self.spawn_reset_status = 6
        self.answer_key = {}

        if input_file is not None and isfile(input_file):
            self.starting_fish = self.load_fish_from_file(input_file)
        else:
            self.starting_fish = []

        if len(self.starting_fish) > 0:
            self.total_fish_count = len(self.starting_fish)
            self.fish_status = self.initialize_fish_status(self.starting_fish)
        else:
            self.total_fish_count = 0
            self.fish_status = []


    def load_fish_from_file (self,input_file):
        """ loads the lantern fish from file """
        # fish load logic:
        #  - input file a series of numbers that represent each current
        #    fish's countdown timer
        #  - entry lines look like "1,4,1,2,1,1,4"
        # note that this list won't change once created

        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # -- parse input file
        with open(input_file,'r') as input_stream:
            raw_data=input_stream.readlines()
        input_stream.close()

        fish_data = list(map(int,raw_data[0].split(',')))

        self.starting_fish=np.array(fish_data)
        return self.starting_fish

    def initialize_fish_status (self, fish_list):
        """ store frequency values from input list of fish """
        results = np.unique(fish_list, return_counts=True)
        self.fish_status = dict(zip(*results))
        return self.fish_status

    def process_new_day(self, fish_status=None):
        """ update fish_status """
        # --new day logic
        # valid values 1 - 8
        # decrement each fish counter by 1
        # we can work on the fish_status dict b/c we want aggregate data
        # for initial value i = 2 - 8:
        #   - new value = i_1
        # for initial value i = 0
        #   - new value = 6
        #   - add new entry where i = 8
        # ----------------------------------------
        #--sanity checks
        if fish_status is None:
            fish_status = self.fish_status
        if len(fish_status) == 0 or type(fish_status) != dict:
            raise ValueError ("+++ERROR: process_new_day() takes a "\
                              "non-empty dictionary of fish status")


        #--decrement every fish status
        updated_status = {}
        for status,curr_count in fish_status.items():
            updated_status[status - 1] = curr_count

        # --create new fish and reset status for those that just spawned
        if -1 in updated_status.keys():
            new_s = self.new_fish_status
            reset_s = self.spawn_reset_status
            fish_to_handle = fish_status[0]

            # -- add new fish
            updated_status[new_s] = fish_to_handle

            # -- restart status for fish that just spawned a new fish
            if reset_s in updated_status.keys():
                updated_status[reset_s] += fish_to_handle
            else:
                updated_status[reset_s] = fish_to_handle

            del updated_status[-1]

        #print(f"orig:{fish_status}")
        #print(f"updt:{updated_status}")

        #-- calculate totatl fish population
        self.total_fish_count = sum(updated_status.values())

        self.fish_status = updated_status
        return updated_status

    def solve_part1(self):
        """ how many fish after 80 days? """
        num_days = 80
        for x in range(num_days):
            self.process_new_day()

        self.answer_key["part 1:"]= self.total_fish_count

    def solve_part2(self):
        """ how many fish after 80 days? """
        num_days = 256
        for x in range(num_days):
            self.process_new_day()

        self.answer_key["part 2:"]= self.total_fish_count


    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key

    def get_total_fish_count(self):
        """ return population """
        return self.total_fish_count
