#!/usr/bin/env python2
# Combiner in: [votes:int|primaryName:str] out: [votes:int|primaryName:str]

import sys

count = 0
# This structure will only 10 elements, so the space is constant O(10) = O(1)
listOfWriters = []

# Since the input comes ordered we only have to take 10 first best ones without repetition
for line in sys.stdin:
    # Split each line of the table to obtain the fields of each column
    parts = line.strip().split("|")

    # if we have 10 writers we dont have to process more data
    if count == 10:
        continue

    if count == 0:
        print(parts[0] + "|" + parts[1])
        listOfWriters.append(parts[1])
        count += 1
    # if we dont have 10 wirters and we still have not printed the new writer we print it and then we add him to the list
    elif parts[1] not in listOfWriters:
        print(parts[0] + "|" + parts[1])
        listOfWriters.append(parts[1])
        count += 1
