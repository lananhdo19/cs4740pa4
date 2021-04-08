#!/usr/bin/env python3

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(",")
    # increase counters
    airline = words[1].strip('"')
    delay = words[14].rstrip('0').rstrip('.')
    if words[14] == "":
        delay = 0
    depart = words[4].strip('"')
    dest = words[9].strip('"')
    if airline == "OH" or airline == "YV" or airline == "G4":
        print("{0}\t{1}\t{2}\t{3}".format(airline, depart, dest, delay))
