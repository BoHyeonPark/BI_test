#!/usr/bin/python
cnt = 0
l = []
nl = []
o_inf = open("sequence.nucleotide.gb",'r')
lines = o_inf.xreadlines()
for line in lines:
    l.append(line.strip())

for i in range(len(l)):
    if "TITLE" in l[i] and cnt == 0:
        cnt = 1
        if "JOURNAL" in l[i+1]:
            nl.append(l[i])
        elif "JOURNAL" not in l[i+1]:
            nl.append(l[i] + ' ' + l[i+1])
    elif "TITLE" in l[i] and cnt == 1:
        if "JOURNAL" in l[i+1]:
            nl.append('          ' + l[i][10:])
        elif "JOURNAL" not in l[i+1]:
            nl.append('          ' + l[i][10:] + ' ' + l[i+1])
result = "\n".join(nl)
print result
o_inf.close()
