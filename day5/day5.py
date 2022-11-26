""" 2021 Advent of Code: Day 5"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103
from os.path import isfile
import numpy as np

class Day5():
    """ 2021 Advent of Code puzzle for Day 5 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.map_counts = {}
        self.answer_key = {}

        #hydrothermal vent coords
        if input_file is not None and isfile(input_file):
            self.vent_coords = self.load_all_coords_from_file(input_file)
        else:
            self.vent_coords = []

        if len(self.vent_coords) > 0:
            self.marked_map = self.map_coords(self.vent_coords)
        else:
            self.marked_map = []


    def load_all_coords_from_file(self,input_file):
        """ loads the map of coords from file """
        # coordinates load logic:
        #  - input file a series of coordinate entries
        #  - entry lines look like "777,778 -> 777,676"
        #  - these are the "start" and "stop" points on a line segment
        #    on a grid
        #  - output is a 2D np array that looks like this:
        #    [[777 778 777 676]
        #     [500 510 378 510]
        #     [...]
        #     [623 450 623 616]]
        #
        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # -- parse input file
        with open(input_file,'r') as input_stream:
            raw_data=input_stream.readlines()
        input_stream.close()

        self.vent_coords = np.empty((0,4), int)

        coord_pairs =np.array([x.rstrip().split(' -> ') for x in raw_data])

        for this_pair in coord_pairs:
            start_pt = this_pair[0]
            stop_pt = this_pair[1]
            xstart, ystart = start_pt.split(',')
            xend, yend = stop_pt.split(',')

            this_row = np.array([[xstart,ystart,xend,yend]])

            #print(f"{xstart}|{ystart}|{xend}|{yend}")
            self.vent_coords = np.r_[self.vent_coords ,this_row.astype(int)]

        return self.vent_coords

    def get_all_coords(self):
        """ get the list of loaded coords """
        return self.vent_coords

    def map_coords(self,coords):
        """ maps a set of coords to self.marked_map """
        # assumption: 1000x1000 grid is sufficient based on input analysis

        # -- create the empty map
        self.marked_map = np.zeros((1000,1000),int)

        # -- process the coordinates
        # -- skip the diagonals on the first pass
        #    - record the answer for part1
        # -- process diagonals
        #    - record the answer for part2
        for c in coords:
            # -- process horizontal and vertical lines
            if c[0] == c[2]:
                # horizontal line
                rownum = c[0]
                target_indices = [x for x in range(min(c[1],c[3])
                                                   ,max(c[1],c[3])+1)]
                np.add.at(self.marked_map[rownum]
                          , target_indices
                          , 1)
                #print(f"result row in marked map:\n{self.marked_map[c[0]]}")
            elif c[1] == c[3]:
                # vertical line
                r_start = min(c[0],c[2])
                r_stop = max(c[0],c[2])+1

                colnum = c[1]
                target_indices = [y for y in range(r_start,r_stop)]

                #print(f"+++INFO: vertical line\n - coords:({c})\n" \
                #      f" - col num:{colnum}\n - range:({r_start},{r_stop})\n" \
                #      f" - targets:{target_indices}")
                np.add.at(self.marked_map[:,colnum]
                          , target_indices
                          , 1)

        # -- record part1 answer
        self.set_map_counts(self.marked_map)
        self.set_answer_for_part(1)

        # -- process diagonals for part2
        for c in coords:
            # -- process horizontal and vertical lines
            if c[0] != c[2] and c[1] != c[3]:
                # get starting point, ie, which coord has lowest x value
                # and direction (up or down)
                if  min(c[0],c[2]) == c[0]:
                    x_start_idx = 0
                else:
                    x_start_idx = 2

                start_x = c[x_start_idx]
                start_y = c[x_start_idx + 1]

                if x_start_idx == 0:
                    end_x = c[2]
                    end_y = c[3]
                else:
                    end_x = c[0]
                    end_y = c[1]

                if start_y > end_y:
                    direction = 'up'
                else:
                    direction = 'down'

                # mark diagonal line
                this_x = start_x
                this_y = start_y

                self.marked_map[this_x][this_y] += 1
                for i in range(start_x,end_x):
                    this_x += 1
                    if direction == 'down':
                        this_y +=1
                    else:
                        this_y -=1

                    self.marked_map[this_x][this_y] += 1
        # -- record part2 answer
        #    NB: this updates the marked map, no going back to part1 state
        self.set_map_counts(self.marked_map)
        self.set_answer_for_part(2)

        return self.marked_map

    def get_map(self):
        """ return marked map"""
        # how to display and scroll?
        return self.marked_map

    def get_map_counts(self):
        """ return map_counts, freq of values of marked_map"""
        return self.map_counts

    def set_map_counts(self,this_map):
        """ store the frequency values from the marked map"""
        results = np.unique(this_map, return_counts=True)
        self.map_counts = dict(zip(*results))
        return self.map_counts

    def set_answer_for_part(self,part_num):
        """ stores the answer for the input part num """

        # -- Answer is how many map points have a value > 2
        freqs = self.map_counts
        count_target = 2
        curr_sum = 0
        for this_key, this_val in freqs.items():
            if this_key >= count_target:
                curr_sum += this_val

        this_key = f"part{str(part_num)}"

        self.answer_key.update({this_key: curr_sum})
        return self.answer_key

    def get_answer_key(self):
        """ returns the dict with the answer for part 1"""

        return self.answer_key
