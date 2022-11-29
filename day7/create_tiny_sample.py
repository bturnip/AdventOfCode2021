""" Generate tiny sample for Day 7 puzzle"""
from config_day7 import *

source_dict = {0:1,1:15,2:19,3:14}

target_file = TINY_SAMPLE

output_file = open(target_file, "w")

data=[]
    
for k,v in source_dict.items():
    for d in range(v):
        data.append(k)

output_line=",".join(str(x) for x in data)

output_file.write(output_line)

print(f'+++DEBUG: source_dict: {source_dict}')
print(f'+++DEBUG: output_line: {output_line}')

