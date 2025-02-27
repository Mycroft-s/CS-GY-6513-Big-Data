#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""

import sys
import re

def read_input(input):
    for line in input:
        # normalize to lowercase and alphanumeric
        line1 = re.sub("[^0-9a-z ]+", " ", line.lower()).strip()
        # split the line into words; keep returning each word
        yield line1.split()


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)

    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
            print('%s%s%d' % (word, separator, 1))
            # keep a global counter: total words seen
            sys.stderr.write("reporter:counter:homework1,words,1\n")


# how to test locally in bash/linus: cat  | python mapper.py
if __name__ == "__main__":
    main()
