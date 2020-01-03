#!/usr/bin/env python2
# Mapper in: title.basics.tsv title.ratings.tsv  out: [tconst:str|primaryTitle:str] [tconst:str]
import sys

SKIPVAL = '\\N'
DELIM = '\t'

for line in sys.stdin:
    # Split each line of the table to obtain the fields of each column
    parts = line.strip().split(DELIM)

    # If we are reading from title.basics.tsv
    if len(parts) == 9:
        # If the fields we are looking for have values and the type is movie and the realase date is between 1990 and 2018
        if parts[1] != SKIPVAL and parts[2] != SKIPVAL and parts[5] != SKIPVAL and parts[1] == 'movie' and int(parts[5]) >= 1990 and int(parts[5]) <= 2018:
            print(parts[0] + "|" + parts[2])

    # If we are reading from title.ratings.tsv
    else:
        # If the fields we are looking for have values and the average is grater than 7.5 and the number of votes is higher than 500000
        if parts[0] != SKIPVAL and parts[1] != SKIPVAL and parts[2] != SKIPVAL and float(parts[1]) >= 7.5 and int(parts[2]) >= 500000:
            print(parts[0])
