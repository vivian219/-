#!/usr/bin/env python
# -*- coding: utf-8 -*-

VECTOR_DIR='1-7data.vector'
EMBEDDING_DIM=50
MAX_SEQUENCE_LENGTH =20
docu_num=1685602
VALIDATION_SPLIT = 0.16 # 验证集比例
TEST_SPLIT = 0.2 #
classNum=66
import codecs

from keras.utils import plot_model
from keras.layers import Embedding
import numpy as np
import gensim
import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

from keras.layers import Dense, Input, Flatten, Dropout,Activation
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.models import Sequential
import random

def getText():
    f=codecs.open('term_1-7.txt',encoding='utf-8')
    text=[]
    for line in f:
        #text.append(line.split(' '))
        text.append(line)
    f.close()
    return text
def getLabel():
    f=codecs.open('label_map1-7Data.txt',encoding='utf-8')
    label=[]
    #counter=0
    for line in f:
        item=line.split('\n')[0]
        if item!='':
            label.append(item)
            #print line+str(counter)
        #counter+=1
    f.close()
    #print label
    return label


all_label=getLabel()
all_text=getText()
tokenizer=Tokenizer()
tokenizer.fit_on_texts(all_text)
sequences = tokenizer.texts_to_sequences(all_text)
word_index = tokenizer.word_index
data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
labels = to_categorical(np.asarray(all_label))

trainUnion = list(zip(data,labels))
random.shuffle(trainUnion)
data[:], labels[:] = zip(*trainUnion)

p1 = int(len(data)*(1-VALIDATION_SPLIT-TEST_SPLIT))
p2 = int(len(data)*(1-TEST_SPLIT))
x_train = data[:p1]
y_train = labels[:p1]
x_val = data[p1:p2]
y_val = labels[p1:p2]
x_test = data[p2:]
y_test = labels[p2:]

w2v_model=gensim.models.KeyedVectors.load_word2vec_format(VECTOR_DIR,binary=False)
embedding_matrix = np.zeros((len(word_index) + 1, EMBEDDING_DIM))
for word, i in word_index.items():
    if unicode(word) in w2v_model:
        embedding_matrix[i] = np.asarray(w2v_model[unicode(word)],
                                         dtype='float32')
embedding_layer = Embedding(len(word_index) + 1,
                            EMBEDDING_DIM,
                            weights=[embedding_matrix],
                            input_length=MAX_SEQUENCE_LENGTH,
                            trainable=True)

model = Sequential()
model.add(embedding_layer)
'''
model.add(Dropout(0.5))

# we add a Convolution1D, which will learn filters
# word group filters of size filter_length:
model.add(Conv1D(10, 3, padding='valid', activation='relu', strides=1))
# we use max pooling:
model.add(MaxPooling1D())

# We add a vanilla hidden layer:
model.add(Dense(EMBEDDING_DIM))
model.add(Dropout(0.5))
model.add(Activation('relu'))

# We project onto a single unit output layer, and squash it with a sigmoid:
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.add(Dense(classNum, activation='softmax'))
#model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
'''
model.add(Dropout(0.2))
model.add(Conv1D(10,3, padding='valid', activation='relu', strides=1))
model.add(MaxPooling1D(3))
#model.add(Dropout(0.5))
#model.add(Conv1D(10, 3, padding='valid', activation='relu', strides=1))
#model.add(MaxPooling1D(2))
model.add(Flatten())
model.add(Dense(EMBEDDING_DIM, activation='relu'))
model.add(Dense(labels.shape[1], activation='softmax'))

model.summary()

#y_train = keras.utils.to_categorical(y_train, 228)
#plot_model(model, to_file='model.png',show_shapes=True)
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['acc'])
model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=8, batch_size=128)
model.save('word_vector_cnn_1-7.h5')