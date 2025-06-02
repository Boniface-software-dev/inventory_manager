# Auto Parts Inventory Manager

A command-line inventory management system designed specifically for auto parts retailers and repair shops. Track spare parts, suppliers, stock levels, and transactions with ease.

## Features

- **Product Management**
  - Add/update/delete auto parts
  - Track prices and stock levels
  - Detailed product descriptions
- **Supplier Tracking**
  - Manage parts suppliers
  - Contact information storage
- **Stock Control**
  - Record purchases and sales
  - Adjust inventory levels
  - Transaction history
- **Reporting**
  - View inventory by category
  - Check low-stock items
  - Review transaction logs

## Technologies Used

- **Python** (v3.8+)
- **SQLAlchemy** (ORM)
- **Alembic** (Database migrations)
- **SQLite** (Database engine)
- **Pipenv** (Dependency management)

## Installation & Setup

### Prerequisites
- Python 3.8+
- Pipenv (`pip install pipenv`)

### Step-by-Step Setup
```bash
# Clone repository
git clone git@github.com:Boniface-software-dev/inventory_manager.git
cd auto-parts-inventory

# Install dependencies
pipenv install

# Activate virtual environment
pipenv shell

# Initialize database
python -c "from lib.db import init_db; init_db()"

# Run database migrations
pipenv run alembic upgrade head

# (Optional) Load sample data
python populate_db.py

# Start application
python run.py


## Usage

#Main Menu
=== AUTO PARTS INVENTORY SYSTEM ===
1. Categories
2. Suppliers
3. Products
4. Stock Transactions
5. Exit
Enter choice: 

## Database Management
# Create new migration after model changes
pipenv run alembic revision --autogenerate -m "description"

# Apply migrations
pipenv run alembic upgrade head

# Reset database (careful!)
rm inventory.db

## Database Schema

erDiagram
    CATEGORY ||--o{ PRODUCT : contains
    SUPPLIER ||--o{ PRODUCT : supplies
    PRODUCT ||--o{ STOCK_TRANSACTION : has
    CATEGORY {
        integer id PK
        string name
        string description
    }
    SUPPLIER {
        integer id PK
        string name
        string contact_info
    }
    PRODUCT {
        integer id PK
        string name
        string description
        float price
        integer quantity_in_stock
        integer category_id FK
        integer supplier_id FK
    }
    STOCK_TRANSACTION {
        integer id PK
        integer product_id FK
        integer change_in_quantity
        string transaction_type
        datetime timestamp
    }

## Support
For assistance, contact:
https://github.com/Boniface-software-dev