# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 20:42:36 2017

@author: Daini Sani
"""

'''
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, 
if s = 'azcbobobegghakl', your program should print:
    
Number of vowels: 5
'''
# s could be any string. This is just a test string
s = 'azcbobobegghakl'
counter = 0

for numVowels in s: 
    if numVowels == 'a' or numVowels == 'e' or numVowels == 'i' or numVowels == 'o' or numVowels == 'u':
        counter += 1
print("Number of vowels: " + str(counter))