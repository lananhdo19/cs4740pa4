#!/usr/bin/env python3

from operator import itemgetter
import sys

current_airline = None
current_depart = None
current_dest = None
current_delay = 0
current_count = 1
airline = None
depart = None
dest = None
delay = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    airline, depart, dest, delay = line.split('\t', 3)

    # convert delay (currently a string) to int
    try:
        delay = int(delay)
    except delayError:
        # delay was not a number, so silently
        # ignore/discard this line
        print("error: " + line)
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: airline) before it is passed to the reducer
    if current_airline == airline and current_depart == depart and current_dest == dest:
        current_delay += delay
        current_count += 1
    else:
        if current_airline:
            current_avg = current_delay / current_count    
            # write result to STDOUT
            print("{0}\t{1}\t{2}\t{3}".format(current_airline, current_depart, current_dest, current_avg))
        current_airline = airline
        current_dest = dest
        current_depart = depart
        current_delay = delay
        current_count = 1

# do not forget to output the last airline if needed!
if current_airline == airline and current_depart == depart and current_dest == dest:
    current_avg = current_delay / current_count
    print("{0}\t{1}\t{2}\t{3}".format(current_airline, current_depart, current_dest, current_avg))

