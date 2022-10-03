import uuid
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_with_a_random_uuid():
    task_id = uuid.uuid4()
    response = client.get(f"/plays/{task_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task informed not found"}


def test_post():
    with open("data.csv", "rb") as f:
        response = client.post("/plays", files={"file": ("filename", f, 'text/csv')})
    assert response.status_code == 202


def test_post_without_file():
    f = None
    response = client.post("/plays", files={"file": f})
    assert response.status_code == 400


def test_post_with_wrong_type_of_file():
    with open("requirements.txt", "rb") as f:
        response = client.post("/plays", files={"file": ("filename", f, 'text/txt')})
    assert response.status_code == 415
    assert response.json() == {"detail": "Invalid type of file."}


def test_post_and_get_results():
    with open("data.csv", "rb") as f:
        response = client.post("/plays", files={"file": ("filename", f, 'text/csv')})
    assert response.status_code == 202
    task_id = response.json()['task_id']
    response2 = client.get(f"/plays/{task_id}")
    assert response2.status_code == 200
