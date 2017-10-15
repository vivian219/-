import random

con=[]
f=open('name_categories.crf.seg')
shuff_file=open('name_categories_shuffle.crf.seg','w')

counter=0

for line in f:
    con.append(line)

random.shuffle(con)

for item in con:
    shuff_file.write(item)
    counter+=1

f.close()
shuff_file.close()