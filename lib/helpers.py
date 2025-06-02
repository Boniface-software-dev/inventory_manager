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

def delete_product(supplier_id):
    supplier = session.query(Supplier).get(supplier_id)
    session.delete(supplier)
    session.commit()
    
