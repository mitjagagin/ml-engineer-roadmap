# Learning log — ML Engineer path

Цель: выйти на уровень Junior / Intern ML Engineer (Python)
Навыки: обучение моделей, REST API, Docker (базово)

Репозиторий: https://github.com/mitjagagin/ml-engineer-roadmap

---
## Текущая настройка (Windows)

- Установлен Miniconda
- Conda-окружение: `ml` (Python 3.11)
- VS Code kernel: `Python (ml)`
- Рабочая папка: `C:\ml_path\ml-engineer-roadmap`

---
## Структура проекта

- `notebooks/` — Jupyter ноутбуки
- `scripts/` — скрипты обучения и тестов
- `app/` — FastAPI сервис
- `tests/` — автотесты pytest
- `models/` — сохранённые модели (.pkl)
- `docs/` — документация (PROJECTS, резюме, лог)
- `environment.yml` — описание conda-окружения
- `.gitignore` — исключения для Git

---
## Выполнено (подтверждено)

1) Базовая настройка
- Создана структура папок
- Настроено conda-окружение (`environment.yml`)
- Интеграция VS Code + Jupyter

2) Notebook: Python basics
- Файл: `notebooks/00_python_basics.ipynb`
- Навыки: функции, структуры данных, метрики precision/recall/f1 вручную

3) Проект Iris: Train -> Serve
- `scripts/train.py`: обучает `LogisticRegression`, сохраняет `models/iris_logreg.pkl`
- `scripts/train.py` поддерживает CLI-аргументы: `--model-path`, `--test-size`, `--random-state`
- `app/main.py` (FastAPI):
  - `GET /health` -> `{"status": "ok"}`
  - `POST /predict` -> возвращает `class_id`, `class_name`, `proba`
- Тестирование API:
  - `scripts/test_api.ps1` (PowerShell, Invoke-RestMethod)
  - `tests/test_api.py` (pytest + TestClient)

4) Проект California Housing (регрессия)
- Файл: `notebooks/01_california_housing_baseline.ipynb`
- Модели: `Ridge` vs `HistGradientBoostingRegressor`
- Метрики: RMSE, MAE, R2, анализ ошибок

5) Проект Titanic (классификация)
- Файл: `notebooks/02_titanic_eda.ipynb`
- Навыки: EDA, работа с пропусками, кодирование категорий, сравнение моделей
- Результат: accuracy около 82 процентов (`RandomForest`)

6) Документация
- `README.md`: краткая навигация по репозиторию
- `docs/PROJECTS.md`: детальное описание проектов
- `docs/hh_resume_draft.md`: черновик резюме для hh.ru
- `docs/cheat_sheet.md`: шпаргалка с паттернами и командами

---
## Как запустить (быстро)

Активация окружения:
`$ conda activate ml`

Обучение модели (Iris):
`$ python scripts/train.py`

Обучение с параметрами:
`$ python scripts/train.py --model-path models/my_model.pkl --test-size 0.3`

Запуск API локально:
`$ uvicorn app.main:app --reload`

Проверка API (PowerShell):
`$ .\scripts\test_api.ps1`

Запуск тестов:
`$ pytest tests/test_api.py -v`

Открытие ноутбука:
`$ jupyter notebook notebooks/02_titanic_eda.ipynb`

---
## План на ближайшую неделю

1) Docker + WSL2
- Создать `requirements.txt` для Iris API
- Написать черновик `Dockerfile`
- Протестировать сборку образа

2) Новый проект (выбор типа данных)
- Варианты: тексты (классификация отзывов) или изображения (MNIST)
- Цель: расширить портфолио за пределы табличных данных

3) SQL + базовый пайплайн данных
- Подключение SQLite через pandas
- Простые запросы: SELECT, WHERE, JOIN

4) Обновление резюме на hh.ru
- Перенести актуальные проекты из черновика
- Добавить навыки: pytest, FastAPI, EDA

---
## Принципы работы

- Микро-сессии 10-20 минут -> видимый результат -> коммит
- Каждый шаг документирован: код + README + лог прогресса
- Портфолио важнее теории: работодатель видит код, а не слова
- Ошибки — это нормально: фиксируем, разбираем, идём дальше

Этот файл обновляется после каждой сессии.
Актуальная версия: https://github.com/mitjagagin/ml-engineer-roadmap/blob/main/docs/learning_log.md