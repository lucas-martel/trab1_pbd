#!/usr/bin/env python

import sys

output = []

for line in sys.stdin:
    value, key = line.strip().split('\t')
    output.append((value, key))

sorted_output = sorted(output, key=lambda x: len(x[1]), reverse=True)

for value, key in sorted_output:
    print(f"{value}\t{key}")
