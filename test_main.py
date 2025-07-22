import pytest
from fastapi.testclient import TestClient
from main import api

client = TestClient(api)

def test_get_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    todos = response.json()
    assert isinstance(todos, list)
    assert len(todos) >= 1

def test_get_todo():
    response = client.get("/todos/1")
    assert response.status_code == 200
    todo = response.json()
    assert todo["todo_id"] == 1

def test_create_todo():
    new_todo = {
        "todo_name": "Test",
        "todo_description": "Test description",
        "priority": 3
    }
    response = client.post("/todos", json=new_todo)
    assert response.status_code == 200
    created = response.json()
    assert created["todo_name"] == "Test"

def test_update_todo():
    update_data = {
        "todo_name": "Updated Name"
    }
    response = client.put("/todos/1", json=update_data)
    assert response.status_code == 200
    updated = response.json()
    assert updated["todo_name"] == "Updated Name"

def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == 200
    deleted = response.json()
    assert deleted["todo_id"] == 1
