#!/usr/bin/python
import re
l = list()
with open("sequence.nucleotide.gb",'r') as fr:
    for line in fr:
        l.append(line.strip())

seq = list()
ind = 0
for i in l[:]:
    ind += 1
    if i == "ORIGIN":
        break
seq = l[ind:]
seq = "\n".join(seq)

p = re.compile("[a-zA-Z]")
m = p.findall(seq)
n_seq = "".join(m).upper()

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
ll = list()
for p in range(len(l)):
    if "CDS" in l[p]:
        ll.append(l[p])
ll = "".join(ll)
q = re.compile("CDS\s+\d+..\d+")
n = q.findall(ll)
for i in n:
    i = i.split(" ")
    i = i[-1].split("..")
start = int(i[0])
end = int(i[1])
p_seq = n_seq[start-1:end]

P_SEQ = list()
for j in range(0,len(p_seq)-len(p_seq)%3,3):
        P_SEQ.append(codon_dic[p_seq[j:j+3]])
P_SEQ = "".join(P_SEQ)
print(P_SEQ)

#70formating
RESULT = ""
for i in P_SEQ:
    if len(RESULT) % 71 == 0:
        RESULT += "\n"
        RESULT += i
    else:
        RESULT += i
RESULT = RESULT.lstrip()
print(RESULT)

