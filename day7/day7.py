""" 2021 Advent of Code: Day 7"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103, C0123
from os.path import isfile
import numpy as np

class Day7():
    """ 2021 Advent of Code puzzle for Day 6 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.fuel_needed = {}
        self.answer_key = {}


        if input_file is not None and isfile(input_file):
            self.starting_crabs = self.load_data_from_file(input_file)
        else:
            self.starting_crabs = []

        if len(self.starting_crabs) > 0:
            self.crab_horiz_pos = self.initialize_crab_horiz_pos(self.starting_crabs)
        else:
            self.crab_horiz_pos = []


    def load_data_from_file (self,input_file):
        """ loads the #TODO from file """
        # load logic:
        #  - input file a series of numbers that represent each current
        #    crab's horizontal location
        #  - entry lines look like "1101,1,29,67,1102,0,1,65,1008,65,35"
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

        crab_data = list(map(int,raw_data[0].split(',')))

        self.starting_crabs=np.array(crab_data)
        return self.starting_crabs

    def initialize_crab_horiz_pos(self, crab_data):
        """ store crab positions from input """
        results = np.unique(crab_data, return_counts=True)
        self.crab_data = dict(zip(*results))
        return self.crab_data

    def calculate_fuel_use(self, crab_pos_data=None, model=None):
        """ calculate fuel units to line up crabs, per position "
            creates self.fuel_needed dict """

        if crab_pos_data is None:
            crab_pos_data = self.crab_horiz_pos

        run_part1_model = False
        run_part2_model = False
        if model is None or model.lower() == "part1":
            model = "part1"
            run_part1_model = True
        elif model.lower() == "part2":
            model = "part2"
            run_part2_model = True
        else:
            err_mssg = "+++ERROR: calculate_fuel_use() with model must "\
                       "be either 'part1' or 'part2'"
            raise ValueError(err_mssg)

        if run_part1_model:
            # --get all positions, calculate fuel use for 1 unit per position
            print(f"+++INFO: making fuel calculations with Model:{model}")
            fuel_needed={}

            for this_pos in crab_pos_data.keys():
                fuel_cost = 0

                for k,v in crab_pos_data.items():
                    #print(f"{fuel_cost} += ({v} * abs({k}-{this_pos}))")
                    fuel_cost += (v * abs(k - this_pos))

                fuel_needed[this_pos] = fuel_cost
                self.fuel_needed = fuel_needed

        if run_part2_model:
            # cycle through all available positions
            min_pos = min(crab_pos_data.keys())
            max_pos = max(crab_pos_data.keys())
            print(f'+++DEBUG: min, max crab pos_: {min_pos},{max_pos}')



            print(f"+++INFO: making fuel calculations with Model:{model}")
            fuel_needed={}

            #for this_pos in crab_pos_data.keys():
            for this_pos in range(min_pos,max_pos):
                fuel_cost = 0
                #print(f'+++DEBUG: calculating for move to {this_pos}')

                for k,v in crab_pos_data.items():
                    base_cost = abs(k - this_pos)
                    cost_multiplier = (base_cost*(base_cost + 1) / 2)
                    fuel_cost += (v * cost_multiplier)

                    """
                    print(f'\tDEBUG: to move a unit from [{k}] to [{this_pos}]: {cost_multiplier}')
                    print(f'\tDEBUG: cost_multiplier: {cost_multiplier}')
                    print(f'\tDEBUG: [{v} * {cost_multiplier}]')
                    print(f'\tDEBUG: fuel_cost: {fuel_cost}\n')
                    """

                fuel_needed[this_pos] = fuel_cost
                self.fuel_needed = fuel_needed

        return fuel_needed

    def solve_part1(self):
        """ What is the least fuel cost to align the crabs """
        self.calculate_fuel_use(model="part1")

        if len(self.fuel_needed) == 0:
            print("+++ERROR: no data in the fuel_cost dict, nothing to do...")
            return 0

        # --find minimum value in the fuel_cost dict and corresponding key
        #print(f"whole dict:\n{self.fuel_needed}")
        min_fuel = min(self.fuel_needed.values())
        pos_key = min(self.fuel_needed, key=self.fuel_needed.get)

        part1_answer = f"Position:({pos_key}) :Fuel Needed:({min_fuel})"
        print(f"+++ANSWER: {part1_answer}" )
        self.answer_key["part 1:"]= part1_answer
        return self.answer_key

    def solve_part2(self):
        """ What is the least fuel cost with updated fuel usage? """
        self.calculate_fuel_use(model="part2")

        if len(self.fuel_needed) == 0:
            print("+++ERROR: no data in the fuel_cost dict, nothing to do...")
            return 0

        min_fuel = min(self.fuel_needed.values())
        pos_key = min(self.fuel_needed, key=self.fuel_needed.get)

        part2_answer = f"Position:({pos_key}) :Fuel Needed:({min_fuel})"
        print(f"+++ANSWER: {part2_answer}" )
        self.answer_key["part 2:"]= part2_answer
        return self.answer_key

    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key
