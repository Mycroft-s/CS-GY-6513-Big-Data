#!/usr/bin/env python
import sys

def main(separator='\t'):
    idx = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        neg_count_str, word = line.split(separator)
        idx += 1
        # 输出： ID \t word
        print(f"{idx}{separator}{word}")

if __name__ == "__main__":
    main()
