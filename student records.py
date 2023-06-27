#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:04:18 2023

@author: dylanmoraes
"""

def calculate_average(grades):
    return sum(grades) / len(grades)

def sort_student_records(records):
    sorted_records = sorted(records, key = lambda x: calculate_average(x[2]))
    
    for record in sorted_records:
        name, age, grades = record
        average_grade = calculate_average(grades)
        print(f"Name: {name} Age:{age} Average grade = {average_grade}")
        
student_records = [
("Alice", 20, [85, 90, 92]), ("Bob", 21, [78, 80, 75]), ("Charlie", 19, [95, 88, 91])
]

sort_student_records(student_records)
