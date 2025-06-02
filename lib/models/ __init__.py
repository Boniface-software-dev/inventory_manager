from sqlalchemy.orm import declarative_base

# lib/models/__init__.py
from .category import Category
from .supplier import Supplier
from .product import Product
from .stock_transaction import StockTransaction

Base = declarative_base()
