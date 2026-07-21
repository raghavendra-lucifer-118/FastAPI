from sqlalchemy import Column , Integer ,String , DECIMAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Product(Base):
    __tablename__ = "prodcuts_list"
    id  = Column(Integer , primary_key = True , index = True)
    price = Column(DECIMAL)
    name = Column(String )
    description = Column(String)
    quantity = Column(Integer)
    