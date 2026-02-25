# Learning log — ML Engineer path

> Цель: выйти на уровень Junior / Intern ML Engineer (Python)  
> Навыки: обучение моделей, REST API, Docker (базово)  
> Репозиторий: https://github.com/mitjagagin/ml-engineer-roadmap

---
## 🖥️ Текущая настройка (Windows)

| Параметр | Значение |
|----------|----------|
| Miniconda | Установлен |
| Conda-окружение | `ml` (Python 3.11) |
| VS Code kernel | `Python (ml)` |
| Рабочая папка | `C:\ml_path\ml-engineer-roadmap` |

---
## 📁 Структура проекта

| Папка/Файл | Назначение |
|------------|------------|
| `notebooks/` | Jupyter ноутбуки |
| `scripts/` | Скрипты обучения и тестов |
| `app/` | FastAPI сервис |
| `tests/` | Автотесты pytest |
| `models/` | Сохранённые модели (.pkl) |
| `docs/` | Документация (PROJECTS, резюме, лог) |
| `environment.yml` | Описание conda-окружения |
| `.gitignore` | Исключения для Git |

---
## ✅ Выполнено (подтверждено)

### 1) Базовая настройка
- Создана структура папок
- Настроено conda-окружение (`environment.yml`)
- Интеграция VS Code + Jupyter

### 2) Notebook: Python basics
- Файл: `notebooks/00_python_basics.ipynb`
- Навыки: функции, структуры данных, метрики precision/recall/f1 вручную

### 3) Проект Iris: Train -> Serve
- `scripts/train.py`: обучает `LogisticRegression`, сохраняет `models/iris_logreg.pkl`
- `app/main.py` (FastAPI):
  - `GET /health` -> `{"status": "ok"}`
  - `POST /predict` -> возвращает `class_id`, `class_name`, `proba`
- Тестирование API:
  - `scripts/test_api.ps1` (PowerShell)
  - `tests/test_api.py` (pytest + TestClient)

### 4) Проект California Housing (регрессия)
- Файл: `notebooks/01_california_housing_baseline.ipynb`
- Модели: `Ridge` vs `HistGradientBoostingRegressor`
- Метрики: RMSE, MAE, R², анализ ошибок

### 5) Проект Titanic (классификация)
- Файл: `notebooks/02_titanic_eda.ipynb`
- Навыки: EDA, работа с пропусками, кодирование категорий, сравнение моделей
- Результат: accuracy ~82% (`RandomForest`)

### 6) Документация
- `README.md`: краткая навигация по репозиторию
- `docs/PROJECTS.md`: детальное описание проектов
- `docs/hh_resume_draft.md`: черновик резюме для hh.ru
- `docs/cheat_sheet.md`: шпаргалка с паттернами и командами

---
## 🚀 Как запустить (быстро)

~~~bash
conda activate ml
python scripts/train.py
python scripts/train.py --model-path models/my_model.pkl --test-size 0.3
uvicorn app.main:app --reload
.\scripts\test_api.ps1
pytest tests/test_api.py -v
jupyter notebook notebooks/02_titanic_eda.ipynb
~~~

---
## 🗓️ План на ближайшую неделю

| Шаг | Задача |
|-----|--------|
| Docker + WSL2 | Создать `requirements.txt` и `Dockerfile` для Iris API |
| Новый проект | Выбрать тип данных (тексты или изображения) |
| SQL + пайплайн | Подключение SQLite через pandas, простые SELECT/JOIN |
| Резюме на hh.ru | Перенести актуальные проекты, добавить навыки |

---
## 📝 Принципы работы

- Микро-сессии 10-20 минут -> видимый результат -> коммит
- Каждый шаг документирован: код + README + лог прогресса
- Портфолио важнее теории: работодатель видит код, а не слова
- Ошибки — это нормально: фиксируем, разбираем, идём дальше

> Этот файл обновляется после каждой сессии.  
> Актуальная версия: [docs/learning_log.md](https://github.com/mitjagagin/ml-engineer-roadmap/blob/main/docs/learning_log.md)