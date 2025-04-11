#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    # 简单判断是否是 job1_output 格式 (3列) 或原始数据 (6列)
    parts = line.split('\t')
    
    # 可能是 job1 的输出: region_code \t station_id \t avg_temp
    if len(parts) == 3:
        region_code = parts[0]
        station_id = parts[1]
        avg_temp_str = parts[2]
        print(f"{region_code}\t{station_id}\tAVG\t{avg_temp_str}")
    else:
        # 否则尝试解析为原始数据 CSV
        csv_fields = line.split(',')
        if len(csv_fields) == 6:
            station_id = csv_fields[0].strip()
            region_code = csv_fields[2].strip()
            try:
                temperature = float(csv_fields[4].strip())
            except ValueError:
                continue
            # 输出 (region_code, station_id, type=DATA, temperature)
            print(f"{region_code}\t{station_id}\tDATA\t{temperature}")
        else:
            # 格式不对，跳过
            continue
