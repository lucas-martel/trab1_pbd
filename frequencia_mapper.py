#!/usr/bin/env python

import sys

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) >= 2:
        key = parts[0]
        words = parts[1].split(',')
        total_words = len(words)
        print(f"{key}\t{total_words}")