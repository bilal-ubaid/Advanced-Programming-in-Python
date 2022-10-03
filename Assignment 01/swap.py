# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:12:57 2022

@author: billu
"""

# Swapping two numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

c = a # store first number in temporary variable
a = b # store second number in first number
b = c # store temporary variable in second number
    
print ("1st swapped number: ", a)
print ("2nd swapped number: ", b)