""" Set up the next day's folder for AdventOfCode """
# --------------------------------------------------------------------
# setup_next_day.py
# 20221126 Danny Anderson <bturnip@Heyday>
# --------------------------------------------------------------------
import os
import argparse
from os.path import basename, isfile
import shutil
from setup_config import *

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
    error_count = 0
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

            file_in = open(src_file,"rt")
            file_out = open(target_file,"wt")

            print(f"\t- populating {os.path.basename(target_file)} " )

            for line in file_in:
                file_out.write(line.replace("{DAY_NUM}","day"+str(target_day)) \
                               .replace("{NUM}",str(target_day)) \
                               .replace("{NEXT_DAY_NUM}","day"+str(target_day + 1))
                       )
            file_in.close()
            file_out.close()


# --program start-----------------------------------------------------
#-- parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-nb", "--nobackup"\
                    ,help = "skip the archive creation step" \
                    , action = "store_true")

args = parser.parse_args()

# --------------------------------------------------------------------
STEP="check paths imported from setup_config"
print(f"+++INFO:{STEP}")
# --------------------------------------------------------------------
check_dir(BASEDIR,"Base path")
check_dir(TEMPLATES_DIR, "Templates")
check_dir(ARCHIVE_DIR, "Archive storage")


# --------------------------------------------------------------------
STEP="set variables: target_day, target_folder"
print(f"+++INFO:{STEP}")
# --------------------------------------------------------------------
target_day = set_next_day_number()
target_folder = f'{BASEDIR}/day'+str(target_day)


# --------------------------------------------------------------------
STEP=f"archive entire AoC {YEAR} folder"
print(f"+++INFO:{STEP}")
# --------------------------------------------------------------------
if args.nobackup:
    print("\t - Archive step skipped by command argument")
else:
    archive_name=f'{ARCHIVE_DIR}{AOC_VINTAGE}_day{target_day-1}'
    shutil.make_archive(archive_name, 'zip', BASEDIR)
    zipped_file = f'{archive_name}.zip'

    if not isfile(zipped_file):
        print(f"+++ERROR: Did not find {basename(zipped_file)} in \n" \
              f"+++ERROR: ARCHIVE_DIR: {ARCHIVE_DIR} \n" \
              f"+++ERROR: Archive manually.")
    else:
        print(f"+++INFO:{basename(zipped_file)} created...")


# --------------------------------------------------------------------
STEP="create directory structure"
print(f"+++INFO:{STEP}")
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

# --------------------------------------------------------------------
STEP="copy templates"
print(f"+++INFO:{STEP}")
# --------------------------------------------------------------------
copy_templates(target_day,target_folder)


# ready to rock and roll
# --------------------------------------------------------------------
print(f"+++INFO: Day{target_day} folders ready, next step: git pull and branch!")
