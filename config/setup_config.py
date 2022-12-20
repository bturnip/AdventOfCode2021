""" config file for setup_next_day.py """

YEAR='2021'
AOC_VINTAGE= f'AdventOfCode{YEAR}'

ROOT = f'/home/bturnip/Documents/Code/python/advent_of_code/'
BASEDIR = f'{ROOT}{AOC_VINTAGE}'

TEMPLATES_DIR = f'{BASEDIR}/config/templates'
ARCHIVE_DIR = f'{ROOT}.archives/'

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
    ,['git_commands_dayNUM.py','{DAY_FOLDER}','git_commands_{DAY_NUM}.py']
    ]

