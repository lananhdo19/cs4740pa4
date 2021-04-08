#!/usr/bin/env python3

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(",")
    # increase counters
    code = words[16].strip('"')
    if code == "A":
        print("Carrier\t1")
    if code == "B":
        print("Weather\t1")
    if code == "C":
        print("National Air System\t1")
    if code == "D":
        print("Security\t1")
