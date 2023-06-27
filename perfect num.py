#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:49:09 2023

@author: dylanmoraes
"""

def is_perfect_number(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) == num

# Example usage:
for num in range(1, 10001):
    if is_perfect_number(num):
        print(num)
