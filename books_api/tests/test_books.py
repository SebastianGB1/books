import json
from app import app  # Importa la instancia de tu aplicación Flask


def test_get_books():
    client = app.test_client()
    response = client.get("/api/books")

    assert response.status_code == 200

    data = json.loads(response.data)

    assert isinstance(data, list)
    if data:
        required_keys = {"title", "author", "read", "id"}
        for book in data:
            assert isinstance(book, dict)
            assert required_keys.issubset(book.keys()), "Missing keys"


def test_create_book():
    client = app.test_client()

    new_book = {"title": "Clean Code", "author": "Robert C. Martin", "read": False}

    response = client.post(
        "/api/books", data=json.dumps(new_book), content_type="application/json"
    )

    assert response.status_code == 201


def test_create_book_with_no_params():
    client = app.test_client()

    # Datos del nuevo libro
    new_book = {"author": "", "read": False}

    response = client.post(
        "/api/books", data=json.dumps(new_book), content_type="application/json"
    )
    data = json.loads(response.data)

    assert response.status_code == 400
    assert "Missing data for required field" in data["message"]
