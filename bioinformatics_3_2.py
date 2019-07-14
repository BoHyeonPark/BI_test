#!/usr/bin/python
fr = open("title.txt",'r')
lines = fr.xreadlines()
for line in lines:
    print "The first line is: %s" % (line.strip())
    break
fr.close()
