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
    try:
        anomaly = float(parts[1])
    except ValueError:
        continue
    # 输出 (region_code, anomaly, anomaly^2, 1)
    print(f"{region_code}\t{anomaly}\t{anomaly**2}\t1")
