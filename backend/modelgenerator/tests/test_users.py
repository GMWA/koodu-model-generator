from . import client


def test_read_all_users():
    response = client.get("/users")
    assert response.status_code == 200
