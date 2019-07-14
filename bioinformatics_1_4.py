#!/usr/bin/python
num1 = raw_input("Enter a integer: ")
num2 = raw_input("Enter another: ")

try:
    num1 = int(num1)
    num2 = int(num2)

except:
    print "Enter only number!"

else:
    if num1 > num2:
        print "%d is greater than %d" % (num1, num2)
    elif num1 < num2:
        print "%d is less than %d" % (num1, num2)
    else:
        print "%d is equal to %d" % (num1, num2)
