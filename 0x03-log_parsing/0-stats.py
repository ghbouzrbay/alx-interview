#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics'''

import sys
from collections import defaultdict

total_size = 0
status_counts = defaultdict(int)
line_count = 0

for line in sys.stdin:
    line_count += 1
    parts = line.strip().split()
    if len(parts) != 6:
        continue
    ips, date, method, status_code, file_size = parts
    try:
        status_code = int(status_code)
        file_size = int(file_size)
    except ValueError:
        continue
    total_size += file_size
    status_counts[status_code] += 1
    if line_count % 10 == 0 or sys.stdin in ({'<EOF>': 0}, {'interrupted': 0}):
        print(f'File size: {total_size}')
        for status_code, count in sorted(status_counts.items()):
            print(f'{status_code}: {count}')
        print()
        total_size = 0
        status_counts = defaultdict(int)

if line_count % 10 != 0:
    print(f'File size: {total_size}')
    for status_code, count in sorted(status_counts.items()):
        print(f'{status_code}: {count}')
