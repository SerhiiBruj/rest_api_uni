from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_book():

    response = client.post(
        "/books/",
        json={
            "title": "Clean Code",
            "author": "Robert Martin",
            "description": "Programming book",
            "status": "available",
            "release_year": 2008
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Clean Code"

    assert "id" in data


def test_get_books():

    response = client.get(
        "/books/?limit=5&offset=0"
    )

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list
    )


def test_get_book_by_id():

    create_response = client.post(
        "/books/",
        json={
            "title": "Book",
            "author": "Author",
            "description": "Desc",
            "status": "available",
            "release_year": 2020
        }
    )

    book_id = create_response.json()["id"]

    response = client.get(
        f"/books/{book_id}"
    )

    assert response.status_code == 200

    assert response.json()["id"] == book_id


def test_delete_book():

    create_response = client.post(
        "/books/",
        json={
            "title": "Delete Book",
            "author": "Author",
            "description": "Desc",
            "status": "available",
            "release_year": 2021
        }
    )

    book_id = create_response.json()["id"]

    response = client.delete(
        f"/books/{book_id}"
    )

    assert response.status_code == 204