# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 10:50:08 2022

@author: billu
"""

a = int(input("enter the sequence number : "))
first_number = 0
second_number = 1
count = 0

print("Fabonacci Sequence: ")
while count < a:
    print(first_number)
    third_number = first_number + second_number
    first_number = second_number
    second_number = third_number
    count +=1
    