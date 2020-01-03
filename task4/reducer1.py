#!/usr/bin/env python2
# Reducer in: [tconst:str|nconst:str|primaryName:str] [tconst:str|nconst:str] [tconst:str|numVotes:int]  out: [votes:int|primaryName:str]

import sys

last_tconst1 = None
last_tconst2 = None
last_num1 = None

#the file comes ordered by tconst then by nconst and lastly by numVotes, this will make that the last values comes first, then the second ones and lastly the first one
for line in sys.stdin:
    parts = line.strip().split("|")

    # Get the first time that the last values ([tconst:str|numVotes:int]) come in, then we save them to compare them with the following ones
    if last_tconst1 is None and len(parts) == 2 and parts[1][0:2] != "nm":
        last_tconst1 = parts[0]
        last_num1 = parts[1]

    # if we dont have a match and the values that are coming ([tconst:str|numVotes:int]) we save them
    elif last_tconst1 != parts[0] and len(parts) == 2 and parts[1][0:2] != "nm":
        last_tconst1 = parts[0]
        last_num1 = parts[1]

    # if we have a match between [tconst:str|nconst:str] and [tconst:str|numVotes:int] we save the name and the second tconst
    elif last_tconst1 == parts[0] and len(parts) == 2:
        last_tconst2 = parts[0]
        last_nconst2 = parts[1]

    # if the two previous ones had a match and the third one are this values [tconst:str|nconst:str|primaryName:str] and the tconst match, then we print the output
    elif last_tconst1 == last_tconst2 and last_tconst2 == parts[0] and last_nconst2 == parts[1] and len(parts) == 3:
        print(last_num1 + "|" + parts[2])
