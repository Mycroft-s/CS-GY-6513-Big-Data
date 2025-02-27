#!/usr/bin/env python

import sys

def read_input(input):
    for line in input:
        # split the line into words; keep returning each word
        yield line.strip().split()


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)

    for payload in data:
        key, value = payload
        # reverse the key and value: we want word counts to be the keys
        # building a compound key; will instruct hadoop to sort numerically and
        # /partition by the "1."
        print('1.%s%s%s' % (value, separator, key))


# how to test locally in bash/linus: cat  | python mapper.py
if __name__ == "__main__":
    main()
