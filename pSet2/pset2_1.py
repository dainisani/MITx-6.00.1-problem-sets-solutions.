# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:48:01 2017

@author: Daini Sani
"""

'''
Write a program to calculate the credit card balance after one year if a person
only pays the minimum monthly payment required by the credit card company each
month. The following variables contain values as described below:
    
    1. balance - the outstanding balance on the credit card
    
    2. annualInterestRate - annual interest rate as a decimal
    
    3. monthlyPaymentRate - minimum monthly payment rate as a decimal
    
For each month, calculate statements on the monthly payment and remaining
balance. At the end of 12 months, print out the remaining balance. Be sure to 
print out no more than two decimal digits of accuracy - so print

    Remaining balance: 813.41
    
instead of

    Remaining balance: 813.4141998135 
    
So your program only prints out one thing: the remaining balance at the end of 
the year in the format:
    
    Remaining balance: 4784.0
        
A summary of the required math is found below:
    Monthly interest rate= (Annual interest rate) / 12.0
    Minimum monthly payment = (Minimum monthly payment rate) x (Previous balan
    ce)
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest 
    rate x Monthly unpaid balance)
'''

monthsInYear = 12.0
numOfMonthsAYear = 12
# one out of many test case values for variables balance, annualInterestRate
# and monthlyPaymentRate
balance, annualInterestRate, monthlyPaymentRate = 484, 0.2, 0.04 

for cash in range(numOfMonthsAYear):
    monthlyInterestRate = annualInterestRate / monthsInYear
    minimumPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minimumPayment
    interest = monthlyInterestRate * unpaidBalance
    balance = unpaidBalance + interest
print("Remaining balance: " + str(round(balance, 2)))