#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getClasNum():
    f=open('label.txt')
    des=open('classNumRes2.xlsx','w')
    classList={}
    for line in f:
        if line in classList:
            classList[line]+=1
        else:
            classList[line]=1
       # classList.append(line)
    for key in classList:
        des.write(key.split('\n')[0]+'\t'+str(classList[key])+'\n')
        #des.write( str(classList[key]) + '\n')
    f.close()
    des.close()
    # print len(classList)
    # print classList
def getBalanceData():
    '''
    balanList=['130302','180204','130801','240100','120104','220400','130411']
    '''
    balanList=[]
    f=open('classNumRes.csv')
    source=open('name_categories.crf.seg')
    #numCount=0
    for line in f :
        lineArr=line.split(',')
        lineArr[1]=int(lineArr[1])
        print type(lineArr[1])
        if lineArr[1]>10000 and lineArr[1]<70000:
            balanList.append(lineArr[0])

    source = open('name_categories.crf.seg')
    res=open('speData.txt','w')
    print len(balanList)
    for line in source:
        lineArr=line.split(' ')
        if lineArr[0] in balanList:
            res.write(line)
    #f.close()
    source.close()
    res.close()
def analyData():
    f=open('speData.txt')
    lenDict={}
    for line in f:
        lineArr=line.split(' ')
        l=len(lineArr)
        if l in lenDict:
            lenDict[l]+=1
        else:
            lenDict[l]=1
    des=open('speDataAna.csv','w')
    for key in lenDict:
        des.write(str(key)+','+str(lenDict[key])+'\n')
    f.close()
    des.close()
def mapLabel():
    '''这七类数据分布比较均匀，总数75688条'''
    #mapDict = {'130302': 0, '180204': 1, '130801': 2, '240100': 3, '120104': 4, '220400': 5, '130411': 6}
    numCount=0
    f=open('label_1-7.txt')
    map_file = open('classNumRes.csv')
    des=open('label_map1-7Data.txt','w')
    mapDict={}
    for line in map_file :
        lineArr=line.split(',')
        lineArr[1]=int(lineArr[1])
        #print type(lineArr[1])
        if lineArr[1]>10000 and lineArr[1]<70000:
            mapDict[lineArr[0]]=numCount
            numCount+=1
    for line in f:
        des.write(str(mapDict[line.split('\n')[0]])+'\n')
    f.close()
    des.close()

#getClasNum()
#getBalanceData()
#analyData()
mapLabel()