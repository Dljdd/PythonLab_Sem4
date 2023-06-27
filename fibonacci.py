#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:41:03 2023

@author: dylanmoraes
"""

def fibo(n):
    fibo_list = [0,1]
    for i in range(2,n):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    return fibo_list

n = 10
fib_sequence = fibo(n)
print(fib_sequence)