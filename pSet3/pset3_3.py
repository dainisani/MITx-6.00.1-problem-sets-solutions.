# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 08:23:04 2017

@author: Daini Sani
"""

'''
Next, implement the function getAvailableLetters that takes in one parameter - 
a list of letters, lettersGuessed. This function returns a string that is 
comprised of lowercase English letters - all lowercase English letters that are 
not in lettersGuessed.

Example Usage:
    >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    >>> print(getAvailableLetters(lettersGuessed))
    abcdfghjlmnoqtuvwxyz
    
Note that this function should return the letters in alphabetical order, as in 
the example above.

For this function, you may assume that all the letters in lettersGuessed are 
lowercase.

Hint: You might consider using string.ascii_lowercase, which is a string 
comprised of all lowercase letters:
    
    >>> import string
    >>> print(string.ascii_lowercase)
    abcdefghijklmnopqrstuvwxyz
'''

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newstr = ""
    for i in lettersGuessed:
        if i in alphabet:
            alphabet = alphabet.replace(i, "")
    return alphabet

print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))
