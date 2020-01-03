#!/usr/bin/env python2
# Reducer in: [genre:str|sum:int|count:int|min_runtime:int|max_runtime:int] out: [avg_runtime:float|max_runtime:int|min_runtime:int|genre:str]
import sys

last_val = None
totalSum = totalCount = 0
totalMin = totalMax = None

for line in sys.stdin:
    # Read each line that contains exactly one genre
    if len(line.strip().split('|')) == 2:
        genre, runtimeMinutes = line.strip().split('|')
        runIntMinutes = int(runtimeMinutes)
        if last_val is None:
            last_val = genre
            totalMin = runIntMinutes
            totalMax = runIntMinutes
        elif last_val != genre:
            if totalCount > 0:
                avg = float(float(totalSum)/totalCount)
            else:
                avg = 0
            print(str("{0:.2f}".format(round(avg,2))) + "|" + str(totalMax) + "|" + str(totalMin) + "|" + str(last_val))
            # reset the values
            last_val = genre
            totalSum = totalCount = 0
            totalMin = runIntMinutes
            totalMax = runIntMinutes

        totalSum += runIntMinutes
        totalCount += 1
        totalMin = min(runIntMinutes, totalMin)
        totalMax = max(runIntMinutes, totalMax)

    else:
        genre, sumOfTimes, count, min_runtime, max_runtime = line.strip().split('|')
        iSumOfTime = int(sumOfTimes)
        iCount = int(count)
        iMinRuntime = int(min_runtime)
        iMaxRuntime = int(max_runtime)

        # Assign the values for the first genre
        if last_val is None:
            last_val = genre
            totalMin = iMinRuntime
            totalMax = iMaxRuntime
        elif last_val != genre:
            # Calculate the average with the total sums from the combiners
            if totalCount > 0:
                avg = float(float(totalSum)/totalCount)
            else:
                avg = 0
            print(str("{0:.2f}".format(round(avg,2))) + "|" + str(totalMax) + "|" + str(totalMin) + "|" + str(last_val))
            # reset the values
            last_val = genre
            totalSum = totalCount = 0
            totalMin = iMinRuntime
            totalMax = iMaxRuntime

        # while we are in the same genre we sum the partial runtime sums from the Combiner
        # and the partial
        totalSum += iSumOfTime
        totalCount += iCount
        totalMin = min(iMinRuntime, totalMin)
        totalMax = max(iMaxRuntime, totalMax)

# Don't forget the last genre of the input
if totalCount > 0:
    avg = float(float(totalSum)/totalCount)
else:
    avg = 0
print(str("{0:.2f}".format(round(avg,2))) + "|" + str(totalMax) + "|" + str(totalMin) + "|" + str(last_val))
