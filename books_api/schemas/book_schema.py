from ma import ma
from models.book import BookModel
from marshmallow import fields, validate

class BookSchema(ma.SQLAlchemyAutoSchema):
    title = ma.String(required=True, validate=validate.Length(min=5))
    author = ma.String(required=True, validate=validate.Length(min=5))
    class Meta:
        model = BookModel
        load_instance = True