from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from lib.db import Base

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    quantity_in_stock = Column(Integer, default=0)
    category_id = Column(Integer, ForeignKey('categories.id'))
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))

    category = relationship("Category", back_populates="products")
    supplier = relationship("Supplier", back_populates="products")
    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price}, quantity_in_stock={self.quantity_in_stock})>"
    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Stock: {self.quantity_in_stock}, Category: {self.category.name if self.category else 'N/A'}, Supplier: {self.supplier.name if self.supplier else 'N/A'}"
    