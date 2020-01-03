#!/usr/bin/env python2
# Combiner in: [genre:str, runtimeMinutes:int] out: [genre:str|sum:int|count:int|min_runtime:int|max_runtime:int]

import sys

# value of last genre
# value of last runtime
# variable to store the minimum runtime for each genre (since we order the output fo the mapper increasingly)
last_val = min_runtime = last_min = None

# counters to have track of the whole sum for each genre and the number of sums
count = sumOfTimes = 0


for line in sys.stdin:
    genre, runtimeMinutes = line.strip().split('|')
    # cast to integer
    runIntMinutes = int(runtimeMinutes)

    # first value, we store each genre and its minimum runtime
    if last_val is None:
        last_val = genre
        min_runtime = runIntMinutes
    # change of genre (we have it ordered by genre and runtime ascending)
    elif last_val != genre:
        print(last_val + "|" + str(sumOfTimes) + "|" + str(count) + "|" + str(min_runtime) + "|" + str(last_min))
        # we reset the counter, assign the new genre and assign the minimum of this new gernre
        last_val = genre
        min_runtime = runIntMinutes
        sumOfTimes = count = 0

    # actualize the counters and safe each time the new runtime, since the last one will be the max we are looking for
    last_min = runIntMinutes
    sumOfTimes += runIntMinutes
    count += 1

print(last_val + "|" + str(sumOfTimes) + "|" + str(count) + "|" + str(min_runtime) + "|" + str(last_min))
