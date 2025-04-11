#!/usr/bin/env python3
import sys
import math

current_region = None
sum_anomaly = 0.0
sum_anomaly_sq = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) != 4:
        continue
    
    region_code = parts[0]
    try:
        anomaly = float(parts[1])
        anomaly_sq = float(parts[2])
        c = int(parts[3])
    except ValueError:
        continue

    if current_region is None:
        current_region = region_code

    if region_code != current_region:
        # 计算上一组region的std
        if count > 0:
            mean_anomaly = sum_anomaly / count
            mean_anomaly_sq = sum_anomaly_sq / count
            std_dev = math.sqrt(mean_anomaly_sq - mean_anomaly**2)
            print(f"{current_region}\t{std_dev}")
        # 重置
        current_region = region_code
        sum_anomaly = anomaly
        sum_anomaly_sq = anomaly_sq
        count = c
    else:
        sum_anomaly += anomaly
        sum_anomaly_sq += anomaly_sq
        count += c

# 最后一组
if current_region is not None and count > 0:
    mean_anomaly = sum_anomaly / count
    mean_anomaly_sq = sum_anomaly_sq / count
    std_dev = math.sqrt(mean_anomaly_sq - mean_anomaly**2)
    print(f"{current_region}\t{std_dev}")
