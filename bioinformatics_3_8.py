#!/usr/bin/python
l = []
seq = ""
with open("sequence.protein.2.fasta",'r') as fr:
    for line in fr:
        l.append(line.strip())
for i in l[1:]:
    seq += i
nl = []
while True:
    amino = raw_input("Searching for: ")
    if amino == "XXX":
        print "Okay, I will stop."
        break
    else:
        nl = []
        for i in range(len(seq)):
            if seq[i] == amino:
                nl.append(str(i+1))
            else:
                continue
        print "Found at:", ','.join(nl)
