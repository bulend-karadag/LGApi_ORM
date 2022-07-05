from typing import List, Union

from pydantic import BaseModel


class bookBase(BaseModel):
    id : int
    title : str
    author : str
    language : str = None
    year : str = None
    extension : str = None
    publisher : str = None
    md5 : str
    
    
class bookCreate(bookBase):
    pass


class book(bookBase):
    pass
    
    class Config:
        orm_mode = True


class langExt(BaseModel):
    language : str = None
    extension : str = None
    
    class Config:
        orm_mode = True

    