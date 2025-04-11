#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    fields = line.split(',')
    if len(fields) != 6:
        # 数据不符合格式，直接跳过
        continue

    station_id = fields[0].strip()
    # country_code = fields[1]  # 不需要在本作业用
    region_code = fields[2].strip()
    # timestamp = fields[3]    # 不需要在本作业用
    try:
        temperature = float(fields[4].strip())
    except ValueError:
        continue

    # 输出键：(region_code, station_id)，值：(temp, count=1)
    # 用\t分隔
    print(f"{region_code}\t{station_id}\t{temperature}\t1")
