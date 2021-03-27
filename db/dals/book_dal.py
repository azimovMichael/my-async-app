from typing import List

from sqlalchemy.future import select
from sqlalchemy.orm import Session

from db.models.book import Book

class BookDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_book(self, name: str, author: str,   release_year: int):
        new_book = Book(name=name,author=author, release_year=release_year)
        self.db_session.add(new_book)
        await self.db_session.flush()

    async def get_all_books(self) -> List[Book]:
        q = await self.db_session.execute(select(Book).order_by(Book.id))
        return q.scalars().all()