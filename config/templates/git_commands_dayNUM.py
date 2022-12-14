#!/bin/bash
# confirm correct day is current branch?
# from {DAY_NUM} folder:
git checkout -b {DAY_NUM}

git add {BASEDIR}/.github/workflows/run_{DAY_NUM}.yml 
git add {BASEDIR}/requirements_{DAY_NUM}.txt 
git add {DAY_FOLDER}/setup.cfg

git add {DAY_FOLDER}/tests/test_{DAY_NUM}.py
git add {DAY_FOLDER}/*.py

git add -f {DAY_FOLDER}/input_files/*.txt

git commit -am"{DAY_NUM}: initial commit of auto-generated templates"
git push -u origin {DAY_NUM}





