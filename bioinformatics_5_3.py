#!/usr/bin/python
l = []
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
#forward1
protein = list()
for j in range(0,len(seq)-len(seq)%3,3):
    protein.append(codon_dic[seq[j:j+3]])
protein = "  ".join(protein)

#forward2
seq2 = seq[1:-2]
protein2 = list()
for k in range(0,len(seq2)-len(seq2)%3,3):
    protein2.append(codon_dic[seq2[k:k+3]])
protein2 = "  ".join(protein2)

#forward3
seq3 = seq[2:-1]
protein3 = list()
for k in range(0,len(seq3)-len(seq3)%3,3):
    protein3.append(codon_dic[seq3[k:k+3]])
protein3 = "  ".join(protein3)

#reverse sequence
compDic = {"A":"T","C":"G","G":"C","T":"A"}
revcomp_seq = ""
for l in seq:
    revcomp_seq += compDic[l]
rev_seq = revcomp_seq
revcomp_seq = revcomp_seq[::-1]

#reverse1
rev_protein = list()
for m in range(0,len(revcomp_seq)-len(revcomp_seq)%3,3):
    rev_protein.append(codon_dic[revcomp_seq[m:m+3]])
rev_protein = "  ".join(rev_protein)
rev_protein = rev_protein[::-1]

#reverse2
revcomp_seq2 = revcomp_seq[1:-2]
rev_protein2 = list()
for n in range(0,len(revcomp_seq2)-len(revcomp_seq2)%3,3):
    rev_protein2.append(codon_dic[revcomp_seq2[n:n+3]])
rev_protein2 = "  ".join(rev_protein2)
rev_protein2 = rev_protein2[::-1]

#reverse3
revcomp_seq3 = revcomp_seq[2:-1]
rev_protein3 = list()
for o in range(0,len(revcomp_seq3)-len(revcomp_seq3)%3,3):
    rev_protein3.append(codon_dic[revcomp_seq3[o:o+3]])
rev_protein3 = "  ".join(rev_protein3)
rev_protein3 = rev_protein3[::-1]
print protein  #forward1
print "",protein2  #forward2
print " ",protein3  #forward3
print seq  #sequence
print rev_seq  #reverse complement sequence
print " ",rev_protein  #reverse1
print "   ",rev_protein2  #reverse2
print "  ",rev_protein3  #reverse3
