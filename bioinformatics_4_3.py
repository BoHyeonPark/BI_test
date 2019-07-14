#!/usr/bin/python
fr = open("sequence.protein.gb",'r')
lines = fr.xreadlines()

l = []
for line in lines:
    line = line.strip()
    l.append(line)

temp = l[1:]

seq = []
ind = 0
for i in temp:
    ind += 1
    if i == "ORIGIN":
        break

seq = temp[ind:]
seq = "\n".join(seq)

import re
p = re.compile("[a-zA-Z]")
m = p.findall(seq)
s = "".join(m)

o = ""
for i in s:
    if len(o) % 71 == 0:
        o += "\n"
        o += i
    else:
        o += i
o=o.lstrip()
print o
fr.close()
