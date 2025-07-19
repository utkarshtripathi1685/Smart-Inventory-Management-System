from datetime import datetime

class Product:
    def __init__(self, name, price, quantity,category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.added_at=datetime.now().isoformat()
        
    def to_dict(self):
        return{
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'category': self.category,
            'added_at': self.added_at
        }