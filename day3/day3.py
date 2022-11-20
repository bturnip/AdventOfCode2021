"""
2021 Advent of Code: Day 2
"""
# suppress specific pylint checks (http://pylint-messages.wikidot.com/all-codes)
# pylint: disable=C0104, C0123, C0413, E0602
import sys
sys.path.append('/home/bturnip/Documents/Code/python/advent_of_code/AdventOfCode2021/advent_tools')
from advent_tools import *
import numpy as np


def create_2D_numpy_array(input_data):
    """ input list of binary strings & return numpy 2D array of ints """

    # sanity checks
    if (len(input_data) <= 0 or type(input_data) != list):
        err_mssg = "input to create_2D_numpy_array() must be a list of len > 0"
        raise ValueError(err_mssg)

    # convert strings to ints and return list
    string_arr = np.array([list(x) for x in input_data])
    return string_arr.astype(int)

def calculate_aoc_day3(input_data):
    """ Calculate the gamma, espilon, power_consumption rates """

    # Calculation method for gamma:
    #   - Input is a list of binary numbers.  To help with calculations,
    #     the list is loaded into a 2D numpy array.
    #   - For each column, count the number of 0's and 1's
    #   - Which ever value has a higher count becomes the value for that
    #     "bit" in the array
    #   - To quickly find this, sum each column, then divide the total by
    #     the number of rows in the array.  For any result > 0.5, there are
    #     more 1's in the column.  Since the values will range stricty
    #     between 0.0 and 1.0, we can round the result to get to the final
    #     answer for each column
    # Calculation methond for epsilon:
    #   - Epsilon rate is inverse of gamma rate.  If gamma_rate = "1001",
    #     epsilon rate = "0110"


    # sanity checks
    if (type(input_data) != np.ndarray or input_data.size <= 0 ):
        err_mssg = "input to calculate_aoc_day3() must " \
                   "be a numpy arrray with size > 0"
        raise ValueError(err_mssg)

    if check_np_array_values(input_data,[0,1]) is False:
        err_mssg = "+++ERROR: only values in [0,1] allowed in input array"
        raise ValueError(err_mssg)

    # initialize results dict
    submarine_status_dict = {"gamma":"0", "epsilon":"0"}

    # get array stats
    num_rows, num_cols = input_data.shape

    # calculate the final bits -----------------------------------------
    # Gamma rate steps:
    #   - Add up the columns sums
    #   - Divide the sums by the rowcount, rounding to 0 or 1
    #   - Cast results into a python list of strings
    #   - Coalesce values into single string, one bit per column
    # Epsilon rate steps:
    #   - Invert the bits of the gamma rate
    # Power consumption:
    #   - Convert the binary values of gamma and epsilon to ints
    #   - Multiply the int values together
    #   - Result is power consumption

    arr_sums = np.array(np.sum(input_data, axis = 0))
    arr_calc = np.around(arr_sums/num_rows)

    # gamma rate
    arr_list_gamma = list(arr_calc.astype(int).astype(str))
    gamma_rate = ''.join(arr_list_gamma)

    # espilon rate
    arr_epsilon = np.bitwise_xor(arr_calc.astype(int),1)
    arr_list_epsilon = list(arr_epsilon.astype(str))
    epsilon_rate = ''.join(arr_list_epsilon)

    # calc power consumption -------------------------------------------
    gamma_int = int(gamma_rate, base=2)
    epsilon_int = int(epsilon_rate, base=2)
    power_consumption = gamma_int * epsilon_int

    # update the results_dict ------------------------------------------
    submarine_status_dict["gamma"] = gamma_rate
    submarine_status_dict["epsilon"] = epsilon_rate
    submarine_status_dict["gamma_int"] = gamma_int
    submarine_status_dict["epsilon_int"] = epsilon_int
    submarine_status_dict["power_consumption"] = power_consumption
    # return results ---------------------------------------------------
    return submarine_status_dict

