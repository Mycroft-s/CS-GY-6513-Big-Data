#!/usr/bin/env python3
import sys

current_key = None  # region_code \t station_id
avg_temp = None
data_records = []  # 缓存当前key下所有DATA的温度

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    parts = line.split('\t')
    if len(parts) != 4:
        continue
    
    region_station = parts[0] + "\t" + parts[1]  # key
    record_type = parts[2]
    value = parts[3]
    
    if current_key is None:
        current_key = region_station
    
    if region_station != current_key:
        # 处理上一组key
        if avg_temp is not None:
            for temp in data_records:
                anomaly = temp - avg_temp
                # 输出: region_code \t anomaly
                rs_split = current_key.split('\t')
                print(f"{rs_split[0]}\t{anomaly}")
        # 重置
        current_key = region_station
        avg_temp = None
        data_records = []
    
    # 根据 record_type 分不同数据
    if record_type == "AVG":
        # 这是avg_temp
        try:
            avg_temp = float(value)
        except ValueError:
            pass
    elif record_type == "DATA":
        # 这是原始数据
        try:
            t = float(value)
            data_records.append(t)
        except ValueError:
            pass

# 处理最后一组
if current_key is not None and avg_temp is not None:
    for temp in data_records:
        anomaly = temp - avg_temp
        rs_split = current_key.split('\t')
        print(f"{rs_split[0]}\t{anomaly}")
