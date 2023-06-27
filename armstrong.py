#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:44:54 2023

@author: dylanmoraes
"""

def is_armstrong_number(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return num == sum

# Example usage:
for num in range(1, 1001):
    if is_armstrong_number(num):
        print(num)