def calculate_aoc_day3_pt2(input_data,status_dict ):
    """ Calculate the oxygen_generator, co2_scrubber, life_support rates """
    # Function will add entries to status_dict for:
    #   - oxygen_generator
    #   - oxygen_generator_int
    #   - co2_scrubber
    #   - co2_scrubber_int
    #   - life_support
    # Calculation method for oxygen_generator:
    #   - For the 1st column/bit, determine frequency of the 1 0 values.
    #     Whichever value is higher (1's win tiebreaker), keep those rows
    #     and remove the rest from consideration.
    #   - Repeat this process with the nth column/bit, reducing the number
    #     of rows until there is only one left.
    #   - Convert the remaining item into an int for the final value.
    # Calculation method for co2_scrubber:
    #   - Repeat the steps for oxygen_generator, keeping the values with
    #     the digit that has the lower frequency for each position until
    #     there is only one left.
    #   - Convert binary digit to int
    # Calculation for life_support:
    #   - multiply the int values of oxygen_generator and co2_scrubber
    # """

    if (type(input_data) != np.ndarray or input_data.size <= 0 ):
        err_mssg = "input to calculate_aoc_day3() must " \
                   "be a numpy arrray with size > 0"
        raise ValueError(err_mssg)

    if check_np_array_values(input_data,[0,1]) is False:
        err_mssg = "+++ERROR: only values in [0,1] allowed in input array"
        raise ValueError(err_mssg)

    # oxygen_generator
    # get array stats
    oxy_gen = input_data.copy()
    num_cols = oxy_gen.shape[1]

    for c in range(num_cols):
        if len(oxy_gen) == 1:
            print(f"+++RESULTS:final answer found in {c} bits: {oxy_gen}")
            break

        test_col = oxy_gen[:,c]
        keep_bit = binary_frequency_select(test_col)

        # filter rows where bit #{c} matches keep_bit
        filter_arr = oxy_gen[:,c] == keep_bit
        oxy_gen=oxy_gen[filter_arr]

    # format oxygen result, store in status dict
    oxy_value = list(oxy_gen[0].astype(int).astype(str))
    oxygen_generation = ''.join(oxy_value)
    oxygen_generation_int = int(oxygen_generation, base=2)

    status_dict["oxygen_generation"]=oxygen_generation
    status_dict["oxygen_generation_int"]=oxygen_generation_int
    
    # co2_scrubber
    #-------------------------------------------------------------------
    # if later puzzles use this method, make it a function and toggle
    # the ==/!= operators
    #-------------------------------------------------------------------
    # get array stats
    co2_scrubber = input_data.copy()
    num_cols = co2_scrubber.shape[1]

    for c in range(num_cols):
        if len(co2_scrubber) == 1:
            print(f"+++RESULTS:final answer found in {c} bits: {co2_scrubber}")
            break

        test_col = co2_scrubber[:,c]
        keep_bit = binary_frequency_select(test_col)

        # filter rows where bit #{c} matches keep_bit
        filter_arr = co2_scrubber[:,c] != keep_bit
        co2_scrubber=co2_scrubber[filter_arr]

    # format oxygen result, store in status dict
    co2_value = list(co2_scrubber[0].astype(int).astype(str))
    co2_scrubber = ''.join(co2_value)
    co2_scrubber_int = int(co2_scrubber, base=2)

    status_dict["co2_scrubber"]=co2_scrubber
    status_dict["co2_scrubber_int"]=co2_scrubber_int 
    
    # life support calc
    status_dict["life_support"] = oxygen_generation_int * co2_scrubber_int
    
      
    
    
    return status_dict

def calculate_power_consumption(input_dict):
    """ Calculate power consumptions using gamma and epsilon """
    # NB: I don't need this separate function, but leaving in here
    # NB: for future reference.
    # sanity checks
    if (len(input_dict) < 2 or type(input_dict) != dict):
        err_mssg = "+++ERROR: input to calculate_power_consumption() "\
                   "must be a dict with gamma and epsilon keys"
        raise ValueError(err_mssg)

    required_keys = ["gamma","epsilon"]
    keys_present = check_dict_keys(required_keys,input_dict)

    if keys_present is False:
        err_mssg = "+++ERROR: input dict missing at least one of" \
                   " the required keys: {required_keys}"
        raise ValueError(err_mssg)

    #gamma = input_dict["gamma"]
    #epsilon = input_dict["epsilon"]
    return 0
