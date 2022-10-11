# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 11:00:29 2022

@author: billu
"""

x = float(input("Enter the number to find the cube root: "))
epsilon = 0.01
num_guesses = 0.0
low = x
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0

print('num guesses =', num_guesses)
print(ans, 'is close to cube root of', x)