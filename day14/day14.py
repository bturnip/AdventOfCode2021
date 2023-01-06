""" 2021 Advent of Code: Day 14"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103, C0123
from os.path import isfile
import functools
import time
import numpy as np



class Day14():
    """ 2021 Advent of Code puzzle for Day14 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.answer_key = {}
        self.polymer_template = ''
        self.insertion_rules = {}
        self.polymer_dict = {}
        self.polymer = ''

        if input_file is not None and isfile(input_file):
            self.load_data_from_file(input_file)

        if len(self.insertion_rules) > 0:
            self.create_polymer_dict()

    def get_polymer(self):
        """ prints out polymer """
        COL_SIZE = 50
        offset = 0
        while offset < len(self.polymer):
            print(self.polymer[offset:offset+COL_SIZE])
            offset+=COL_SIZE

        return self.polymer


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

    def create_polymer_dict(self):
        """ Creates a dict of all possible elements in polymer """
        if len(self.insertion_rules) == 0:
            err_mssg = "+++ERROR: insertion_rules dict must be populated..."
            raise ValueError(err_mssg)
        elements = set()
        for v in self.insertion_rules.values():
            elements.add(v)


    def process_polymer_chunks(self
                               ,num_cycles
                               ,chunk_size=2000000):
        """ process polymer in chunks """
        #-- toggle back and forth during each iteration
        #-- the output of loop1 becomes the input into loop2, etc...
        file1 = './temp_polymer1.txt'
        file2 = './temp_polymer2.txt'
        use_file1 = True
        INPUT = file1
        OUTPUT = file2


        #--prime the loop: write the starting polymer to file
        if self.polymer == '':
            p = self.polymer_template
        else:
            p = self.polymer

        with open(INPUT,'w',encoding="utf-8") as poly_in:
            poly_len = len(p)
            print(f'+++DEBUG: priming file processing with starting polymer with len: {poly_len}')
            poly_in.write(p)


        for i in range(num_cycles):
            cycle_start = time.perf_counter()
            print(f'+++DEBUG: Cycle #:{i}')
            if use_file1:
                INPUT = file1
                OUTPUT = file2
            else:
                INPUT = file2
                OUTPUT = file1

            last_element = ''

            with open(INPUT,'r',encoding="utf-8") as poly_in:
                with open(OUTPUT,'w+',encoding="utf-8") as poly_out:
                    while True:
                        input_chunk = poly_in.read(chunk_size)
                        if i<4:
                            print(f'+++DEBUG: input_chunk: {input_chunk}')

                        if input_chunk == '':
                            output_chunk += last_element
                            poly_out.write(last_element)
                            break
                        last_element = input_chunk[-1]

                        #--process data
                        output_chunk = self.process_polymer(input_chunk)
                        poly_out.write(output_chunk)
                        if i<4:
                            print(f'+++DEBUG: output_chunk: {output_chunk}')
            
            poly_in.close()
            poly_out.close()


            #--toggle the input/output files
            use_file1 = not use_file1
            
            #--report time stats
            cycle_stop = time.perf_counter()
            print(f'+++DEBUG:\tsecs elapsed: {cycle_stop - cycle_start:0.4f}')
            
            #--report cache stats
            stats = self.process_polymer.cache_info()
            print(f'+++DEBUG: stats: {stats}')

        #--load final polymer
        with open(OUTPUT,'r',encoding="utf-8") as final:
            self.polymer = final.read()

    @functools.lru_cache(maxsize=256)
    def process_polymer(self, input_polymer):
        """ expands polymner using the insertion rules """

        p = input_polymer
        #--build the pairs to process in this step
        polymer_pairs = []
        for r in range(0,len(p)-1):
            polymer_pairs.append(f'{p[r]}{p[r+1]}')

        #--process the pairs
        new_p = ''
        for pair in polymer_pairs:
            new_p +=  f'{pair[0]}{self.insertion_rules[pair]}'
        #--add the last element back to the chain
        #--do not do this with the piece-wise method
        #--only add back the very final last element
        #new_p += polymer_pairs[-1][1]

        return new_p


    @functools.lru_cache(maxsize=48)
    def process_polymer_recurs(self, num_cycles, polymer):
        """ expand polymner recursively to allow for caching"""
        cycle_start = time.perf_counter()
        if num_cycles < 1:
            return self.polymer

        if self.polymer == '':
            p = self.polymer_template
        else:
            p = polymer

        polymer_pairs = []
        for r in range(0,len(p)-1):
            polymer_pairs.append(f'{p[r]}{p[r+1]}')

        #--process the pairs
        new_p = ''
        for pair in polymer_pairs:
            new_p +=  f'{pair[0]}{self.insertion_rules[pair]}'
        #--add the last element back to the chain
        new_p += polymer_pairs[-1][1]

        cycle_stop = time.perf_counter()

        print(f'+++DEBUG: {num_cycles}, '\
              f'len(new_p): {len(new_p)}, '\
              f'secs elapsed: {cycle_stop - cycle_start:0.4f}')

        self.polymer = new_p
        return self.process_polymer_recurs(num_cycles-1, self.polymer)



    def solve_part1(self):
        """
        What do you get if you take the quantity of the most common
        element and subtract the quantity of the least common element?
        """
        #--reset any polymerization
        self.polymer=''
        self.polymer = self.process_polymer_recurs(10,self.polymer)

        x=np.array(list(self.polymer))
        unique,frequency = np.unique(x, return_counts = True)


        frequency.sort()
        part1_score = frequency[-1] - frequency[0]

        self.answer_key['part1'] = part1_score

        return part1_score


    def solve_part2(self):
        """
        What do you get if you take the quantity of the most common
        element and subtract the quantity of the least common element?
        Run 40x instead of 10
        """
        #--reset any polymerization
        self.polymer=''

        # ~ self.polymer = self.process_polymer_recurs(10,self.polymer)
        # ~ self.polymer = self.process_polymer_recurs(10,self.polymer)
        # ~ self.polymer = self.process_polymer_recurs(10,self.polymer)
        # ~ self.polymer = self.process_polymer_recurs(10,self.polymer)
        for i in range(40):
            self_polymer = self.process_polymer_recurs(1,self.polymer)


        x=np.array(list(self.polymer))
        unique,frequency = np.unique(x, return_counts = True)

        frequency.sort()
        part2_score = frequency[-1] - frequency[0]

        if num_cycles == 40:
            self.answer_key['part2'] = part2_score

        return part2_score

    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key
