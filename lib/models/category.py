from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models.db import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    
    # Relationships

    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}', description='{self.description}')>"
