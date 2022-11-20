"""
2021 Advent of Code: Common tools

"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=C0123, R1705

import numpy as np

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

def load_input_file_into_list(this_file,strip_newline=False):
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
    if line_count != len(raw_load):
        err_mssg = (f"\n+++ERROR: file: [{this_file}] linecount [{line_count}]"\
                    f" does not match loaded list length [{len(raw_load)}]")
        raise ValueError(err_mssg)

    if strip_newline:
        print("+++INFO: Stripping newlines in file load...")
        return [x.rstrip() for x in raw_load]
    else:
        return raw_load

def intify_list(input_list):
    """ Takes a list and returns that list with all elements cast to int """
    if type(input_list) != list:
        err_mssg = (f"+++ERROR: input parameter {input_list} " \
                    f"+++ERROR: is not of type list")
        raise TypeError(err_mssg)

    return list(map(int,input_list))

def check_dict_keys(key_list, dict_to_check):
    """ Takes a key list and checks dict that all keys exist"""
    # sanity checks
    if type(key_list) != list:
        raise TypeError()
    if type(dict_to_check) != dict:
        raise TypeError()
    if len(key_list) == 0:
        err_mssg = "+++ERROR: key_list cannot be empty"
        raise ValueError(err_mssg)
    if len(dict_to_check) == 0:
        err_mssg = "+++ERROR: dict_to_check cannot be empty"
        raise ValueError(err_mssg)

    for this_key in key_list:
        if this_key not in dict_to_check:
            err_mssg = f"+++ERROR: {this_key} not found in dict"
            print(err_mssg)
            return False

    return True

def bin_str_to_int(binary_str):
    """ Takes a str that looks like a binary number and returns int """
    err_mssg = "+++ERROR: bin_str_to_int() input must be "\
               "a string with only '1' and '0' chars."
    # sanity checks
    if (type(binary_str) != str) or (len(binary_str) <  1) \
       or (len(binary_str.replace('1','').replace('0','')) > 0):
        raise ValueError(err_mssg)

    return int(binary_str,base=2)

def check_np_array_values(this_arr, valid_values):
    """ checks that np array only has values given in list"""
    # sanity checks
    err_mssg = "+++ERROR: check_np_array_values(this_arr, valid_values)"\
               "takes a non-empty numpy array, and a non-empty list of " \
               "valid values to check against."
    if (type(this_arr) != np.ndarray) or (type(valid_values) != list):
        raise TypeError()
    if (this_arr.size < 1) or (len(valid_values) < 1):
        raise ValueError(err_mssg)

    # check data, return True if everything is ok, False otherwise
    # get arr stats
    if this_arr.ndim == 1:
        is_single_row = True
        num_rows = 1
    else:
        is_single_row = False
        num_rows = this_arr.shape[0]

    for r in range(num_rows):
        if is_single_row:
            this_row = this_arr
        else:
            this_row = this_arr[r]

        filter_arr = this_row[np.in1d(this_row, valid_values)]

        if len(this_row) != len(filter_arr):
            print (f"+++ERROR: row number{r} in array has "\
                   f"[{len(this_row) - len(filter_arr)}] invalid values"\
                   f"...stopping at first error.")
            return False
    return True

def binary_frequency_select(input_arr):
    """ takes an array of 1's and 0's, returns val with highest frequency """
    # sanity checks
    if(type(input_arr) != np.ndarray) \
        or (input_arr.size <= 0):
        err_mssg = "+++ERROR: input to binary_frequency_select() " \
                   "must be a numpy arrray with size > 0"
        raise ValueError(err_mssg)
    if input_arr.ndim > 1:
        err_mssg = "+++ERROR: input array can only have 1 dimension.)"

    value_check_passes = check_np_array_values(input_arr,[0,1])

    if value_check_passes is False:
        err_mssg = "+++ERROR: only values in [0,1] allowed in input array"
        raise ValueError(err_mssg)

    freq = np.bincount(input_arr)
    # - bincount will return a list with len of 1 or 2
    # - if result is len(1), it implies that the results were all "0""
    # - if result is len(2), it implies there are zero or more "0" values
    #   and at least one "1" value
    # - NB: numpy rounds down on .5 values, ie. 0.5 --> to 0.0, so we 
    #   need to check the value directly
    if len(freq) == 2:
        decimal_result = freq[1]/input_arr.size
        if decimal_result >= 0.5:
            return 1
        else:
            return 0
    return 0

