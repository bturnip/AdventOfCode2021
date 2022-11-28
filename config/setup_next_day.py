""" Set up the next day's folder for AdventOfCode """
# --------------------------------------------------------------------
# setup_next_day.py
# 20221126 Danny Anderson <bturnip@Heyday>
# --------------------------------------------------------------------
import os
from os.path import basename, isfile
import shutil

# --function defs----------------------------------------------------
def check_dir (fullpath, short_name=None):
    """ Check that a directory exists """
    if short_name is None:
        display_name = f"[.../{basename(fullpath)}]"
    else:
        display_name = f"[{short_name}]"

    if os.path.exists(fullpath):
        print(f"+++INFO:  {display_name} directory is good...")
    else:
        raise ValueError(f"+++ERROR: [{display_name}] in not reachable:\n"\
                         f"{fullpath}")

def set_next_day_number():
    """ looks in full path for day* files, picks the next one """
    dir_list = os.listdir(BASEDIR)
    day_list = [x for x
              in dir_list
              if x[0:3] == 'day'
                and x[3:].isnumeric()]

    target = 0
    for this_day in day_list:
        day_num = this_day[3:]
        if int(day_num) > target:
            target = int(day_num)
    target += 1
    return target


def copy_templates (day_number,target_folder):
    """ Process TEMPLATE_DESTINATIONS """
    # template list entries look like:
    # [<template file>, <destination folder>, <new_file_pattern>]
    # ['puzzle_steps.yml', '{DAY_FOLDER}','steps_{DAY_NUM}.yml']
    # ------------------------------------------------------------
    global error_count
    for this_template in TEMPLATE_LIST:
        PROCESS_FILE = True
        #-- get src path
        src_file = f'{TEMPLATES_DIR}/{this_template[0]}'
        #-- check src exists
        if not isfile(src_file):
            print(f"\t+++ERROR: did not find template:\n" \
                  f"\t+++ERROR:[{src_file}]\n" \
                  f"\t+++ERROR:, skipping [{basename(src_file)}]...")
            error_count += 1
            PROCESS_FILE = False

        if PROCESS_FILE:
            #-- set target
            t_folder = str(this_template[1])                  \
                      .replace("{DAY_FOLDER}",target_folder)  \
                      .replace("{BASEDIR}",BASEDIR)

            t_file = str(this_template[2]).replace("{DAY_NUM}","day"+str(day_number))
            target_file = f'{t_folder}/{t_file}'

            #-- check target, do not overwrite
            if isfile(target_file):
                print(f"+++WARNING: file already exists: {target_file}, skipping...")
                break

            # -- copy template files to target folder
            print(f"\t- copying {os.path.basename(src_file)} " \
                  f"---> {os.path.basename(target_file)}")
            shutil.copy(src_file,target_file)




# --program start-----------------------------------------------------

# --set variables
YEAR='2021'
AOC_VINTAGE= f'AdventOfCode{YEAR}'

# ---list key: [<template file>, <destination folder>, <new_file_pattern>]
TEMPLATE_LIST = [
    ['puzzle_steps.yml', '{DAY_FOLDER}','steps_{DAY_NUM}.yml']
    ,['setup.cfg','{DAY_FOLDER}','setup.cfg']
    ,['config_dayNUM.py','{DAY_FOLDER}','config_{DAY_NUM}.py']
    ,['dayNUM.py','{DAY_FOLDER}','{DAY_NUM}.py']
    ,['solve_dayNUM.py','{DAY_FOLDER}','solve_{DAY_NUM}.py']
    ,['requirements_dayNUM.txt','{BASEDIR}','requirements_{DAY_NUM}.txt']
    ,['test_dayNUM.py','{DAY_FOLDER}/tests','test_{DAY_NUM}.py']
    ,['dayNUM.yml','{BASEDIR}/.github/workflows','run_{DAY_NUM}.yml']
    ]

error_count = 0


# --------------------------------------------------------------------
STEP="set paths and check"
print(f"+++INFO:{STEP}")
# --------------------------------------------------------------------
BASEDIR = f'/home/bturnip/Documents/Code/python/advent_of_code/{AOC_VINTAGE}'
TEMPLATES_DIR = f'{BASEDIR}/config/templates'

check_dir(BASEDIR,"Base path")
check_dir(TEMPLATES_DIR)


# --------------------------------------------------------------------
STEP="get dir contents, set next day"
print(f"+++INFO:{STEP}")
# --------------------------------------------------------------------
target_day = set_next_day_number()

# --------------------------------------------------------------------
STEP="set target folder, create directory structure"
print(f"+++INFO:{STEP}")
# --------------------------------------------------------------------
target_folder = f'{BASEDIR}/day'+str(target_day)

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


# --------------------------------------------------------------------
STEP="copy templates"
print(f"+++INFO:{STEP}")
# --------------------------------------------------------------------
copy_templates(target_day,target_folder)
#print("+++INFO: copying steps YAML file")
#src_path = PUZZLE_STEPS
#dst_path = f'{target_folder}/steps_day{str(target_day)}.yml'
#shutil.copy(src_path, dst_path)

# ready to rock and roll
# --------------------------------------------------------------------
print("+++INFO: folders ready, next step: git pull and branch!")
