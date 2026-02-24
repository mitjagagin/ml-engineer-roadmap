import pytest
from fastapi.testclient import TestClient
from app.main import app

# Создаём тестовый клиент
client = TestClient(app)

def test_health():
    """Проверяем, что /health возвращает status: ok"""
    response = client.get("/health")
    
    # Проверяем статус код
    assert response.status_code == 200
    
    # Проверяем тело ответа
    assert response.json() == {"status": "ok"}

def test_predict():
    """Проверяем, что /predict возвращает предсказание"""
    data = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=data)
    
    assert response.status_code == 200
    assert "class_id" in response.json()
    assert "class_name" in response.json()
    assert "proba" in response.json()