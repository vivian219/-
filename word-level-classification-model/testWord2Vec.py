#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gensim

model = gensim.models.Word2Vec.load("1-7data.model")

#print model.most_similar(u"餐厅")

result = model.most_similar(u"大厦")

for e in result:
    print e[0], e[1]