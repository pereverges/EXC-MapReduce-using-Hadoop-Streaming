#!/usr/bin/env python2
# Mapper in: title.basics.tsv && title.ratings.tsv  out: [tconst:str|primaryTitle:str|decade:int|genre:str] [tconst:str|averageRating:float]
import sys

SKIPVAL = '\\N'
DELIM = '\t'

for line in sys.stdin:
    # Split each line of the table to obtain the fields of each column
    parts = line.strip().split(DELIM)

    # If it is the title.basics.tsv we check that is type movie and it is on the range that we want
    if len(parts) == 9:
        if parts[0] != SKIPVAL and parts[1] != SKIPVAL and parts[1] == 'movie' and parts[2] != SKIPVAL and parts[5] != SKIPVAL and int(parts[5]) >= 1900 and int(parts[5]) <= 1999 and parts[8] != SKIPVAL:
            for genre in parts[8].split(','):
                print(parts[0] + "|" + parts[2] + "|" + parts[5][2] + "|" + genre)

    # if it is the title.ratings.tsv we check that it has values
    else:
        if parts[0] != SKIPVAL and parts[1] != SKIPVAL:
            print(parts[0] + "|" + parts[1])
