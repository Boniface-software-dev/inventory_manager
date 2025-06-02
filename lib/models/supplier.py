from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.db import Base

class Supplier(Base):
    __tablename__ = 'suppliers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    contact_info = Column(String)

    products = relationship("Product", back_populates="supplier")
    def __repr__(self):
        return f"<Supplier(id={self.id}, name='{self.name}', contact_info='{self.contact_info}')>"