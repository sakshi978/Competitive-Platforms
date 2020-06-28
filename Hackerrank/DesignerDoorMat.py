'''
Question:
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N X M. (N is an odd natural number,and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Sample Designs
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
    
Input Format
A single line containing the space separated values of N and M.

Output Format
Output the design pattern.

Sample Input
9 27
Sample Output
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().split())

s1 = ".|."
s2 = "WELCOME"

#upper part
for i in range(int(n/2)):
    print((s1*((i*2)+1)).center(m,'-'))

#middle part
print(s2.center(m,'-'))

#lower part
for i in range(int(n/2)-1,-1,-1):
    print((s1*((i*2)+1)).center(m,'-'))
