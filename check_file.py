# Check missing line header in datasets

import os, sys
import re

file_list = ["A", "B", "C", "D", "E", "F", "G"]

for file in file_list:
    ln = 1
    file += ".txt"
    print(f'{file}.txt : ')
    with open(os.path.join(sys.path[0], "origin_data/", file), "r") as f:
        for i in f.readlines():
            if not bool(re.match(r"^\$GP", i)):
                print(ln)
            ln += 1


## OUTPUT : 
#
# A.txt.txt : 
# 67
# 135
# 174
# B.txt.txt : 
# C.txt.txt : 
# D.txt.txt : 
# E.txt.txt : 
# F.txt.txt : 
# 28
# 29
# G.txt.txt : 