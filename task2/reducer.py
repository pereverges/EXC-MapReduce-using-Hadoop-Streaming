#!/usr/bin/env python2
# Reducer in: [genre:str] out: [genre:str]
import sys

last_val = None
last_title = None

# In the reducer we get the data ordered, which means that first will arrive the lines with size 1 and after if
# we have a match the tconst plus the name of the movie, this way we only have to store one varaible in memory
for line in sys.stdin:
    # Split each line of the table to obtain the fields of each column
    parts = line.strip().split('|')

    # if we dont have any value saved and comes without title, we save it
    if last_val is None and len(parts) == 1:
        last_val = parts[0]
    # if the value saved mathces the new one and the data has the title then we printe the title of the movie
    elif len(parts) == 2 and last_val == parts[0]:
        print(parts[1])
    # if the data is only the tconst we save to compare it with the next one
    elif len(parts) == 1:
            last_val = parts[0]
