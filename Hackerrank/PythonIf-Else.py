"""
Question:
Task
Given an integer,n , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Input Format

A single line containing a positive integer,n .

Constraints
1<=n<=100

Output Format
Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0
3
Sample Output 0
Weird
Explanation 0
3 is odd and odd numbers are weird, so we print Weird.

Sample Input 1
24
Sample Output 1
Not Weird
"""
#!/bin/python3

import math
import os
import random
import re
import sys

def main():
    n = int(input())
    if((n<1) or (n>100)):
        return
    if((n%2)!=0):
        print("Weird")
    else:
        if((n>=2) and (n<=5)):
            print("Not Weird")
        elif ((n>=6) and (n<=20)):
            print("Weird")
        elif (n>20):
            print("Not Weird")

if __name__ == '__main__':
    main()
