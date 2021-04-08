#!/usr/bin/env python3

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(",")
    # increase counters
    airline = words[1]
    delay = words[14].rstrip('0').rstrip('.')
    if words[14] == "":
        delay = 0
    print("{0}\t{1}".format(airline, delay))
