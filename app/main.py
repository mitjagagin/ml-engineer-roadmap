import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# Создаём веб-приложение
app = FastAPI(title="Iris classifier")

# Загружаем модель один раз при старте сервиса (не на каждый запрос)
model = joblib.load("models/iris_logreg.pkl")


# Описываем входные данные (FastAPI будет валидировать типы)
class IrisRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# Endpoint для проверки "жив ли сервис"
@app.get("/health")
def health():
    return {"status": "ok"}


# Основной endpoint предсказания
@app.post("/predict")
def predict(req: IrisRequest):
    # Превращаем вход в массив 1x4 — это формат, который ждёт sklearn
    x = np.array(
        [[req.sepal_length, req.sepal_width, req.petal_length, req.petal_width]]
    )

    # Класс (0/1/2)
    pred = int(model.predict(x)[0])

    # Вероятности по классам
    proba = model.predict_proba(x)[0].tolist()

    return {"class_id": pred, "proba": proba}
