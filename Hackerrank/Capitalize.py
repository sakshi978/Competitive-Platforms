'''
Question:
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
alison heck => Alison Heck
Given a full name, your task is to capitalize the name appropriately.

Input Format
A single line of input containing the full name,S .

Output Format
Print the capitalized string, .

Sample Input
chris alan

Sample Output
Chris Alan
'''
import math
import os
import random
import re
import sys

def solve(s):
    strList = s.split(" ")
    res = ''

    for i in strList:
        res = res + i.capitalize() + ' '

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
