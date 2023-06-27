#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:21:19 2023

@author: dylanmoraes
"""

def dec_to_bin(decimal):
    return bin(decimal)[2:]

def bin_to_dec(binary):
    return int(binary, 2)

decimal_number = 42
binary_number = '101010' 
print(dec_to_bin(decimal_number)) 
# Output: 101010 
print(bin_to_dec(binary_number)) # Output: 42