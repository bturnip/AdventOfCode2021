""" 2021 Advent of Code: Day 14"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103, C0123
from os.path import isfile
import numpy as np

class Day14():
    """ 2021 Advent of Code puzzle for Day14 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.answer_key = {}
        self.polymer_template = ''
        self.insertion_rules = {}
        self.polymer = ''

        if input_file is not None and isfile(input_file):
            self.load_data_from_file(input_file)


    def load_data_from_file (self,input_file):
        """ loads input data from file """
        # load logic:
        #  - This first line is the polymer template
        #  - Remaining lines populate the pair_insertion_rules dict

        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # -- parse input file
        with open(input_file,'r',encoding="utf-8") as input_stream:
            raw_data=input_stream.readlines()
        input_stream.close()

        self.polymer_template = raw_data[0].rstrip()

        rules = raw_data[2:]
        for r in rules:
            data = r.split(' -> ')
            self.insertion_rules[data[0]] = data[1].rstrip()


    def run_polymerization_chain (self,num_cycles=1):
        """ Calls the process_polymer function num_cycles times """
        for i in range(num_cycles):
            p = self.process_polymer()


    def process_polymer(self, input_polymer=None):
        """ expands polymner using the insertion rules """

        if input_polymer is None:
            update_instance_polymer = True
            if self.polymer == '':
                p = self.polymer_template
            else:
                p = self.polymer
        else:
            p=input_polymer

        #--build the pairs to process in this step
        polymer_pairs = []
        for r in range(0,len(p)-1):
            polymer_pairs.append(f'{p[r]}{p[r+1]}')

        #--process the pairs
        new_p = ''
        for pair in polymer_pairs:
            new_p +=  f'{pair[0]}{self.insertion_rules[pair]}'
        #--add the last element back to the chain
        new_p += polymer_pairs[-1][1]

        #--update self.polymer if no input was given
        if update_instance_polymer:
            self.polymer = new_p
        return new_p

    def solve_part1(self):
        """
        What do you get if you take the quantity of the most common
        element and subtract the quantity of the least common element?
        """
        #--reset any polymerization
        self.polymer=''
        self.run_polymerization_chain(10)

        x=np.array(list(self.polymer))
        unique,frequency = np.unique(x, return_counts = True)

        frequency.sort()
        part1_score = frequency[-1] - frequency[0]

        # ~ z=zip(unique,frequency)
        # ~ foo = {key: value for key, value in z}
        # ~ print(f'+++DEBUG: foo: {foo}')
        # ~ print(f'+++DEBUG: frequency: {frequency}')
        
        self.answer_key['part1'] = part1_score

        return part1_score

    def solve_part2(self):
        """ TODO: enter part 2 question here """
        """
        What do you get if you take the quantity of the most common
        element and subtract the quantity of the least common element?
        Run 40x instead of 10
        """
        #--reset any polymerization
        self.polymer=''
        self.run_polymerization_chain(40)

        x=np.array(list(self.polymer))
        unique,frequency = np.unique(x, return_counts = True)

        frequency.sort()
        part1_score = frequency[-1] - frequency[0]

        # ~ z=zip(unique,frequency)
        # ~ foo = {key: value for key, value in z}
        # ~ print(f'+++DEBUG: foo: {foo}')
        # ~ print(f'+++DEBUG: frequency: {frequency}')
        
        self.answer_key['part2'] = part2_score

        return part2_score

    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key
