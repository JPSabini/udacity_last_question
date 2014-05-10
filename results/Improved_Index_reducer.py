#!/usr/bin/python
import sys
import csv
from collections import defaultdict

Total = 0
cnt=0
oldWord=None

newWord = None
""" 
Index Improvement

Input is sorted and shuffled key value pairs. 
The dict D_tags is a dict of key user id and values as a list of 
list tuples. For example :
{"foo": [10000, 200002, 300003, 3]
  "etc": [300001,300002,300003,2000,100, 5]
}
 Where the key is the word and the first element of the list tuple is 
 the docment address or position and the Index[word][-1] is 
 frequency of the word.

"""
WIndex =defaultdict(list)

writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)        
reader = csv.reader(sys.stdin, delimiter='\t')  
for line in reader:
    data_mapped = line
    
    if len(data_mapped)!= 2 : 
        print "line input error", data_mapped
        continue

    newWord , position = data_mapped
  
    if oldWord and oldWord != newWord:
        
        # This is the break transition from one occcurrence of 
        # sorted words to the next word
        # 

        WIndex[oldWord].append(cnt)
        cnt = 0
        print oldWord, "\t", WIndex[oldWord]
        oldWord = newWord
        
    cnt +=1
    WIndex[oldWord].append(position)
    oldWord = newWord
    
   
if oldWord != None:
    print oldWord, "\t", WIndex[oldWord]
        