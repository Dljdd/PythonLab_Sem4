#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:35:17 2023

@author: dylanmoraes
"""

def encrypt_message(message, mapping):
    encrypted_message = ""
    for char in message:
        if char in mapping:
            encrypted_message += mapping[char]
        else:
            encrypted_message += char
    
    return encrypted_message

def decrypt_message(message, mapping):
    decrypted_message = ""
    
    reverse_mapping = {v:k for k,v in mapping.items()}
    
    for char in message:
        if char in reverse_mapping:
            decrypted_message += reverse_mapping[char]
        else:
            decrypted_message += char
    
    return decrypted_message

char_mapping = {
'a': 'm', 
'b': 'n','c': 'o', 'd': 'p', 'e': 'q', 'f': 'r', 'g': 's', 'h': 't', 'i': 'u', 'j': 'v', 'k': 'w', 'l': 'x', 'm': 'a', 'n': 'b', 'o': 'c', 'p': 'd', 'q': 'e', 'r': 'f', 's': 'g', 't': 'h', 'u': 'i', 'v': 'j', 'w': 'k', 'x': 'l', 'y': 'y', 'z': 'z'
}
message = "hello world"

encrypted_message = encrypt_message(message, char_mapping) 
decrypted_message = decrypt_message(encrypted_message, char_mapping) 
print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)