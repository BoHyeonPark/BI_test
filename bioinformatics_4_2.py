#!/usr/bin/python
fr = open("sequence.protein.gb",'r')
lines = fr.xreadlines()

l = []
for line in lines:
    line = line.strip()
    l.append(line)

title = l[0]
temp = l[1:]

seq = []
ind = 0
for i in temp:
    ind += 1
    if i == "ORIGIN":
        break

seq = temp[ind:]
seq = "\n".join(seq)

print "title: %s" % (title)

import re
p = re.compile("[a-zA-Z]")
m = p.findall(seq)

print "seq: %s" % ("".join(m))
fr.close()
