#!/usr/bin/env python3

import sys
from functools import reduce

def getResults(*_files):
    _dict = {}
    for _file in _files:
        with open(_file) as _:
            for line in _:
                result = line.strip().split()
                # print(result)
                # print(_dict)
                if result[0] in _dict:
                    # print('in')
                    # _dict[result[0]] = _dict[result[0]].append(result[2])
                    _dict[result[0]].append((result[2], result[-3], _file))
                else:
                    # print('out')
                    _dict[result[0]] = [(result[2], result[-3], _file)]
    return _dict

def sortDict(sessions, users):
    # Create weights in weighed sort
    if isinstance(users, list):
        weights = { user: 1 / len(users) for user in users}
    elif isinstance(users, dict):
        weights = users
    else:
        print('Wrong Weights!!')
        sys.exit()

    name = reduce(lambda x, y: x + '_' + y, users)
    writeFile = open(name, 'w')

    for session in sessions:
        rankList = sessions[session]
        _dict = {}
        for rank in rankList:
            _dict[rank[0]] = _dict.get(rank[0], 0.0) + 1 / float(rank[1]) * weights[rank[2]]
        print(_dict)
        combinedRank = sorted(_dict, key=lambda x: _dict[x], reverse=True)[:100]
        cnt = 1
        for webID in combinedRank:
            writeInto = ' '.join([session,'Q0',webID,str(cnt),'X','indri']) + '\n'
            writeFile.write(writeInto)
            cnt += 1
    writeFile.close()

def createCombinedResult():
    pass

def createWeights(users, points):
    if len(users) != len(points):
        print('Wrong weight points')
        sys.exit()
    return dict(zip(users, points))

def main():
    _files  = sys.argv[1:]
    _dict   = getResults(*_files)
    print(_dict)
    _files  = createWeights(_files, [0.25, 0.75])
    sortDict(_dict, _files)

if __name__ == '__main__':
    main()
