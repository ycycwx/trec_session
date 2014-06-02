#!/usr/bin/env python3

def replace(filename, outfilename):
    specials = {}.fromkeys([ line.rstrip() for line in open('specialList') ])
    outFile = open(outfilename, 'w')
    with open(filename, 'r') as f:
        for line in f:
            for i in line:
                if i in specials: line = line.replace(i, ' ')
            outFile.write(line)
        outFile.write('\n')
    outFile.close()

if __name__ == '__main__':
    replace('querys.xml', 'query.xml')
