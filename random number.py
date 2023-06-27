#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:47:58 2023

@author: dylanmoraes
"""

import random

def guess_number():
    target_number = random.randint(1,100)
    num_guesses = 0
    
    while True:
        
        guess = int(input("Guess the number between 1 to 100:  "))
        num_guesses +=1
        
        if guess < target_number:
            print("Too low!")
        elif guess > target_number:
            print("Too high!")
        else:
            print(f"Congratulations u guessed the number in {num_guesses} guesses")
            break

guess_number()