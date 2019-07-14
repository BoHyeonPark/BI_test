#!/usr/bin/python
inf = raw_input("Enter input file: ")
outf = raw_input("Enter output file: ")
print "Option-1) Read a FASTA format DNA sequence file and make a reverse sequence file."
print "Option-2) Read a FASTA format DNA sequence file and make a reverse complement sequence file."
print "Option-3) Convert GenBank format file to FASTA format file."
op = raw_input("Select the option: ")

if inf == "sequence.nucleotide.fasta" and outf == "reverse.sequence.nucleotide.fasta" and op == "1":
    with open("reverse.sequence.nucleotide.fasta",'w') as o_outf:
        with open("sequence.nucleotide.fasta",'r') as o_inf:
            l = []
            seq = ""
            for line in o_inf:
                l.append(line.strip())
            title = l[0]
            for i in l[1:]:
                seq += i
            rev_seq = seq[::-1]
            o_outf.write(title+"\n"+rev_seq)

elif inf == "sequence.nucleotide.fasta" and outf == "reverse.complement.sequence.nucleotide.fasta" and op == "2":
    with open("reverse.complement.sequence.nucleotide.fasta",'w') as o_outf:
        with open("sequence.nucleotide.fasta",'r') as o_inf:
            l = []
            seq = ""
            for line in o_inf:
                l.append(line.strip())
            title = l[0]
            for i in l[1:]:
                seq += i
            rev_seq = seq[::-1]
            compDic = {"A":"T","C":"G","G":"C","T":"A"}
            revcomp_seq = ""
            for s in rev_seq:
                revcomp_seq += compDic[s]
            o_outf.write(title+"\n"+revcomp_seq)

elif inf == "sequence.nucleotide.gb" and outf == "new.sequence.nucleotide.fasta" and op == "3":
    with open("new.sequence.nucleotide.fasta",'w') as o_outf:
        with open("sequence.nucleotide.gb",'r') as o_inf:
            l = []
            for line in o_inf:
                l.append(line.strip())
            title = l[0]
            seq = []
            ind = 0
            for i in l[1:]:
                ind += 1
                if i == "ORIGIN":
                    break
            seq = l[1:][ind:]
            seq = "\n".join(seq)
            import re
            p = re.compile("[a-zA-Z]")
            m = p.findall(seq)
            o_outf.write(">"+title+"\n"+"".join(m))
