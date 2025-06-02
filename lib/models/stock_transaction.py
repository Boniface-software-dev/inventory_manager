from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from lib.db import Base

class StockTransaction(Base):
    __tablename__ = 'stock_transactions'
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    change_in_quantity = Column(Integer, nullable=False)
    transaction_type = Column(String, nullable=False)  # 'purchase', 'sale', 'adjustment'
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationships
    product = relationship("Product", back_populates="stock_transactions")
    
    def __repr__(self):
        return (f"<StockTransaction(id={self.id}, product_id={self.product_id}, "
                f"change_in_quantity={self.change_in_quantity}')>")