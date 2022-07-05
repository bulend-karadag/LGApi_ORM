from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import desc

from . import models, schemas


def get_book_title(db: Session, 
                   book_title : str, 
                   book_language : str,
                   book_extension : str,
                   skip: int = 0, 
                   limit: int = 20):
    title = "%{}%".format(book_title)
    language = "%{}%".format(book_language)
    extension = "%{}%".format(book_extension)
    return db.query(models.books).filter(models.books.title.like(title),
                                         models.books.language.like(language),
                                         models.books.extension.like(extension),
                                         ).order_by(models.books.year.desc()).offset(skip).limit(limit).all()
    
def get_book_author(db: Session, 
                    book_author: str, 
                    book_language : str,
                    book_extension : str,
                    skip: int = 0, 
                    limit: int = 20):
    author = "%{}%".format(book_author)
    language = "%{}%".format(book_language)
    extension = "%{}%".format(book_extension)
    return db.query(models.books).filter(models.books.author.like(author),
                                         models.books.language.like(language),
                                         models.books.extension.like(extension),
                                         ).order_by(models.books.year.desc()).offset(skip).limit(limit).all()

def get_book_publisher(db: Session, 
                    book_publisher: str, 
                    book_language : str,
                    book_extension : str,
                    skip: int = 0, 
                    limit: int = 20):
    publisher = "%{}%".format(book_publisher)
    language = "%{}%".format(book_language)
    extension = "%{}%".format(book_extension)
    return db.query(models.books).filter(models.books.publisher.like(publisher), 
                                         models.books.language.like(language),
                                         models.books.extension.like(extension),
                                         ).order_by(models.books.year.desc()).offset(skip).limit(limit).all()



def create_book(db: Session, book: schemas.bookCreate):
    db_book = models.books(title=book.title, 
                           author=book.author,
                           language=book.language,
                           year=book.year,
                           extension=book.extension,
                           publisher=book.publisher)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

