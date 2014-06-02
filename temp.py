#!/usr/bin/env python3

from collections import defaultdict

with open('formalQuery.txt') as f:
    number = 0
    d = defaultdict(list)
    for line in f:
        try:
            number = int(line.strip())
        except:
            d[number].append(line.strip())

    for k,v in d.items():
        print(k)
        print(v)
