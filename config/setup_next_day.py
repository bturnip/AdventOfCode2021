""" Set up the next day's folder for AdventOfCode """
# -------------------------------------------------------------------- 
# setup_next_day.py 
# 20221126 Danny Anderson <bturnip@Heyday> 
# --------------------------------------------------------------------
import os
from os.path import basename
import shutil


# set variables
YEAR='2021'
AOC_VINTAGE= f'AdventOfCode{YEAR}'
BASEDIR = f'/home/bturnip/Documents/Code/python/advent_of_code/{AOC_VINTAGE}'

PUZZLE_STEPS = f'{BASEDIR}/config/puzzle_steps.yml'

print(f"+++INFO: BASEDIR:\n\t{BASEDIR}")


# check that BASEDIR is good
# -------------------------------------------------------------------- 
if os.path.exists(BASEDIR):
    print("+++INFO: Base directory is good...")
else:
    raise ValueError(f"+++ERROR: Base directory:{BASEDIR} not reachable")


# get dir contents, find out what next day will be
# -------------------------------------------------------------------- 
dir_list = os.listdir(BASEDIR)
day_list = [x for x 
              in dir_list 
              if x[0:3] == 'day'
                and x[3:].isnumeric()]

target_day = 0
for this_day in day_list:
    day_num = this_day[3:]
    if int(day_num) > target_day:
        target_day = int(day_num)
target_day += 1

target_folder = f'{BASEDIR}/day'+str(target_day)


# make target folders
# -------------------------------------------------------------------- 
print(f"+++INFO: Creating directories for Day{str(target_day)}...")
targets = [target_folder
            ,f'{target_folder}/input_files'
            ,f'{target_folder}/tests'
           ]
for this_dir in targets:
    print(f"\t- creating:.../{basename(this_dir)}")
    try:
        os.makedirs(this_dir)
    except FileExistsError:
        pass

# copy puzzle steps into target dir
# -------------------------------------------------------------------- 
print("+++INFO: copying steps YAML file")
src_path = PUZZLE_STEPS
dst_path = f'{target_folder}/steps_day{str(target_day)}.yml'
shutil.copy(src_path, dst_path)

# ready to rock and roll
# -------------------------------------------------------------------- 
print("+++INFO: folders ready, next step: git pull and branch!")


  
