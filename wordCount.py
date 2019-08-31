#! /usr/bin/env python3
from sys import argv
from collections import Counter
import re 
import string

list1 = []
f = open(argv[1],"r") #takes argument 1 from command line "declaration.txt"
out = open(argv[2],"w") #takes second arg "output.txt"
for line in f.readlines():#reads line by line from f
    for word in line.split():
        word = re.sub(',','', word).replace('.','')
        #word = re.sub('.','', word)
        list1.append(word.lower())
list1.sort()
counter = Counter(list1)
for item in counter.items():
    out.write("{}\t{}\n".format(*item))
f.close()
out.close()