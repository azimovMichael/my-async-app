from typing import List, Optional

from fastapi import APIRouter, Depends

from db.dals.book_dal import BookDAL
from db.models.book import Book
from dependencies import get_book_dal

router = APIRouter()


@router.post("/books")
async def create_book(name: str, author: str, release_year: int, book_dal: BookDAL = Depends(get_book_dal)):
    return await book_dal.create_book(name, author, release_year)


@router.put("/books/{book_id}")
async def update_book(book_id: int, name: Optional[str] = None, author: Optional[str] = None, release_year: Optional[int] = None,
                      book_dal: BookDAL = Depends(get_book_dal)):
    return await book_dal.update_book(book_id, name, author, release_year)


@router.get("/books")
async def get_all_books(book_dal: BookDAL = Depends(get_book_dal)) -> List[Book]:
    return await book_dal.get_all_books()
