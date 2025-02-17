from models.book import BookModel

def create_data_if_not_exists(db):

    books_data = [
        {"title": "On the Road", "author": "Jack Kerouac", "read": True},
        {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "read": False},
        {"title": "Green Eggs and Ham", "author": "Dr. Seuss", "read": True}
    ]
    for book_data in books_data:
        existing_book = db.session.query(BookModel).filter_by(title=book_data['title']).first()

        if not existing_book:
            new_book = BookModel(
                # id=uuid.uuid4().hex,
                title=book_data['title'],
                author=book_data['author'],
                read=book_data['read']
            )
            db.session.add(new_book)

    db.session.commit()

if __name__ == "__main__":
    create_data_if_not_exists()