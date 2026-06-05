from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert "message" in r.json()


def test_health():
    r = client.get("/health")
    assert r.json() == {"status": "ok"}


def test_create_and_get_item():
    payload = {"name": "Widget", "description": "A nice widget", "price": 9.99}
    r = client.post("/items/", json=payload)
    assert r.status_code == 201
    item = r.json()
    assert item["name"] == "Widget"

    r2 = client.get(f"/items/{item['id']}")
    assert r2.status_code == 200
    assert r2.json()["price"] == 9.99


def test_update_item():
    r = client.post("/items/", json={"name": "Old", "price": 1.0})
    item_id = r.json()["id"]

    r2 = client.put(f"/items/{item_id}", json={"name": "New"})
    assert r2.json()["name"] == "New"
    assert r2.json()["price"] == 1.0  # unchanged


def test_delete_item():
    r = client.post("/items/", json={"name": "Temp", "price": 0.5})
    item_id = r.json()["id"]

    client.delete(f"/items/{item_id}")
    r2 = client.get(f"/items/{item_id}")
    assert r2.status_code == 404


def test_list_items():
    r = client.get("/items/")
    assert isinstance(r.json(), list)
