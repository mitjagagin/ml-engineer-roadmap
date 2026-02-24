# ML Engineer Roadmap (с нуля)

> Цель: выйти на уровень Junior / Intern ML Engineer (Python)
> Формат: микро-сессии 10–20 минут → видимый результат → коммит

---

## 📚 Полная документация

- **Портфолио проектов** → см. docs/PROJECTS.md
- **Черновик резюме** → см. docs/hh_resume_draft.md
- **Лог прогресса** → см. docs/learning_log.md

---

## 🚀 Быстрый старт

### 1) Создание окружения (Windows + Miniconda)

Команда 1: conda env create -f environment.yml
Команда 2: conda activate ml

### 2) Запуск в VS Code

- Откройте репозиторий в VS Code
- Выберите интерпретатор: Python (ml)
- Откройте ноутбук или скрипт → запустите

### 3) Проверка установки

Команда: python --version (ожидается: Python 3.11.x)
Команда: python -c "import sklearn; print(sklearn.__version__)" (ожидается: 1.8.0)

---

## 📂 Проекты в репозитории

**1) Python basics**
- Файл: notebooks/00_python_basics.ipynb
- Описание: Основы Python, метрики precision/recall/f1

**2) Iris API**
- Файлы: app/main.py + scripts/train.py
- Описание: FastAPI сервис для предсказаний

**3) California Housing**
- Файл: notebooks/01_california_housing_baseline.ipynb
- Описание: Регрессия, анализ ошибок

**4) Titanic**
- Файл: notebooks/02_titanic_eda.ipynb
- Описание: Классификация, полный ML-цикл

**Подробнее** → см. docs/PROJECTS.md

---

## 🛠 Использование скрипта обучения

**Запуск с настройками по умолчанию:**
python scripts/train.py

**Свои параметры:**
python scripts/train.py --model-path models/my_model.pkl --test-size 0.3

**Показать все опции:**
python scripts/train.py --help

**Аргументы:**
- --model-path (по умолчанию: models/iris_logreg.pkl) — путь для сохранения модели
- --test-size (по умолчанию: 0.2) — доля тестовой выборки
- --random-state (по умолчанию: 42) — seed для воспроизводимости

---

## 🧪 Тестирование API

**Быстрая проверка (PowerShell):**
.\scripts\test_api.ps1

**Автотесты (pytest):**
pytest tests/test_api.py -v

---

## 🔗 Ссылки

- GitHub: https://github.com/mitjagagin
- Kaggle: https://www.kaggle.com/mitjagagin
- Python basics на Kaggle: https://www.kaggle.com/code/mitjagagin/python-basics-portfolio

---

## 📁 Структура репозитория

ml-engineer-roadmap/
├── README.md (этот файл)
├── environment.yml (Conda-окружение)
├── notebooks/ (Jupyter ноутбуки)
├── scripts/ (скрипты обучения и тесты)
├── app/ (FastAPI сервис)
├── tests/ (pytest тесты)
├── models/ (сохранённые модели)
└── docs/ (документация: PROJECTS, резюме, лог)

---

> Принцип работы: микро-сессии → видимый результат → коммит → документирование
> Актуальная версия: https://github.com/mitjagagin/ml-engineer-roadmap