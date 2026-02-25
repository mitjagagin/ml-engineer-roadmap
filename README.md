# ML Engineer Roadmap (с нуля)

> Цель: выйти на уровень Junior / Intern ML Engineer (Python)  
> Формат: микро-сессии 10-20 минут -> видимый результат -> коммит

---

## 📚 Документация

| Файл | Описание |
|------|----------|
| [docs/PROJECTS.md](docs/PROJECTS.md) | Портфолио проектов с деталями |
| [docs/hh_resume_draft.md](docs/hh_resume_draft.md) | Черновик резюме для hh.ru |
| [docs/learning_log.md](docs/learning_log.md) | Лог прогресса обучения |
| [docs/cheat_sheet.md](docs/cheat_sheet.md) | Шпаргалка с паттернами и командами |

---
## 🚀 Быстрый старт

### Создание окружения (Windows + Miniconda)

~~~bash
conda env create -f environment.yml
conda activate ml
~~~

### Запуск в VS Code

1. Откройте репозиторий в VS Code
2. Выберите интерпретатор: `Python (ml)`
3. Откройте ноутбук или скрипт -> запустите

### Проверка установки

~~~bash
python --version
python -c "import sklearn; print(sklearn.__version__)"
~~~

---
## 📂 Проекты в репозитории

| Проект | Файл | Описание |
|--------|------|----------|
| Python basics | `notebooks/00_python_basics.ipynb` | Основы Python, метрики precision/recall/f1 |
| Iris API | `app/main.py`, `scripts/train.py` | FastAPI сервис для предсказаний |
| California Housing | `notebooks/01_california_housing_baseline.ipynb` | Регрессия, анализ ошибок |
| Titanic | `notebooks/02_titanic_eda.ipynb` | Классификация, полный ML-цикл |

**Подробнее** → см. [docs/PROJECTS.md](docs/PROJECTS.md)

---
## 🛠 Скрипт обучения (CLI)

### Запуск по умолчанию

~~~bash
python scripts/train.py
~~~

### Свои параметры

~~~bash
python scripts/train.py --model-path models/iris_logreg.pkl --test-size 0.3
~~~

### Показать опции

~~~bash
python scripts/train.py --help
~~~

### Аргументы

| Аргумент | По умолчанию | Описание |
|----------|--------------|----------|
| `--model-path` | `models/iris_logreg.pkl` | Путь для сохранения модели |
| `--test-size` | `0.2` | Доля тестовой выборки (0.0–1.0) |
| `--random-state` | `42` | Seed для воспроизводимости |

---
## 🧪 Тестирование API

### Быстрая проверка (PowerShell)

~~~bash
.\scripts\test_api.ps1
~~~

### Автотесты (pytest)

~~~bash
pytest tests/test_api.py -v
~~~

### Ожидаемый результат

~~~
tests/test_api.py::test_health PASSED
tests/test_api.py::test_predict PASSED
~~~

---
## 🔗 Ссылки

- **GitHub**: https://github.com/mitjagagin
- **Kaggle**: https://www.kaggle.com/mitjagagin
- **Python basics на Kaggle**: https://www.kaggle.com/code/mitjagagin/python-basics-portfolio

---

> Принцип работы: микро-сессии -> видимый результат -> коммит -> документирование  
> Актуальная версия: https://github.com/mitjagagin/ml-engineer-roadmap