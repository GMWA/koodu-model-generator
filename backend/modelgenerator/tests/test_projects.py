from . import client


def test_read_all_projects():
    response = client.get("/projects")
    assert response.status_code == 200
