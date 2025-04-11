#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) != 2:
        continue
    region_code = parts[0]
    std_str = parts[1]
    print(f"{region_code}\t{std_str}")
