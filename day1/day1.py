"""
2021 Advent of Code: Day 1
"""
DATA_PATH = '/home/bturnip/Documents/Code/python/advent_of_code/2021/day1/'
DATA_FILE = 'day1_input.txt'
INPUT_FILE = f"{DATA_PATH}{DATA_FILE}"


def create_windowed_list(input_list,chunk_size):
    """
    returns an output list by creating each list element
    as the sum of the chunk_size windows of the input list
    """
    # sanity checks
    if (len(input_list) <= 0 or len(input_list) < chunk_size):
        err_mssg = (f"length of input list({len(input_list)}) "\
                   f"cannot be zero or less than "\
                   f"chunk_size ({chunk_size})")

        raise ValueError(err_mssg)

    # start building windowed sums
    i = 0
    last_index = chunk_size
    max_index = len(input_list)
    output_list = []

    while last_index <= max_index:
        output_list.append( sum(input_list[i:last_index]) )
        #print(f'i:{i},last_index:{last_index}, elements: {input_list[i:last_index]}')
        i+=1
        last_index +=1

    return output_list

def count_depth_increases(input_list):
    """
    takes a list and counts the number of increases from one measurement
    to the next.
    """
    i = 1
    increase_count = 0

    while i < len(input_list):
        prev = int(input_list[i-1])
        curr = int(input_list[i])
        #print(f'prev: {prev}\tcurr:{curr}')
        if prev < curr:
            increase_count += 1
        i += 1

    return increase_count

def load_input_file_into_list(input_file):
    """ Loads input file into a list and returns list"""
    with open(input_file,'r') as f:
        raw_load = f.readlines()
        list_result = list(map(int,raw_load))

    return list_result
