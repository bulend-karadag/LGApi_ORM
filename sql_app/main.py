from typing import List
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books", response_model=List[schemas.book])
def index_params(search, keyword, language, extension, limit, page, db: Session = Depends(get_db)):
    l=int(limit)
    p=int(page)
    skip = l*p
    if search=='Title':
        books = crud.get_book_title(db, book_title= keyword, book_language=language ,book_extension=extension, skip=skip, limit=limit)
    elif search=='Author':
        books = crud.get_book_author(db, book_author= keyword, book_language=language ,book_extension=extension, skip=skip, limit=limit)
    elif search=='Publisher':
        books = crud.get_book_publisher(db, book_publisher= keyword, book_language=language ,book_extension=extension, skip=skip, limit=limit)
    
    if books is None:
        raise HTTPException(status_code=404, detail="book not found")
    return books


