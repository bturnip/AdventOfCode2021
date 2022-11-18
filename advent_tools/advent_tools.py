"""
2021 Advent of Code: Common tools
"""
DAY_NUM = 0
BASE_PATH = '/home/bturnip/Documents/Code/python/advent_of_code/'\
            'AdventOfCode2021/day{DAY_NUM}/'
DATA_FILE = 'day{DAY_NUM}_input.txt'

def get_input_file_name(day=DAY_NUM):
    """ return the input file name for this day's puzzle"""
    this_day = str(day)
    base_str = f"{BASE_PATH}{DATA_FILE}"
    input_file = base_str.replace("{DAY_NUM}",this_day)
    return input_file

def get_file_linecount(this_file):
    """ returns line count of file """
    return sum(1 for _ in open(this_file))

def load_input_file_into_list(this_file):
    """ Loads input file into a list and returns list"""
    # get line count
    line_count = get_file_linecount(this_file)
    if line_count == 0:
        return []

    # load file
    with open(this_file,'r') as file_stream:
        raw_load = file_stream.readlines()
        #list_result = list(map(int,raw_load))

    # check that the list and the line count match
    #line_count = 100
    if line_count != len(raw_load):
        err_mssg = (f"\n+++ERROR: file: [{this_file}] linecount [{line_count}]"\
                    f" does not match loaded list length [{len(raw_load)}]")
        raise ValueError(err_mssg)

    return raw_load

def intify_list(input_list):
    """ Takes a list and returns that list with all elements cast to int """
    if type(input_list) != list:
        err_mssg = (f"+++ERROR: input parameter {input_list} " \
                    f"+++ERROR: is not of type list")
        raise TypeError(err_mssg)

    return list(map(int,input_list))
    
    
    
