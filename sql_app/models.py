from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class books(Base):
    __tablename__ = "books"

    id = Column(Integer,  primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    language = Column(String, index=True)
    year = Column(String, index=True)
    extension = Column(String, index=True)
    publisher = Column(String, index=True)
    md5 = Column(String)



