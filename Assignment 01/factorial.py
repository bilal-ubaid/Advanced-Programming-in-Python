# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 21:18:22 2022

@author: billu
"""

a = int(input("enter the number: "))

for i in range(1,a)[::-1]:
        print(i)
        a = i*a
        i -= 1
print ("The factorial of the number is: ", a)