#!/usr/bin/env python2
# Combiner in: [decade:int|genre:str|averageRating:float|primaryTitle:str] out: [decade:int|genre:str|averageRating:float|primaryTitle:str] [decade:int|genre:str|title:str]
import sys

last_decade = None
last_genre = None

# Since the input comes ordered we ouput the best title of each genre and decade, this way we reduce the work that need to do the reducer afterwards (because since it has to be ordered we can only use one)
for line in sys.stdin:

    parts = line.strip().split("|")
    # we get the first decade and we print it since it is ordered from higher to lower
    if last_decade is None:
        last_decade = parts[0]
        last_genre = parts[1]
        print(parts[0] + "|" + parts[1] + "|" + parts[2] + "|"  + parts[3])

    # Every time the decade or genre chagnes we print the values
    elif last_decade != parts[0] or last_genre != parts[1]:
        last_decade = parts[0]
        last_genre = parts[1]
        print(parts[0] + "|" + parts[1] + "|" + parts[2] + "|" + parts[3])
