#!/usr/bin/env python2
# Mapper in: [votes:int|primaryName:str] out: [votes:int|primaryName:str]
import sys

for line in sys.stdin:
    # Split each line of the table to obtain the fields of each column
    print(line)
