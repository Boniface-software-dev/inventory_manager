from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

from lib.models.supplier import Supplier
from lib.models.category import Category
from lib.models.product import Product
from lib.models.stock_transaction import StockTransaction
# Initialize the database connection and session

engine = create_engine('sqlite:///inventory.db')
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    Base.metadata.create_all(engine)