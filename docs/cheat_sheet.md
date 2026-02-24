# Мастер-шпаргалка ML Engineer (Python)

Для: Дмитрия | Путь: Junior / Intern ML Engineer
Формат: микро-сессии 10-20 минут -> видимый результат -> коммит
Последнее обновление: [дата]

---
## Главная цель

Выйти на уровень Junior / Intern ML Engineer (Python):
- Уметь обучать модели (регрессия, классификация)
- Уметь сервить модели через REST API (FastAPI)
- Знать базовые инженерные практики (Git, тесты, Docker)
- Иметь портфолио из 4+ проектов на GitHub

---
## Проекты в портфолио

1) Python basics
- Файл: notebooks/00_python_basics.ipynb
- Навыки: функции, списки, словари, метрики precision/recall/f1 вручную
- Ссылка: https://www.kaggle.com/code/mitjagagin/python-basics-portfolio

2) Iris API (FastAPI)
- Файлы: scripts/train.py, app/main.py, tests/test_api.py
- Навыки: обучение модели, CLI-аргументы, REST API, pytest
- Эндпоинты: GET /health, POST /predict
- Ссылка: https://github.com/mitjagagin/ml-engineer-roadmap

3) California Housing (регрессия)
- Файл: notebooks/01_california_housing_baseline.ipynb
- Навыки: Ridge vs HistGradientBoosting, метрики RMSE/MAE/R2, анализ ошибок
- Результат: R2 около 0.84 (улучшенная модель)

4) Titanic (классификация)
- Файл: notebooks/02_titanic_eda.ipynb
- Навыки: EDA, работа с пропусками, кодирование категорий, train/test split, сравнение моделей
- Результат: accuracy около 82 процентов (RandomForest)

---
## Паттерн 1: Обучение и сохранение модели

1. Подготовка данных:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

2. Обучение:
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

3. Оценка:
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

4. Сохранение:
import joblib, os
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/my_model.pkl")

---
## Паттерн 2: Очистка данных (Titanic-style)

Заполнить пропуски в числе (медиана):
df['age'] = df['age'].fillna(df['age'].median())

Заполнить пропуски в категории (мода):
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])

Удалить колонку с более 70 процентов пропусков:
df = df.drop(columns=['deck'])

Закодировать категории (One-Hot Encoding):
df = pd.get_dummies(df, columns=['sex', 'embarked'])

---
## Паттерн 3: Тест для FastAPI

Файл: tests/test_api.py

from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

Запуск тестов:
pytest tests/test_api.py -v

---
## Паттерн 4: CLI аргументы (argparse)

В начале скрипта:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--model-path", type=str, default="models/model.pkl")
parser.add_argument("--test-size", type=float, default=0.2)
parser.add_argument("--random-state", type=int, default=42)
args = parser.parse_args()

Использование:
model_path = args.model_path
test_size = args.test_size

Запуск:
python script.py --model-path models/new.pkl --test-size 0.3

---
## Git: базовые команды

Посмотреть статус:
git status

Посмотреть изменения в файле:
git diff имя_файла

Добавить файл:
git add путь/к/файлу

Закоммитить:
git commit -m "type: краткое описание"

Отправить на GitHub:
git push

Типы коммитов:
- feat: новая фича
- fix: исправление бага
- docs: обновление документации
- test: добавление тестов
- chore: рутинные изменения

---
## Чек-лист: Я это могу

Пройдитесь мысленно — если на большинство можете ответить да, вы готовы двигаться дальше:

- Могу загрузить датасет из sklearn/seaborn
- Могу найти и обработать пропуски (медиана/мода/drop)
- Могу закодировать текстовые колонки через get_dummies
- Могу разделить данные на train/test со stratify
- Могу обучить LogisticRegression и RandomForest
- Могу посчитать accuracy и вывести confusion matrix
- Могу сохранить модель через joblib.dump
- Могу написать простой тест для FastAPI эндпоинта
- Могу добавить CLI аргументы через argparse
- Могу закоммитить изменения и отправить на GitHub
- Могу объяснить разницу между RMSE, MAE, R2
- Могу объяснить, зачем нужен train/test split

---
## План развития

Ближайшие шаги:

1) Docker + WSL2
- Цель: контейнеризация Iris API для деплоя
- Ресурсы: docs/Dockerfile (черновик), официальная документация Docker

2) Новый проект (тексты или изображения)
- Цель: расширение портфолио за пределы табличных данных
- Идеи: классификация отзывов, распознавание цифр (MNIST)

3) SQL + базовый пайплайн данных
- Цель: работа с реальными источниками данных
- Ресурсы: SQLite + pandas, простые SELECT/JOIN

4) Участие в Kaggle-соревновании
- Цель: практика в условиях дедлайна и лидерборда
- Старт: соревнования уровня Getting Started

---
## Полезные команды (PowerShell)

Активация окружения:
conda activate ml

Проверка версий:
python --version
pip list | findstr sklearn

Запуск ноутбука из терминала:
jupyter notebook notebooks/02_titanic_eda.ipynb

Запуск API локально:
uvicorn app.main:app --reload

Запуск тестов:
pytest tests/test_api.py -v

Поиск по файлам:
findstr /S /I "текст" *.*

Очистка вывода ноутбука (перед коммитом):
В VS Code: Command Palette -> Jupyter: Clear All Outputs

---
Принцип работы: микро-сессии 10-20 минут -> видимый результат -> коммит -> документирование
Этот файл обновляется по мере обучения. Актуальная версия — в репозитории.
Репозиторий: https://github.com/mitjagagin/ml-engineer-roadmap