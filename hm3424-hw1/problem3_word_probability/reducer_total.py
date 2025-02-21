#!/usr/bin/env python
import sys

def main(separator='\t'):
    total_count = 0
    for line in sys.stdin:
        line = line.strip()
        # line 应当是 "word  count"
        word, count_str = line.split(separator)
        count = int(count_str)
        total_count += count

    # 只输出一行: "TOTAL_COUNT    total_count"
    print(f"TOTAL_COUNT{separator}{total_count}")

if __name__ == "__main__":
    main()
