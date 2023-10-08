from . import client


def test_read_all_tables():
    response = client.get("/tables")
    assert response.status_code == 200
