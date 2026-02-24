# Портфолио проектов — ML Engineer (Python)

Репозиторий: https://github.com/mitjagagin/ml-engineer-roadmap
Формат: микро-сессии 10-20 минут -> видимый результат -> коммит
Цель: уровень Junior / Intern ML Engineer (Python)

---
## 1) Python: основы и метрики классификации

Задача: Закрепить базовые конструкции Python для ML-инженерии, реализовать метрики вручную.

Что сделано:
- Базовые структуры: списки, словари, циклы, функции
- Функция `precision_recall_f1(tp, fp, fn)` без библиотек
- Документирование через Markdown (Goal / Contents / Summary)
- Проверка окружения: `conda env ml`, `Python 3.11`, `VS Code + Jupyter`

Стек: Python, Pandas (базово), Jupyter Notebook, conda, Git/GitHub

Результат:
- Уверенная работа с синтаксисом Python
- Понимание формул precision, recall, F1 на практике
- Готовый шаблон для будущих ноутбуков

Ссылки:
- GitHub: https://github.com/mitjagagin/ml-engineer-roadmap/tree/main/notebooks/00_python_basics.ipynb
- Kaggle: https://www.kaggle.com/code/mitjagagin/python-basics-portfolio

---
## 2) Iris: сервис предсказаний на FastAPI

Задача: Полный пайплайн «обучение -> сохранение модели -> REST API».

Что сделано:
- `scripts/train.py`: обучает `LogisticRegression`, сохраняет `models/iris_logreg.pkl`, поддерживает CLI-аргументы
- `app/main.py` (FastAPI): `GET /health`, `POST /predict` (возвращает `class_id`, `class_name`, `proba`)
- Тесты: `tests/test_api.py` (pytest + TestClient), `scripts/test_api.ps1` (PowerShell)

Стек: Python, scikit-learn, joblib, FastAPI, uvicorn, pytest, PowerShell, Git/GitHub

Результат:
- Рабочий ML-сервис с двумя эндпоинтами
- Понимание цикла: train -> save -> serve
- Навык написания автотестов для API

Ссылка: https://github.com/mitjagagin/ml-engineer-roadmap

---
## 3) California Housing: регрессия стоимости жилья

Задача: Построить baseline для табличных данных, улучшить модель, проанализировать ошибки.

Что сделано:
- Загрузка: `fetch_california_housing(as_frame=True)` -> 20 640 строк, 9 колонок
- Модели: `Ridge` (baseline) vs `HistGradientBoostingRegressor` (улучшенная)
- Разбиение: `train/test split` с `random_state=42`
- Метрики на тесте:
  - Ridge: RMSE 0.746, MAE 0.533, R2 0.576
  - HGB: RMSE 0.464, MAE 0.310, R2 0.836
- Анализ ошибок: Actual vs Predicted, гистограмма ошибок, bias по ценовым диапазонам

Стек: Python, Pandas, NumPy, scikit-learn, Matplotlib, Seaborn

Результат:
- Понимание разницы между простыми и ансамблевыми моделями
- Навык визуального анализа ошибок регрессии
- Умение интерпретировать RMSE/MAE/R2 в контексте задачи

Ссылка: https://github.com/mitjagagin/ml-engineer-roadmap/blob/main/notebooks/01_california_housing_baseline.ipynb

---
## 4) Titanic: предсказание выживания пассажиров

Задача: Полный цикл ML-проекта для бинарной классификации.

Что сделано:
- EDA: загрузка через `sns.load_dataset`, визуализация, анализ пропусков
- Предобработка:
  - Заполнение пропусков: `Age` -> медиана, `Embarked` -> мода
  - Удаление колонок с более 70 процентов пропусков (`Deck`)
  - One-Hot Encoding для `sex` и `embarked` через `get_dummies`
  - Разбиение на train/test со стратификацией (`stratify=y`)
- Модели: `LogisticRegression` (около 78 процентов accuracy) vs `RandomForest` (около 82 процентов accuracy)
- Анализ: `confusion matrix`, `feature importances` (`sex`, `fare`, `pclass` — наиболее значимые)
- Сохранение артефактов через `joblib`

Стек: Python, Pandas, NumPy, scikit-learn, Seaborn, Matplotlib, joblib

Результат:
- Полный пайплайн: загрузка -> EDA -> очистка -> кодирование -> обучение -> оценка -> сохранение
- Понимание работы с пропусками и категориями
- Навык сравнения моделей и интерпретации метрик

Ссылка: https://github.com/mitjagagin/ml-engineer-roadmap/blob/main/notebooks/02_titanic_eda.ipynb

---
## План развития

Ближайшие шаги:

1) Docker + WSL2
- Цель: контейнеризация Iris API для деплоя

2) Новый проект (тексты или изображения)
- Цель: расширение портфолио за пределы табличных данных

3) SQL + базовый пайплайн данных
- Цель: работа с реальными источниками данных

4) Участие в Kaggle-соревновании
- Цель: практика в условиях дедлайна и лидерборда

---
Принцип работы: микро-сессии 10-20 минут -> видимый результат -> коммит -> документирование