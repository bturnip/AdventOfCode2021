""" 2021 Advent of Code: Day 8"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103, C0123
from os.path import isfile

class Day8():
    """ 2021 Advent of Code puzzle for Day 8 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.unscrambled_numbers = []
        self.answer_key = {}

        if input_file is not None and isfile(input_file):
            self.segment_observations = self.load_data_from_file(input_file)
        else:
            self.segment_observations = []

    def load_data_from_file (self,input_file):
        """ loads the #TODO from file """
        # load logic:
        #  - split the incoming line on the "|", and further split each
        #    half of the result into lists
        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # -- parse input file
        with open(input_file,'r') as input_stream:
            raw_data=input_stream.readlines()
        input_stream.close()

        self.segment_observations = [[y[0].split(),y[1].split()] for y in
                                         [x.split('|') for x in raw_data]
                                    ]
        return self.segment_observations

    def solve_part1(self):
        """ how many times do digits 1, 4, 7, or 8 appear in output? """

        target_count = 0

        if len(self.segment_observations) > 1:
            part1_outputs = [x[1] for x in self.segment_observations ]

            for x in part1_outputs:
                this_count=len([y for y in x if (len(y) ==7 or \
                                             len(y) ==2  or \
                                             len(y) ==3  or \
                                             len(y) ==4)]
                              )
                target_count += this_count
        else:
            print("+++WARNING: empty segment_observations data, nothing to do...")
            return 0

        part1_answer = f"Total count of 1,4,7,8 in outputs:[{target_count}]"
        print(f"+++ANSWER: {part1_answer}" )
        self.answer_key["part 1:"]= part1_answer

        return self.answer_key

    def solve_part2(self):
        """ What is the sum total of all the output? """

        #--solve all segments
        for obs in self.segment_observations:
            number_key = self.solve_number_key(obs)
            self.update_unscrambled_numbers(number_key,obs)

        part2_total = sum(self.unscrambled_numbers)
        part2_answer = f"Sum total of outputs:[{part2_total}]"
        print(f"+++ANSWER: {part2_answer}" )
        self.answer_key["part 2:"]= part2_answer

        return self.answer_key

    def get_segment_observations(self):
        """ Returns the segment observations loaded from file """
        for x in self.segment_observations:
            print(x)

    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key

    def solve_number_key(self,observation):
        """ use the input segments to populate solved_numbers dict"""
        scrambled_segments = observation[0]

        #--create solved_numbers dict where entry looks like {'abc':7},etc
        solved_numbers = {}
        for s in scrambled_segments:
            solved_numbers[self.sort_answer(s)] = -1

        #--solve for numbers, split into functions
        solved_numbers = self.solve_numbers_1478(solved_numbers)
        solved_numbers = self.solve_number_3(solved_numbers)
        solved_numbers = self.solve_number_6(solved_numbers)
        solved_numbers = self.solve_numbers_25(solved_numbers)
        solved_numbers = self.solve_numbers_90(solved_numbers)

        return solved_numbers

    def update_unscrambled_numbers(self,number_key, observation):
        """ Uses answer key to unscamble display digits """
        # will update self.unscrambled_numbers
        scrambled_digits = observation[1]

        clear_output=''
        for this_digit in scrambled_digits:
            scrambled = self.sort_answer(this_digit)
            clear_digit = number_key[scrambled]
            clear_output += str(clear_digit)

        self.unscrambled_numbers.append(int(clear_output))
        return int(clear_output)

    def solve_numbers_90(self, solved_numbers):
        """ loads 'solved_numbes' for numbers 2,5 """
        # determine the value of segment "E" by comparing #6 and #5
        #  - "E" = the segment in #6 and missing from #5
        #  - #0 will have segment "E", while #9 will not

        len6_numbers = []
        for k,v in solved_numbers.items():
            if v == 6:
                number_6 = k
            if v == 5:
                number_5 = k
            #--only consider unsolved numbers
            if len(k) == 6 and v <0:
                len6_numbers.append(k)

        for e in number_6:
            if e not in number_5:
                segment_e = e
                break

        for this_num in len6_numbers:
            if segment_e in this_num:
                number_0 = this_num
            else:
                number_9 = this_num
        solved_numbers[number_0] = 0
        solved_numbers[number_9] = 9

        return solved_numbers

    def solve_numbers_25(self, solved_numbers):
        """ loads 'solved_numbes' for numbers 2,5 """
        # determine the value of segment "C" by comparing #6 and #8
        #  - "C" = the segment in #8 and missing from #6
        #  - #2 will have segment "C", while #5 will not

        len5_numbers = []
        for k,v in solved_numbers.items():
            if v == 8:
                number_8 = k
            if v == 6:
                number_6 = k
            #--only consider unsolved numbers
            if len(k) == 5 and v <0:
                len5_numbers.append(k)

        for e in number_8:
            if e not in number_6:
                segment_c = e
                break

        for this_num in len5_numbers:
            if segment_c in this_num:
                number_2 = this_num
            else:
                number_5 = this_num

        solved_numbers[number_2] = 2
        solved_numbers[number_5] = 5

        return solved_numbers

    def solve_number_3(self, solved_numbers):
        """ loads 'solved_numbes' for # 3 """
        # the #3 will have len=5 and both segments of #1
        len5_numbers = []
        for k,v in solved_numbers.items():
            if len(k) == 2:
                number_1 = k
            if len(k) == 5:
                len5_numbers.append(k)

        for this_num in len5_numbers:
            if number_1[0] in this_num:
                if number_1[1] in this_num:
                    number_3 = this_num
        solved_numbers[number_3] = 3
        return solved_numbers

    def solve_number_6(self, solved_numbers):
        """ loads 'solved_numbes' for # 6 """
        # the #6 will have len=6 and only 1 segment of #1
        len6_numbers = []
        for k,v in solved_numbers.items():
            if len(k) == 2:
                number_1 = k
            if len(k) == 6:
                len6_numbers.append(k)

        for this_num in len6_numbers:
            count=0
            if number_1[0] in this_num:
                count+=1
            if number_1[1] in this_num:
                count+=1
            if count == 1:
                number_6 = this_num
                break

        solved_numbers[number_6] = 6
        return solved_numbers

    def solve_numbers_1478(self, solved_numbers):
        """ loads 'solved_numbes' answers based on segment series len """
        # -- solve by len: 1,4,7,8 -------------------------------------
        for k,v in solved_numbers.items():
            if len(k)==2:
                solved_numbers[k] = 1
            if len(k)==3:
                solved_numbers[k] = 7
            if len(k)==4:
                solved_numbers[k] = 4
            if len(k)==7:
                solved_numbers[k] = 8
        return solved_numbers

    def sort_answer (self,data_in):
        """ Part 2 needs a lot of sorting, so sort! """
        if type(data_in) == list:
            return ''.join(map(str,sorted(data_in[0])))
        if type(data_in) == str:
            return ''.join(map(str,sorted(data_in)))
        else:
            err_mssg = f"+++ERROR: sort_answer() only sorts lists and "\
                       f"strings, data_in was {data_in}, which is " \
                       f"type:{type(data_in)}"
            raise TypeError(err_mssg)
