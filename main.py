from modules.product import Product
from modules.inventory import Inventory

def main():
    inv = Inventory()

    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Remove Product")
        print("4. Exit")
        print("5. Filter Products by Category")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Product name: ")
            price = int(input("Price :"))
            qty = int(input("Quantity: "))
            category = input("Category: ")
            prod = Product(name, price, qty, category)
            inv.add_product(prod)
            print("✅ Product added.")
        elif choice == '2':
            print("📦 Inventory:")
            for item in inv.view_inventory():
                print(f"{item['name']} | Qty: {item['quantity']} | Price: {item['price']} | Added: {item['added_at']}")

        elif choice == '3':
            name = input("Product name to remove: ")
            if inv.remove_product(name):
                print("✅ Product removed.")
            else:
                print("❌ Product not found.")
        elif choice == '4':
            print("👋 Exiting Inventory System. Goodbye!")
            break
        
        elif choice == '5':
            category = input("Enter category to filter: ")
            filtered = inv.filter_by_category(category)
            if filtered:
                print(f"\n📦 Products in '{category}' category:")
                for item in filtered:
                    print(f"{item['name']} | Qty: {item['quantity']} | Price: ₹{item['price']} | Added: {item['added_at']}")
            else:
                print("❌ No products found in this category.")



if __name__ == "__main__":
    main()
