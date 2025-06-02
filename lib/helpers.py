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
   