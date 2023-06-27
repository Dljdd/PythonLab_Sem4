#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:18:01 2023

@author: dylanmoraes
"""

def is_palindrome(string):
    string = string.lower()
    
    i = 0 
    j = len(string) - 1
    
    while i < j:
        if string[i] != string[j]:
            return False
        else:
            i +=1
            j -=1
    
    return True

input_string = input("Enter a string: ") 
if is_palindrome(input_string):
    print("The string is a palindrome.") 
else:
    print("The string is not a palindrome.")