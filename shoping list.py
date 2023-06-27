#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:34:44 2023

@author: dylanmoraes
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:18:15 2023

@author: dylanmoraes
"""

class ShoppingList:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        self.display_shopping_list()
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.display_shopping_list()
        else:
            print(f"{item} is not in the shopping list")
    
    def update_quantity(self, item, quantity):
        for i in range(len(self.items)):
            if self.items[i][0] == item:
                name, current_quantity, price = self.items[i]
                self.items[i] = (name, quantity, price)
                self.display_shopping_list()
                return
        
        print(f"{item} is not in the shopping list")
        
    def calculate_total_cost(self):
        total_cost = 0
        
        for item, quantity, price in self.items:
            total_cost += quantity*price
            
        return total_cost
    
    def display_shopping_list(self):
        print("Shopping List: ")
        
        for item, quantity, price in self.items:
            print(f"{item} - Quantity: {quantity}, Price: {price}")
        print("")
    
def merge_shopping_lists(list1, list2):
    merged_list = list1 + list2
    return merged_list

shopping_list = ShoppingList()
shopping_list.add_item(("Apple", 3, 1.5)) 
shopping_list.add_item(("Banana", 5, 0.5)) 
shopping_list.add_item(("Orange", 2, 1.2))
# Remove items 
shopping_list.remove_item(("Banana", 5, 0.5)) 
# Update quantity 
shopping_list.update_quantity("Apple", 5)
# Calculate total cost
total_cost = shopping_list.calculate_total_cost() 
print(f"Total cost: {total_cost}")
# Merge shopping lists
list1 = [("Apple", 3, 1.5), ("Banana", 5, 0.5)] 
list2 = [("Orange", 2, 1.2), ("Grapes", 4, 2.0)] 
merged_list = merge_shopping_lists(list1, list2) 
print(merged_list)