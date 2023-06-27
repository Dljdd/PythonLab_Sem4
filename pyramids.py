#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:23:55 2023

@author: dylanmoraes
"""

for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()
print()
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
    
    
print()

#pascal triangle

rows = 6

for i in range(rows):
    num =1
    for j in range(i+1):
        print(num, end=" ")
        num = int(num * (i-j) / (j + 1))
    print()
    
print()

#floyd triangle

num = 1

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(num, end=" ")
        num +=1
    print()
    
print()
#number pyramid

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    
print()
#reverse number pyramid
rows = 5

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()