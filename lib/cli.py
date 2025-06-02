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
            print("Invalid choice")



