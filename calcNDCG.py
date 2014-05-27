#!/usr/bin/env python3

import trec
import pickle

Dict = {}
with open('qrels.txt') as f:
    for line in f:
        result = line.strip().split()
        topic = result[0]
        if topic in Dict:
            Dict[topic].append(int(result[-1]))
        else:
            Dict[topic] = [ int(result[-1]) ]

finalResult = {}

for topic in Dict:
    points = sorted(Dict[topic])[-10:]
    points = points[::-1]
    finalResult[topic] = trec.calcDCG(points)

file = open('IDCG.dat', 'wb')
pickle.dump(finalResult, file)
file.close()

# with open('iDCG.dat', 'rb') as f:
#     print(pickle.load(f))
