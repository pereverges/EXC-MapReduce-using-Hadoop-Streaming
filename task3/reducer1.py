#!/usr/bin/env python2
# Reducer in: [tconst:str|primaryTitle:str|decade:int|genre:str] [tconst:str|averageRating:float] out: [decade:int|genre:str|averageRating:float|primaryTitle:str]
import sys

last_val = None
last_avg = None

# In this reducer we want to join by tconst key, since we hve order them we know that
# first will come the file of two fields and then the other
for line in sys.stdin:
    # Split each line of the table to obtain the fields of each column
    parts = line.strip().split("|")

    if last_val is None:
        # If length is 2 we save the const (to merge) and the averageRating
        if len(parts) == 2:
            last_val = parts[0]
            last_avg = parts[1]
    # If we have a match we print it
    elif last_val == parts[0]:
        print(parts[2] + "|" + parts[3] + "|" + last_avg + "|" + parts[1])
    # If length is 2 we save the const (to merge) and the averageRating
    elif len(parts) == 2:
        last_val = parts[0]
        last_avg = parts[1]
