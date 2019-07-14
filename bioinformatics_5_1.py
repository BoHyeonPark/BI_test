#!/usr/bin/python
l = []
seq = ""
with open("sequence.nucleotide.fasta",'r') as inf:
    for line in inf:
        l.append(line.strip())

sequ = l[1:]
for i in sequ:
    seq += i
for k in range(0,len(seq)):
    if k % 3 == 0:
        print seq[k:k+3]
