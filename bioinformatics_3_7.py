#!/usr/bin/python
fr = open("sequence.protein.2.fasta",'r')
lines = fr.xreadlines()

l = []
seq = ""
for line in lines:
    line = line.rstrip()
    l.append(line)
for i in l[1:]:
    seq += i
fr.close()

while True:
    pos = raw_input("Position: ")
    if pos == "XXX":
        print "Okay, I will stop."
        break
    else:
        pos = int(pos)
        print "Three amino acids: ", seq[pos-1:pos+2]
