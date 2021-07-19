import math

d1 = open('Homework4/d1.txt', 'r').read().split()
d2 = open('Homework4/d2.txt', 'r').read().split()
d3 = open('Homework4/d3.txt', 'r').read().split()
d4 = open('Homework4/d4.txt', 'r').read().split()
d5 = open('Homework4/d5.txt', 'r').read().split()

doc_list = [d1, d2, d3, d4, d5]
word_set = set()
for d in doc_list:
    for x in d:
        word_set.add(x)

# make tf dictionary

# initialize tf with 0
tf = {}
for i in range(len(doc_list)):
    doc_id = "d" + str(i+1)
    tf[doc_id] = dict()
    for word in word_set:
        tf[doc_id][word] = 0

# assign value to tf
for i in range(len(doc_list)):
    doc_id = "d" + str(i+1)
    for word in word_set:
        tf[doc_id][word] = doc_list[i].count(word)

# make TfIdf dictionary
tf_idf = tf

for word in word_set:
    count = 0
    for doc_id in tf_idf.keys():
        if tf[doc_id][word] != 0:
            count += 1
    for doc_id in tf_idf.keys():
        tf_idf[doc_id][word] = math.log2(5/count) * tf[doc_id][word]
