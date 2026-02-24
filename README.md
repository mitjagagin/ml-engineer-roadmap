# ML Engineer Roadmap (с нуля)

Цель: выйти на уровень Junior / Intern ML Engineer (Python)
Формат: микро-сессии 10-20 минут -> видимый результат -> коммит

---
## Документация

- Портфолио проектов: docs/PROJECTS.md
- Черновик резюме: docs/hh_resume_draft.md
- Лог прогресса: docs/learning_log.md

---
## Быстрый старт

### Создание окружения (Windows + Miniconda)

- conda env create -f environment.yml
- conda activate ml

### Запуск в VS Code

- Откройте репозиторий в VS Code
- Выберите интерпретатор: Python (ml)
- Откройте ноутбук или скрипт -> запустите

### Проверка установки

- python --version (должно быть: Python 3.11.x)
- python -c "import sklearn; print(sklearn.__version__)" (должно быть: 1.8.0)

---
## Проекты в репозитории

1. Python basics
   - Файл: notebooks/00_python_basics.ipynb
   - Описание: Основы Python, метрики precision/recall/f1

2. Iris API
   - Файлы: app/main.py, scripts/train.py
   - Описание: FastAPI сервис для предсказаний

3. California Housing
   - Файл: notebooks/01_california_housing_baseline.ipynb
   - Описание: Регрессия, анализ ошибок

4. Titanic
   - Файл: notebooks/02_titanic_eda.ipynb
   - Описание: Классификация, полный ML-цикл

Подробнее: docs/PROJECTS.md

---
## Скрипт обучения (CLI)

Запуск по умолчанию:
- python scripts/train.py

Свои параметры:
- python scripts/train.py --model-path models/my_model.pkl --test-size 0.3

Показать опции:
- python scripts/train.py --help

Аргументы:
- --model-path: путь для сохранения модели (по умолчанию: models/iris_logreg.pkl)
- --test-size: доля тестовой выборки (по умолчанию: 0.2)
- --random-state: seed для воспроизводимости (по умолчанию: 42)

---
## Тестирование API

Быстрая проверка (PowerShell):
- .\scripts\test_api.ps1

Автотесты (pytest):
- pytest tests/test_api.py -v

---
## Ссылки

- GitHub: https://github.com/mitjagagin
- Kaggle: https://www.kaggle.com/mitjagagin
- Python basics на Kaggle: https://www.kaggle.com/code/mitjagagin/python-basics-portfolio

---
Принцип работы: микро-сессии -> видимый результат -> коммит -> документирование
Актуальная версия: https://github.com/mitjagagin/ml-engineer-roadmap