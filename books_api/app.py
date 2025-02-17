from flask import Flask, request, Response
from db import db
from ma import ma
from flask_cors import CORS

from handlers import book as book_handler
from utils.form_exception import FormException

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin@db:3306/books"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
CORS(app)

ma.init_app(app)
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/api/books")
def get_books():
    try:
        return book_handler.get_all()
    except Exception as e:
        return Response(FormException(str(e)).json(), status=400)


@app.route("/api/books", methods=["POST"])
def create_book():
    try:
        book = request.get_json()
        book_handler.create(body=book)
        return Response(status=201)
    except Exception as e:
        return Response(FormException(str(e)).json(), status=400)

@app.route("/api/books/<string:id>", methods=["DELETE"])
def delete_book(id):
    try:
        return book_handler.delete(id)
    except Exception as e:
        return Response(FormException(str(e)).json(), status=400)

@app.route("/api/books/<string:id>", methods=["PUT"])
def update_book(id):
    try:
        book = request.get_json()
        return book_handler.update(id, body=book)
    except Exception as e:
        return Response(FormException(str(e)).json(), status=400)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
