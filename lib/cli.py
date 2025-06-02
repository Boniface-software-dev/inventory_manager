from lib.helpers import *

# CLI for Inventory Management System

def main_menu():
    print("\n=== INVENTORY MANAGEMENT SYSTEM ===")
    print("1. Categories")
    print("2. Suppliers")
    print("3. Products")
    print("4. Stock Transactions")
    print("5. Exit")
    return input("Select an option (1-5): ")

# Function to handle category management

def category_menu():
    while True:
        print("\n=== CATEGORY MANAGEMENT ===")
        print("1. Add Category")
        print("2. View Categories")
        print("3. Update Category")
        print("4. Delete Category")
        print("5. Back to Main Menu")
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            name = input("Enter category name: ")
            description = input("Enter category description (optional): ")
            create_category(name, description)
            print(f"Category '{name}' added successfully.")

        elif choice == '2':
            categories = get_all_categories()
            display_categories(categories)

        elif choice == '3':
            category_id = int(input("Enter category ID to update: "))
            name = input("Enter new category name: ")
            description = input("Enter new category description (optional): ")
            update_category(category_id, name or None, description or None)
            print("Category updated successfully.")

        elif choice == '4':
            category_id = int(input("Enter category ID to delete: "))
            delete_category(category_id)
            print("Category deleted successfully.")

        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

# Function to handle supplier management
def supplier_menu():
    while True:
        print("\n--- SUPPLIER MANAGEMENT ---")
        print("1. List all suppliers")
        print("2. Add new supplier")
        print("3. Update supplier")
        print("4. Delete supplier")
        print("5. Back to main menu")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            suppliers = get_all_suppliers()
            display_suppliers(suppliers)

        elif choice == '2':
            name = input("Supplier name: ")
            contact = input("Contact info (optional): ")
            create_supplier(name, contact)
            print(f"Supplier '{name}' created!")

        elif choice == '3':
            sup_id = int(input("Supplier ID to update: "))
            new_name = input("New name (leave blank to keep): ")
            new_contact = input("New contact info (leave blank to keep)")
            update_supplier(sup_id, new_name or None, new_contact or None)
            print(f"{new_name}, updated succesfully!")

        elif choice == '4':
            sup_id = int(input("Supplier ID to delete: "))
            delete_supplier(sup-id)
            print("Supplier deleted!")

        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

#Product menu fuctions
def Product_menu():
    while True:
        print("\n --- PRODUCT MANAGEMENT ---")
        print("1. List all products")
        print("2. Add new product")
        print("3. Update product")
        print("4. Delete product")
        print("5. Back to main menu")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            products = get_all_products()
            display_products(products)
        
        elif choice == '2':
            name = input("Product name: ")
            price = float(input("Price: "))
            quantity = int(input("Initial quantity: "))
            cat_id = int(input("Category ID: "))
            sup_id = int(input("Supplier ID: "))
            desc = input("Description (optional): ")
            
            create_product(name, price, cat_id, sup_id, desc, quantity)
            print(f"Product '{name}' created!")

        elif choice == '3':
            prod_id = int(input("Product ID to update: "))
            print("Leave fields blank to keep current values")
            
            updates = {}
            if name := input("New name: "):
                updates['name'] = name
            if price := input("New price: "):
                updates['price'] = float(price)
            if quantity := input("New quantity: "):
                updates['quantity_in_stock'] = int(quantity)
            if cat_id := input("New category ID: "):
                updates['category_id'] = int(cat_id)
            if sup_id := input("New supplier ID: "):
                updates['supplier_id'] = int(sup_id)
            if desc := input("New description: "):
                updates['description'] = desc
                
            update_product(prod_id, **updates)
            print("Product updated!")
        
        elif choice == '4':
            prod_id = int(input("Product ID to delete: "))
            delete_product(prod_id)
            print("Product deleted!")

        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

# Function to handle stock transactions
def transaction_menu():
    while True:
        print("\n=== STOCK TRANSACTION MANAGEMENT ===")
        print("1. Add Stock Transaction")
        print("2. View Transactions by Product")
        print("3. View All Transactions")
        print("4. Delete Transaction")
        print("5. Back to Main Menu")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            product_id = int(input("Enter product ID: "))
            change_in_quantity = int(input("Enter change in quantity: "))
            transaction_type = input("Enter transaction type (purchase/sale/adjustment): ")
            create_stock_transaction(product_id, change_in_quantity, transaction_type)
            print("Stock transaction added successfully.")

        elif choice == '2':
            product_id = int(input("Enter product ID to view transactions: "))
            transactions = get_transactions_by_product(product_id)
            if transactions:
                for transaction in transactions:
                    print(transaction)
            else:
                print("No transactions found for this product.")

        elif choice == '3':
            transactions = get_all_stock_transactions()
            if transactions:
                for transaction in transactions:
                    print(transaction)
            else:
                print("No stock transactions found.")

        elif choice == '4':
            transaction_id = int(input("Enter transaction ID to delete: "))
            try:
                delete_stock_transaction(transaction_id)
                print("Transaction deleted successfully.")
            except ValueError as e:
                print(e)

        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

# Main function to run the CLI


        
            



