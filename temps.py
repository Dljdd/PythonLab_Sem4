#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 05:28:27 2023

@author: dylanmoraes
"""

def calculate_average_temperature(forecasts):
    monthly_temperatures = {}
    monthly_counts = {}
    for forecast in forecasts:
        date = forecast["date"]
        month = date.split("-")[1]
        temperature = forecast["temperature"]
        if month in monthly_temperatures:
            monthly_temperatures[month] += temperature
            monthly_counts[month] += 1
        else:
            monthly_temperatures[month] = temperature
            monthly_counts[month] = 1
    
    average_temperatures = {}
    for month, total_temperature in monthly_temperatures.items():
        average_temperatures[month] = total_temperature / monthly_counts[month]
    
    return average_temperatures

# Example usage
forecasts = [
    {"date": "2023-01-01", "temperature": 25},
    {"date": "2023-01-15", "temperature": 28},
    {"date": "2023-02-10", "temperature": 30},
    {"date": "2023-02-20", "temperature": 32},
    {"date": "2023-03-05", "temperature": 27},
    {"date": "2023-03-15", "temperature": 26},
]

average_temperatures = calculate_average_temperature(forecasts)
for month, average_temperature in average_temperatures.items():
    print(f"Month: {month}, Average Temperature: {average_temperature}")
