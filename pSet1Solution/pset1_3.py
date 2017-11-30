# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:06:32 2017

@author: Daini Sani
"""

'''
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your 
program should print:

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print:

Longest substring in alphabetical order is: abc
'''

s = 'fymwlelgxtxguixyfa'
subStr = ''
arr = []
count = 0

for i in range(len(s)):
    if i == count:
        subStr = s[i]
        for j in range(len(s)):
            if j > i:
                if s[j] < s[j - 1]:
                    if j == len(s) - 1:
                        count = j
                    count = j
                    break
                elif s[j] >= s[j - 1]:
                    subStr += s[j]
        arr.append(subStr)
   
longestStr = arr[0]
for i in range(len(arr)):
    b = len(longestStr)
    if i == len(arr) - 1:
        c = len(arr[i])
        if c > b:
            longestStr = arr[i]
    elif len(arr[i + 1]) > len(longestStr):
        longestStr = arr[i + 1]
        
print("Longest substring in alphabetical order is:", longestStr)