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

    id = 1

    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)

    # get the next K,V
    # In hadoop streaming, the "sequence" is sent as a sorted-by-key list, one k,v per line
    last_key = None
    values = []
    for key, value in data:
        # track all words with this count (key)
        values.append(value)

        # new key?
        if key != last_key:
            if last_key is not None:
                for v in values:
                    print("%d%s%s" % (id, separator, v))
                    # next id
                    id += 1
                values = []

        last_key = key

    # no more input; empty the counter
    if last_key is not None:
        for v in values:
            print("%d%s%s" % (id, separator, v))
            # next id
            id += 1

if __name__ == "__main__":
    main()
