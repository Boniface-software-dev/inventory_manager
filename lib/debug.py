from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models.db import Base

engine = create_engine('sqlite:///inventory.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
