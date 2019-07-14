#!/usr/bin/python
dan = raw_input("Which times table: ")

try:
    dan = int(dan)
    if dan < 0 or dan > 10:
        raise
except:
    print "What? enter only number(1~9)"
else:
    for i in range(1,10):
        print "%d * %d = %d" % (dan, i, dan * i)
