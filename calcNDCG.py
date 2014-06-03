#!/usr/bin/env python3

import trec
import pickle
import collections

_dict = collections.defaultdict(list)

with open('qrels.txt') as f:
    for line in f:
        result = line.strip().split()
        topic = result[0]
        _dict[topic].append(int(result[-1]))

finalResult = {}

for topic in _dict:
    points = sorted(_dict[topic])[-10:][::-1]
    finalResult[topic] = trec.calcDCG(points)

# print(finalResult)

# file = open('IDCG.dat', 'wb')
# pickle.dump(finalResult, file)
# file.close()

# with open('iDCG.dat', 'rb') as f:
#     print(pickle.load(f))
