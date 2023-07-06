'''Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to 2 to 5, print Not Weird
If  is even and in the inclusive range of  to 6 to 20, print Weird
If  is even and greater than 20 , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints
1<=n<=100'''

import sys


N = int(raw_input().strip())

if N % 2 != 0:
    print "Weird"
else:
    if N >= 2 and N <= 5:
        print "Not Weird"
    elif N >= 6 and N <= 20:
        print "Weird"
    elif N > 20:
        print ("Not Weird")
