#!/usr/bin/env python3
import sys

region_list = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) != 2:
        continue

    region_code = parts[0]
    try:
        std_dev = float(parts[1])
    except ValueError:
        continue

    region_list.append((region_code, std_dev))

# 在Reducer中进行排序并取前3
region_list.sort(key=lambda x: x[1], reverse=True)
top3 = region_list[:3]

for (rc, stdv) in top3:
    print(f"{rc}\t{stdv}")
