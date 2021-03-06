#!/usr/bin/env python3

import json
import io
import xmltodict

def xml2json():
    infile  = io.open('sessiontrack2013.xml',  'r')
    outfile = io.open('sessiontrack2013.json', 'w')
    o = xmltodict.parse(infile.read())
    json.dump(o, outfile)

def printJson(jsonFile):
    f = open(jsonFile)
    jsonDict = json.load(f)
    cnt = 0
    for item in jsonDict['sessiontrack2013']['session']:
        if cnt == 10: break
        print(item)
        cnt += 1

def main():
    xml = open('sessiontrack2013.xml', 'r')
    obj = xmltodict.parse(xml.read())
    sessions = obj['sessiontrack2013']['session']
    cnt = 1
    for session in sessions:
        # if cnt == 88: break
        if cnt == 3: break
        # print(session['@num'])
        # print(session['topic']['@num'])
        # for key in session.items():
        #     print(key)
        interactions = session['interaction']
        # print(interactions)
        # print(session['currentquery'])
        # print(type(interactions))
        # for interaction in interactions:
        #     print(interaction)
        #     print('==============')
        #     # for k,v in interaction.items():
        #     #     print(k,v)
        cnt += 1

if __name__ == '__main__':
    # xml2json()
    # printJson('sessiontrack2013.json')
    main()
