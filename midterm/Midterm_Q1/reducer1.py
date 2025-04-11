#!/usr/bin/env python3
import sys

current_key = None  # 形如 "region_code \t station_id"
sum_temp = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) != 4:
        # 格式不对，跳过
        continue

    # key: (region_code \t station_id)
    key = parts[0] + "\t" + parts[1]
    try:
        temp = float(parts[2])
        c = int(parts[3])
    except ValueError:
        continue

    if current_key is None:
        # 第一行数据
        current_key = key
        sum_temp = temp
        count = c
    elif key == current_key:
        # 同一个 key 累加
        sum_temp += temp
        count += c
    else:
        # key 发生变化，输出上一组的平均值
        region_station = current_key.split('\t')  # [region_code, station_id]
        if count != 0:
            avg_temp = sum_temp / count
            print(f"{region_station[0]}\t{region_station[1]}\t{avg_temp}")
        # 重置到新 key
        current_key = key
        sum_temp = temp
        count = c

# 处理最后一组
if current_key is not None and count != 0:
    region_station = current_key.split('\t')
    avg_temp = sum_temp / count
    print(f"{region_station[0]}\t{region_station[1]}\t{avg_temp}")
