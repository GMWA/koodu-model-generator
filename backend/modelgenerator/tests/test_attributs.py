from . import client


def test_read_all_attributs():
    response = client.get("/attributs")
    assert response.status_code == 200