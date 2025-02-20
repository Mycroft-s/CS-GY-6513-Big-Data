#!/usr/bin/env python
import sys
import re

def read_input(input):
    for line in input:
        # 1) 转小写
        line = line.lower()
        # 2) 将非字母数字字符替换为空格
        line = re.sub('[^a-z0-9]', ' ', line)
        # 3) split 拆分
        words = line.split()
        # 返回拆分出的单词列表
        yield words

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            # 输出 word \t 1
            print(f"{word}{separator}1")

if __name__ == "__main__":
    main()
