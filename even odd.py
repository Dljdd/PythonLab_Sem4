#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:54:05 2023

@author: dylanmoraes
"""

def filter_even(numbers):
    filtered_nums =[]
    for num in numbers:
        if num % 2 != 0:
            filtered_nums.append(num)
    return filtered_nums
def get_even(numbers):
    even_nums = [num for num in numbers if num%2==0]
    return even_nums

input_numbers = [1, 2, 3, 4, 5, 6]
filtered_numbers = filter_even(input_numbers) 
print(filtered_numbers)
even_nums = get_even(input_numbers)
print(even_nums)