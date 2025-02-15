from db import db
from models.book import BookModel
from typing import List


class BookRepo:
    def create(self, book):
        db.session.add(book)
        db.session.commit()

    def fetchById(self, id) -> "BookModel":
        return db.session.query(BookModel).filter_by(id=id).first()

    def fetchAll(self) -> List["BookModel"]:
        return db.session.query(BookModel).all()

    def delete(self, id) -> None:
        book = db.session.query(BookModel).filter_by(id=id).first()
        db.session.delete(book)
        db.session.commit()

    def update(self, book_data):
        db.session.merge(book_data)
        db.session.commit()
