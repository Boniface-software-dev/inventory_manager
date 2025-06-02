from lib.db import session
from lib.models.category import Category
from lib.models.product import Product
from lib.models.supplier import Supplier
from lib.models.stock_transaction import StockTransaction

# CRUD Operations
#  for Category
def create_category(name, description=""):
    category = Category(name=name, description=description)
    session.add(category)
    session.commit()
    return category

def get_all_categories():
    return session.query(Category).all()

def get_category_by_id(category_id):
    return session.query(Category).get(category_id)

def update_category(category_id, new_name=None, new_description=None):
    category = session.query(Category).get(category_id)
    if new_name:
        category.name = new_name
    if new_description:
        category.description = new_description
    session.commit()
    return category

def delete_category(category_id):
    category = session.query(Category).get(category_id)
    session.delete(category)
    session.commit()
   
# CRUD Operations for Product
def create_product(name, description, price, category_id, supplier_id, quantity=0):
    product = Product(name=name,
                      description=description, 
                      price=price,
                      category_id=category_id, 
                      supplier_id=supplier_id,
                      quantity_in_stock=quantity)
    session.add(product)
    session.commit()
    return product

def get_all_products():
    return session.query(Product).all()

def get_product_by_id(product_id):
    return session.query(Product).get(product_id)

def update_product(product_id, **kwargs):
    product = session.query(Product).get(product_id)
    for key, value in kwargs.items():
        if hasattr(product, key):
            setattr(product, key, value)
    session.commit()
    return product

def delete_product(product_id):
    product = session.query(Product).get(product_id)
    session.delete(product)
    session.commit()
    
# CRUD Operations for Supplier
def create_supplier(name, contact_info=""):
    supplier = Supplier(name=name, contact_info=contact_info)
    session.add(supplier)
    session.commit()
    return supplier

def get_all_suppliers():
    return session.query(Supplier).all()

def get_supplier_by_id(supplier_id):
    return session.querry(Supplier).get(supplier_id)

def update_supplier(supplier_id, new_name=None, new_contact_info=None):
    supplier = session.query(Supplier).get(supplier_id)
    if new_name:
        supplier.name = new_name
    if new_contact_info:
        supplier.contact_info = new_contact_info
    session.commit()
    return supplier

def delete_supplier(supplier_id):
    supplier = session.query(Supplier).get(supplier_id)
    session.delete(supplier)
    session.commit()

# CRUD Operations for StockTransaction
def create_stock_transaction(product_id, change_in_quantity, transaction_type):
    #update product stock
    product = session.query(Product).get(product_id)
    if transaction_type == 'purchase':
        product.quantity_in_stock += change_in_quantity
    elif transaction_type == 'sale':
        product.quantity_in_stock -= change_in_quantity
    elif transaction_type == 'adjustment':
        product.quantity_in_stock += change_in_quantity 
    else:
        raise ValueError("Invalid transaction type. Must be 'purchase', 'sale', or 'adjustment'.")
    
    # Create the stock transaction record
    transaction = StockTransaction(
        product_id=product_id,
        change_in_quantity=change_in_quantity,
        transaction_type=transaction_type
    )
    session.add(transaction)
    session.commit()
    return transaction

def get_transactions_by_product(product_id):
    return session.query(StockTransaction).filter_by(product_id=product_id).all()

def get_all_stock_transactions():
    return session.query(StockTransaction).all()

def delete_stock_transaction(transaction_id):
    transaction = session.query(StockTransaction).get(transaction_id)
    if transaction:
        # Adjust the product stock before deleting the transaction
        product = session.query(Product).get(transaction.product_id)
        if transaction.transaction_type == 'purchase':
            product.quantity_in_stock -= transaction.change_in_quantity
        elif transaction.transaction_type == 'sale':
            product.quantity_in_stock += transaction.change_in_quantity
        elif transaction.transaction_type == 'adjustment':
            product.quantity_in_stock -= transaction.change_in_quantity
        
        session.delete(transaction)
        session.commit()
    else:
        raise ValueError("Transaction not found.")
    return transaction

#Display Helpers
def display_categories(categories):
    print("\nCategories:")
    for cat in categories:
        print(f"{cat.id}: {cat.name} - {cat.description or 'No description'}")

def display_products(products):
    print("\nProducts:")
    for prod in products:
        cat_name = prod.category.name if prod.category else "No Category"
        sup_name = prod.supplier.name if prod.supplier else "No Supplier"
        print(f"{prod.id}: {prod.name} - ${prod.price:.2f}, Stock: {prod.quantity_in_stock}")
        print(f"Category: {cat_name}, Supplier: {sup_name}")

def display_suppliers(suppliers):
    print("\nSuppliers:")
    for sup in suppliers:
        print(f"{sup.id}: {sup.name} - {sup.contact_info or 'No contact info'}")

def display_transactions(transactions):
    print("\nStock Transactions:")
    for trans in transactions:
        print(f"{trans.timestamp}: Product {trans.product_id} - {trans.chang_in_qantity} units ({trans.transaction_type}) ")