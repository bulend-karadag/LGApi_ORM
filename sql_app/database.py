from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://user:password@localhost:3306/LibGen'
#SQLALCHEMY_DATABASE_URL = "sqlite:////sql_app/libgen.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    #SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    SQLALCHEMY_DATABASE_URL, encoding='utf8', echo=False
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()