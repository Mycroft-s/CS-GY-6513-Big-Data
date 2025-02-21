#!/usr/bin/env python
import sys

def main(separator='\t'):
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # 第一步输出： word \t count
        word, count_str = line.split(separator)
        count = int(count_str)
        # 输出复合键：-count, word（占位符确保第三个字段存在）
        print(f"{-count}{separator}{word}{separator}")

if __name__ == "__main__":
    main()
