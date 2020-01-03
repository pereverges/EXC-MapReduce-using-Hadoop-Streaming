#!/usr/bin/env python2
# Reducer in: [decade:int|genre:str|averageRating:float|primaryTitle:str] out: [decade:int|genre:str|title:str]
import sys

last_decade = None
last_genre = None

# Here we repeat the same proces as we did in the combiner
for line in sys.stdin:

    parts = line.strip().split("|")

    if last_decade is None:
        last_decade = parts[0]
        last_genre = parts[1]
        print(parts[0] + "|" + parts[1] + "|" + parts[3])

    elif last_decade != parts[0] or last_genre != parts[1]:
        last_decade = parts[0]
        last_genre = parts[1]
        print(parts[0] + "|" + parts[1] + "|" + parts[3])
