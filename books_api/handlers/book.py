from schemas.book_schema import BookSchema
from repositories.book_repo import BookRepo


bookRepo = BookRepo()
bookSchema = BookSchema()
bookCreateSchema = BookSchema(only=("title", "author", "read"))
bookListSchema = BookSchema(many=True)
bookUpdateSchema = BookSchema(only=("title", "author", "read"), partial=True)


def get_all():
    return bookListSchema.dump(bookRepo.fetchAll()), 200


def create(body):
    item_data = bookSchema.load(body)
    bookRepo.create(item_data)
    return bookSchema.dump(item_data), 201


def delete(id):
    item_data = bookRepo.fetchById(id)
    if item_data:
        bookRepo.delete(id)
        return {"message": "Item deleted successfully"}, 200
    return {"message": "Item not found"}, 404


def update(id, body):
    item_data = bookRepo.fetchById(id)
    if item_data and bookUpdateSchema.load(body):
        item_data.title = body.get("title", item_data.title)
        item_data.author = body.get("author", item_data.author)
        item_data.read = body.get("read", item_data.read)
        bookRepo.update(item_data)
        return bookSchema.dump(item_data), 200
    return {"message": "Item {} not found".format(id)}, 404
