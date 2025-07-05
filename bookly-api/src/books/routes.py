from fastapi import status, APIRouter
from fastapi.exceptions import HTTPException
from typing import List

from src.books.schema import Book, BookUpdateModel
from src.books.book_data import books

book_router = APIRouter()


@book_router.get('/', response_model=List[Book])
def get_books():
  return books


@book_router.get('/{book_id}')
def get_one_book(book_id: int) -> dict:
  for book in books:
    if book['id'] == book_id:
      return book
  
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book Not found') 


@book_router.post('/', status_code=status.HTTP_201_CREATED, response_model=Book)
def create_book(book_data: Book):
  new_book = book_data.model_dump()
  books.append(new_book)
  return new_book



@book_router.patch('/{book_id}', response_model=Book, status_code=status.HTTP_202_ACCEPTED)
def edit_book(book_id: int, book_data: BookUpdateModel):
  for book in books:
    if book['id'] == book_id:
      book['title'] = book_data.title
      book['author'] = book_data.author
      book['publisher'] = book_data.publisher
      book['page_count'] = book_data.page_count
      book['language'] = book_data.language    
      return books[book_id - 1]
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book Not found') 


@book_router.delete('/{book_id}', response_model=Book, status_code=status.HTTP_202_ACCEPTED)
def delete_book(book_id: int):
  for book in books:
    if book['id'] == book_id:
      books.remove(book)
      return book
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book Not found') 


# @book_router.put('/books/{book_id}', response_model=Book, status_code=status.HTTP_202_ACCEPTED)
# def update_book(book_id: int, book_data: BookUpdateModel):
#   for book in books:
#     if book['id'] == book_id:
#       book = book_data.model_dump() 
#     return books[book_id - 1]
#   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book Not found') 
  