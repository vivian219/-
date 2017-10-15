#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

f=codecs.open('speData.txt',encoding='utf-8')
term=codecs.open('term_speData.txt','w',encoding='utf-8')
label=codecs.open('label_speData.txt','w',encoding='utf-8')


for line in f:
    if line=='\n':
        continue
    lineArr=line.split(' ')
    label.write(lineArr[0]+'\n')
    i=1
    while i<len(lineArr):
        term.write(lineArr[i])
        if i!=len(lineArr)-1:
            #term.write('\n')
            term.write(' ')
        # else:
        #     term.write(' ')
        i+=1

f.close()
term.close()
label.close()