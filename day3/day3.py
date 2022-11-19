"""
2021 Advent of Code: Day 2
"""
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
    """ Calculate the gamma and espilon rate, returned in a dict """

    """
    Calculation method for gamma:
      - Input is a list of binary numbers.  To help with calculations,
        the list is loaded into a 2D numpy array.
      - For each column, count the number of 0's and 1's
      - Which ever value has a higher count becomes the value for that
        "bit" in the array
      - To quickly find this, sum each column, then divide the total by
        the number of rows in the array.  For any result > 0.5, there are
        more 1's in the column.  Since the values will range stricty
        between 0.0 and 1.0, we can round the result to get to the final
        answer for each column
    Calculation methond for epsilon:
      - Epsilon rate is inverse of gamma rate.  If gamma_rate = "1001",
        epsilon rate = "0110"
    """

    # sanity checks
    if (type(input_data) != np.ndarray or input_data.size <= 0 ):
        err_mssg = "input to calculate_aoc_day3() must " \
                   "be a numpy arrray with size > 0"
        raise ValueError(err_mssg)

    # initialize results dict
    rate_dict = {"gamma":"0", "epsilon":"0"}

    # get array stats
    num_rows, num_cols = input_data.shape

    # calculate the final bits -----------------------------------------
    """
    Gamma rate steps:
      - Add up the columns sums
      - Divide the sums by the rowcount, rounding to 0 or 1
      - Cast results into a python list of strings
      - Coalesce values into single string, one bit per column
    Epsilon rate steps:
      - Invert the bits of the gamma rate
    Power consumption:
      - Convert the binary values of gamma and epsilon to ints
      - Multiply the int values together
      - Result is power consumption
    """
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
    rate_dict["gamma"] = gamma_rate
    rate_dict["epsilon"] = epsilon_rate
    rate_dict["gamma_int"] = gamma_int
    rate_dict["epsilon_int"] = epsilon_int
    rate_dict["power_consumption"] = power_consumption
    # return results ---------------------------------------------------
    return rate_dict

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

    if keys_present== False:
        err_mssg = f"+++ERROR: input dict missing at least one of" \
                    " the required keys: {required_keys}"
        raise ValueError(err_mssg)

    gamma = input_dict["gamma"]
    epsilon = input_dict["epsilon"]
    return



