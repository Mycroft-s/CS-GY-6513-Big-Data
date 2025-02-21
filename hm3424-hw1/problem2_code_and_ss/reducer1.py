#!/usr/bin/env python
"""An simple Reducer """

import sys


# receive the output of a mapper, (key, [value, value, ...])
def read_mapper_output(input, separator='\t'):
    for line in input:
        #  return each (key, [value, value, ...]) tuple
        #  though there is only one key and one value per line in hadoop streaming
        yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)

    # get the next K,V
    # In hadoop streaming, the "sequence" is sent as an sorted list, one k,v per line
    last_key = None
    counter = 0
    for key, value in data:
        # new key?
        if key != last_key:
            if last_key is not None:
                print("%s%s%d" % (last_key, separator, counter))
                counter = 0

        last_key = key
        # add this word count
        try:
            # value is a string
            counter += int(value)
        except ValueError:
            # count was not a number, so silently discard this item
            pass
    # no more input; empty the counter
    if last_key is not None:
        print("%s%s%d" % (last_key, separator, counter))


if __name__ == "__main__":
    main()