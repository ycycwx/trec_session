#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import math

def getDictionary():
    with open('qrels.txt') as qrels:
        topic_dict = {}
        for line in qrels:
            result = line.strip().split()
            topic_dict[tuple((int(result[0]),result[2]))] = int(result[-1])
    return topic_dict

def extractCurrentQuery():
    topic_dict = getDictionary()

    tree = ET.parse('sessiontrack2013.xml')
    root = tree.getroot()

    queryList = []
    
    for session in root:
        if session.attrib['num'] == '88': break

        for topic in session.iter('topic'):
            top = topic.attrib['num']

        for currentquery in session.iter('currentquery'):
            for query in currentquery.iter('query'):
                que = query.text

        queryList.append((top, que))

    return queryList

def createXML(queryList):
    parameters = ET.Element('parameters')

    for tuple in queryList:
        top, que = tuple
        query   = ET.SubElement(parameters, 'query')
        type    = ET.SubElement(query, 'type')
        number  = ET.SubElement(query, 'number')
        text    = ET.SubElement(query, 'text')
        type.text   = 'indri'
        number.text = top
        text.text   = '#combine(' + que + ')'

    tree = ET.ElementTree(parameters)
    tree.write('result.xml', encoding='utf-8')

def calcDCG(ranklist):
    cnt = 1
    DCG = 0
    for point in ranklist:
        DCG += (2 ** point - 1)/ math.log(1 + cnt, 2)
        cnt += 1
    return DCG

def calcIDCG():
    import pickle
    return pickle.load(open('IDCG.dat', 'rb'))

def calcTest(result_file, threshold):
    IDCG = calcIDCG()
    topic_dict = getDictionary()

    with open(result_file) as rf:
        cnt = 1
        List = []
        ndcgList = []
        for line in rf:
            result = line.strip().split()
            if len(result) == 0 or result[-1] != 'indri': continue
            List.append(topic_dict.get((int(result[0]), result[2]), 0))
            if cnt == threshold:
                # print(List)
                DCG     = calcDCG(List[:10])
                # print(DCG)
                NDCG    = IDCG[result[0]]
                # print(NDCG)
                ndcgList.append(DCG/NDCG)
                List = []
                cnt = 0
            cnt += 1
        print(sum(ndcgList) / len(ndcgList))

def main():
    topic_dict = getDictionary()

    tree = ET.parse('sessiontrack2013.xml')
    root = tree.getroot()
    
    # cnt = 0
    for session in root:
        # if cnt == 1: break
        # cnt += 1
        # print('===============================')
        tuples = []
        # print(session.tag, session.attrib)
        # for i in session:
        #     print(i.tag)
        for topic in session.iter('topic'):
            topic_id = int(topic.attrib['num'])
            # print(topic.attrib)
        for interaction in session.iter('interaction'):
            # print(interaction.tag, interaction.attrib)
            # for query in interaction.iter('query'):
            #     print(query.text)
            for results in interaction.iter('results'):
                # print(results.tag, results.attrib)
                for result in results:
                    # print(result.tag, result.attrib)
                    for clueweb12id in result.iter('clueweb12id'):
                        # print(clueweb12id.text)
                        clue_id = clueweb12id.text
                        tuples.append((topic_id, clue_id))
    print(tuples)

    ranklist = []
    for tup in tuples:
        ranklist.append(topic_dict.get(tup, -2))
    print(ranklist)

    # print(calcDCG(ranklist))

if __name__ == '__main__':
    # query = extractCurrentQuery()
    # createXML(query)
    # main()
    calcTest('resultTrec', 100)
