#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 12:37:46 2023

@author: dylanmoraes
"""

num = int(input("Enter a number: "))

# find the number of digits in the given number
num_digits = len(str(num))

# initialize sum to 0
sum = 0

# iterate over each digit in the given number
for digit in str(num):
    # add the cube of each digit to the sum
    sum += int(digit) ** num_digits

# check if the sum is equal to the given number
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
