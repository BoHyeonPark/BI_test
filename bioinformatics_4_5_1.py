#!/usr/bin/python

o_inf = open("sequence.nucleotide.gb",'r')
lines = o_inf.xreadlines()
l = []
for line in lines:
    line = line.strip()
    l.append(line)
#l = "\n".join(l)
#print l
'''
seq = ""
idx = 0
for i in l:
    idx += 1
    if i == "TITLE":
        seq = l[1:][idx:]
        seq = "\n".join(seq)
print seq
'''
'''
import re
p = re.compile("^TITLE", re.MULTILINE)
m = p.finditer(l)
for i in m:
    startIndex = i.start()
    endIndex = i.end()
    print i.span()
    print l[startIndex:endIndex]
'''

'''
ind = 0
for i in l:
    ind += 1
    if i == "ORIGIN":
        break
seq = l[1:][ind:]
seq = "\n".join(seq)

'''
o_inf.close()
