#!/usr/bin/env python
import sys
import re

def read_input(input):
    for line in input:
        line = line.lower().strip()
        line = re.sub(r'[^a-z0-9]', ' ', line)
        words = line.split()
        for word in words:
            # 跳过纯数字
            if not word.isdigit():
                yield word

def main(separator='\t'):
    data = read_input(sys.stdin)
    for word in data:
        print(f"{word}{separator}1")

if __name__ == "__main__":
    main()
