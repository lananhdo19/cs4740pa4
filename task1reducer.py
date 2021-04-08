#!/usr/bin/env python3

from operator import itemgetter
import sys

current_word = None
current_count = 1
current_value = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, value = line.split('\t', 1)
   # print("{0}\t{1}\t{2}".format(word, value, current_count))
    # convert value (currently a string) to int
    #value = value.split('.')[0]
    try:
        value = int(value)
    except ValueError:
        # value was not a number, so silently
        # ignore/discard this line
        print("error: " + line)
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_value += value
        current_count += 1
    else:        
        if current_word:
            current_avg = current_value / current_count    
            # write result to STDOUT
            print("{0}\t{1}".format(current_word, current_avg))
           # print("{0}\t{1}\t{2}\t{3}".format(current_word, current_avg, current_value, current_count))
        current_value = value
        current_word = word
        current_count = 1

# do not forget to output the last word if needed!
if current_word == word:
    print("{0}\t{1}".format(current_word, current_value/current_count))
  #   current_avg = current_value / current_count    
 #    print("{0}\t{1}\t{2}\t{3}".format(current_word, current_avg, current_value, current_count))
