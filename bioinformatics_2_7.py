#!/usr/bin/python
dic = {}
while True:
    base = raw_input("Enter three-base codon to build: ")
    if base == "XXX":
        print "Okay, I will switch."
        break
    amino = raw_input("Enter amino acid: ")
    dic[base] = amino

while True:
    search = raw_input("Enter three-base codon to search: ")
    if search == "XXX":
        print "Okay, I will stop."
        break
    elif dic.has_key(search):
        print "Amino acid for %s: %s" % (search, dic[search])
    else:
        print "Not exist three-base codon"

