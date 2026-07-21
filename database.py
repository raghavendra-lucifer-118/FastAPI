from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:postgreSQL@localhost:5432/database2"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False , autoflush= False , bind = engine)