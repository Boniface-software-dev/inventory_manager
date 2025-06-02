# populate_db.py
from lib.models.db import session
from lib.models.category import Category
from lib.models.supplier import Supplier
from lib.models.product import Product
from lib.models.stock_transaction import StockTransaction
from datetime import datetime, timedelta

def populate_database():
    # Clear existing data
    session.query(StockTransaction).delete()
    session.query(Product).delete()
    session.query(Supplier).delete()
    session.query(Category).delete()
    session.commit()

    # Create categories
    categories = [
        Category(name="Engine Components", description="Internal combustion engine parts"),
        Category(name="Braking System", description="Brakes and related components"),
        Category(name="Electrical", description="Wiring, batteries, electronics"),
        Category(name="Suspension", description="Shocks, struts, steering parts"),
        Category(name="Exhaust System", description="Mufflers, pipes, converters"),
    ]
    session.add_all(categories)
    session.commit()
    print("Added categories")

    # Create suppliers
    suppliers = [
        Supplier(name="AutoParts Pro", contact_info="contact@autopartspro.com"),
        Supplier(name="Brake Masters", contact_info="sales@brakemasters.com"),
        Supplier(name="ElectroAuto", contact_info="support@electroauto.net"),
        Supplier(name="Suspension World", contact_info="info@suspensionworld.org"),
        Supplier(name="Exhaust Experts", contact_info="orders@exhaustexperts.io"),
    ]
    session.add_all(suppliers)
    session.commit()
    print("Added suppliers")

    # Create products
    products = [
        Product(name="Spark Plug", price=4.99, quantity_in_stock=100, 
                description="Iridium tip, long lifespan", 
                category_id=1, supplier_id=1),
        Product(name="Oil Filter", price=12.50, quantity_in_stock=50, 
                description="High efficiency filtration", 
                category_id=1, supplier_id=1),
        Product(name="Brake Pads", price=35.00, quantity_in_stock=40, 
                description="Ceramic, low dust", 
                category_id=2, supplier_id=2),
        Product(name="Brake Rotor", price=45.00, quantity_in_stock=30, 
                description="Vented, drilled", 
                category_id=2, supplier_id=2),
        Product(name="Car Battery", price=120.00, quantity_in_stock=20, 
                description="12V, 700CCA", 
                category_id=3, supplier_id=3),
        Product(name="Alternator", price=150.00, quantity_in_stock=15, 
                description="120A output", 
                category_id=3, supplier_id=3),
        Product(name="Shock Absorber", price=85.00, quantity_in_stock=25, 
                description="Gas-charged", 
                category_id=4, supplier_id=4),
        Product(name="Strut Assembly", price=120.00, quantity_in_stock=18, 
                description="Complete assembly", 
                category_id=4, supplier_id=4),
        Product(name="Catalytic Converter", price=250.00, quantity_in_stock=12, 
                description="EPA compliant", 
                category_id=5, supplier_id=5),
        Product(name="Muffler", price=90.00, quantity_in_stock=22, 
                description="Stainless steel", 
                category_id=5, supplier_id=5),
    ]
    session.add_all(products)
    session.commit()
    print("Added products")

    # Create stock transactions with realistic timestamps
    transactions = [
        StockTransaction(product_id=1, change_in_quantity=200, 
                         transaction_type="purchase", 
                         timestamp=datetime.now() - timedelta(days=10)),
        StockTransaction(product_id=3, change_in_quantity=-5, 
                         transaction_type="sale", 
                         timestamp=datetime.now() - timedelta(days=8)),
        StockTransaction(product_id=5, change_in_quantity=10, 
                         transaction_type="adjustment", 
                         timestamp=datetime.now() - timedelta(days=6)),
        StockTransaction(product_id=6, change_in_quantity=-3, 
                         transaction_type="sale", 
                         timestamp=datetime.now() - timedelta(days=5)),
        StockTransaction(product_id=7, change_in_quantity=30, 
                         transaction_type="purchase", 
                         timestamp=datetime.now() - timedelta(days=4)),
        StockTransaction(product_id=10, change_in_quantity=-8, 
                         transaction_type="sale", 
                         timestamp=datetime.now() - timedelta(days=3)),
        StockTransaction(product_id=2, change_in_quantity=-5, 
                         transaction_type="adjustment", 
                         timestamp=datetime.now() - timedelta(days=1)),
    ]
    session.add_all(transactions)
    session.commit()
    print("Added stock transactions")

    print("\nDatabase populated successfully with test data!")

if __name__ == "__main__":
    populate_database()