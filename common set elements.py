#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:40:34 2023

@author: dylanmoraes
"""

def find_common_elements(sets):
    
    common_elements = set.intersection(*sets)
    
    return common_elements

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 6, 7, 8}
common_elements = find_common_elements([set1, set2, set3]) 
print(common_elements)
