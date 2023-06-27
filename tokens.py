#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:52:09 2023

@author: dylanmoraes
"""

def split_string(inpstr):
    tokens = inpstr.split()
    return tokens
    
input_string = input("Enter a string: ") 
tokens = split_string(input_string) 
print(tokens)