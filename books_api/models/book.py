import uuid
from db import db

class BookModel(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.String(32), primary_key=True, default=lambda: str(uuid.uuid4().hex))
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    read = db.Column(db.Boolean, nullable=False, default=False)

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'read': self.read,
        }