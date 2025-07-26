import json
import os
from datetime import datetime

class Inventory:
    def __init__(self, username, filepath='data/inventories.json'):
        self.filepath = filepath
        self.username = username
        self.inventories = self.load_data()

    def load_data(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    def save_data(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.inventories, f, indent=2)

    def add_product(self, product):
        user_inventory = self.inventories.get(self.username, [])
        user_inventory.append(product.to_dict())
        self.inventories[self.username] = user_inventory
        self.save_data()

    def view_inventory(self):
        return self.inventories.get(self.username, [])

    def remove_product(self, name):
        user_inventory = self.inventories.get(self.username, [])
        new_inventory = [p for p in user_inventory if p['name'].lower() != name.lower()]
        self.inventories[self.username] = new_inventory
        self.save_data()
        return len(new_inventory) < len(user_inventory)
