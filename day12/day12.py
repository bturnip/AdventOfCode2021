""" 2021 Advent of Code: Day 12"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=R1721, C0103, C0123
from os.path import isfile
#import numpy as np

class Cave():
    """ Caves are fancy nodes """
    def __init__(self, cave_name, connection=None):

        self.name = cave_name
        self.connects_to = []

        if cave_name.upper() == cave_name:
            self.cave_size = "big"
        else:
            self.cave_size = "small"

        if connection is not None:
            if type(connection) == list:
                self.connects_to = connection
            if type(connection) == str:
                self.connects_to.append(connection)

    def __repr__(self):
        return self.name

    def get_stats(self):
        """ report stats """
        return vars(self)

    def get_name(self):
        """ returns name """
        return self.name

    def add_connection(self, cave_name):
        """ adds new link (connection) to cave """
        if cave_name not in (self.connects_to):
            self.connects_to.append(cave_name)

    def get_connections(self):
        """ returns all connections """
        return self.connects_to


class Day12():
    """ 2021 Advent of Code puzzle for Day12 """

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.cave_list = []
        self.cave_paths_pt1 = []
        self.answer_key = {}

        if input_file is not None and isfile(input_file):
            self.input_data = self.load_data_from_file(input_file)
        else:
            self.input_data = []

        if len(self.input_data)>0:
            self.cave_list = self.build_cave_list()


    def load_data_from_file (self,input_file):
        """ loads the list of cave paths from file """

        # --sanity checks ---------------------------------------------
        if not isfile(input_file):
            err_mssg = f"+++ERROR: input file [{input_file}] is not "\
                       f" a valid file."
            raise TypeError(err_mssg)

        # -- parse input file
        with open(input_file,'r', encoding="utf-8") as input_stream:
            raw_data=input_stream.readlines()
        input_stream.close()

        return [x.rstrip() for x in raw_data]

    def get_cave_index_by_name(self,target_name):
        """ returns index of self.cave_list for target_name """
        if len(self.cave_list) == 0 \
               or not any(cave.name == target_name for cave in self.cave_list):
            return -1

        result = next((obj for obj in self.cave_list \
                           if obj.name == target_name)\
                      ,None)
        return self.cave_list.index(result)


    def build_cave_paths_pt1(self,caves=None):
        """
        Builds a list of paths from start to end that follow pt1 rules
        """
        #--Path Rules
        #  Start at "start" and discover all paths to "end"
        #  Big size caves can be traversed multiple times
        #  Small size caves can only be traversed once
        #  Start and End are both small size caves
        if caves is None:
            caves = self.cave_list
        
        curr_path = ["start"]
        curr_path = self.get_cave_path(curr_path)
        

   
                
    def get_cave_path(self,curr_path):
        """
        Func to be called recursively
        """
        path_data = curr_path.copy()
        
        while len(path_data) > 0:
            idx = self.get_cave_index_by_name(curr_path[-1])
            if idx < 0:
                return
            
            next_conns = self.
        for this_conn in next_conns:
            print(f'+++DEBUG: this_conn: {this_conn}')
            #--small cave twice, reject path
            if this_conn in curr_path and this_conn.lower() == this_conn:
                return
            #-- end path, return completed path
            if this_conn == "end":
                curr_path.append(this_conn)
                print(f'+++DEBUG: curr_path: {curr_path}')
                return curr_path
            print(f'+++DEBUG: adding this_conn: {this_conn}')
            curr_path.append(this_conn)
            next_conns.reverse()
            print(f'+++DEBUG: next_conns: {next_conns}')
            next_conns.pop()
            print(f'+++DEBUG: next_conns after pop: {next_conns}')
            
            self.get_cave_path(curr_path)

        print(f'+++DEBUG: bottom: {curr_path}')
        return curr_path




    def build_cave_list(self, input_list=None):
        """ Take list of paths, build a list of cave objects """
        if input_list is None:
            input_list = self.input_data

        for this_path in input_list:
            start_node, end_node = this_path.split('-')
            print(f'+++DEBUG: start_node, end_node: {start_node}, {end_node}')
            #--start nodes
            cave_index = self.get_cave_index_by_name(start_node)
            if cave_index < 0:
                self.cave_list.append(Cave(start_node, connection=end_node))
            else:
                self.cave_list[cave_index].add_connection(end_node)

            #--end nodes
            cave_index = self.get_cave_index_by_name(end_node)
            if cave_index < 0:
                self.cave_list.append(Cave(end_node, connection=start_node))
            else:
                self.cave_list[cave_index].add_connection(start_node)

        return self.cave_list


    def solve_part1(self):
        """
        How many paths through this cave system are there that visit
        small caves at most once?
        """
        part1_score = 0
        self.build_cave_paths_pt1()

        return part1_score


    def solve_part2(self):
        """ TODO: enter part 2 question here """
        part2_score = 0
        return part2_score


    def get_answer_key(self):
        """ return answer key"""
        return self.answer_key
