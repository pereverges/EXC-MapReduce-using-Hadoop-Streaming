#!/usr/bin/env python2
# Mapper in: name.basics.tsv title.crew.tsv title.ratings.tsv  out: [tconst:str|nconst:str|primaryName:str] [tconst:str|nconst:str] [tconst:str|numVotes:int]
import sys

SKIPVAL = '\\N'
DELIM = '\t'

for line in sys.stdin:
    # We read the three files making sure of avoiding missing values
    parts = line.strip().split(DELIM)
    if len(parts) == 6:
        if parts[0] != SKIPVAL and parts[1] != SKIPVAL and parts[5] != SKIPVAL:
            for tconst in parts[5].split(','):
                print(tconst + "|" + parts[0] + "|" + parts[1])
    elif isinstance(parts[1], float):
        if parts[0] != SKIPVAL and parts[2] != SKIPVAL:
            print(parts[0] + "|" + int(parts[2]))
    else:
        if parts[0] != SKIPVAL and parts[2] != SKIPVAL:
            for nconst in parts[2].split(','):
                print(parts[0] + "|" + nconst)
