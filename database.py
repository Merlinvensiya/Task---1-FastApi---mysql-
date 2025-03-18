from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Replace with your actual MySQL credentials
DATABASE_URL = "mysql+pymysql://root:Meruvensi#2425@127.0.0.1:3306/hex_quitq"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()