#!/usr/bin/python
fr = open("sequence.protein.2.fasta",'w')
f = open("sequence.protein.fasta",'r')
lines = f.xreadlines()
for line in lines:
    fr.write(line)
f.close()
fr.close()

