'''
Question:
Task
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

Input Format
A single line containing the space separated string S and the integer value k.

Output Format
Print the permutations of the string S on separate lines.

Sample Input
HACK 2

Sample Output
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

Explanation
All possible size  permutations of the string "HACK" are printed in lexicographic sorted order.
'''
from itertools import permutations

string,size = input().split()
size = int(size)

lst = list((permutations(string,size)))
lst.sort()

for i in range(len(lst)):
    string = ''.join(lst[i])
    print(string)
    
