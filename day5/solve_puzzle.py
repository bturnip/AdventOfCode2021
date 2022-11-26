""" Advent Of Code 2021 Day 5 driver """
from day5 import *
from config_day5 import *

# file chooser -----------------------------------

# -- uncomment one of these file choices below
this_file = FULL_FILE
#this_file = TEN_LINE_SAMPLE
print(f"+++INFO: using {this_file}")

test_vent_coords = np.array([
[777,778,777,676]
,[500,510,378,510]
,[441,657,441,638]
,[724,480,724,778]
,[702,85,44,85]
,[973,961,28,16]
,[913,125,483,125]
,[714,895,870,739]
,[273,774,273,795]
,[623,450,623,616]
])
# print(test_vent_coords)

# puzzle runner ----------------------------------
puzzle = Day5(this_file)
print(f"raw map counts:{puzzle.get_map_counts()}")
print(f"Part 1 puzzle answer:{puzzle.get_part1_answer()}")






