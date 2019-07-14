#!/usr/bin/python
fr = open("sequence.protein.2.fasta",'r')
lines = fr.xreadlines()

l = []
for line in lines:
    line=line.rstrip()
    l.append(line)
print "The second line is:",l[1]
fr.close()
