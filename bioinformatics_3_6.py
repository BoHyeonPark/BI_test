#!/usr/bin/python
fr = open("sequence.protein.2.fasta",'r')
lines = fr.xreadlines()

l = []
seq = ""
for line in lines:
    line = line.rstrip()
    l.append(line)
print "title: %s" % (l[0])

for i in l[1:]:
    seq += i
print "seq: %s" % (seq)
fr.close()
