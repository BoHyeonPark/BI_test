#!/usr/bin/python
l = list()
seq = ""
with open("sequence.nucleotide.fasta",'r') as inf:
    for line in inf:
        l.append(line.strip())
sequ = l[1:]
for i in sequ:
    seq += i

codon_dic = {
'TTT':'F', 'TTC':'F', 'TTA':'L', 'TTG':'L',
'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',
'TAT':'Y', 'TAC':'Y', 'TAA':'*', 'TAG':'*',
'TGT':'C', 'TGC':'C', 'TGA':'*', 'TGG':'W',
'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
'ATT':'I', 'ATC':'I', 'ATA':'I', 'ATG':'M',
'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
'AAT':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
'AGT':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
'GAT':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
}

protein = list()
for j in range(0,len(seq)-len(seq)%3,3):
    protein.append(codon_dic[seq[j:j+3]])
protein = "  ".join(protein)

nseq = list()
for p in seq:
    if len(nseq) % 61 == 0:
        nseq.append(p)
    else:
        nseq.append(p)
nseq = "".join(nseq)
nseq = nseq.lstrip()

pseq = list()
for q in protein:
    if len(pseq) % 61 == 0:
        pseq.append(q)
    else:
        pseq.append(q)
pseq = "".join(pseq)
pseq = pseq.lstrip()

for ind in range(0,len(nseq),60):
    print nseq[ind:ind+60]
    print pseq[ind:ind+60]
