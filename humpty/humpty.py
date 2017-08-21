#!/usr/bin/python

import subprocess
import sys
import os
import operator
import re

def elfhash(key):
    h = 0
    x = 0
    for i in range(len(key)):
      h = (h << 4) + ord(key[i])
      x = h & 0xF0000000
      if x != 0:
        h ^= (x >> 24)
        h &= ~x
    return h & 0x7FFFFFFF

path = sys.argv[1]
bins = os.listdir(path)

for i in bins[:]:
    if not i.endswith("bin"):
        bins.remove(i)

flags = {}

for i in bins:
    flags[subprocess.check_output(path+"/"+i).strip("\n")] = elfhash(subprocess.check_output(path+"/"+i).strip("\n"))

sorted_flags = sorted(flags.items(), key=operator.itemgetter(1))
#print sorted_flags

j = 0
for key in sorted_flags[:]:
    sorted_flags[j] = re.findall('\'.+\'',str(key))
    j += 1

flat_list = [item for sublist in sorted_flags for item in sublist]
#print flat_list
k = 0
for flag in flat_list[:]:
    flag = flag.replace("'", "")
    flag = flag.replace('"', "")
    flat_list[k] = flag
    k += 1
#print flat_list
print ('CWN{%s_%s_%s_%s}' % (flat_list[0],flat_list[1],flat_list[2],flat_list[3]))