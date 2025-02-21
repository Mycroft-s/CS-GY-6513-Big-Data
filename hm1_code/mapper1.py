#!/usr/bin/env python
import sys
import re

def read_input(input):
    for line in input:
        # 1) 转小写
        line = line.lower().strip()
        # 2) 将非字母数字字符替换为空格
        line = re.sub(r'[^a-z0-9]', ' ', line)
        # 3) 拆分单词并过滤纯数字
        words = line.split()
        for word in words:
            # 新增条件：跳过纯数字的单词（如"1234"）
            if not word.isdigit():
                yield word

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            # 输出 word \t 1
            print(f"{word}{separator}1")

if __name__ == "__main__":
    main()
