import json
import os
from datetime import datetime

class Inventory:
    def __init__(self, filepath='data/inventory.json'):
        self.filepath = filepath
        self.inventory = self.load_inventory()
    
    def load_inventory(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def save_inventory(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.inventory, f, indent=2)
    
    def add_product(self, product):
        self.inventory.append(product.to_dict())
        self.save_inventory()
    
    def view_inventory(self):
        return self.inventory

    def remove_product(self, name):
        original_len = len(self.inventory)
        self.inventory = [p for p in self.inventory if p['name'].lower() != name.lower()]
        self.save_inventory()
        return original_len != len(self.inventory)
    
    def filter_by_category(self,category):
        return [item for item in self.inventory if item['category'].lower() == category.lower()]
